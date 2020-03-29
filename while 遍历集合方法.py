A =set("1234235")

try:
    while True:
        print(A.pop(),end="")
except:
    pass

B = [0,1,2,3,4,5,6]
del B[::3]
print(B)