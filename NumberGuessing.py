playerNumber = "58"
correctNumber = "58"
FIRST = "This number is too high. Please try again."
SECOND = "This number is too low. Please try again."
THIRD = "Correct!"

if (playerNumber > correctNumber):
    print(FIRST)
else:
    if (playerNumber < correctNumber):
        print(SECOND)
    else:
        if (playerNumber == correctNumber):
            print(THIRD)