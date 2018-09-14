def median(ls):
    ls.sort()
    if len(ls)%2 ==0:
        minimo = ((len(ls)-1)/2)
        maximo = (len(ls)/2)
        medio = float
        medio = (ls[int(maximo)] + ls[int(minimo)] ) /2

    else:
        position = (len(ls)+1)/2
        position -= 1
        medio = ls[int(position)]
    print (ls)
    return float(medio)








a = [9,8,7,6,5,4,3,2,1]
b = [9,8,7,6,5,4,3,2]
c = [1,2,3,4,5]
d = [4, 5, 5, 4]
f = [6, 8, 12, 2, 23]

print(median(f))