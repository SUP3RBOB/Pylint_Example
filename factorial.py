"""Calculating factorial script."""

import time

final_list = []

def factorial(n):
    """Calculating factorial."""

    time.sleep(.1)

    fac = 1

    for i in range (1,n+1):
        fac = fac * i

    return fac

def sum_factorial():
    """Calculating sum factorial."""

    for i in range(50):
        final_list.append(factorial(i))

    result=sum(final_list)

    print(f"Final SUM = {result}")

    return result

if __name__ == "__main__":
    sum_factorial()
