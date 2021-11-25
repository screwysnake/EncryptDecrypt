import sys


def main():
    script_name, password, input_file, output_file = sys.argv

    f = open(input_file, "r")
    text = list(f.read())
    f.close()

    j = 0
    for i in range(len(text)):
        text[i] = chr(ord(text[i]) ^ ord(password[j % len(password)]))
        j += 1
    text = "".join(text)

    f = open(output_file, "wb")
    f.write(text.encode("utf-8"))
    f.close()


if __name__ == "__main__":
    main()
