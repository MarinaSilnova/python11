
import matplotlib.pyplot as pit

x = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
result =[]
for i in x:
    y = 5 * i**2 + 10 * i - 30
    result.append(y)
    pit.plot(result)
    if y<0:
        pit.axhline()

pit.show()