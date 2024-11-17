def reverse_complement(dna):
    """Returns the reverse complement of a DNA sequence."""
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(dna))

def find_reverse_palindromes(dna, min_len=4, max_len=12):
    """Finds all reverse palindromes in the DNA sequence."""
    results = []
    n = len(dna)
    for length in range(min_len, max_len + 1):
        for i in range(n - length + 1):
            segment = dna[i:i + length]
            if segment == reverse_complement(segment):
                results.append((i + 1, length))  # 1-based index
    return results

def main():
    # Ask for input from the user
    print("Please input the DNA string in FASTA format. End input with an empty line:")
    lines = []
    while True:
        try:
            line = input().strip()
            if not line:
                break
            lines.append(line)
        except EOFError:
            break
    
    # Combine the lines (ignoring the first line, which is the FASTA header)
    if lines[0].startswith(">"):
        dna = ''.join(lines[1:])
    else:
        dna = ''.join(lines)
    
    # Find reverse palindromes
    results = find_reverse_palindromes(dna)
    
    
    if results:
        print("Position Length")
        for position, length in results:
            print(position, length)
    else:
        print("No reverse palindromes found.")

if __name__ == "__main__":
    main()

