def maximumToys(prices, k):
    # Step 1: Sort the toy prices in ascending order
    prices.sort()
    
    # Step 2: Count how many toys Mark can buy
    total_cost = 0
    count = 0
    for price in prices:
        if total_cost + price <= k:
            total_cost += price
            count += 1
        else:
            break  # Stop once the budget is exceeded
    return count

# FUNCTION FOR HECHERANK
if __name__ == "__main__":
    import sys
    input = sys.stdin.read  # Read all input at once
    data = input().split()  # Split input into parts
    
    #  number of toys and budget
    n, k = map(int, data[0:2])
    #  prices of toys
    prices = list(map(int, data[2:]))
    
    
    result = maximumToys(prices, k)
    print(result)
