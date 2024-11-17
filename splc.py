# Codon table for translating RNA to protein
CODON_TABLE = {
    "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*",
    "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",
    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
}

def transcribe_dna_to_rna(dna):
    """Converts a DNA sequence to an RNA sequence."""
    return dna.replace("T", "U")

def translate_rna_to_protein(rna):
    """Converts an RNA sequence to a protein sequence."""
    protein = []
    for i in range(0, len(rna) - 2, 3):  # Read in codons (triplets)
        codon = rna[i:i + 3]
        amino_acid = CODON_TABLE.get(codon, "")
        if amino_acid == "*":  # Stop codon
            break
        protein.append(amino_acid)
    return ''.join(protein)

def read_fasta_input():
    """Reads input from the terminal in FASTA format and returns a dictionary of sequences."""
    print("Please input the DNA string and introns in FASTA format. End input with an empty line:")
    data = []
    current_label = None
    sequences = {}
    
    while True:
        try:
            line = input().strip()
            if not line:
                break
            if line.startswith(">"):
                current_label = line[1:]  # Remove ">" and use as label
                sequences[current_label] = ""
            else:
                sequences[current_label] += line
        except EOFError:
            break
    
    return sequences

def remove_introns(dna, introns):
    """Removes all introns from the DNA sequence."""
    for intron in introns:
        dna = dna.replace(intron, "")
    return dna

def main():
    sequences = read_fasta_input()
    
    # Extract the main DNA sequence (first entry) and introns (rest)
    labels = list(sequences.keys())
    dna = sequences[labels[0]]
    introns = [sequences[label] for label in labels[1:]]
    
    # Remove introns from the DNA sequence
    exon_only_dna = remove_introns(dna, introns)
    
    # Transcribe the exon-only DNA to RNA
    rna = transcribe_dna_to_rna(exon_only_dna)
    
    # Translate the RNA to a protein string
    protein = translate_rna_to_protein(rna)
    
    # Output the protein string
    print(protein)

if __name__ == "__main__":
    main()

