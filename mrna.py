def calculate_rna_strings(protein):
    # Codon table
    codon_table = {
        'F': 2, 'L': 6, 'S': 6, 'Y': 2, 'C': 2, 'W': 1,
        'P': 4, 'H': 2, 'Q': 2, 'R': 6, 'I': 3, 'M': 1,
        'T': 4, 'N': 2, 'K': 2, 'V': 4, 'A': 4, 'D': 2,
        'E': 2, 'G': 4, '*': 3  # '*' represents the stop codon
    }

    # Initiating the total combinations with 1
    total = 1

   
    for aa in protein:
        total *= codon_table[aa]
        total %= 1_000_000  


    total *= codon_table['*']
    total %= 1_000_000  

    return total


if __name__ == "__main__":
    protein = input("Enter the protein string: ").strip()
    result = calculate_rna_strings(protein)
    print(f"The total number of RNA strings modulo 1,000,000 is: {result}")

