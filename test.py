


b=[-1,-1]

bb=[0,0]

p=0

cc=0
c=0
l=0

k=-1

def mark(x):
    global b,p,c,cc,l,k,bb
    l+=1
    k+=1
    try:
        idx = b.index(x)
        print(k,x,'i',l,b,bb)
        return c
    except ValueError:
        print(k,x,'o',l,b,bb)
        print(abs(k-min(bb)))
        l=0
        b[p] = x
        bb[p] = k
        print('.')
        p = int(not p)
        cc += 1
        if not cc % 2:
            c += 1
        return c



_input = [2, 1, 2, 2, 3, 3, 1, 3, 5]


input2 = [2, 2, 1, 2,1,2,1,1,2,2, 3, 3, 1, 3, 5,3,4,4,2,5,3,5,2,3,4,5,5]


def mark_all(l):
    return [mark(x) for x in l]


print(input2)
print(mark_all(input2))







