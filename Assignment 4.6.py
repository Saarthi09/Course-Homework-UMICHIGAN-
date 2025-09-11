hrs = input("Enter hours: ")
h = int(hrs)
rate = input("Enter Rate: ")
r = float(rate)
pay = "Pay "
def computepay(h,r):
    if h<= 40:
        return h*r
    elif h>40:
        extra = 40
        e = int(extra)
        worked = h - e
        w = float(worked)
        overtime = 1.5*r
        o = float(overtime)
        pay1 = e*r
        pay2 = o*w
        p1 = float(pay1)
        p2 = float(pay2)
        netpay = p1 + p2
        np = float(netpay)
        return np

p = computepay(h,r)
print("Pay ", p)
