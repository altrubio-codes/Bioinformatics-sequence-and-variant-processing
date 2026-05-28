"""
This script cleans a messy DNA sequence by removing spaces
and converting all letters to uppercase.
It then calculates and prints the total length of the cleaned DNA sequence.
The script first defines a raw DNA sequence that contains spaces and mixed case letters.
It uses the `replace` method to remove all spaces and the `upper` method to convert all letters to uppercase.
Finally, it calculates the length of the cleaned DNA sequence and prints it.
"""

# A messy DNA sequence with spaces and mixed case letters
raw_dna = "  atgC gGat TTaCca   aTgCggtA  "

# Remove spaces and convert to uppercase
no_space = raw_dna.replace(" ", "")
clean_dna = no_space.upper()

# Calculate the total length of the cleaned DNA sequence
len(clean_dna)
total_length = len(clean_dna)

# Print the cleaned DNA sequence and its total length
print("Total length of the cleaned DNA sequence:", total_length)
