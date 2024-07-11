import random

mu = random.gauss(mu=1.0, sigma=1.0)
if mu < 0: mu = 0.67 
print(f"The coefficient of friction is {mu:.2f}.")
