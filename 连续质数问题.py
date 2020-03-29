def prime(m):
    for i in range(2,m):
        if m%i == 0:
            return False
    else:
        return True

n = eval(input())

num = int(n)
num=num+1 if num<n else num

count = 5

while count >0 :
    if prime(num):
        if count >1:
            print(num,end=',')
        else:
            print(num,end='')
        count-=1
    num+=1

'''
#输出时最后一个不带逗号，其他都带 ，方法：
1。
t = ""
...
t += "{},".format(str(a))
...
print(t[:-1]) #最后一个字符,不输出
2。

t = []
...
t.append(str(a))
...
print(','.join(t))
'''