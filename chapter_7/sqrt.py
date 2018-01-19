def sqrt(n):
    approx = n/2
    while True:
        better = (approx + n/approx)/2
        if abs(better - approx) < .001:
            return better
        approx = better


mysq = sqrt(25)