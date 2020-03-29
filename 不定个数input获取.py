def getNum():
    nums = []
    Str = input('请输入')
    while Str != '':
        nums.append(eval(Str))
        Str = input()
    return nums