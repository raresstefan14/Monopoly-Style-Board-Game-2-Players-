import tkinter as tk
import numpy as np
import random
import matplotlib.pyplot as plt

N = 40
marime_caseta = 60
coloane = 11
randuri = 11

nume_casete = {
    0: "Start", 1: "Str. Aviatorilor", 2: "Str. Paris", 3: "Str. Polonă", 4: "Taxă de lux",
    5: "Gara de Nord", 6: "Str. Mihai Eminescu", 7: "Str. Londra", 8: "Str. Vasile Lascăr",
    9: "Bd. Dacia", 10: "Închisoare / Doar în vizită", 11: "Str. Călărași", 12: "Electricitate",
    13: "Str. Pache Protopopescu", 14: "Str. Matei Basarab", 15: "Gara Obor", 16: "Str. Iancului",
    17: "Str. Verona", 18: "Str. Traian", 19: "Str. Ferdinand", 20: "Parcare gratuită",
    21: "Str. Romană", 22: "Str. Berzei", 23: "Str. Universității", 24: "Bd. Regina Elisabeta",
    25: "Gara Filaret", 26: "Bd. Carol", 27: "Bd. Hristo Botev", 28: "Apă Canal",
    29: "Bd. Nicolae Bălcescu", 30: "Du-te la închisoare", 31: "Bd. Magheru",
    32: "Str. C.A. Rosetti", 33: "Str. Dionisie Lupu", 34: "Piața Rosetti", 35: "Gara de Sud",
    36: "Str. Academiei", 37: "Bd. Libertății", 38: "Taxă de lux", 39: "Piața Unirii"
}

proprietati_cumparabile = [
    1,2,3,5,6,7,8,9,11,12,13,14,15,16,17,18,19,
    21,22,23,24,25,26,27,28,29,31,32,33,34,35,36,37,39
]

pozitii_tabla = {}
for i in range(11):
    pozitii_tabla[i]       = (10 - i, 10)
    pozitii_tabla[10 + i]  = (0, 10 - i)
    pozitii_tabla[20 + i]  = (i, 0)
    pozitii_tabla[30 + i]  = (10, i)

def arunca_zaruri():
    return random.randint(1,6), random.randint(1,6)

P = np.zeros((N, N))
prob_zaruri = {i: sum(1 for d1 in range(1,7) for d2 in range(1,7) if d1+d2==i) / 36 for i in range(2,13)}
for i in range(N):
    for d, prob in prob_zaruri.items():
        P[i][(i + d) % N] += prob

jucatori = [
    {"pozitie":0, "bani":1500, "culoare":"red",   "inchis":False, "ture_inchisoare":0, "proprietati_detinute":[]},
    {"pozitie":0, "bani":1500, "culoare":"blue",  "inchis":False, "ture_inchisoare":0, "proprietati_detinute":[]}
]
jucator_curent = 0
joc_terminat = False
vizite_casete = [0] * N

fereastra = tk.Tk()
fereastra.title("Monopoly - 2 Jucători")
fereastra.geometry("900x850")
fereastra.configure(bg="lightgray")

panza = tk.Canvas(fereastra, width=marime_caseta * coloane, height=marime_caseta * randuri, bg="white")
panza.place(x=20, y=20)

casete = {}
etichete_casete = {}
proprietar_proprietate = [None for _ in range(N)]

