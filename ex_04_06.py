def computepay(h,r):
    if (h>40):
        pay = (40*r)+((h-40)*(1.5*r))
    else:
        pay = (h*r)
    return pay

hrs = input("Enter Hours:")
h = float(hrs)
rte = input("Enter Rate:")
r = float(rte)
p = computepay(h,r)
print(p)
