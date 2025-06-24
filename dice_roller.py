import random
import time
import sys

def rolling_animation():
    print("Rolling", end="")
    for _ in range(3):
        sys.stdout.flush()
        time.sleep(0.5)
        print(".", end="")
    print()

def roll_die():
    return random.randint(1, 6)

def main():
    print(" Welcome to the Dice Roller!")
    input("Press Enter to roll the die...")
    rolling_animation()
    result = roll_die()
    print(f"\n You rolled a {result}!\n")

if __name__ == "__main__":
    main()
