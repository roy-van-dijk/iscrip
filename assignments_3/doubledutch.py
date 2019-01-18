def main():
    dutchLetter = medeklinkers('dutchLetters.txt')
    print(dutchLetter['s'])
    print(dutchLetter['q'])
    print(dutchLetter['d'])
    # print(dutchLetter['e'])

    print(vertaalWoord('took', dutchLetter))
    print(vertaalWoord('BAMBOO', dutchLetter))
    print(vertaalWoord('Yesterday', dutchLetter))

    dutchLetter = medeklinkers('dutchLetters.txt')
    print(vertaal('I took a walk to the park yesterday.', dutchLetter))


def medeklinkers(path):
    file = open(path)

    # file = open('/Users/royvandijk/Documents
    # /School/iscrip/assignments_3/dutchLetters.txt')
    # /Users/royvandijk/Documents/School/iscrip/assignments_3/dutchLetters.txt

    with file as f:
        consonants = ["b", "k", "s", "c", "l", "t", "d", "m", "v", "f", "n",
                      "w", "g", "p", "x", "h", "q", "y", "j", "r", "z"]
        dict = {}
        lines = f.readlines()
        lines = [x.strip() for x in lines]
        seen = []

        for line in lines:
            letter = line[:1]
            syllable = line.split("-", 1)[1].strip() if "-" in line else ""

            try:
                assert(letter in consonants)
                assert(letter == syllable[0])
                assert(letter not in seen)
            except AssertionError as e:
                raise AssertionError("ongeldige vertaling.")

            dict[letter] = syllable
            seen.append(letter)

        try:
            assert(all(item in seen for item in consonants))
        except AssertionError as e:
            raise AssertionError("ongeldige vertaling.")

        return dict


def vertaalWoord(i, ii):
    def capIfCap(cap, l):
        return l.capitalize() if cap else l

    new_word = ""
    max_index = (len(i) - 1)
    skips = []

    for index, letter in enumerate(i):
        cap = True if letter.isupper() else False

        letter = letter.lower()

        if index != max_index:
            if letter == i[index+1].lower():
                if letter not in ii:
                    new_word += (capIfCap(cap, "s") + "quat" + letter + "h")
                    skips.append(index)
                    skips.append(index+1)
                else:
                    new_word += (capIfCap(cap, "s") + "qua" + letter)
                    skips.append(index)

        if index not in skips:
            if letter in ii:
                new_word += capIfCap(cap, ii[letter])
            else:
                new_word += capIfCap(cap, letter)

    return new_word


def vertaal(i, ii):
    separator = " "
    words = i.split(separator)
    new_words = []

    for word in words:
        new_words.append(vertaalWoord(word, ii))

    return separator.join(new_words)


if __name__ == "__main__":
    main()
