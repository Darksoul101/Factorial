M = int(input())

def fund(T):
    a=5
    f=0
    while True:
        if T%5 == 0:
            while a<T:
                f = f+T/a
                a=a*5
            break
        T = T-(T%5)
    print(int(f))

if M > 1000000000:
   print('Error')
   return False
else:
    fund(M)


