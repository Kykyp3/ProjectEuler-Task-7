# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def find_prime():
    number=5
    prime_count=2
    while prime_count < 10001:
        for i in range(3,number,2):
            if number % i == 0:
                break
            elif i+2 == number:
                prime_count += 1
                print("Порядок простого числа:{}".format(prime_count))
                print("Простое число:{}".format(number))
        number += 2
    return number

if __name__=="__main__":
    print(find_prime())