import sys


def main():
    script_name, password, input_file, output_file = sys.argv

    f = open(input_file, "rb")
    data = f.read()
    text = data.decode('utf-8')
    #text = f.read()
    f.close()

    text = list(text)
    j = 0
    for i, char in enumerate(text):
        text[i] = chr(ord(text[i]) ^ ord(password[j % len(password)]))
        j += 1
    text = "".join(text)

    f = open(output_file, "w")
    f.write(text)
    f.close()


if __name__ == "__main__":
    main()
