"""
Reverse Complement Generator
This script generates the reverse complement of a given DNA sequence.
"""

# Original DNA sequence
dna = "AAAACCCGGT"

# Create a translation table to swap the nucleotides: A <-> T and C <-> G
change_table = str.maketrans("ATCG", "TAGC")

# Apply the translation table to swap the letters in the original DNA sequence to get the complement
complement_dna = dna.translate(change_table)

# Reverse the complement DNA sequence to get the reverse complement
reverse_complement = complement_dna[::-1]

# Print the reverse complement of the DNA sequence
print(reverse_complement)
