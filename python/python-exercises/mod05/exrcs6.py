# pi_approximation = 4 * i / N
# x**2 + y**2 = d**2
import random
N = int(input("how many random points to generate: "))
i = 0 #(how many has generated)
n = 0 #(how many are inside the circle)
while i < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 <= 1:
        n += 1
    i += 1
    pi = 4 * n / N
print(f"Approximation of pi: {pi}")