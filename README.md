# Reverse Codon Translator

# Description:
The Reverse Codon Translator calculates the number of possible RNA sequences that can encode a given amino acid sequence (peptide), based on the degeneracy of the genetic code. It uses the standard RNA codon table to create a reverse mapping (amino acid → list of codons) and then multiplies the codon possibilities for each amino acid in the input peptide.

This allows researchers or students to estimate how many different RNA sequences can generate the same protein.

# Functionality:
reverse_genetic_code(genetic_code):
This function creates a reverse dictionary from a standard codon table, mapping each amino acid to all RNA codons that encode it.
Returns a dictionary:
{ "A": ["GCU", "GCC", "GCA", "GCG"], ... }

count_possible_sequences(amino_acid_sequence, reverse_genetic_code):
This function calculates the number of unique RNA sequences that could encode the provided amino acid sequence by multiplying the number of codons for each amino acid.

# Parameters:
genetic_code (dict): Standard RNA codon table in dictionary format.

amino_acid_sequence (str): A string of single-letter amino acids (e.g., "MFTW" for Methionine, Phenylalanine, Threonine, Tryptophan).

# Example Usage:
```
# Input amino acid sequence
sequence = "MFTW"

# Reverse the genetic code
reverse_code = reverse_genetic_code(genetic_code)

# Count number of RNA sequences that encode the sequence
possible_sequences = count_possible_sequences(sequence, reverse_code)

print("Number of RNA sequences encoding Tyrocidine B1:", possible_sequences)
```
# Output Example:
Number of RNA sequences encoding Tyrocidine B1: 48

# Applications:
This script can be applied in various bioinformatics and molecular biology contexts, including:
Codon Optimization: For designing synthetic genes using the most efficient codons.
Reverse Translation: Useful in primer design or back-translating proteins to possible nucleic sequences.
Degeneracy Analysis: Explore the redundancy in the genetic code and its implications.
Protein Engineering: Estimate mutation space or variability at the nucleotide level for a given protein.
Teaching Tool: A clear demonstration of codon degeneracy and its impact on genetic translation.

### License
This project is licensed under the MIT License.






