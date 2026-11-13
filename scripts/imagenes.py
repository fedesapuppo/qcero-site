import os, re, sys, subprocess, unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORIGEN = sys.argv[1]
DESTINO = os.path.join(RAIZ, "assets/img")
PATRON = re.compile(r"\b(\d{4}_\d{2}_[^\s\"'\]]+?\.(?:jpe?g|png|gif|webp))\b", re.I)

def nombre(original):
    base = os.path.splitext(original)[0]
    base = unicodedata.normalize("NFKD", base).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", base.lower()).strip("-") + ".webp"

def convertir(original, final):
    fuente = os.path.join(ORIGEN, original)
    for carpeta, ancho in (("", 1600), ("s", 640)):
        salida = os.path.join(DESTINO, carpeta, final)
        if os.path.exists(salida):
            continue
        os.makedirs(os.path.dirname(salida), exist_ok=True)
        subprocess.run(["magick", fuente + "[0]", "-auto-orient", "-strip", "-resize", f"{ancho}x{ancho}>", "-quality", "74", salida], check=True)

faltan = set()
for dirpath, _, archivos in os.walk(RAIZ):
    if any(p in dirpath for p in ("/.git", "/_site", "/assets", "/scripts", "/vendor")):
        continue
    for a in archivos:
        if not a.endswith((".md", ".html", ".yml")):
            continue
        ruta = os.path.join(dirpath, a)
        texto = open(ruta, encoding="utf-8").read()
        def reemplazo(m):
            original = m.group(1)
            if not os.path.exists(os.path.join(ORIGEN, original)):
                faltan.add(f"{a}: {original}")
                return original
            final = nombre(original)
            convertir(original, final)
            return final
        nuevo = PATRON.sub(reemplazo, texto)
        if nuevo != texto:
            open(ruta, "w", encoding="utf-8").write(nuevo)

for f in sorted(faltan):
    print("FALTA", f)
