"""
This code reads a DNA sequence from a FASTA file,
transcribes it into RNA, and then translates the RNA into a protein sequence using a codon table.
The final protein product is printed at the end.
"""

# Make a translation table for DNA to RNA transcription
transcription_table = str.maketrans("T", "U")

# Dictionary to check each 3 letter codon and translate it to the corresponding amino acid
codon_table = {
    "AUG": "M", "UUU": "F", "GGC": "G", "CCA": "P",
    "UAA": "*", "UAG": "*", "UGA": "*"
}

# Path to the FASTA file containing the DNA sequence
file_path = "../sample.fasta"

# Read the DNA sequence from the FASTA file
with open(file_path, "r") as file:
    lines = file.readlines()

# Stores the DNA sequence, removing any leading/trailing whitespace and the FASTA header
clean_dna = lines[1].strip()

# Stores the RNA sequence after transcription from the DNA sequence using the translation table
rna_sequence = clean_dna.translate(transcription_table)

# Initialize an empty string to build the protein sequence to be produced from the RNA sequence
protein = ""

# Check each 3 letter codon in the RNA sequence and translate it to the corresponding amino acid using the codon table
for i in range(0, len(rna_sequence), 3):
    codon = rna_sequence[i:i+3]

    # Get the corresponding amino acid for the codon, or "?" if the codon is not found in the codon table
    amino_acid = codon_table.get(codon, "?")

    # If the amino acid is a stop codon (represented by "*"), break the loop as the protein sequence is complete
    if amino_acid == "*":
        # Stop codon encountered, end of protein sequence
        break

    # Add the amino acid to the protein sequence
    protein += amino_acid

# Print the final protein product
print("Final Protein product: ", protein)
