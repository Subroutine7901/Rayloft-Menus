from time import sleep

usedCodes = []
codes = ["Demo", "Aelius", "Uglyorc", "Entrance128"]

print("Welcome adventurer, to the world of Rayloft™!")

while True:
    sleep(1)
    print("1. New Game \n 2. Load Game \n 3. Settings \n 4. Input Code \n 5. Quit")
    userinput = input("Please choose an option\n>")
    sleep(1)

    match userinput:
        case "1":
            print("\nInvalid Option")

        case "2":
            print("Please choose a file. \n 1. Rayloft \n 2. \n 3.")
            input(">")
            sleep(1)
            print("\nInvalid choice")
            sleep(1)
            print("\nDefaulting to file 'Rayloft'")
            if not usedCodes:
                print("With no codes enabled.")
            else:
                outputstr = str(usedCodes).replace("'", "").strip("[]")[::-1].replace(",", " and"[::-1], 1)[::-1]
                print(f"With the following codes enabled: {outputstr}")
            print("(Start play)")
            sleep(1)
            exit()

        case "3":
            print("Options: \n 1. Ï̵̜̓n̵͈̄v̴̼̗̓́a̵͚͐̄ͅl̸̹͇̍ȋ̸̱͖͊d̶̝̭͊͐ ̷̛̳͝c̴̛̻̈ŏ̸̼̜m̴͈͓̍m̸̗̈́a̴̟̱̕n̷̻͌d̶̺͉̒ \n 2. Į̶̙͂n̵̤̳̅͛v̷̮̳͛͒a̷̭̚l̴̻̻͋̔ỉ̸̡̖͝d̶̘͘̚ ̷̺̃̾c̵̬͍̿o̴̰͐̿m̶̟͖͋m̴͚̚a̵̦̾n̸̠̯͌̎d̸̲̾  \n 3. Ì̸̡ņ̷͉̋͜v̵̠͕̔ã̴̡l̶̩̓̈́i̵͈̮͆͋̇d̷̖̄͛̚ ̸̗̻̰͐ć̴̯ǫ̷̀m̶̧̲̽̄͋m̸̰̹͍̌̈́ạ̶̓͊ñ̶̯̆d̸̦̠͘͝ͅd̸̗̤̞͆d̵͖̯̄͂ḍ̷̢͎̃͛͐  \n")
            input("Please select an option.\n>")
            sleep(1)
            print("\nInvalid choice")
            sleep(1)

        case "4"
            userinput = input("\nInput Code\n>").lower().capitalize()
            sleep(1)
            if userinput in codes:
                usedCodes.append(userinput) 
                print("\nCode Correct!")
            else:
                print("\nINVALID CODE")
            sleep(1)

        case "5"
            print("\nGoodbye!\n")
            sleep(1)
            exit()