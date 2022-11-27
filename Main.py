from time import sleep
usedcodes = []
codes = ["Demo", "Aelius", "Uglyorc", "Entrance128"]
print("Welcome adventurer to the world of Rayloft™!")
while(True):
    sleep(1)
    print("""
1. New Game
2. Load Game
3. Settings
4. Input Code
5. Quit
""")
    usrinput = input("Please choose an option\n>")
    sleep(1)
    if usrinput == "1":
        print("\nInvalid Option")
    elif usrinput == "2":
        print("""
Please choose a file.

1. Rayloft
2.
3.
""")
        input(">")
        sleep(1)
        print("\nInvalid choice")
        sleep(1)
        print("\nDefaulting to file 'Rayloft'")
        if usedcodes == []:
            print("With no codes enabled.")
        else:
            for i in usedcodes:
                if len(i) == 1:
                    outputstr = "".join(usedcodes)
                else:
                    outputstr = " and ".join([", ".join(usedcodes[:-1]), usedcodes[-1]])
            print(f"With the following codes enabled: {outputstr}")
        print("(Start play)")
        sleep(1)
        exit()
    elif usrinput == "3":
        print("""
Options:

1. Ï̵̜̓n̵͈̄v̴̼̗̓́a̵͚͐̄ͅl̸̹͇̍ȋ̸̱͖͊d̶̝̭͊͐ ̷̛̳͝c̴̛̻̈ŏ̸̼̜m̴͈͓̍m̸̗̈́a̴̟̱̕n̷̻͌d̶̺͉̒
2. Į̶̙͂n̵̤̳̅͛v̷̮̳͛͒a̷̭̚l̴̻̻͋̔ỉ̸̡̖͝d̶̘͘̚ ̷̺̃̾c̵̬͍̿o̴̰͐̿m̶̟͖͋m̴͚̚a̵̦̾n̸̠̯͌̎d̸̲̾
3. Ì̸̡ņ̷͉̋͜v̵̠͕̔ã̴̡l̶̩̓̈́i̵͈̮͆͋̇d̷̖̄͛̚ ̸̗̻̰͐ć̴̯ǫ̷̀m̶̧̲̽̄͋m̸̰̹͍̌̈́ạ̶̓͊ñ̶̯̆d̸̦̠͘͝ͅd̸̗̤̞͆d̵͖̯̄͂ḍ̷̢͎̃͛͐
        """)
        input("Please select an option.\n>")
        sleep(1)
        print("\nInvalid choice")
        sleep(1)
    elif usrinput == "4":
        usrinput = input("\nInput Code\n>").capitalize()
        sleep(1)
        if usrinput in codes:
            usedcodes.append(usrinput) 
            print("\nCode Correct!")
        else:
            print("\nINVALID CODE")
        sleep(1)
    elif usrinput == "5":
        print("\nGoodbye!\n")
        sleep(1)
        exit()

