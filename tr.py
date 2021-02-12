def calc_b(a,b):
  if(len(b)<=0):
    return 0
  else:
    return calc_b(a[1:],b[0:-1])+(a[0]*b[-1])

def calc_x(b1,b2):
  return b1/b2


n=int(input("Enter num of a: "))
a=list()
for i in range(n):
  v=float(input(f"a{i+1}:"))
  a.append(v)

b=[]
b.append(1)
b.append(a[0])
for j in range(2,n):
  #print(a[0:j],b[0:j])
  b.append(calc_b(a[0:j],b[0:j]))
print(b)
x=[]
for k in range(n-1):
  x.append(calc_x(b[k],b[k+1]))
print(f"So, the root is: {round(min(x))}")