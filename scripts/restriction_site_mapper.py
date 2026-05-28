"""
Restriction Site Mapper
This script identifies the position of a restriction enzyme site within a given DNA sequence.
"""

# DNA sequence to search within
dna = "ACTGATCGGAATTCGCTAG"

# Restriction enzyme site to search for
enzyme_site = "GAATTC"

# Find the position of the enzyme site in the DNA sequence
cut_position = dna.find(enzyme_site)

# Check if the enzyme site was found and print the result
if cut_position != -1:
    print("Enzyme cuts at position: ", cut_position)
else:
    # If the enzyme site is not found, print a message indicating that it was not found
    print("Restriction site not found.")
