# Statik sayfalari uretir. Var olan html dosyalarinin uzerine yazar.
from pathlib import Path

root = Path(r"G:\mavipruvaanaokulu.com")
IC = "images/icons"
BEBEK = f"{IC}/11062b_93788172d8cc4931a7e2160caa259c43.svg"
OYUN = f"{IC}/11062b_e368f3f2ade846a8a6611947f3abb241.svg"
KUTU = f"{IC}/11062b_6250c5d5d61448daa12dbbddd6fba029.svg"
KUS = f"{IC}/2e2a49_c52f797c3a4c48c88245e42a45c62ff2.svg"
SAAT = f"{IC}/2e2a49_319bbd73b9044a44b81e47a4f78a9a93.svg"
KONUM = f"{IC}/2e2a49_a23b983734c8437282ab7f798331146d.svg"
SANAT = f"{IC}/2e2a49_6e243609b37d464d9ca6059b53aa5217.svg"
MUZIK = f"{IC}/2e2a49_6b6c957ab7e24a1eaa95a0e22276f108.svg"
SPOR = f"{IC}/2e2a49_341f12a2847c42e0ba4bbf73ce964f08.svg"
DIL = f"{IC}/2e2a49_e685781283484a1fa38933f48a1f8ea4.svg"

def shell(filename, title, body, extra=""):
    home = filename == "index.php"
    if home:
        top = """  <div class="opening">
    <?php include __DIR__ . '/partials/header.html'; ?>
    <section class="hero"><img src="images/hero.jpg" alt="Özel Mersin Mavi Pruva Anaokulu binası"><div class="hero-actions"><a class="btn btn-solid" href="kayitlar.php">Kayıt ve randevu</a><a class="btn btn-wa" href="https://wa.me/905324637882" target="_blank" rel="noopener noreferrer">WhatsApp</a></div></section>
  </div>"""
    else:
        top = "  <?php include __DIR__ . '/partials/header.html'; ?>"
    body_class = ' class="home"' if home else ""
    return f"""<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="2-6 yaş çocuklar için okul öncesi hizmeti veren özel anaokulu. Esenbağlar, Mezitli/Mersin.">
  <link rel="icon" href="images/logo.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@300;400;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css">
</head>
<body{body_class}>
{top}
  <main>
{body}
  </main>
  <?php include __DIR__ . '/partials/footer.html'; ?>
  {extra}
</body>
</html>
"""

def card(icon, title, text):
    klass = "icon-img" if icon.endswith(".png") else "icon"
    return f'''<article class="card"><img class="{klass}" src="{icon}" alt=""><h3>{title}</h3><p>{text}</p></article>'''

classes = [
    (BEBEK, False, "Bebek / Oyun Grubu", "24 ayını doldurmuş miniklerimiz için güvenli, şefkatli ve uyarıcı bir ortam sunuyoruz. Duyusal oyunlar, motor beceri geliştirici etkinlikler ve bireysel ilgiyle ilk sosyalleşme adımlarını güvenle atmalarını sağlıyoruz."),
    (OYUN, False, "Oyun &amp; Maceracılar", "2-3 yaş arası çocukların merak ve keşfetme arzusunu destekliyoruz. Dil gelişimi, ince-kaba motor becerileri ve paylaşma duygusunu pekiştiren eğlenceli ve etkileşimli aktivitelerle özgüven inşa ediyoruz."),
    (KUTU, False, "Okul Öncesi", "Sosyal, duygusal ve zihinsel gelişimin hız kazandığı bu dönemde; yaratıcı sanat çalışmaları, grup oyunları ve temel yaşam becerileri ile çocukların potansiyellerini ortaya çıkarıyoruz."),
    ("images/hedgehog.png", True, "Anasınıfı / İlkokul Hazırlık", "İlkokula geçiş sürecini kolaylaştıracak sistemli bir program sunuyoruz. Mantıksal düşünme, problem çözme, temel okuma-yazma farkındalığı ve özdisiplin kazandırarak onları geleceğe hazırlıyoruz."),
]