for pos in range(N):
    if pos not in pozitii_tabla:
        continue
    x, y = pozitii_tabla[pos]
    x0 = x * marime_caseta
    y0 = y * marime_caseta
    x1 = x0 + marime_caseta
    y1 = y0 + marime_caseta
    dreptunghi = panza.create_rectangle(x0, y0, x1, y1, fill="lightgray", outline="black")
    eticheta = nume_casete.get(pos, "")
    panza.create_text((x0+x1)//2, (y0+y1)//2, text=str(pos), font=("Arial", 8))
    if eticheta:
        etichete_casete[pos] = panza.create_text((x0+x1)//2, y0+10, text=eticheta, font=("Arial", 6), fill="blue")
    casete[pos] = dreptunghi

marcatori = []
for jucator in jucatori:
    marker = panza.create_oval(0,0,0,0, fill=jucator["culoare"])
    marcatori.append(marker)

def actualizeaza_marcatori():
    for i, jucator in enumerate(jucatori):
        pos = jucator["pozitie"]
        x, y = pozitii_tabla[pos]
        offset = i * 20
        x0 = x * marime_caseta + 10 + offset
        y0 = y * marime_caseta + 10
        x1 = x0 + 20
        y1 = y0 + 20
        panza.coords(marcatori[i], x0, y0, x1, y1)

eticheta_status = tk.Label(fereastra, text="", font=("Helvetica", 12), bg="lightgray")
eticheta_status.place(x=marime_caseta*coloane + 40, y=20)

eticheta_zaruri = tk.Label(fereastra, text="Zaruri: -", font=("Helvetica", 12), bg="lightgray")
eticheta_zaruri.place(x=marime_caseta*coloane + 40, y=60)

eticheta_caseta = tk.Label(fereastra, text="Casetă: -", font=("Helvetica", 12), fg="blue", bg="lightgray")
eticheta_caseta.place(x=marime_caseta*coloane + 40, y=100)

buton_cumpara = tk.Button(fereastra, text="Cumpără proprietatea", state=tk.DISABLED)
buton_cumpara.place(x=marime_caseta*coloane + 40, y=140, width=200, height=30)

def afiseaza_diagrama_frecventa():
    plt.figure(figsize=(10,4))
    plt.bar(range(N), vizite_casete)
    plt.title("Frecvența vizitelor pe poziții")
    plt.xlabel("Poziție")
    plt.ylabel("Număr vizite")
    plt.tight_layout()
    plt.show()

buton_diagrama = tk.Button(fereastra, text="Afișează frecvențe", command=afiseaza_diagrama_frecventa)
buton_diagrama.place(x=marime_caseta*coloane + 40, y=180, width=200, height=30)

def incearca_cumparare():
    global jucator_curent
    jucator = jucatori[jucator_curent]
    pos = jucator["pozitie"]
    if proprietar_proprietate[pos] is None and pos in proprietati_cumparabile:
        cost = 100
        if jucator["bani"] >= cost:
            jucator["bani"] -= cost
            jucator["proprietati_detinute"].append(pos)
            proprietar_proprietate[pos] = jucator_curent
            panza.itemconfig(casete[pos], fill=jucator["culoare"])
            actualizeaza_status()
        buton_cumpara.config(state=tk.DISABLED)
        urmatorul_jucator()

def actualizeaza_status():
    j = jucatori[jucator_curent]
    pos = j["pozitie"]
    et = nume_casete.get(pos, "(Poziție obișnuită)")
    eticheta_caseta.config(text=f"Casetă: {et}")
    eticheta_status.config(text=f"Jucător {jucator_curent + 1} | Poziție: {pos} | Bani: ${j['bani']}")

def urmatorul_jucator():
    global jucator_curent
    jucator_curent = 1 - jucator_curent

def pas_urmator():
    global jucator_curent, joc_terminat
    if joc_terminat:
        return
    j = jucatori[jucator_curent]
    if j["bani"] < 0:
        eticheta_status.config(text=f"Jucător {jucator_curent + 1} a dat faliment! GAME OVER.")
        joc_terminat = True
        return
    if j["inchis"]:
        j["ture_inchisoare"] += 1
        d1, d2 = arunca_zaruri()
        eticheta_zaruri.config(text=f"Zaruri: {d1}, {d2}")
        if d1 == d2 or j["ture_inchisoare"] >= 3:
            j["inchis"] = False
            j["ture_inchisoare"] = 0
        else:
            actualizeaza_marcatori()
            actualizeaza_status()
            urmatorul_jucator()
            return
    d1, d2 = arunca_zaruri()
    eticheta_zaruri.config(text=f"Zaruri: {d1}, {d2}")
    mutare = d1 + d2
    poz_anterioara = j["pozitie"]
    j["pozitie"] = (j["pozitie"] + mutare) % N
    pos = j["pozitie"]
    vizite_casete[pos] += 1
    if pos < poz_anterioara:
        j["bani"] += 200
    if pos == 30:
        j["pozitie"] = 10
        j["inchis"] = True
        j["ture_inchisoare"] = 0
    if nume_casete.get(pos, "") == "Taxă de lux":
        j["bani"] -= 100
    proprietar = proprietar_proprietate[pos]
    if proprietar is not None and proprietar != jucator_curent:
        nr_prop = len(jucatori[proprietar]["proprietati_detinute"])
        chirie = 25 * nr_prop
        j["bani"] -= chirie
        jucatori[proprietar]["bani"] += chirie
    actualizeaza_marcatori()
    actualizeaza_status()
    if proprietar_proprietate[pos] is None and pos in proprietati_cumparabile:
        buton_cumpara.config(state=tk.NORMAL)
    else:
        buton_cumpara.config(state=tk.DISABLED)
        urmatorul_jucator()

buton_cumpara.config(command=incearca_cumparare)
buton_urmator = tk.Button(fereastra, text="Pas următor", font=("Helvetica",12), command=pas_urmator, bg="#4CAF50", fg="white")
buton_urmator.place(x=marime_caseta*coloane + 40, y=220, width=200, height=30)

actualizeaza_marcatori()
actualizeaza_status()

fereastra.mainloop()


