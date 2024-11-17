def parse_fasta():
    """Reads FASTA input from the terminal and returns a list of sequences."""
    print("Please input the DNA strings in FASTA format. End input with an empty line:")
    sequences = []
    current_seq = []
    
    while True:
        try:
            line = input().strip()
            if not line:
                break
            if line.startswith(">"):
                if current_seq:
                    sequences.append("".join(current_seq))
                    current_seq = []
            else:
                current_seq.append(line)
        except EOFError:
            break
    
    if current_seq:
        sequences.append("".join(current_seq))
    
    return sequences

def count_transitions_transversions(s1, s2):
    """Counts the number of transitions and transversions between two DNA strings."""
    transitions = 0
    transversions = 0
    
    for a, b in zip(s1, s2):
        if a != b:  # Mismatch
            if (a, b) in [("A", "G"), ("G", "A"), ("C", "T"), ("T", "C")]:
                transitions += 1
            else:
                transversions += 1
    
    return transitions, transversions

def main():
    sequences = parse_fasta()
    
    if len(sequences) != 2:
        print("Error: Please provide exactly two DNA sequences in FASTA format.")
        return
    
    s1, s2 = sequences
    if len(s1) != len(s2):
        print("Error: The two DNA strings must have the same length.")
        return
    
    transitions, transversions = count_transitions_transversions(s1, s2)
    
    if transversions == 0:
        print("Error: Division by zero (no transversions). The ratio cannot be calculated.")
    else:
        ratio = transitions / transversions
        print(f"Transition/Transversion Ratio: {ratio:.3f}")

if __name__ == "__main__":
    main()

