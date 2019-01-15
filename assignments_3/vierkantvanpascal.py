def main():
    print(vierkant(3))
    print(vierkant(3, 100))
    print(vierkant(4))
    print(paden(3))
    print(paden(3, 100))
    print(paden(4))
    print(paden(6))
    print(paden(8))
    print(paden(10))


def vierkant(m, n=1):
    square = []
    for rowIndex in range(0, m):
        row = []
        for colIndex in range(0, m):
            if rowIndex == 0:
                row.append(n)
            else:
                if colIndex == 0:
                    row.append(n)
                else:
                    row.append(row[colIndex-1] + square[rowIndex-1][colIndex])
        square.append(row)
    return square


def paden(m, n=1):
    rows = vierkant(m, n)
    length = len(str(max(map(max, rows))))
    output = ''

    for row in rows:
        for column in row:
            output += '\t' + str(column).rjust(length)
        output += '\n'

    return output


if __name__ == "__main__":
    main()
