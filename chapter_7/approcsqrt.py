

def sqrt(n):
    approx = n/2
    while True:
        better = (approx + n/approx)/2
        print(better)
        if abs(better - approx) < 0.0000001:
            
            return better
        approx = better
    
print(sqrt(25))