home_cards = "\n".join(card(icon, title, text) for icon, _photo, title, text in classes)
quotes = [
    ("Çocuğumuzu Mavi Pruva Anaokulu’na güvenle emanet ediyoruz. Öğretmenlerin ilgisi, güler yüzü ve okulun sıcak atmosferi sayesinde çocuğumuz her gün okula istekle gidiyor. İyi ki yollarımız kesişmiş!", "Alihan'ın Annesi", "Okul Öncesi Velimiz"),
    ("Çocuğumuzu ilk kez aile ortamından ayırıp okula başlatırken içimizde büyük bir endişe vardı. Ancak Mavi Pruva Anaokulu’nun sıcak, şefkatli yaklaşımı ve güler yüzlü ekibi sayesinde oryantasyon sürecini çok rahat atlattık. Çocuğumuzun sosyalleştiğini, kendine olan güveninin arttığını ve her sabah okula neşeyle koşarak gittiğini görmek bizim için paha biçilemez.", "Elif'in Annesi", "Bebek Grubu Velimiz"),
    ("Okulun sunduğu güvenli ortam, temizlik ve düzen konusundaki hassasiyetleri ilk günden beri takdirimizi kazandı. Sadece bir bakım alanı değil; çocukların merak duygusunu destekleyen, eğlenerek öğrenmelerini sağlayan çok nitelikli bir program uyguluyorlar. Emek veren tüm öğretmenlerimize ve yönetime gönülden teşekkür ederiz.", "Timur'un Babası", "Okul Öncesi Velimiz"),
]
quote_html = []
for i, (text, who, role) in enumerate(quotes):
    cls = "quote active" if i == 0 else "quote"
    quote_html.append(f'''<article class="{cls}"><h2>Ebeveynler Ne Düşünüyor?</h2><p class="text">{text}</p><p class="who">{who}</p><p class="role">{role}</p></article>''')

index = f'''
  <section class="wrap center">
    <h2 class="section-title">SINIFLARIMIZ (2-6 yaş)</h2>
    <div class="cards">
      {home_cards}
    </div>
  </section>
  <section class="wrap">
    <div class="split">
      <img class="photo" src="images/felsefe.jpg" alt="Okulumuzdan bir an">
      <div class="copy">
        <h2>Eğitim Felsefemiz</h2>
        <p>Özel Mersin Mavi Pruva Anaokulu olarak, çocuklarımızın doğal meraklarını ve keşfetme arzularını merkeze alan bir eğitim modeli uyguluyoruz. Oyun temelli öğrenme, sevgi dolu bir çevre ve bireysel gelişimi destekleyen etkinliklerimizle miniklerimizin güvenle, mutlulukla ve özgüvenle büyümelerine rehberlik ediyoruz.</p>
        <a class="btn" href="hakkimizda.php">Hakkımızda</a>
      </div>
    </div>
  </section>
  <section class="quotes" aria-label="Slayt Gösterisi">
    {''.join(quote_html)}
    <button class="slider-btn prev" type="button" aria-label="Geri">‹</button>
    <button class="slider-btn next" type="button" aria-label="İleri">›</button>
  </section>
'''

hakkimizda = '''
  <section class="wrap">
    <div class="page-title"><span class="eyebrow">Hakkımızda</span></div>
    <div class="blocks">
      <article class="block">
        <img class="block-photo" src="images/hakkimizda.jpg" alt="Çocuklar birlikte oynuyor">
        <div class="block-copy">
          <h2>Çocuğunuz Emin Ellerde</h2>
          <h3>Eğitim Felsefemiz</h3>
          <p>Her çocuğun benzersiz bir potansiyele, merak duygusuna ve öğrenme hızına sahip olduğuna inanıyoruz. Özel Mersin Mavi Pruva Anaokulu’nda amacımız; çocuklarımızı kalıplara sokmak değil, onların doğal meraklarını ve keşfetme arzularını desteklemektir. Sevgi, şefkat ve güven odaklı ortamımızda; çocuklarımızın sosyal, duygusal ve fiziksel gelişimlerini bir bütün olarak ele alıyoruz. Oyun temelli etkinliklerle özgüvenli, sorumluluk sahibi, çevreye duyarlı ve mutlu bireyler yetiştirmek temel ilkemizdir.</p>
        </div>
      </article>
      <article class="block">
        <img class="block-photo" src="images/psikolog.jpg" alt="Psikoloğun ofisi">
        <div class="block-copy">
          <h2>Sağlık, Güven ve Psikolojik Danışmanlık</h2>
          <p>Çocuklarımızın fiziki ve ruhsal güvenliği bizim için her şeyden önce gelir. Okulumuz; yaş gruplarına özel tasarlanmış korunaklı alanları, düzenli dezenfekte edilen sınıf ve oyun ekipmanları ile miniklerimize hijyenik ve emniyetli bir ortam sunar. Okulumuz bünyesinde görev yapan uzman psikoloğumuz; çocuklarımızın gelişim süreçlerini, uyum haftalarını ve duygusal ihtiyaçlarını yakından takip eder. Düzenli veli bilgilendirmeleri ve bireysel rehberlik çalışmalarıyla çocuklarımızın sağlıklı bir psikolojik gelişim göstermelerine destek oluyoruz. Gelişim süreçlerini yakından takip eden uzman psikoloğumuz ile çocuklarımızın oryantasyon, duygusal gelişim ve sosyal beceri kazanım süreçlerinde hem çocuklarımızın hem de velilerimizin yanındayız.</p>
        </div>
      </article>
    </div>
  </section>
'''

