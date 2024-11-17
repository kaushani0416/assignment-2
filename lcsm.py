def read_fasta_input():
    """Reads multiple lines of FASTA format DNA strings from terminal input."""
    sequences = []
    current_seq = []
    
    print("Enter your FASTA input (end input with an empty line):")
    
    while True:
        line = input().strip()
        if line == "":
            break  # End of input
        if line.startswith(">"):
            if current_seq:
                sequences.append(''.join(current_seq))
            current_seq = []
        else:
            current_seq.append(line)
    
    if current_seq:  # Append the last sequence if any
        sequences.append(''.join(current_seq))
    
    return sequences

def longest_common_substring(strings):
    """Finds the longest common substring of a collection of strings."""
    # Start with the shortest string as the base for comparison
    shortest_string = min(strings, key=len)
    n = len(shortest_string)
    longest_substrs = set()  # To store all longest substrings
    
    # Iterate through every possible substring length (longest to shortest)
    for length in range(n, 0, -1):
        for start in range(n - length + 1):
            candidate = shortest_string[start:start + length]
            # Check if candidate substring exists in all strings
            if all(candidate in s for s in strings):
                longest_substrs.add(candidate)
        if longest_substrs:  # Break once we find the longest substrings
            break
    
    # Return one of the lexicographically smallest substrings if ties exist
    return min(longest_substrs) if longest_substrs else ""

if __name__ == "__main__":
    # Read the input DNA strings
    dna_strings = read_fasta_input()
    
    if len(dna_strings) < 2:
        print("You must provide at least two DNA sequences.")
    else:
        # Find the longest common substring
        lcs = longest_common_substring(dna_strings)
        if lcs:
            print(f"The longest common substring is: {lcs}")
        else:
            print("No common substring found.")



