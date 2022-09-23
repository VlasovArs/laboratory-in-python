a = [int(input()) for k in range(10)]    #Генератор массива а
i=int(input())    #1 индекс
j=int(input())    #2 индекс
if a[i]*a[j]>0:
    a[i],a[j]=a[j],a[i]
else:
    for m in range(i+1,j):    #Все элементы между i и j
        a[m]=0
print(a)
