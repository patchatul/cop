
# A while a+1 loop continues as a less than c,b=b+c
a = 1 
b = 2
c = 5
while a < c:
    a = a+1
    b = b+c
    print(a, b, c)

#B while d+1,e-1 loop until d more than f
d = 4 
e = 6
f = 7
while d < f:
    d = d + 1
    e = e - 1
    print(d, e, f)

#C while g+1 loop as g less than h
g = 4
h = 6
while g < h:
    g = g + 1
    print(g, h)

#D while j less than k m=6, j+1, while m less than n print Goodbye & m+1
j = 2
k = 5
n = 9
while j < k:
    m = 6
    while m < n:
        print("Goodbye")
        m = m + 1
    j = j + 1
    print(j,k,n)

#E while j less than k j+1, m less than n print Hello & m+1
j = 2
k = 5
n = 9
m = 6
while j < k:
    while m < n:
        print("Hello")
        m = m + 1
    j = j + 1

#F p+1 while p less than q print,r+1 while r less than q print
p = 2
q = 4
while p < q:
    print("Adios")
    r = 1
    while r < q:
        print("Adios")
        r = r + 1
    p = p + 1