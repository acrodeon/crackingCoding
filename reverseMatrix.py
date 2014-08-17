
carre = [['00', '01', '02'], ['10', '11', '12'], ['20', '21', '22']]

for row in carre:
    print (row)

size = len(carre[0])

for i in range(size):
    for j in range (i, size):
        if i != j:
            print(carre[i][j], carre[j][i])
            carre[i][j], carre[j][i] = carre[j][i], carre[i][j]

print("ROTATION 90")

for row in carre:
    print (row)
