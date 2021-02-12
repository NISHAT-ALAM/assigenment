#Bisection Method
import math

def fun(x):
  return (5*x*math.log10(x))-6

def xr(a,b):
 return (a+b)/2

lst_x=[0,0,0,0,0,0,0,0,0,0]

for i in range(1,5):
 if (fun(i)*fun(i+1)<0):
   a=i
   b=i+1
   break
x_r=xr(a,b)
print("a=",a,", b=",b, "Xr=",x_r, "f(xr)=",fun(x_r))
for i in range (10):
 lst_x[i-1]=x_r
 if(fun(a)*fun(x_r))<0:
   b=x_r
 else:
   a=x_r
 x_r=xr(a,b)
 print("a=",a,", b=",b, " Xr=",x_r, " f(xr)=",fun(x_r))
print(lst_x)