"""
This script calculates the GC content of a given DNA sequence.
The GC content is the percentage of bases in the DNA that are either guanine (G) or cytosine (C).
This is an important measure in bioinformatics
as it can provide insights into the stability of the DNA molecule
and its potential for gene expression.
"""


# Variable to hold the DNA sequence
dna = "ATGCGTACGT"

# Count the number of G and C bases in the DNA sequence
g_count = dna.count("G")
c_count = dna.count("C")

# Calculate the total length of the DNA sequence
total_length = len(dna)

# Calculate the GC content percentage
gc_percentage = ((g_count + c_count) / total_length) * 100

# Print the GC content percentage
print("GC content:", gc_percentage, "%")
