<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>İletişim | Özel Mersin Mavi Pruva Anaokulu</title>
  <meta name="description" content="2-6 yaş çocuklar için okul öncesi hizmeti veren özel anaokulu. Esenbağlar, Mezitli/Mersin.">
  <link rel="icon" href="images/logo.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@300;400;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <?php include __DIR__ . '/partials/header.html'; ?>
  <main>

  <section class="wrap">
    <div class="page-title"><span class="eyebrow">İletişim</span><h2 class="section-title">Bize Ulaşın</h2></div>
    <div class="contact-grid">
      <div>
        <h3 class="center">İletişime Geçin</h3>
        <div class="note" id="form-note" hidden></div>
        <form class="contact" action="gonder.php" method="post">
          <div class="hp" aria-hidden="true"><label>Website<input name="website" tabindex="-1" autocomplete="off"></label></div>
          <input type="hidden" name="baslangic" id="baslangic" value="">
          <label>Adınız<input name="ad" required maxlength="80" autocomplete="given-name"></label>
          <label>Soyadınız<input name="soyad" required maxlength="80" autocomplete="family-name"></label>
          <label>Email<input name="email" type="email" required maxlength="120" autocomplete="email"></label>
          <label>Telefon<input name="telefon" type="tel" required maxlength="30" autocomplete="tel"></label>
          <label>Bize mesaj bırakın<textarea name="mesaj" maxlength="4000"></textarea></label>
          <button class="btn" type="submit">Gönder</button>
        </form>
      </div>
      <div>
        <div class="hours">
          <div class="icon-row"><img src="images/icons/2e2a49_319bbd73b9044a44b81e47a4f78a9a93.svg" alt=""></div>
          <h2>Açılış Saatimiz</h2>
          <p>Pazartesi–Cuma 08:00–17:30</p>
        </div>
        <div class="visit">
          <div class="icon-row"><img src="images/icons/2e2a49_a23b983734c8437282ab7f798331146d.svg" alt=""></div>
          <h2>Bizi Ziyaret Edin</h2>
          <p>Esenbağlar Mh. 71048 Sk. No:5 Mezitli/Mersin</p>
          <p>Tel: <a href="tel:+905324637882">05324637882</a></p>
          <p>Mail: <a href="mailto:bilgi@pruvaanaokulu.com">bilgi@pruvaanaokulu.com</a></p>
        </div>
      </div>
    </div>
    <iframe class="map" title="Özel Mersin Mavi Pruva Anaokulu haritası" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://maps.google.com/maps?q=36.7447215,34.4817405&amp;z=16&amp;output=embed"></iframe>
  </section>
  <script>
    document.getElementById("baslangic").value = String(Math.floor(Date.now() / 1000));
    var durum = new URLSearchParams(location.search).get("durum");
    var note = document.getElementById("form-note");
    if (durum === "ok") {
      note.hidden = false;
      note.textContent = "Mesajınız alındı. En kısa sürede size dönüş yapacağız.";
    } else if (durum === "hata") {
      note.hidden = false;
      note.textContent = "Mesaj gönderilemedi. Lütfen 0532 463 78 82 numarasını arayın veya bilgi@pruvaanaokulu.com adresine yazın.";
    }
  </script>

  </main>
  <?php include __DIR__ . '/partials/footer.html'; ?>
  
</body>
</html>
