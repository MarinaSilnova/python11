#Имеются данные о площади и стоимости 15 домов.
#Риелтору требуется узнать в каких домах стоимость квадратного метра меньше 50000 рублей.
#Предоставьте ему графические данные о стоимости квадратного метра каждого дома и список подходящих ему домов, отсортированных по площади.
#Данные о домах сформируйте случайным образом. Площади от 100 до 300 кв. метров, цены от 3 до 20 млн.

import matplotlib.pyplot as pit
import random

sqrt = []
price = []
result = []

for i in range(15):
    sqrt.append(random.randint(100,300))
    price.append(random.randint(3000000,20000000))
    y = price[i]/sqrt[i]
    result.append(y)
    pit.plot(result, 'ro')
    pit.axhline(y = 50000)
    

print(sqrt)
print(price)
print(result)



pit.show()
