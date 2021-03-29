"""
File: nimm.py
-------------------------
Looks like now everything sounds. However there is a bug in a concept, that would require improvement.
After the recall for correct answer, the program will accept also different numbers than 1 and 2.
Sorry for not relevant comments to the code, but it's quite late already.
Have a good day!
"""
# we start with box of 20 stones
# two players makes a move alternately
# there are just two moves
# remove1 - remove 1 stone
# remove2 - remove 2 stones
# give answer
# the winner is opposite to the player who removed last stone

def ask_for_answer(i):
    answer = int(input("Player " + str(i) + " would you like to remove 1 or 2 stones? "))
    inputisinvalid = (answer != 1) and (answer != 2)
    while inputisinvalid:
        answer = int(input("Please enter 1 or 2: "))
        break
    print("")
    return answer

def main():
    box = 20
    while box > 0:
        for i in range(1, 3):
            print("There are " + str(box) + " stones left")

            answer = ask_for_answer(i)

            box -= answer
            if box == 0:
                break

    show_winner(i)

def show_winner(i):
    if i == 1:
        print("Player " + str(i +1) + " wins!")
    else:
        print("Player " + str(i - 1) + " wins!")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()