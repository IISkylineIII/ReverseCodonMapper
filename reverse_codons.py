# reverse_codons.py

def reverse_genetic_code(genetic_code):
    """
    Creates a reverse dictionary where amino acids point to all codons that encode them.
    """
    reverse_code = {}
    for codon, amino_acid in genetic_code.items():
        if amino_acid not in reverse_code:
            reverse_code[amino_acid] = []
        reverse_code[amino_acid].append(codon)
    return reverse_code

def count_possible_sequences(amino_acid_sequence, reverse_genetic_code):
    """
    Counts how many RNA sequences can generate the given amino acid sequence.
    """
    possible_sequences = 1
    for amino_acid in amino_acid_sequence:
        possible_sequences *= len(reverse_genetic_code.get(amino_acid, []))
    return possible_sequences

# Standard genetic code (RNA codons)
genetic_code = {
    "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "UAU": "Y", "UAC": "Y", "UAA": "STOP", "UAG": "STOP",
    "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "UGU": "C", "UGC": "C", "UGA": "STOP", "UGG": "W",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
}

# Remove STOP codons
filtered_genetic_code = {codon: aa for codon, aa in genetic_code.items() if aa != "STOP"}

# Build reverse genetic code
reverse_code = reverse_genetic_code(filtered_genetic_code)

tyrocidine_b1_sequence = "MFTW"

possible_sequences = count_possible_sequences(tyrocidine_b1_sequence, reverse_code)

print("Number of RNA sequences encoding Tyrocidine B1:", possible_sequences)
