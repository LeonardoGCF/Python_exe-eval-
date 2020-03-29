import time
scale = 50
print("Please Wait".center(scale+8,"="))
for i in range(scale+1):
    a = "|" * i
    b = "." * (scale - i)
    c =( i/scale)*100
    print("\r{:^3.0f}%[{}->{}]".format(c,a,b),end='')
    time.sleep(0.05)
print("\n","finish".center(scale+8,"="))