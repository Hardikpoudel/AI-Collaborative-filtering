import numpy as np

while True:
    def usrInput():
        # creating an empty list
        lst = []
        # as there are three values of the rating
        for i in range(3):
            ele = int(input())

            lst.append(ele)  # adding the element to the list
        return lst

    # assigning the list to a variable
    val = usrInput()

    def pearson(y):

        # value of jason is assigned to x
        x = [9, 7, 5]
        a = sum((x-np.mean(x))*(y-np.mean(y)))
        b = pow(sum(pow(x-np.mean(x), 2)), 0.5) * \
            pow(sum(pow(y-np.mean(y), 2)), 0.5)
        return a/b

    print(pearson(val))

    opinion = input("you want to continue : y/n")

    if opinion == "y":
        continue
    else:
        break
