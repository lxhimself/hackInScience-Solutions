import re

text = """This is a sampletext.
But dont worry, we can do this.
Or not. Idontreallyknowbutwhocares."""


def longest_word(text):
    wortliste = (re.split(" |\n", text))
    ergebnis = ""
    i = 0
    while i < len(wortliste):
        for x in wortliste:
            if len(x) < len(ergebnis):
                i += 1
            else:
                ergebnis = x 
                i += 1
    print(ergebnis)


longest_word(text)

