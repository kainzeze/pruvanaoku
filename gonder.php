<?php
/**
 * Iletisim formu.
 * Etki: pruvaanaokulu@gmail.com adresine duz metin e-posta gonderir.
 * Kayit: form verisi sunucuda dosyaya yazilmaz.
 * Geri donus: gonderim basarisizsa ziyaretci telefon ve e-posta ile yonlendirilir.
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

$to = 'pruvaanaokulu@gmail.com';
$subject = 'Mavi Pruva web sitesi iletisim formu';
$body = "Ad: {$ad}\nSoyad: {$soyad}\nE-posta: {$email}\nTelefon: {$telefon}\n\nMesaj:\n{$mesaj}\n";
$headers = "MIME-Version: 1.0\r\nContent-Type: text/plain; charset=UTF-8\r\nReply-To: {$email}\r\n";

$sent = @mail($to, '=?UTF-8?B?' . base64_encode($subject) . '?=', $body, $headers);
header('Location: iletisim.php?durum=' . ($sent ? 'ok' : 'hata'));
exit;
