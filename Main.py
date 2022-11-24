from time import sleep
print("Welcome adventurer to the world of Rayloft™!")
sleep(1)
while(True):
    print("""
1. New Game
2. Load Game
3. Settings
4. Input Code
5. Quit
""")
sleep(1)
while(usrinput):
    if input("Please choose an option\n>") == "1":
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
        input("\nInput Code\n>")
        sleep(1)
        print("\nINVALID CODE")
        sleep(1)
    elif usrinput == "5":
        print("\nGoodbye!\n")
        sleep(1)
        exit()

