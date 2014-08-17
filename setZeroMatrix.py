##Write an algorithm such that if an element in an MxN matrix is 0,
##its entire row and column is set to 0.

matrix = [[2,0,1], [1,1,1], [2,2,1]]
print(matrix)


nbRows = len(matrix)
if nbRows > 0:
    nbColumns = len(matrix[0])
    rows = set()
    columns = set()
    for i in range(nbRows):
        for j in range(nbColumns):
            if (matrix[i][j] == 0):
                columns.add(j)
                rows.add(i)
                break

for i in rows:
    for j in range(nbColumns):
        matrix[i][j] = 0

for j in columns:
    for i in range(nbRows):
        matrix[i][j] = 0

print("if an element in an MxN matrix is 0, entire row and column is set to 0")
print(matrix)
