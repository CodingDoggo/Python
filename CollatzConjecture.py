import matplotlib.pyplot as plt
from numpy import equal

def CollatzConjecture(n):
    list = []
    while True:
        if n==1:
            list.append(n)
            break

        if n%2==1:
            list.append(n)
            n = n*3+1
        else:
            list.append(n)
            n = n/2
    return list

n = 341
newlist = CollatzConjecture(n)
list = []
i=0

while i!=len(newlist):
      list.append(i)
      i=i+1


plt.plot(list,newlist,'H-.r',mec='y',mfc='b',ms='10')
plt.title("Collatz Conjecture for number " + str(n) + "\n \n" + str(newlist))
plt.show()