sinif_photos = ["images/sinif-1.jpg", "images/sinif-2.jpg", "images/sinif-3.jpg", "images/sinif-4.jpg"]
sinif_blocks = []
for photo, (icon, is_photo, title, text) in zip(sinif_photos, classes):
    icon_html = f'<img class="icon-img" src="{icon}" alt="">' if is_photo else f'<img class="icon" src="{icon}" alt="">'
    sinif_blocks.append(f'''<article class="block"><img class="block-photo" src="{photo}" alt="{title}"><div class="block-copy">{icon_html}<h2>{title}</h2><p>{text}</p></div></article>''')
siniflar = f'''
  <section class="wrap">
    <div class="page-title"><span class="eyebrow">Sınıflarımız</span><h2 class="section-title">Çeşitli Öğrenme Ortamları</h2></div>
    <div class="blocks">{''.join(sinif_blocks)}</div>
  </section>
'''

def gallery(folder, count, title, square=False):
    cls = "gallery square" if square else "gallery"
    buttons = []
    for i in range(1, count + 1):
        src = f"images/{folder}/{i:02d}.jpg"
        buttons.append(f'<button type="button"><img src="{src}" data-full="{src}" alt="Okul görseli {i}"></button>')
    return f'''
  <section class="wrap">
    <div class="page-title"><span class="eyebrow">{title}</span></div>
    <div class="{cls}">{''.join(buttons)}</div>
  </section>
  <div class="lightbox" role="dialog" aria-modal="true" aria-label="Görsel">
    <button class="close" type="button" aria-label="Kapat">×</button>
    <button class="nav prev" type="button" aria-label="Önceki">‹</button>
    <img alt="">
    <button class="nav next" type="button" aria-label="Sonraki">›</button>
  </div>
'''

brans = [
    (SANAT, "Sanat", "Çocukların hayal güçlerini ve ince motor becerilerini serbestçe ifade edebilecekleri boyama, seramik ve özgün tasarım atölyeleri sunuyoruz."),
    (MUZIK, "Müzik &amp; Orff Eğitimi", "Ritim duygusunu, kulak dolgunluğunu ve işitsel algıyı geliştiren ritim çalgıları ve eğlenceli müzik etkinlikleri uyguluyoruz."),
    (SPOR, "Jimnastik &amp; Çocuk Yogası", "Kaba motor becerilerini, denge ve koordinasyonu güçlendiren fiziksel aktiviteler ve eğlenceli parkur oyunları düzenliyoruz."),
    (DIL, "Yabancı Dil &amp; Dil Gelişimi", "İngilizceyi oyunlar, şarkılar ve günlük aktivitelerle doğal bir süreçte, severek öğrenmelerini sağlıyoruz."),
    (OYUN, "Matematik &amp; Akıl Oyunları", "Somut materyaller ve zekâ oyunlarıyla mantıksal düşünme, eşleştirme ve problem çözme becerilerini geliştiriyoruz."),
    (KUS, "Satranç", "Odaklanma, sabır, stratejik düşünme ve problem çözme becerilerini erken yaşta geliştiren eğlenceli satranç etkinlikleri sunuyoruz."),
]
brans_html = "\n".join(card(icon, title, text) for icon, title, text in brans)
brans_page = f'''
  <section class="wrap center">
    <span class="eyebrow">Branş Derslerimiz</span>
    <h2 class="section-title">Gelişim Alanlarımız</h2>
    <div class="grid-3" style="margin-top:28px">{brans_html}</div>
  </section>
'''

