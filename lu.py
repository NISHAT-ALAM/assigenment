#Solving equation by LU Decomposition
import numpy as dd

IdM=dd.identity(3)
print("Matrix A: ")
A=[]
for i in range(3):
  T=[]
  for j in range(3):
    T.append(float(input(f"A[{i+1}][{j+1}]:")))
  A.append(T)
print("Matrix B: ")
B=[]
for i in range(3):
  B.append(float(input(f"B[{i+1}][1]:")))
u11=float(A[0][0])
u12=float(A[0][1])
u13=float(A[0][2])
l21=float(A[1][0]/u11)
u22=float(A[1][1]-(l21*u12))
u23=float(A[1][2]-(l21*u13))
l31=float(A[2][0]/u11)
l32=float((A[2][1]-(l31*u12))/u22)
u33=float(A[2][2]-(l31*u13)-(l32*u23))
L=IdM
L[1][0]=l21
L[2][0]=l31
L[2][1]=l32
print("L martix: ")
for i in L:
  print(i)
U=dd.identity(3)
U[0][0]=u11
U[0][1]=u12
U[0][2]=u13
U[1][1]=u22
U[1][2]=u23
U[2][2]=u33

print("U martix: ")
for i in U:
  print(i)

Y=[]
y1=B[0]
Y.append(y1)
y2=B[1]-(y1*l21)
Y.append(y2)
y3=B[2]-(l31*y1)-(l32*y2)
Y.append(y3)
print("Y matrix: ")
print(Y)
X=[]
x3=y3/u33
x2=((y2-(u23*x3))/u22)
x1=(y1-((u12*x2)+(u13*x3)))
l1=[]
l1.append(float(x1))
l2=[]
l2.append(float(x2))
l3=[]
l3.append(float(x3))
X.append(l1)
X.append(l2)
X.append(l3)
print("X matrix: ")
print(X)
print("Verifying result: ")
print("A matrix: ")
for i in A:
  print(i)
print("LU martix: ")
print(L@U)
print("B matrix: ")
for i in B:
  print(i)
print("AX matrix:")
AX = [[0],
         [0],
         [0]]
for i in range(len(A)):
   for j in range(len(X[0])):
       for k in range(len(X)):
           AX[i][j] += A[i][k] * X[k][j]
for r in AX:
  print(r)