"""
This script creates a consensus sequence from three DNA strands
by determining the most common nucleotideat each position.
The consensus sequence is built by comparing the nucleotides
at each position across the three strands and selecting the one that appears most frequently.
The resulting consensus sequence is printed at the end.
"""

# Define the three DNA strands
strand1 = "AGGCA"
strand2 = "ATCCA"
strand3 = "TTGCA"

# Variable to hold the resulting consensus sequence
consensus = ""

# Go over each index of each strand and determine the most COMMON nucleotide at that position and add it to the consensus sequence
for i in range(len(strand1)):
    pool = strand1[i] + strand2[i] + strand3[i]

    if pool.count('A') >= 2:
        consensus += "A"
    elif pool.count('T') >= 2:
        consensus += "T"
    elif pool.count('G') >= 2:
        consensus += "G"
    elif pool.count('C') >= 2:
        consensus += "C"

# Print the resulting consensus sequence
    print(consensus)
