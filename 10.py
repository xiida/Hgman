import random

def hangman(word):
    stage = ["---------------",
             "|       |      ",
             "|       O      ",
             "|     / | \    ",
             "|      / \     ",
             "|              ",
             "|-----------   "
             ]
    rletter = list(word)
#    rletter = word
    wrong = 0
    board = ["_"] * len(word)
#    board = []
    win = False
#    for i in range(len(rletter)):
#        board.append("_")
    while wrong < len(stage) - 1:
        cans = input("Guess the alphabet:")
        if len(cans) != 1:
            print("Please type 'one' character!")
            continue
        if cans in rletter:
            hitarr = rletter.index(cans)
            board[hitarr] = cans
#            board[hitarr] = board[hitarr].replace("_",cans)
            rletter[hitarr] = "$"
#            rletter[hitarr] = rletter[hitarr].replace(cans, "$")
#            rletter = rletter.replace(cans, "$")
            print(rletter)
            view = " ".join(board)
            print("\nHit!\n'{}'\n".format(view))
            if "_" not in board:
                win = True
        else:
            wrong += 1
            print("\n".join(stage[0:wrong + 1 ]))
        if win == True:
            print("You Win!!!")
            break
            
words = ["rope", "cat", "dog", "ichigo", "coffee"]
ramdword = words[random.randint(0, 4)]
#ramdword = words[random.randint(0, 5)]
hangman(ramdword)
