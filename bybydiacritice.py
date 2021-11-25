# Comanda de rulare a script-ului
# python bybydiacritice.py <input_file>
# Script-ul inlocuieste toate dicriticele dintr-un fisier
# cu literele corespunzatoare din alfabetul englez

import sys


class TextNormalizer():
    diacritics = "ĂăÂâÎîȘșȚțŢţ"
    substitute = "AaAaIiSsTtTt"

    def __init__(self, file_name):
        self.file_name = file_name
        self.text = ""

    def read_file(self):
        f = open(self.file_name, "r", encoding="utf-8")
        self.text = f.read()
        f.close()

    def replace_diacritics(self):
        for index, letter in enumerate(TextNormalizer.diacritics):
            self.text = self.text.replace(
                letter, TextNormalizer.substitute[index])

    def write_file(self):
        f = open(self.file_name, "w", encoding="utf-8")
        f.write(self.text)
        f.close()

    def eliminate_diacritics(self):
        self.read_file()
        self.replace_diacritics()
        self.write_file()


def main():
    text_normalizer = TextNormalizer(sys.argv[1])
    text_normalizer.eliminate_diacritics()


if __name__ == "__main__":
    main()
