def citire_fisier(nume_fisier):
    with open(nume_fisier, "rb") as f:
        data = f.read()
        text = data.decode('utf-8')
    return text


def main():
    text = citire_fisier("output1")
    valid_chars = []
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.!?-,:;'[] " + '"' + "\n"
    print(len(text))
    for cringe_char in text:
        vc = []
        for char in alphabet[:-13]:
            if chr(ord(char) ^ ord(cringe_char)) in alphabet:
                vc.append(char)
        valid_chars.append(vc)

    for lg in range(10, 20):
        password = []
        found = 1
        cnt_ap = len(text) // lg
        for x in range(lg):
            freq = [0] * 74
            for j in range(x, len(text), lg):
                for char in valid_chars[j]:
                    freq[alphabet.index(char)] += 1
            ok = 0
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
