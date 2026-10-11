<?php
/**
 * Iletisim formu.
 * Etki: bilgi@pruvanaokulu.com hesabiyla SMTP (465) uzerinden
 *       bilgi@pruvanaokulu.com ve pruvaanaokulu@gmail.com adreslerine duz metin gonderir.
 * Kayit: form verisi ve parola sunucuda dosyaya yazilmaz. Parola mail.local.php icindedir.
 * Geri donus: gonderim basarisizsa ziyaretci telefon ve e-posta ile yonlendirilir.
 * Risk: Plesk sertifikasi alan adina ait degil (CN=Plesk). Bu yuzden TLS kimligi
 *       dogrulanmadan sifreli baglanti kurulur. Eski haline donmek icin
 *       _kaynak/_yedek/2026-10-11-mail-oncesi/gonder.php kopyalanir.
 */
declare(strict_types=1);

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header('Location: iletisim.php');
    exit;
}

function clean(string $value, int $max): string
{
    $value = str_replace(["\r", "\n", "\0"], ' ', trim($value));
    if (function_exists('mb_substr')) {
        return mb_substr($value, 0, $max, 'UTF-8');
    }
    return substr($value, 0, $max);
}

function mail_config(): array
{
    $path = __DIR__ . '/mail.local.php';
    if (!is_file($path)) {
        error_log('iletisim: mail.local.php yok');
        return [];
    }
    $cfg = require $path;
    return is_array($cfg) ? $cfg : [];
}

function smtp_read($fp): string
{
    $data = '';
    while (!feof($fp)) {
        $line = fgets($fp, 1024);
        if ($line === false) {
            break;
        }
        $data .= $line;
        if (strlen($line) >= 4 && $line[3] === ' ') {
            break;
        }
    }
    return $data;
}

function smtp_code(string $reply): int
{
    return (int)substr($reply, 0, 3);
}

function smtp_cmd($fp, string $command, array $ok): bool
{
    if (fwrite($fp, $command . "\r\n") === false) {
        return false;
    }
    $reply = smtp_read($fp);
    if ($reply === '' || !in_array(smtp_code($reply), $ok, true)) {
        error_log('iletisim smtp: ' . smtp_code($reply));
        return false;
    }
    return true;
}

function smtp_text(string $text): string
{
    $text = str_replace(["\r\n", "\r"], "\n", $text);
    $lines = [];
    foreach (explode("\n", $text) as $line) {
        while (strlen($line) > 900) {
            $lines[] = substr($line, 0, 900);
            $line = substr($line, 900);
        }
        $lines[] = $line;
    }
    foreach ($lines as $i => $line) {
        if (str_starts_with($line, '.')) {
            $lines[$i] = '.' . $line;
        }
    }
    return implode("\r\n", $lines);
}

function smtp_send(array $cfg, string $subject, string $bodyText, string $replyTo): bool
{
    $host = (string)($cfg['host'] ?? '');
    $port = (int)($cfg['port'] ?? 0);
    $username = (string)($cfg['username'] ?? '');
    $password = (string)($cfg['password'] ?? '');
    $from = (string)($cfg['from'] ?? '');
    $fromName = (string)($cfg['from_name'] ?? '');
    $recipients = $cfg['recipients'] ?? [];
    if ($host === '' || $port < 1 || $username === '' || $password === '' || !filter_var($from, FILTER_VALIDATE_EMAIL)) {
        error_log('iletisim: posta ayari eksik');
        return false;
    }
    if (!is_array($recipients)) {
        return false;
    }
    $recipients = array_values(array_filter($recipients, static function ($address): bool {
        return is_string($address) && filter_var($address, FILTER_VALIDATE_EMAIL);
    }));
    if ($recipients === []) {
        return false;
    }

    $context = stream_context_create([
        'ssl' => [
            'verify_peer' => false,
            'verify_peer_name' => false,
            'allow_self_signed' => true,
            'SNI_enabled' => true,
            'peer_name' => $host,
        ],
    ]);
    $errno = 0;
    $errstr = '';
    $fp = stream_socket_client(
        'ssl://' . $host . ':' . $port,
        $errno,
        $errstr,
        20,
        STREAM_CLIENT_CONNECT,
        $context
    );
    if ($fp === false) {
        error_log('iletisim smtp baglanti: ' . $errno);
        return false;
    }
    stream_set_timeout($fp, 20);

    $banner = smtp_read($fp);
    if (smtp_code($banner) !== 220) {
        fclose($fp);
        error_log('iletisim smtp banner: ' . smtp_code($banner));
        return false;
    }
    $ok = smtp_cmd($fp, 'EHLO pruvanaokulu.com', [250])
        && smtp_cmd($fp, 'AUTH LOGIN', [334])
        && smtp_cmd($fp, base64_encode($username), [334])
        && smtp_cmd($fp, base64_encode($password), [235])
        && smtp_cmd($fp, 'MAIL FROM:<' . $from . '>', [250]);
    foreach ($recipients as $address) {
        $ok = $ok && smtp_cmd($fp, 'RCPT TO:<' . $address . '>', [250, 251]);
    }
    $encodedName = '=?UTF-8?B?' . base64_encode($fromName) . '?=';
    $encodedSubject = '=?UTF-8?B?' . base64_encode($subject) . '?=';
    $headers = [
        'Date: ' . date('r'),
        'From: ' . $encodedName . ' <' . $from . '>',
        'To: ' . $recipients[0],
        'Cc: ' . implode(', ', array_slice($recipients, 1)),
        'Reply-To: ' . $replyTo,
        'MIME-Version: 1.0',
        'Content-Type: text/plain; charset=UTF-8',
        'Content-Transfer-Encoding: 8bit',
        'Subject: ' . $encodedSubject,
    ];
    $data = implode("\r\n", $headers) . "\r\n\r\n" . smtp_text($bodyText) . "\r\n.";
    $ok = $ok
        && smtp_cmd($fp, 'DATA', [354])
        && smtp_cmd($fp, $data, [250])
        && smtp_cmd($fp, 'QUIT', [221]);
    fclose($fp);
    return $ok;
}

if (trim((string)($_POST['website'] ?? '')) !== '') {
    header('Location: iletisim.php?durum=ok');
    exit;
}

$started = (int)($_POST['baslangic'] ?? 0);
if ($started > 0 && (time() - $started) < 3) {
    header('Location: iletisim.php?durum=hata');
    exit;
}

$ad = clean((string)($_POST['ad'] ?? ''), 80);
$soyad = clean((string)($_POST['soyad'] ?? ''), 80);
$email = clean((string)($_POST['email'] ?? ''), 120);
$telefon = clean((string)($_POST['telefon'] ?? ''), 30);
$mesaj = clean((string)($_POST['mesaj'] ?? ''), 4000);

$gecerli = $ad !== '' && $soyad !== '' && $telefon !== '' && filter_var($email, FILTER_VALIDATE_EMAIL);
if (!$gecerli) {
    header('Location: iletisim.php?durum=hata');
    exit;
}

$subject = 'Mavi Pruva web sitesi iletisim formu';
$body = "Ad: {$ad}\nSoyad: {$soyad}\nE-posta: {$email}\nTelefon: {$telefon}\n\nMesaj:\n{$mesaj}\n";
$sent = smtp_send(mail_config(), $subject, $body, $email);
header('Location: iletisim.php?durum=' . ($sent ? 'ok' : 'hata'));
exit;
