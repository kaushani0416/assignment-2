def mortal_fibonacci(n, m):
    # Array to track rabbits (up to m months)
    ages = [0] * m
    # Initially, there's one pair of rabbits
    ages[0] = 1
    
    for month in range(1, n):
        # Newborns are equal to the sum of rabbits that are mature
        newborns = sum(ages[1:])
        # Shift ages: rabbits get older
        for i in range(m - 1, 0, -1):
            ages[i] = ages[i - 1]
        # The oldest age group dies and is replaced by new births
        ages[0] = newborns
    
    # Total rabbits are the sum of all alive age groups
    return sum(ages)


n = int(input("input the number of months: "))
m = int(input("input the number of rabbit pairs"))

print(mortal_fibonacci(n,m))