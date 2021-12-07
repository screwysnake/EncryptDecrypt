import time
def citire_fisier(nume_fisier):
    with open(nume_fisier, "rb") as f:
        data = f.read()
        text = data.decode('utf-8')
    return text


def main():
    text = citire_fisier("output_ruxi12")
    # valid_chars este o lista de liste
    valid_chars = []
    password_alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    text_alphabet = password_alphabet + "-=~!@#$%^&*()_+,./;'[]\<>?:\"}{|—" + "\n" + " " + "\t"
    # alfabetul valid
    for cringe_char in text:
        # vc este o lista care contine caracterele valide pentru parola
        vc = []
        # xoram fiecare caracter din alfabetul valid cu caracterul din output
        # adaugam la lista vc doar rezultatele valide
        for char in password_alphabet:
            if chr(ord(char) ^ ord(cringe_char)) in text_alphabet:
                vc.append(char)
        valid_chars.append(vc)

    for lg in range(10, 16):
        # fixam lungimea parolei (care poate fi 10-15 caractere)
        password = []
        found = 1
        # cnt_ap este numarul de aparitii necesare al unui caracter din parola presupusa
        cnt_ap = len(text) // lg
        # cautam caracterul de pe pozitia x din parola
        for x in range(lg):
            freq = [0] * len(text_alphabet)
            # facem frecventa caracterului de pe pozitia x in fiecare lista de la pozitia x + k * lg, unde 0 <= k <= cnt_ap
            for j in range(x, len(text), lg):
                for char in valid_chars[j]:
                    freq[text_alphabet.index(char)] += 1
            ok = 0
            # daca frecventa unui caracter coincide cu cnt_ap atunci acesta este caracterul corect al parolei pe pozitia x 
            for i in range(len(freq)):
                if freq[i] >= cnt_ap:
                    password.append(text_alphabet[i])
                    ok = 1
                    break
            if ok == 0:
                found = 0
                break
        if found == 1:
            return "".join(password)

    return "hai ma frate ce-i asta"


if __name__ == "__main__":
    start_time = time.time()
    password = main()
    end_time = time.time()
    print(password)
    time_real = end_time - start_time
    print(f"Timpul de executare este {time_real} secunde")
