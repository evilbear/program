#进制转换和质数判断
import time

#进制转换加反转
def num_reverse(n, x):
    b, num = [], 0
    while True:
        s = n // x
        y = n % x
        b.append(y)
        if s == 0:
            break
        n = s
    b.reverse()
    for step, i in enumerate(b):
        num += i * (x**step)
    return num

#判断质数
def prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        i = 2
        while i<num:
            if num%i == 0:
                return False
                break
            i += 1
        else:
            return True

def main(n, x):
    if not prime(n):
        print('no')
    else:
        num = num_reverse(n, x)
        if prime(num):
            print('yes')
        else:
            print('no')

if __name__ == "__main__":
    start = time.clock()
    main(31, 3)
    end = time.clock()
    print('%.5f ms'%(1000*(end-start)))