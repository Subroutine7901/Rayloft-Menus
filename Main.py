from defs import *
from time import wait

usrinput = True
print("""
Welcome adventurer to the world of Rayloft:tm:!

1. New Game
2. Load Game
3. Settings
4. Input Code
5. Quit
""")
wait(1)
while(usrinput):
    if input("Please choose an option\n>") == 1:
        print("""
        Please choose a file.

        1. Rayloft
        2.
        3.
        """)
        input(">")
        print("Invalid choice")
        wait(0.5)
        print("Defaulting to file 'Rayloft'")
        print("(Start play)")
