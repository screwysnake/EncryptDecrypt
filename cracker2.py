def citire_fisier(nume_fisier):
    with open(nume_fisier, "rb") as f:
        data = f.read()
        text = data.decode('utf-8')
    return text


def main():
    text = citire_fisier("output2")
    # valid_chars este o lista de liste
    valid_chars = []
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.!?-,:;'[] " + '"' + "\n"
    # alfabetul valid pentru input.txt este "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 " + "\n" + '"'
    for cringe_char in text:
        # vc este o lista care contine caracterele valide pentru parola
        vc = []
        # xoram fiecare caracter din alfabetul valid cu caracterul din output
        # adaugam la lista vc doar rezultatele valide
        for char in alphabet[:-13]:
            if chr(ord(char) ^ ord(cringe_char)) in alphabet:
                vc.append(char)
        valid_chars.append(vc)

    for lg in range(10, 15):
        # fixam lungimea parolei (care poate fi 10-15 caractere)
        password = []
        found = 1
        # cnt_ap este numarul de aparitii necesare al unui caracter din parola presupusa
        cnt_ap = len(text) // lg
        # cautam caracterul de pe pozitia x din parola
        for x in range(lg):
            freq = [0] * 74
            # facem frecventa caracterului de pe pozitia x in fiecare lista
            for j in range(x, len(text), lg):
                for char in valid_chars[j]:
                    freq[alphabet.index(char)] += 1
            ok = 0
            # daca frecventa unui caracter coincide cu cnt_ap atunci acesta este caracterul corect al parolei pe pozitia x 
            for i in range(len(freq)):
                if freq[i] >= cnt_ap:
                    password.append(alphabet[i])
                    ok = 1
                    break
            if ok == 0:
                found = 0
                break
        if found == 1:
            return "".join(password)

    return "hai ma frate ce-i asta"


if __name__ == "__main__":
    password = main()
    print(password)
