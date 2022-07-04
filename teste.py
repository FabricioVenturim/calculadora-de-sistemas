import numpy as np

matrix = np.array([[6,3,2,1],  
                   [3,2,5,0],  
                   [4,5,4,3]], dtype="double") 

for coluna in range(3, (len(matrix[0]) - 1)):
    print(coluna)