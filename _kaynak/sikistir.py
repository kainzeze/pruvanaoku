# Web icin JPEG/PNG boyutunu dusurur. Orijinaller images/_orijinal altina kopyalanmaz;
# islem oncesi her dosyanin yedegi images/_yedek altina alinir.
import shutil
import urllib.request
from pathlib import Path
from PIL import Image

root = Path(r"G:\mavipruvaanaokulu.com\images")
backup = root / "_yedek"
backup.mkdir(exist_ok=True)

hak = root / "hakkimizda.jpg"
if not hak.exists():
    urls = [
        "https://static.wixstatic.com/media/2e2a49_559f3e28ca2f4386b2c6678ae8bbbee3~mv2_d_6000_3876_s_4_2.jpg",
        "https://static.wixstatic.com/media/2e2a49_559f3e28ca2f4386b2c6678ae8bbbee3~mv2.jpg/v1/fill/w_1800,h_1164,al_c,q_85/hakkimizda.jpg",
    ]
    for url in urls:
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": "Mozilla/5.0",
                "Referer": "https://www.mavipruvaanaokulu.com/",
            })
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            print("hakkimizda", url[:80], len(data), data[:8])
            if len(data) > 2000 and data[:3] != b"<!D":
                hak.write_bytes(data)
                break
        except Exception as e:
            print("hakkimizda fail", e)

for src in root.rglob("*"):
    if not src.is_file() or "_yedek" in src.parts:
        continue
    if src.suffix.lower() not in {".jpg", ".jpeg", ".png"}:
        continue
    rel = src.relative_to(root)
    dest = backup / rel
    if not dest.exists():
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)

def shrink(path: Path):
    im = Image.open(path)
    im = im.convert("RGB") if path.suffix.lower() in {".jpg", ".jpeg"} else im
    w, h = im.size
    max_side = 1600 if path.name != "logo.png" else 700
    if max(w, h) > max_side:
        scale = max_side / max(w, h)
        im = im.resize((int(w * scale), int(h * scale)), Image.Resampling.LANCZOS)
    if path.suffix.lower() == ".png" and path.name == "logo.png":
        im.save(path, "PNG", optimize=True)
    elif path.suffix.lower() == ".png":
        return
    else:
        im.save(path, "JPEG", quality=82, optimize=True, progressive=True)

for src in list(root.rglob("*")):
    if not src.is_file() or "_yedek" in src.parts:
        continue
    if src.suffix.lower() not in {".jpg", ".jpeg", ".png"}:
        continue
    before = src.stat().st_size
    if before < 180_000 and src.name != "logo.png":
        continue
    try:
        shrink(src)
        after = src.stat().st_size
        print(f"{src.relative_to(root)} {before//1024}KB -> {after//1024}KB")
    except Exception as e:
        print("skip", src, e)

# serit alpha
serit = Image.open(root / "serit.png")
print("serit mode", serit.mode, serit.size)
