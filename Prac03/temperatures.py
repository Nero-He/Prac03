"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def calculate_to_fahrenheit(c):
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def calculate_to_celsius(f):
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def main():
    menu = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            calculate_to_fahrenheit()
            c = fahrenheit
            print("Result: {:.2f} F".format(c))
        elif choice == "F":
            calculate_to_celsius()
            f = celsius
            print("Result: {:.2f} C".format(c))
            # TODO: Write this section to convert F to C and display the result
            # Hint: celsius = 5 / 9 * (fahrenheit - 32)
            # Remove the "pass" statement when you are done. It's a placeholder.
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()

        print("Thank you.")


main()