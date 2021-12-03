def citire_fisier(nume_fisier):
    with open(nume_fisier, "r") as f:
        text = f.read()
    return text


def main():
    input_text = citire_fisier("input2.txt")
    output_text = citire_fisier("output2")
    for lg in range(10, 16):
        password = []
        for i in range(0, 2 * lg):
            password.append(chr(ord(input_text[i]) ^ ord(output_text[i])))
        if password[0:lg] == password[lg:]:
            return "".join(password[0:lg])


if __name__ == "__main__":
    print(main())
