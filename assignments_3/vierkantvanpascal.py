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
    for row_index in range(0, m):
        row = []
        for col_index in range(0, m):
            if row_index == 0:
                row.append(n)
            else:
                if col_index == 0:
                    row.append(n)
                else:
                    row.append(row[col_index-1] + square[row_index-1][col_index])
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
