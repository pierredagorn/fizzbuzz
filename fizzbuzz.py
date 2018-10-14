def getinput():
    """This is for getting the inputs in order to choose the variables"""
    validinput = False
    while not validinput:
        # Get user input
        try:
            startrange = int(input("The start of the range is?"))
            endrange = int(input("The end of the range is?"))
            mylistfizzbuzz = list(range(startrange, endrange))
            num1 = int(input("What is number 1?"))
            num2 = int(input("What is number 2?"))
            validinput = True
        except ValueError:
            print('oops, try again')
    return mylistfizzbuzz, num1, num2


def fizzbuzzalgo(thelistinfizzbuzzalgo, firstmultiple, secondmultiple):
    """This algo detect if integers in a list are multiples
    of other choosen integers."""
    listedesdeux = []
    listedupremier = []
    listedusecond = []
    for i in thelistinfizzbuzzalgo:
        if i % firstmultiple == 0 and i % secondmultiple == 0:
            print("FizzBuzz")
            listedupremier.append(i)
            listedusecond.append(i)
            listedesdeux.append(i)
        elif i % firstmultiple == 0:
            print("Fizz")
            listedupremier.append(i)
        elif i % secondmultiple == 0:
            print("Buzz")
            listedusecond.append(i)
        else:
            print(i)
        print(listedupremier)
        print(listedusecond)
        print(listedesdeux)
    return listedupremier, listedusecond, listedesdeux


def main():
    """la fonction principale"""
    mylistfizzbuzz, num1, num2 = getinput()
    fizzbuzzalgo(mylistfizzbuzz, num1, num2)
    listedupremier, listedusecond, listedesdeux = fizzbuzzalgo(mylistfizzbuzz, num1, num2)
    print("la longueur de ma liste est de", (len(mylistfizzbuzz)), "éléments")
    print("les multiples sont", num1, "et", num2)
    print("les éléments multiples de", num1, "sont", listedupremier)
    print("les éléments multiples de", num2, "sont", listedusecond)
    print("les éléments multiples de", num1,"et de", num2, "sont", listedesdeux)


main()
