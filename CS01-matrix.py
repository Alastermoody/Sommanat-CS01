import numpy as np
from numpy.core.fromnumeric import reshape
MatrixOne = []
MatrixTwo = []
loop = 1 
MatrixColumns = int(input("EnterYourColumns : "))
MatrixRows - int(input("EnterYourRows : "))
while( loop <= 2):
    print("EnterYourMatrix",loop)
    for i in range(MatrixRows) :
        for j in range(MatrixColumns) :
            print("MatrixColumns [",i,",",j,"] :",end = "")
            if(loop == 1):
                MatrixOneInput = int(input("")
                MatrixOne.append(MatrixOneInput)
            else:
                MatrixTwoInput = int(input(""))
                MatrixTwo.append(MatrixTwoinput)
    loop += 1
NumpyMatrixOne = np.asarray(MatrixOne)
NumpymatrixTwo = np.asarray(matrixTwo)
NewMatrixOne=NumpyMatrixOne.reshape(MatrixRows,MatrixColumns)
NewMatrixTwo=NumpyMatrixTwo.reshape(MatrixRows,MatrixColumns)
print(NewMatrixOne,"\n=======")
print(NewMatrixTwo,"\n=======")
sum = np.add(NewMatrixOne, NewmatrixTwo)
print(sum)