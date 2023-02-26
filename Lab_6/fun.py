import math

def fB(x,y,z):
  b1=(pow(abs(z),0.3))/x
  b2=pow(math.tan((x+z*z)/(2*x-1.4)),2)
  b3=y*pow(abs(b1+b2),(1/3))
  b4=z*pow(math.e,(x*x-y))
  b=b3-b4
  return b

def fA(x,y,z,fB):
  a1=pow((1+y),2)
  a2=(pow(abs(x+y),0.3))/fB(x,y,z)*fB(x,y,z)+z
  a3=1+pow(math.e,-(x-z))+pow(abs(y),0.43)
  a=a1*(a2/a3)
  return a