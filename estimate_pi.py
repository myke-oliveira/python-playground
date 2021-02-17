from random import random, seed

def estimate_pi(n):
    seed()
    qtd_inner_points = 0
    qtd_total = 0
    for _ in range(n):
        x, y = random(), random()
        distance = x**2 + y**2
        if distance < 1:
            qtd_inner_points += 1
        qtd_total += 1

    return 4 * qtd_inner_points / qtd_total

print(estimate_pi(10))
print(estimate_pi(100))
print(estimate_pi(1000))
print(estimate_pi(10000))
