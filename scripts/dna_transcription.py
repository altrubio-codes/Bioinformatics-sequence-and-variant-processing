"""
DNA Transcription
This script takes a DNA sequence,
converts it to uppercase,
and then replaces all occurrences of 'T' with 'U' to create the corresponding RNA sequence.
The original DNA sequence and the resulting RNA sequence are both printed at the end.
"""

# DNA sequence
dna_sequence = "atgcttcgataa"

# Convert the DNA sequence to uppercase and replace 'T' with 'U' to get the RNA sequence
dna = dna_sequence.upper()
rna_sequence = dna.replace("T", "U")

# Print the original DNA sequence and the transcribed RNA sequence
print(dna)
print(rna_sequence)
