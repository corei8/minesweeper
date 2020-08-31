import time
from random import randint


chart = [
        ["O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O"]
]

for e in range(0, len(chart)):
    for f in range(0, len(chart)):
        y = randint(0, 6)
        if y != 5:
            chart[e][f] = "O"
        else:
            chart[e][f] = "X"

mem = []


def PrintBoard():
    # make this dynamic:
    print("\n0  1 2 3 4 5\n")
    for y in range(0, len(chart)):
        z = str(y+1) + "  "
        pool = []
        for x in mem:
            if x[0] == y:
                pool.append(x[1])
            else:
                continue
        for r in range(0, len(chart[y])):
            if r in pool:
                if chart[y][r] == "X":
                    z = z + "X "
                else:
                    z = z + "O "
            else:
                z = z + "* "
        print(z)
    print("")


user = ""

while user != "quit":
    PrintBoard()
    user = input("Enter Coordinates (H L) ('quit' to exit game): ")
    print("")
    if user == "quit":
        break
    else:
        try:
            y = int(str(user).split(" ")[0])-1
            x = int(str(user).split(" ")[1])-1
            time.sleep(0.3)
            mem.append([y, x])
            if chart[y][x] == "X":
                PrintBoard()
                print("You Loose! Too Bad!!! :(")
                user = "quit"
                break
            else:
                continue
        except IndexError:
            print("\nHmmm... something's not right!")
            print(" - The coordinate is not within the minefield")
            print(" - Or, you did not enter them the right way: H L")
            print("Please try again.\n")