kayitlar = '''
  <section class="page-hero"><img src="images/hero.jpg" alt="Okul binası"></section>
  <section class="wrap center">
    <span class="eyebrow">Kayıtlar</span>
    <h2 class="section-title">Gelecek Yıl İçin Başvuruların Kabulü</h2>
    <h3>Ön Kayıt &amp; Randevu</h3>
    <p>Çocuğunuzun geleceğine birlikte yön vermek ve okulumuzu yakından tanımak için sizleri ağırlamaktan mutluluk duyarız. Sınırlı kontenjanlarımızdan yararlanmak ve okul turu randevusu oluşturmak için iletişim seçeneğinden formu doldurabilir veya hemen bizimle iletişime geçebilirsiniz.</p>
    <p><a class="btn" href="tel:+905324637882">Daha fazla bilgi için 05324637882</a></p>
    <p><a class="btn" href="iletisim.php">İletişim formu</a></p>
  </section>
'''

iletisim = '''
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
          <div class="icon-row"><img src="''' + SAAT + '''" alt=""></div>
          <h2>Açılış Saatimiz</h2>
          <p>Pazartesi–Cuma 08:00–17:30</p>
        </div>
        <div class="visit">
          <div class="icon-row"><img src="''' + KONUM + '''" alt=""></div>
          <h2>Bizi Ziyaret Edin</h2>
          <p>Esenbağlar Mh. 71048 Sk. No:5 Mezitli/Mersin</p>
          <p>Tel: <a href="tel:+905324637882">05324637882</a></p>
          <p>Mail: <a href="mailto:pruvaanaokulu@gmail.com">pruvaanaokulu@gmail.com</a></p>
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
      note.textContent = "Mesaj gönderilemedi. Lütfen 0532 463 78 82 numarasını arayın veya pruvaanaokulu@gmail.com adresine yazın.";
    }
  </script>
'''

pages = {
    "index.php": ("Özel Mersin Mavi Pruva Anaokulu | anaokulu | Esenbağlar, Mezitli/Mersin", index, ""),
    "hakkimizda.php": ("Hakkımızda | Özel Mersin Mavi Pruva Anaokulu", hakkimizda, ""),
    "siniflarimiz.php": ("Sınıflarımız | Özel Mersin Mavi Pruva Anaokulu", siniflar, ""),
    "gorsel-galeri.php": ("Görsel Galeri | Özel Mersin Mavi Pruva Anaokulu", gallery("galeri", 36, "Görsel Galeri"), ""),
    "okul-gorselleri.php": ("Okul Görselleri | Özel Mersin Mavi Pruva Anaokulu", gallery("okul", 17, "Okul Görselleri", square=True), ""),
    "brans-dersleri.php": ("Branş Dersleri | Özel Mersin Mavi Pruva Anaokulu", brans_page, ""),
    "kayitlar.php": ("Kayıtlar | Özel Mersin Mavi Pruva Anaokulu", kayitlar, ""),
    "iletisim.php": ("İletişim | Özel Mersin Mavi Pruva Anaokulu", iletisim, ""),
}

for name, (title, body, extra) in pages.items():
    (root / name).write_text(shell(name, title, body, extra), encoding="utf-8")
    print("wrote", name)

for old in [name.replace(".php", ".html") for name in pages]:
    stale = root / old
    if stale.exists():
        stale.unlink()
        print("removed", old)

sitemap = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for name in pages:
    loc = "https://mavipruvaanaokulu.com/" if name == "index.php" else "https://mavipruvaanaokulu.com/" + name
    sitemap.append(f"<url><loc>{loc}</loc></url>")
sitemap.append("</urlset>")
(root / "sitemap.xml").write_text("\n".join(sitemap), encoding="utf-8")
(root / "robots.txt").write_text("User-agent: *\nAllow: /\nSitemap: https://mavipruvaanaokulu.com/sitemap.xml\n", encoding="utf-8")
print("done")
