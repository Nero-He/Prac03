"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!
import random


def contrast(score):
    if score > 50:
        return "Passable"
    elif score > 90:
        return "Excellent"
    elif score < 50:
        return "Bad"
    if score < 0 or score > 100:
        return "Invalid score"


def main():
    score = float(input("Enter score: "))
    contrast(score)
    print(contrast(score))
    a = random.randint(0, 99)
    print(a)


main()



