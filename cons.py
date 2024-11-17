import sys

def read_fasta_from_input():
    """Reads multiple lines of FASTA format DNA sequences from terminal input."""
    seq = []
    cur_seq = ""
    print("Enter your FASTA input (end input with an empty line):")
    
    while True:
        line = input().strip()
        if line == "":
            break  # End of input
        if line.startswith(">"):  # Header line in FASTA
            if cur_seq:
                seq.append(cur_seq)
            cur_seq = ""
        else:
            cur_seq += line
    
    if cur_seq:  
        seq.append(cur_seq)
    
    return seq

def gen_matrix(seq):
    """Generates a position matrix from the list of DNA sequences."""
    n = len(seq[0])  # Assuming all sequences are of equal length
    p_mat = {'A': [0] * n, 'C': [0] * n, 'G': [0] * n, 'T': [0] * n}
    for s in seq:
        for j in range(n):
            base = s[j]
            p_mat[base][j] += 1
    return p_mat

def gen_string(p_mat, n):
    """Generates the consensus string from the position matrix."""
    consensus = []
    for j in range(n):
        max_count = -1
        max_base = ''
        
        for base in 'ACGT':
            if p_mat[base][j] > max_count:
                max_count = p_mat[base][j]
                max_base = base
                
        consensus.append(max_base)
    
    return ''.join(consensus)

def print_matrix(p_mat):
    """Prints the position matrix."""
    for base in 'ACGT':
        print(f"{base}: {' '.join(map(str, p_mat[base]))}")

if __name__ == "__main__":
    # Read the FASTA format input from the terminal
    seq = read_fasta_from_input()
    
    if not seq:
        print("No sequences provided.")
    else:
        # Generate the position matrix and consensus string
        p_mat = gen_matrix(seq)
        consensus_string = gen_string(p_mat, len(seq[0]))
        
        # Print the consensus string and the position matrix
        print(f"Consensus String: {consensus_string}")
        print("\nPosition Matrix:")
        print_matrix(p_mat)








