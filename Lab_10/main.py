import matplotlib.pyplot as plt
import math
import numpy as np

def zav11():
    x=list(range(0,5))
    a=12
    b=21
    y = []
    for i in x:
        y.append(a*pow(i,2)-b*math.cos(i))
    plt.plot(y,linestyle ='dashed')
    plt.title('Завдання 1:\nГрафік 1')
    plt.show()

def zav12():
    x=[8,2,7,4,3,6]
    y=[9,11,1,7,6,6]
    z=[5,9,4,5,4,9]
    plt.plot(x,label='line x',marker='o',ms=17)
    plt.plot(y, 'k',label='line y', linestyle ='dashed',marker='o',ms=17,mfc = 'r')
    plt.plot(z,'r',label='line z',marker='o',ms=17,mfc = 'g')
    plt.legend(loc="upper right")
    plt.xlabel('вісь x')
    plt.ylabel('вісь y')
    plt.title('Завдання 1:\nГрафік 2')
    plt.show()

def zav13():
    activitis=['eat','sleep','work','play']
    slice=[4,8,5,6]
    mycolor=['aqua', 'green', 'red', 'blue']

    plt.annotate("Max activitis", xy=(-0.7,0.7), xytext=(-1.5, 1),
                arrowprops=dict(arrowstyle="->"))
    plt.annotate("Min activitis", xy=(0.7, 0.7), xytext=(1.5, 1),
                 arrowprops=dict(arrowstyle="->"))

    plt.pie(slice,labels=activitis,colors = mycolor,autopct='%1.1f%%')
    plt.title('Завдання 1:\nГрафік 3')
    plt.show()

def zav2():
    x=list(range(1,5))
    y=[]
    z=[]
    v=[]
    q=[]
    for i in x:
        y.append(i)
        z.append(math.exp(i))
        v.append(np.log(i))
        q.append(math.tan(i))
    plt.plot(x,y,label='Grafic y=x')
    plt.plot(x,z,label='Grafic y=exp(x)')
    plt.plot(x,v,label='Grafic y=ln(x)')
    plt.plot(x,q,label='Grafic y=tg(x)')
    plt.legend(loc="upper left")
    plt.title('Завдання 2')
    plt.show()

def zav3():
    x=np.arange(-2*math.pi,2*math.pi)
    z=[]
    for i in x:
        z.append(((1+math.sin(i))/i)*(math.sin(i)/i))
    plt.plot(z)
    plt.title('Завдання 3')
    plt.show()

zav11()
zav12()
zav13()
zav2()
zav3()









