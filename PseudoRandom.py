import random


pseudo_aleatorio = round(random.random()*100)
random.seed(23)
pseudo_aleatorio2 = round(random.random()*100)
print(f"seed não  fixado: {pseudo_aleatorio}")
print(f"seed fixado: {pseudo_aleatorio2}");