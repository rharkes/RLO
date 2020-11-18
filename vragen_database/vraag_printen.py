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

opgavepaden = [
    Path(Path.cwd(), 'H3_Electriciteit_00000.toml'),
    Path(Path.cwd(), 'H3_Electriciteit_00001.toml'),
]
for i_opg, opgavepad in enumerate(opgavepaden):
    opg = toml.load(opgavepad)

    print("Opgave " + str(i_opg+1) + " : " + opg['naam'])
    print(opg['text'])
    vragen = []
    for v in opg:
        if 'vraag' in v:
            vragen.append(v)
    vragen.sort()
    if len(vragen) > 1:
        for i, vraag in enumerate(vragen):
            print(abc[i] + ") " + opg[vraag]['text'])
    else:
        print(opg[vragen[0]]['text'])
    print("")
