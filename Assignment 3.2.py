hrs = input("Enter hours: ")
try:
    h = int(hrs)
    rate = input("Enter Rate: ")
    r = float(rate)
    if h>40:
        extra = 40
        e = int(extra)
        worked = h - e
        w = int(worked)
        overtime = 1.5*r
        o = float(overtime)
        pay1 = (e*r)
        pay2 = o*w
        p1 = float(pay1)
        p2 = float(pay2)
        netpay = p1 + p2
        np = float(netpay)
        print(np)
    elif h<= 40:
        print(h*r)
except:
        print("please input a number only")