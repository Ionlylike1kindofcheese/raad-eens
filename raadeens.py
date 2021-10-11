# ---------------------Preparations--------------------------------------------------------------------------------------

import random

teklein = "groter"
tegroot = "kleiner"
reallywarmoutput = "U bent heel warm"
warmoutput = "U bent warm"
geraden = "U heeft het getal geraden"
punten = 0
start = 0
stopprogram = 0

# ------------------The game-----------------------------------------------------------------------------------------------
execute = input("Start programma? Typ 'ja'. ")
if execute == "ja":
    while start != 20:
        anwser = input("wilt u een getal raden? typ dan 'ja'. wilt u stoppen? Typ dan 'nee'. ")
        if anwser == "nee":
            break
        if anwser == "ja":
            correctnumber = random.randrange(1,1000)
            numberguessed = False
            pogingen = 10
            while numberguessed == False or pogingen == 0:
                positivereallywarm = correctnumber + 20
                negativereallywarm = correctnumber - 20
                positivewarm = correctnumber + 50
                negativewarm = correctnumber - 50
                minus1 = correctnumber - 1
                plus1 = correctnumber + 1
                # ---cheat (reveal anwser)---

                print(correctnumber)

                # ---uncomment to activate---
                number = int(input("Raad een getal tussen 1 en 1000. "))
                if number == correctnumber:
                    print(geraden)
                    punten = punten + 1
                    start = start + 1
                    if start != 20:
                        print("ronde: ", str(start))
                        print("aantal punten: ", str(punten))
                    numberguessed = True
                elif number in range(correctnumber, positivereallywarm) or number in range(negativereallywarm, correctnumber):
                    print(reallywarmoutput)
                elif number in range(correctnumber, positivewarm) or number in range(negativewarm, correctnumber):
                    print(warmoutput)
                if number >= plus1:
                    print(tegroot)
                if number <= minus1:
                    print(teklein)
                if number != correctnumber:
                    pogingen = pogingen - 1
                    print("U heeft nog " + str(pogingen) + " pogingen over.")

#--------------------------final results------------------------------------------------------------------------------------------

print("aantal rondes gespeeld: ", str(start))
print("aantal punten: ", str(punten))