# Just a normal game
# A game by Wandir

# imports
import Menu
import sys,time

# def

def slow_prt(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

answer = input("Do you want to play this game? (yes or no): ")

if answer.lower().strip() == "no":
    slow_prt("Okay then...")
    time.sleep(2)
    sys.exit(0)

if answer.lower().strip() == "yes":

    answer = input("Do you REALLY want to play this game? (yes): ").lower().strip()
    if answer == "yes":
        answer = input("Okay. You know...")
        sys.exit(0)