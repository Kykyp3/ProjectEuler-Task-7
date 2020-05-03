# ProjectEuler-Task-7
10001st prime

1. Made self a solution, using simple counter and bruteforce to check prime numbers, thus its is possible to run it and takes less then a minute

The solution is very unefficient, and could be enhanced by neglecting all even numbers from the computation. Thus it takes some changes, for the algorithm not to be stuck - as if we put into original code

8   ->  for i in range(3,number,2):
15  ->  number += 2

We got stuck as upper_bound would be equal to i. So just changed initial prime to 5 and count to 3 -> bit faster called Euler7_2.py

Thus, there are many ways to make the solution much faster and I've came across some solutions on web to enhace the calculation performance, links further:
