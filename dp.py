#动态规划
import time
import numpy as np

def fun1(price):
    day = len(price)
    profit_list = np.array([[0]*day]*day)
    for i in range(1, day):
        m = 0
        n = m + i
        while n < day:
            n_m = price[n] - price[m]
            if (n - m) == 1:
                profit_list[m][n] = n_m
            elif (n - m) < 4:
                profit_list[m][n] = max(profit_list[m+1][n], profit_list[m][n-1], n_m)
            else:
                temp = [profit_list[m+1][n], profit_list[m][n-1], n_m]
                for a in range(m+2, n-1):
                    temp.append(profit_list[m][a-1]+profit_list[a+1][n])
                profit_list[m][n] = max(temp)
            m += 1
            n += 1
    # print(profit_list)
    return profit_list[0][day-1]

def main(price):
    print('最大利润:'+str(fun1(price)))

if __name__ == "__main__":
    start = time.clock()
    main([3, 4, 5, 1, 3])
    end = time.clock()
    print('%.5f ms'%(1000*(end-start)))