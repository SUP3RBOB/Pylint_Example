# factorial.py

import time

final_list = []

def factorial(n):

    time.sleep(.1)

    fac = 1

    for i in range (1,n+1):
        fac = fac * i

    return fac

def sum_factorial():

    for i in range(50):
        final_list.append(factorial(i))

    result=sum(final_list)

    print("Final SUM = {}".format(result))

    return result

def main():
    if __name__ == "__main__":
        sum_factorial()
