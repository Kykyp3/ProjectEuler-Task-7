# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def poisk():
    number=3
    poryadok=1
    while poryadok < 10001:
        for i in range(2,number,1):
            if number % i == 0:
                break
            elif i+1 == number:
                poryadok += 1
                print("Порядок простого числа:{}".format(poryadok))
                print("Простое число:{}".format(number))
        number += 1
    return number

if __name__=="__main__":
    print(poisk())



