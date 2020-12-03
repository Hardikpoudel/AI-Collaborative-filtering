#!/usr/bin/python3
import math

while True:
    def userInput():
        # creating an empty list

        lst = []
        # number of elemetns as input
        n = int(input("Enter number of elements : "))
        # iterating till the range

        for i in range(0, n):
            ele = int(input())

            lst.append(ele)  # adding the element

        tupl = tuple(lst)  # converting list into tuple

        return tupl  # print tuple

    # assigning the returned value of a function to a variable
    tupel = userInput()
    print(tupel)

    #lisa = (3.5, 3.5, 2.5)
    # calculating euclidean distance between two points

    def distance():
        # setting the jason as the default value
        jason = (9, 7, 5)
        # calculating distance
        dist = math.sqrt(sum([(a-b)**2 for a, b in zip(jason, tupel)]))

        # calculating similarity using the distance value
        simScore = 1/(1+dist)
        print("distance", simScore)

    # calling discount function for calculating the similarity
    distance()
    # asking if they want to continue
    opinion = input("you want to continue : y/n")

    if opinion == "y":
        continue
    else:
        break
