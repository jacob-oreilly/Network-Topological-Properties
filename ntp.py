
## Author: Jacob O'Reilly

import numpy
import matplotlib.pyplot as plt

filename = ""
X = numpy.loadtxt(filename, dtype=int)
n = max(max(X[:,0]),max(X[:,1]))
A = numpy.zeros((n + 1,n + 1))
numNodes = X.shape[0] + X.shape[1]
cofList = []
numSum = 0
numsArray = []
numsArrayCopy = []

## CREATING A ADJACENCY MATRIX OF THE DATA
for i in range(len(X)):
    first = X[i][0]     
    second = X[i][1]
    A[first][second] = 1
    A[second][first] = 1
print("Made it through matrix creation")
##PLOTTING THE DATA
rows, cols = numpy.where(A == 1)
# allrows, allcols = numpy.where(A >= 0)
# allNodes = zip(allrows, allcols)
edges = zip(rows, cols)
for i in edges:
    plt.scatter(i[0], i[1])
plt.show()

## GETTING THE CLUSTERING COEFFICIENCE
for i in range(len(A + 1)):
    nums = 0
    print("here")
    for j in range(len(A[i])):
        if A[i][j] == 1:
            nums += 1
            print(nums)
    numsArray.append(nums)
    cc = nums / 2
    if nums >= 2:
        cof = float((float(cc)*2)/(nums * (nums - 1)))
        cofList.append(cof)
cofSum = numpy.sum(cofList)  
graphCof = cofSum/n
print(graphCof)

## Plotting (j, P(j))
u = numpy.unique(numsArray)
print(u)
edgeCountArray = []
countArray = []
newUniqueList = []
for i in range(len(u)):
    if u[i] != 0:
        newUniqueList.append(u[i])
        count = 0
        for j in range(len(numsArray)):
            if numsArray[j] != 0:
                if u[i] == numsArray[j]:
                    count += 1
        countArray.append(count)
        edgeCountArray.append((u[i], count))      
prob = 0
probArray = []
for i in edgeCountArray:
    print(i[1])
    prob = float(i[1])/len(edges)
    probArray.append(prob)
    plt.scatter(numpy.log2(i[1]), prob)
plt.show()
print(prob)
print(probArray)
