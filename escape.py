# Room1
print("\nYou wake and quickly get up once you realize your circumstances. You've been put in some mysterious room.")
print("With no clear exits as far as you were aware. Scanning the room you spot two things.")
print("Weird writing on a WALL and a FLOWER in the corner of the room.\nDo you check the WALL or FLOWER?")

do = None
while do != "TEAPOT":
    do = input(":: ")
    if do == "WALL":
        print("\nWriting on the wall is unown to you, but you somehow decipher what is written.")
        print("It's a riddle that reads\nIT HISSES BUT IT'S NOT A SNAKE.\nIT HOLDS WATER BUT NOT A LAKE.\nWHAT AM I?")
        print("Surely answering it is your ticket out of here. So, what is the answer?")

        do = input(":: ")
        if do == "TEAPOT":
            print("\nYou say your answer out loud.")
            print("Hearing the sound of something opening, you turn around. A doorway has open and you go through it.")
            print("It's another room. This going to be fun. . . .Is what you would say if you were into puzzles.")

            # Room2
            print("\nIn this room there is PROJECTOR, a DOOR and golden RING. A bit more eventful then the first room.")

            do = None
            while do != "RING":
                do = input(":: ")
                if do == "RING":
                    print(
                        "\nYou walk over to the golden ring. It's tied to a rope and hangs from the wall in front of "
                        "you.")
                    print("For some reason it makes you think of a blue hedgehog, but hedgehogs aren't even blue.")
                    print(
                        "Without thinking you pull the ring. A doorway next to the ring opens. You go into the new "
                        "room.")

                    # Room3
                    print(
                        "\nWoah, this room is by far the best room. It's just so overwhelming. This room will "
                        "definitely take a while.")
                    print("It has a BARREL and a POTATO. Nice.")

                    do = None
                    while do != "ROLL":
                        do = input(":: ")
                        if do == "BARREL":
                            print("\nThere isn't much to the barrel. Do a barrel ROLL to see what's under?")

                            do = input(":: ")
                            if do == "ROLL":
                                print(
                                    "\nYou roll the barrel over. There's a key underneath. You take the key and shove "
                                    "it in your pocket.")
                                print("You go to the locked door in the second room and try the key.")
                                print("It turns in the keyhole, allowing you to move forward.")

                                # Room4
                                print(
                                    "\nMaybe the sarcasm caught up to you after the key room, but this room only has "
                                    "wall writing.")
                                print("Which you assumed was another riddle. In which you were right. The riddle reads")
                                print("GIVE ME FOOD AND I WILL LIVE.\nGIVE ME WATER AND I WILL DIE.\nWHAT AM I?")

                                do = None
                                while do != "FIRE":
                                    do = input(":: ")
                                if do == "FIRE":
                                    print("\nYou say your answer out loud.")
                                    print("Once again you hear sound of something opening and you turn around.")
                                    print("New doorway meaning new room, but something is going on with the riddle.")
                                    print(
                                        "The unown letters appear to be alive, when they begin moving around. Forming "
                                        "a new riddle.")
                                    print("Again, this going to be fun, if you were into puzzles. This riddle reads")
                                    print("\nI AM A CARIBBEAN SHAPE THAT MAKES SHIPS DISAPPEAR.\nWHAT AM I?")
                                    input(":: ")
                                    print("\nYou say your answer out loud.")
                                    print(
                                        "Nothing happens. Well at least you got something out of the first riddle. "
                                        "Moving on, way to go superstar.")

                                    # Room5
                                    print(
                                        "\nSome more Wall writing and BUTTONS are in this room. Short and simple does "
                                        "get you out faster.")

                                    do = None
                                    while do != "BUTTONS":
                                        do = input(":: ")
                                        if do == "BUTTONS":
                                            print(
                                                "\nThere are three buttons. A RED SQUARE, BLUE TRIANGLE and YELLOW "
                                                "CIRCLE.")
                                            print("Which one do you press?")

                                            do = None
                                            while do != "BLUE TRIANGLE":
                                                do = input(":: ")
                                                if do == "BLUE TRIANGLE":
                                                    print("\nYou push the blue triangle button.")
                                                    print("You hear the sound of a door opening from the previous room."
                                                          "")
                                                    print("You head into the new room.")

                                                    # Room6
                                                    print(
                                                        "\nYou immediately take note of the pair of giant doors. Is "
                                                        "this the last room?")
                                                    print(
                                                        "There's only a switch in this room. It feels all too easy, "
                                                        "doesn't it?\nDO or DON'T flip the switch?")

                                                    do = None
                                                    while do != "DO":
                                                        do = input(":: ")
                                                        if do == "DO":
                                                            print(
                                                                "\nYou flip the switch.\n.\n. .\n. . .\nYou hear a "
                                                                "chime and then a part in the ceiling above you opens.")
                                                            print(
                                                                "You flip the switch again in hopes that what ever "
                                                                "was up there, stays up there. It doesn't close it")
                                                            print(
                                                                "A message comes down, reading 'The End?' Why the "
                                                                "question mark, though?")
                                                            print(
                                                                "\nThe giant doors slowly open slightly blinding you "
                                                                "with the light that creeps in.")
                                                            print(
                                                                "Your eyes being adjusted to the dimly lit rooms. Once "
                                                                "your eyes adjust you see freedom awaits.")
                                                            print(
                                                                "What a strange experience you've had. Hopefully, "
                                                                "you won't have to do something like that again.")
                                                            print(" . . . . .YOU MADE IT!!! . . . . .")

                                                        elif do == "DON'T":
                                                            print(
                                                                "\nWell you kind of don't have a choice. You don't "
                                                                "want to stay here, do you?")
                                                            do = input(":: ")
                                                            if do == "NO":
                                                                print("\nDO flip the switch?")

                                                            elif do == "YES":
                                                                print(
                                                                    "\n'Oh, ok. You stayed. Not sure why.' \n   . . "
                                                                    ".You made it??? . . .")
                                                                break

                                                    print(
                                                        "\n\n                    * * * *BONUS* * * *\n              "
                                                        "Did you find the secret ending?")
                                                    print("How about all the video game references? There's a total "
                                                          "of 12.")
                                                    print("\nHINT: You might want to trigger some traps.")

                                                elif do == "RED SQUARE":
                                                    print("\nYou push the red square button.")
                                                    print("All doors shut and water begins pouring in the room.")
                                                    print(
                                                        "With no way for the water and you to escape, you'll have to "
                                                        "hold your breathe.")
                                                    print(
                                                        "\n*Insert Dark Souls YOU DIED Clip*\n . . .You didn't make "
                                                        "it. . . ")
                                                    break

                                                else:
                                                    print("\nYou push the yellow circle button.")
                                                    print("All doors shut and water begins pouring in the room.")
                                                    print(
                                                        "With no way for the water and you to escape, you'll have to "
                                                        "hold your breathe.")
                                                    print(
                                                        "\n'Looks like we have an imposter.'\n . . .You didn't make "
                                                        "it. . . ")
                                                    break

                                        elif do == "WALL":
                                            print(
                                                "\nThis wall reads\nRED MAKES ME ANGRY.\nBLUE MAKES ME SAD.\nYELLOW "
                                                "MAKES ME...")
                                            print("The last part isn't there. You'll have to go off the rest of it.")

                                else:
                                    print(
                                        "\nA cannon comes down from the ceiling and starts shooting fireballs at you.")
                                    print("You don't do a great job a dodging. Terrible job really.")
                                    print(
                                        "\n'SORRY BUT YOUR PRINCESS IS . . . Oh, wait, wrong script.'\n   . . .You "
                                        "didn't make it. . .")
                                    break

                        elif do == "POTATO":
                            print("\nInspecting the potato you find nothing. Wouldn't it be nice to be a potato?")
                            print("You hear a faint caw from somewhere. Maybe be not with birds around.")

                elif do == "PROJECTOR":
                    print("\nYou press what you think is the play button on the projector. Miraculously it works.")
                    print("You look at the screen there's a stick figure that seems to be dancing.")
                    print(".")
                    print(". .")
                    print(". . .")
                    print("It's just a distraction.")

                elif do == "DOOR":
                    print("\nLooking at the you see that there is a keyhole. You have to find the key.")

        else:
            print("\nYou say your answer out loud.")
            print("Trying to figure out what went wrong, you failed to notice the snake coming out of a hole.")
            print("You also fail to notice the snake coming towards you. Eventually it takes hold of you.")
            print("\n'Snake! What happened? Snake! Snaaaake!'\n   . . .You didn't make it. . .")
            break

    elif do == "FLOWER":
        print("\nYou go to the yellow flower in a pot.")
        print("In front is a card that reads 'Howdy, I'm Flowey. Flowey the Flower.'")
        print("Something tells you not to trust it and it fills you with determination?")
