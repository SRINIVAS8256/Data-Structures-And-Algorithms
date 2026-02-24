def main():
    test=2

    for test in range(0,test,1):
        p10()
        print(" ")


def p1():
    n= int(input(" enter number of rows n = "))
    for i in range(0,n,1):
        for j in range(0,n,1):
            print(" * ",end="")
        print()
        # * * * *
        # * * * *
        # * * * *
        # * * * *

def p2():
    n = int(input(" enter number of rows n  = "))
    n=n+1
    for i in range(0,n,1):
        for j in range(0,i,1):
            print("*",end=" ")
        print(" ")
        # *
        # * *
        # * * *
        # * * * *

def p3():
    n = int(input(" enter number of rows n  = "))
    n=n+1
    for i in range(0,n,1):
        for j in range(1,i+1,1):
            print( j ,end="  ")
        print("")
                # 1
                # 1  2
                # 1  2  3

def p4():
    n = int(input(" enter number of rows n  = "))
    n=n+1
    for i in range(0,n,1):
        for j in range(1,i+1,1):
            print(i,end=" ")
        print("")
                    # 1
                    # 2 2
                    # 3 3 3
                    # 4 4 4

def p5():
    n = int(input(" enter number of rows n  = "))
    for i in range(0,n,1):
        for j in range(0,n-i,1):
            print("*",end=" ")
        print("")

                # * * *
                # * *
                # *

def p6():
    n = int(input(" enter number of rows n  = "))
    n=n+1
    for i in range(0,n,1):
        for j in range(1,n-i,1):
            print(j,end=" ")
        print("")
                # 1 2 3 4 5
                # 1 2 3 4
                # 1 2 3
                # 1 2
                # 1


def p7():
    n = int(input("Enter number of rows n = "))

    for i in range(n):
        # Print spaces
        for j in range(n - i - 1):
            print(" ", end="")

        # Print stars
        for k in range(2 * i + 1):
            print("*", end="")

        print()  # Move to next line
            #    *
            #   ***
            #  *****
            # *******


def p8():
    n = int(input(" enter number of rows n  = "))
    for i in range(0,n,1):
        for j in range(i):
            print(" ",end=" ")
        for k in range(2*n-(2*i+1)):
            print("*",end=" ")
        print(" ")
            # * * * * * * *
            #   * * * * *
            #     * * *
            #       *

def p9():
    n = int(input(" enter number of rows n  = "))
    for i in range(n):
        # Print spaces
        for j in range(n - i - 1):
            print(" ", end=" ")

        # Print stars
        for j in range(2 * i + 1):
            print("*", end=" ")

        print()
    for i in range(0, n, 1):
        for j in range(i):
            print(" ", end=" ")
        for j in range(2 * n - (2 * i + 1)):
            print("*", end=" ")
        print(" ")


        # here we have merged two patterns 7 and 8

            #       *
            #     * * *
            #   * * * * *
            # * * * * * * *
            # * * * * * * *
            #   * * * * *
            #     * * *
            #       *

def p10():
    n=int(input("n = "))
    for i in range(1,2*n,1):
        stars=i
        if i > n :
            stars=2*n-i
        for j in range(stars):
            print("*",end=" ")
        print()

            # *
            # * *
            # * * *
            # * * * *
            # * * *
            # * *
            # *


def p11():




main()