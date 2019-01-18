def main():
    print(leesBord('tictactoe1.txt'))
    print(toonBord(['OX ', 'OX ', ' X ']))
    print(toonBord(['XXO', 'OOX', 'XOX']))
    print(winnaar(['OX ', 'OX ', ' X ']))
    print(winnaar(['OOO', ' XX', 'X  ']))
    print(winnaar([' XO', ' OX', ' OX']))


def leesBord(path):
    file = open(path)
    with file as f:
        lines = f.readlines()
        lines = [x.strip("\n") for x in lines]
        board = []

        for line in lines:
            board.append(line)

        return board


def toonBord(rows):
    board = ""
    for row in rows:
        formatted = ""
        for char in row:
            if char == " ":
                formatted += "."
            else:
                formatted += char
            formatted += " "
        board += formatted.strip() + "\n"

    return board


def winnaar(rows):
    def isEqual(arr, p0, p1, p2):
        return arr[0] != " " and arr[p0] == arr[p1] and arr[p0] == arr[p2]

    cells = list(''.join(map(str, rows)))
    winning_cells = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],

        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],

        [0, 4, 8],
        [2, 4, 6]
    ]

    for cell in winning_cells:
        if isEqual(cells, cell[0], cell[1], cell[2]):
            return cells[cell[0]] + " wint"

    return "gelijkspel"


if __name__ == "__main__":
    main()
