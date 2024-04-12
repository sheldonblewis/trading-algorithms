rates = [[1, 0.48, 1.52, 0.71], [2.05, 1, 3.26, 1.56], [0.64, 0.3, 1, 0.46], [1.41, 0.61, 2.08, 1]]

max = 0
saved_max = [0,0,0,0]
first = 3
sixth = 3
 
for second in range(4):
    for third in range(4):
        for fourth in range(4):
            for fifth in range(4):
                value = rates[first][second] * rates[second][third] * rates[third][fourth] * rates[fourth][fifth] * rates[fifth][sixth]
                if value >= max:
                    max = value
                    saved_max = [second, third, fourth, fifth]

print(max, saved_max)
