"""
Voorbeeld om een vraag te printen op basis van een .toml file
Er lijken me twee mogelijke methoden om een toets te genereren
1) genereren een .tex file (latex) van de vragen en genereer daarmee een .pdf
2) genereren direct een pdf

In alle gevallen moet de informatie uit de .toml files worden gebruikt.
"""
from pathlib import Path
import toml
from string import ascii_lowercase as abc

base_path = Path("C:\\Users\\Rolf\\githubreps\\rlo\\vragen_database")
opgavepaden = [
    Path(base_path, 'H3_Electriciteit_00000.toml'),
    Path(base_path, 'H3_Electriciteit_00001.toml'),
    Path(base_path, 'H3_Electriciteit_00002.toml')
]


def print_tabel(tabel):
    """
    Tsja, hier heb je een functie nodig die netjes een tabel print.
    Iets met tabs...
    :param tabel:
    :return:
    """
    if tabel['kop']:
        print(tabel['kop'])
    for regel in tabel['inhoud']:
        print(regel)


def print_vraag(vraag, iter=-1):
    """
    Functie om een vraag te printen
    :param vraag:
    :param iter:
    :return:
    """
    if 'tabel' in vraag.keys():
        if vraag['tabel']['boven']:
            print_tabel(vraag['tabel'])
    vraagstring = str(vraag['punten']) + "p "
    if iter > -1:
        vraagstring += abc[iter] + ") "
    vraagstring += vraag['text']
    print(vraagstring)
    if 'tabel' in vraag.keys():
        if not vraag['tabel']['boven']:
            print_tabel(vraag['tabel'])


for i_opg, opgavepad in enumerate(opgavepaden):
    opg = toml.load(opgavepad)

    print("Opgave " + str(i_opg + 1) + " : " + opg['naam'])
    if opg['text']:
        print(opg['text'])
    vragen = []
    for v in opg:
        if 'vraag' in v:
            vragen.append(v)
    vragen.sort()
    if len(vragen) > 1:
        for i, vraag in enumerate(vragen):
            print_vraag(opg[vraag], i)
    else:
        print_vraag(opg[vragen[0]])
    print("")
