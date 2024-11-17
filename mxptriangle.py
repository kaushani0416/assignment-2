def maximumPerimeterTriangle(sticks):
    # Step 1: Sort the sticks in non-decreasing order
    sticks.sort()
    
    # Step 2: Check triplets from largest to smallest
    for i in range(len(sticks) - 1, 1, -1):
        a, b, c = sticks[i-2], sticks[i-1], sticks[i]
        if a + b > c:  # Triangle inequality
            return [a, b, c]
    
    # Step 3: If no valid triangle, return -1
    return [-1]

# FUNCTION FOR HECHERANK
if __name__ == "__main__":
    import sys
    input = sys.stdin.read  # Read all input at once
    data = input().split()  # Split input into parts
    n = int(data[0])  # First line is the number of sticks
    sticks = list(map(int, data[1:]))  # The remaining input is the stick lengths
    
    result = maximumPerimeterTriangle(sticks)
    if result == [-1]:
        print(-1)
    else:
        print(" ".join(map(str, result)))  
