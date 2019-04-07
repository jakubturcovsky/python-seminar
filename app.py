#!/usr/bin/env python
import sys


# Inspired by https://www.learnpython.org
# - print(“Hello World”) from terminal
# - explain functions, indexing
# - create project, init, args, print help
# - variables, variable types, casting

def __main__():
    # To handle application arguments
    # if len(sys.argv) > 1:
    #     if sys.argv[1] == "--help":
    #         print("This is a test project, no parameters to use")
    #         return
    conditions()


def printing():
    # Printing
    print("Ahoj, mami!")
    print("Ahoj", ",", "mami", "!")

    # Formatting
    print("French greeting is %s" % "Bonjour!")
    print("my name is %s %s asdf sdfljsdlafj " % ("Good", "bye"))
    print("%d" % 42)
    print("%d %s %s" % (10, "green", "bottles"))


def obsah_obdelnika(a, b):
    obsah = a * b
    return obsah

def variables():
    # Int
    my_int = 5
    print(my_int)

    # String
    my_string = "Ahoj, tati!"
    print(my_string)

    # Float
    my_float = 5.5
    print(my_float)

    # Boolean
    boolean1 = True
    boolean2 = False
    print(boolean1, boolean2)

    # Empty variable
    c = None
    # c = 1
    print(c)

    d = 1
    d = "asdf"
    print(d)

    f = 5.5
    print(int(f))
    print(f)


# noinspection PyListCreation
def lists():
    # Basics
    my_list = ["a", "b", "c"]
    print(my_list[1])

    # Adding items
    strings = ["mates", 56]
    strings.append("hello")
    strings.append("world")
    print(strings)

    numbers = []
    numbers.append(1)
    numbers.append(2)
    numbers.append(3)

    # Removing items
    numbers.append(88)
    numbers.append(89)
    numbers.pop(3)
    numbers.remove(89)
    print(numbers)

    # Create list with name and surname
    # append age and height
    # Use the existing print() with variables from your list by accessing its items list[0]


def operators():
    # Basic mathematics
    print(1 + 2 * 3 / 4)
    result1 = 1 + 2 * 3 / 4
    print(result1)

    # Incrementation, decrementation
    x = 1
    print(x)
    x += 3
    print(x)
    x -= 5
    print(x)

    # Modulo
    remainder = 11 % 3
    print("Remainder =", remainder)

    # Power
    squared = 3 ** 2
    cubed = 3 ** 3
    print(squared)
    print(cubed)

    # String concatenation
    hello = "hello"
    world = "world"
    hello_world = hello + " " + world
    print(hello_world)

    # Repeating concatenation
    lots_of_hellos = "hello" * 10
    print(lots_of_hellos)

    # Vypocitej a vypis povrch a objem kvadru o stranach x = 3, y = 4, z = 5
    # Vypocitej a vypis povrch a objem koule o prumeru 8


def string_operations():
    question = "Do bears have claws?"

    # Length
    print("Question has %d characters" % len(question))

    # Index
    print("Index of \'s\' is %d" % question.index("s"))

    # Count
    print("There are %d characters \'a\'" % question.count("a"))

    # Substring
    print(question[4:10])
    print(question[4:15:2])  # step 2
    print(question[3:-2])  # position from end

    # Reversal = back step
    print(question[::1])
    print(question[::-1])
    print(question[::-2])

    # Uppercase
    print(question.upper())
    print(question.lower())

    # Split
    print(question.split(" "))

    # Napiste si Tristatricettri... do promenne
    # Kolik je v nem pismen 'r'?
    # Jak je dlouhy?
    # Index prvniho 'r'?
    # Substring od prvniho 'r' po posledni 'r'
    # Otoc string
    # Vypis string s krokem 3
    # Vypis otoceny string s krokem 4


def conditions():
    # Basics
    x = 2
    print(x == 2)
    print(x == 3)
    print(x < 3)
    boolean = x == 2
    print(boolean)
    print("__________")

    # Logic operators
    bool1 = True
    bool2 = False
    print(not bool1)
    print(bool1 and bool2)
    print(bool1 or bool2)

    # If-ElseIf-Else
    name = "Bart"
    if name == "Bart":
        print("Your name is Bart")
    elif name == "Lisa":
        print("Your name is Lisa")
    else:
        print("I don't know your name")

    age = 10
    if name == "Bart" and age == 10:
        print("Your name is Bart and you're 10 years old")

    if name == "Lisa" or name == "Bart":
        print("Your name is Lisa or Bart")

    if name in ["Bart", "Lisa"]:
        print("Your name is Lisa or Bart")

    # Not
    if not name == "Bart":
        print("Your name is not Bart")


def loops():
    primes = [2, 3, 5, 7]
    for prime in primes:
        print(prime)

    for x in range(3, 6):
        print(x)

    count = 0
    while count < 5:
        print(count)
        count += 1

    # Prints out 0,1,2,3,4
    count = 0
    while True:
        print(count)
        count += 1
        if count >= 5:
            break

    # Prints out only odd numbers - 1,3,5,7,9
    for x in range(10):
        # Check if x is even
        if x % 2 == 0:
            continue
        print(x)


# This is where the magic begins
__main__()
