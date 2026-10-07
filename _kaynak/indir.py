# Gorselleri Wix CDN'den yerel klasore indirir. Mevcut dosyanin uzerine yazar.
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

root = Path(r"G:\mavipruvaanaokulu.com\images")
(root / "galeri").mkdir(parents=True, exist_ok=True)
(root / "okul").mkdir(parents=True, exist_ok=True)
(root / "icons").mkdir(parents=True, exist_ok=True)

files = {
    "logo.png": "58ab6e_63a8fe4cffa545a89dd892779f1b2b56~mv2.png",
    "hero.jpg": "58ab6e_061c64416c064672b9716aeeefa3590f~mv2.jpeg",
    "hedgehog.png": "1e47b2_742c4aaf89354d1fae0e2a73498b0044~mv2.png",
    "felsefe.jpg": "58ab6e_398287bbf2314c5cac5f22c0b61885a0~mv2.jpeg",
    "serit.png": "2e2a49_93ce02fa25d342c19a5f6033c576b841~mv2.png",
    "ig.png": "11062b_55e4be1e75564866b6c28290f9a9d271~mv2.png",
    "wa.png": "11062b_1db239e728f641c3a3be5b7ca708f239~mv2.png",
    "fb.png": "11062b_2381e8a6e7444f4f902e7b649aa3f0ac~mv2.png",
    "hakkimizda.jpg": "2e2a49_559f3e28ca2f4386b2c6678ae8bbbee3~mv2.jpg",
    "psikolog.jpg": "11062b_816c4f06b94a4e928bca40ea0cc0559b~mv2.jpg",
    "sinif-1.jpg": "58ab6e_7bc1f3b4cbf84f25a92f204c58a94e91~mv2.jpeg",
    "sinif-2.jpg": "58ab6e_35cd01ed2cc04c0aa0edb37cabdde21c~mv2.jpeg",
    "sinif-3.jpg": "58ab6e_6cbb38f2eb224eb7bbfe73b6bea78d4e~mv2.jpeg",
    "sinif-4.jpg": "58ab6e_caf3c51285e744258dc5ea3b8111060c~mv2.jpeg",
}
galeri = [
    "58ab6e_32e97d3d01be42748ecd4cd86d7a2480~mv2.jpeg",
    "58ab6e_4ac0d7ea18ea4327bcc332f36f3d7487~mv2.jpeg",
    "58ab6e_83566f3dfc4d41ebad470f6e1dd5840b~mv2.jpeg",
    "58ab6e_9e20c1305f3241dd86016df8a968ac1e~mv2.jpeg",
    "58ab6e_19d6093de369454cb0ab882890b40d47~mv2.jpeg",
    "58ab6e_caf3c51285e744258dc5ea3b8111060c~mv2.jpeg",
    "58ab6e_8c582159c6794ab9911d30e1eed713db~mv2.jpeg",
    "58ab6e_19959d0f561d48d6b2064d0a7d23f40d~mv2.jpeg",
    "58ab6e_2971686a617545798835230d03603986~mv2.jpeg",
    "58ab6e_35cd01ed2cc04c0aa0edb37cabdde21c~mv2.jpeg",
    "58ab6e_5f1d692481a847ffaac630c49e2707d4~mv2.jpeg",
    "58ab6e_95291ce35e93485eb534076eef49a12f~mv2.jpeg",
    "58ab6e_7bc1f3b4cbf84f25a92f204c58a94e91~mv2.jpeg",
    "58ab6e_398287bbf2314c5cac5f22c0b61885a0~mv2.jpeg",
    "58ab6e_da1fa30a90be4c14b14f7c2ddc3910c3~mv2.jpeg",
    "58ab6e_db49711628454e0dbb7f8a9b3da795cc~mv2.jpeg",
    "58ab6e_ee652c53356c427baa56af0ed4b28587~mv2.jpeg",
    "58ab6e_073f51c09d654d1a8643dcd28661c341~mv2.jpeg",
    "58ab6e_595568e6fe224bb6a1183df513e586af~mv2.jpeg",
    "58ab6e_2132e997df244a588d7e123d795cab2e~mv2.jpeg",
    "58ab6e_0f42d5b2e16c42a7a0e9eb29856e9f07~mv2.jpeg",
    "58ab6e_f3e2f396659849349b910db5e88a42cc~mv2.jpeg",
    "58ab6e_6cbb38f2eb224eb7bbfe73b6bea78d4e~mv2.jpeg",
    "58ab6e_993f005375df40329e7ef4fa8ab4544b~mv2.jpeg",
    "58ab6e_247fcfbc930f4823bbc982590735cf03~mv2.jpeg",
    "58ab6e_7d1543ac7a304706bdd64fb4ab83ef07~mv2.jpeg",
    "58ab6e_153e04d1b0b04517a2dd92d6a2c05495~mv2.jpeg",
    "58ab6e_f6cf8593ff7447da95253e10ab770a9a~mv2.jpeg",
    "58ab6e_26a04af154ff4661b7eaf76b07b49841~mv2.jpeg",
    "58ab6e_4918c54d47544c02b69b65d2292b8bc2~mv2.jpeg",
    "58ab6e_7f323b749ad34ca0a434d85b0ad320b9~mv2.jpeg",
    "58ab6e_d6c3ee7fdf82478c8c1292ae7634d703~mv2.jpeg",
    "58ab6e_766fa5a5d8124801887aa4c05a83b3fe~mv2.jpeg",
    "58ab6e_2d2a60b97e2a4ce88195d012aa4e6434~mv2.jpeg",
    "58ab6e_9f2d45c088b749ff81c4fe2b6c8e1db4~mv2.jpeg",
    "58ab6e_91a9d41f3f3d4a5aa598d91f5abc24dd~mv2.jpeg",
]
okul = [
    "58ab6e_2dcbec0ff8974455a444fff7613080bd~mv2.jpeg",
    "58ab6e_d11709e3a987421cb4a097fd385382b4~mv2.jpeg",
    "58ab6e_928815e4ace24f888cbae2633f81ee3d~mv2.jpeg",
    "58ab6e_136be733f4ac467d9fb2fb2f53f22123~mv2.jpeg",
    "58ab6e_e6136b0d98294938af59ee930c8612a4~mv2.jpeg",
    "58ab6e_058b826b09034d04b72401c3a30f3882~mv2.jpeg",
    "58ab6e_76c32280b6cd4088b566eabe2a9e371f~mv2.jpeg",
    "58ab6e_d1ad566fc2014744914aa01af617589e~mv2.jpeg",
    "58ab6e_6822560ed75641be9d3ec29f14043295~mv2.jpeg",
    "58ab6e_d259922c3c1f498a985e319b4d4058b7~mv2.jpeg",
    "58ab6e_29c291c213eb48fc8b6a7c9290d227bb~mv2.jpeg",
    "58ab6e_3415060a58bb44aea317441cb29b5c69~mv2.jpeg",
    "58ab6e_063e73afd8f9412498ab30ad9757b01b~mv2.jpeg",
    "58ab6e_b7b2592224f44e2e9deb66fbb513bda6~mv2.jpeg",
    "58ab6e_73baa5e362df466ead6cae7f6e329b34~mv2.jpeg",
    "58ab6e_a4cd936ed7954468a653c423f2806705~mv2.jpeg",
    "58ab6e_da2af6c3847c476fb9fe43b6875599ed~mv2.jpeg",
]
svgs = [
    "11062b_93788172d8cc4931a7e2160caa259c43.svg",
    "11062b_e368f3f2ade846a8a6611947f3abb241.svg",
    "11062b_6250c5d5d61448daa12dbbddd6fba029.svg",
    "2e2a49_c52f797c3a4c48c88245e42a45c62ff2.svg",
    "2e2a49_1e2c7565947e4e72ae8b89189f317d1b.svg",
    "2e2a49_6e243609b37d464d9ca6059b53aa5217.svg",
    "2e2a49_6b6c957ab7e24a1eaa95a0e22276f108.svg",
    "2e2a49_341f12a2847c42e0ba4bbf73ce964f08.svg",
    "2e2a49_e685781283484a1fa38933f48a1f8ea4.svg",
    "11062b_b0f0013ffadd4a908c80e14e33d13fa7.svg",
    "2e2a49_319bbd73b9044a44b81e47a4f78a9a93.svg",
    "2e2a49_a23b983734c8437282ab7f798331146d.svg",
    "97f502986a6847c195bc069f8aec5d21.svg",
]
for i, mid in enumerate(galeri, 1):
    files[f"galeri/{i:02d}.jpg"] = mid
for i, mid in enumerate(okul, 1):
    files[f"okul/{i:02d}.jpg"] = mid

jobs = [(root / rel, "https://static.wixstatic.com/media/" + mid) for rel, mid in files.items()]
jobs += [(root / "icons" / name, "https://static.wixstatic.com/shapes/" + name) for name in svgs]


def fetch(item):
    dest, url = item
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            data = r.read()
            ctype = r.headers.get("content-type", "")
        if len(data) < 400 or "text/html" in ctype:
            return f"FAIL {dest.name} {len(data)} {ctype}"
        dest.write_bytes(data)
        return f"OK {dest.relative_to(root)} {len(data)}"
    except Exception as e:
        return f"ERR {dest.name} {e}"


ok = fail = 0
with ThreadPoolExecutor(max_workers=8) as ex:
    futs = [ex.submit(fetch, j) for j in jobs]
    for fut in as_completed(futs):
        line = fut.result()
        print(line)
        if line.startswith("OK"):
            ok += 1
        else:
            fail += 1
print(f"DONE ok={ok} fail={fail} jobs={len(jobs)}")
