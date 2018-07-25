#斐波那契
import time

def fibo(num):
    if num == 0:
        res = 1
    elif num == 1:
        res = 2
    else:
        res = fibo(num-1) + fibo(num-2)
    return res

def step(n):
    listlist = []
    i = 0
    while i < n:
        listlist += [fibo(i)]
        i += 1
    return listlist[-1]

def main(n):
    print(step(n))

if __name__ == "__main__":
    start = time.clock()
    main(10)
    end = time.clock()
    print('%.5f ms'%(1000*(end-start)))