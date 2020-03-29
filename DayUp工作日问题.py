dayup = 1.0
dayfactor = 0.01
for i in range(365):
    if i %7 in [6,0]:
        dayup = dayup * (1 - dayfactor)
    else:
        dayup = dayup * (1 + dayfactor)
print("{:.2f}".format(dayup))

def dayUP(df):
    Dayup = 1.0

    for i in range( 365 ):
        if i % 7 in [6, 0]:
            Dayup = Dayup * (1 - 0.01)
        else:
            Dayup = Dayup * (1 + df)
    return Dayup

dayf = 0.01
while dayUP(dayf)< 37.78:
    dayf = dayf + 0.001
print("{:.3f}".format(dayf))
