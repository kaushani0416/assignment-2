import itertools

def generate_permutations(n):
    # Generate the list of integers from 1 to n
    numbers = list(range(1, n + 1))
    
    # Generate all permutations using itertools.permutations
    permutations = list(itertools.permutations(numbers))
    
    # Print the total number of permutations
    print(f"Total permutations: {len(permutations)}")
    
    # Print each permutation
    for perm in permutations:
        print(perm)

if __name__ == "__main__":
   
    n = int(input("Enter a positive integer n (≤ 7): "))
    
    # Ensure n is within the valid range
    if 1 <= n <= 7:
        generate_permutations(n)
    else:
        print("Please enter a number between 1 and 7.")
