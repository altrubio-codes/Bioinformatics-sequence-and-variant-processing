"""
Master Pipeline for Bioinformatics Analysis
This script reads a DNA sequence from
a FASTA file, transcribes it to RNA, and translates it into a protein sequence.
This pipeline integrates the following steps:
1. Reading a FASTA file to extract the DNA sequence.
2. Transcribing the DNA sequence to RNA.
3. Translating the RNA sequence into a protein sequence using codon mapping.
The script is designed to be modular, allowing for easy extension
and integration of additional bioinformatics analyses in the future.
"""

# Importing random is not necessary for the current pipeline, but it can be used for future extensions such as simulating mutations or generating random sequences.
import random


def read_fasta(file_path):
    """ Reads a FASTA file and combines all sequence lines, ignoring headers """

    # Initialize an empty list to store sequence lines
    sequence_lines = []

    # Open the FASTA file and read it line by line
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith(">") or not line:
                continue
            # Add the sequence line to the list
            sequence_lines.append(line)

    # Join all sequence lines into a single string and convert to uppercase
    return "".join(sequence_lines).upper()


def transcribe_dna(dna_sequence):
    """ Transcribes DNA to RNA by replacing Thymine (T) with Uracil (U) """

    # Replace 'T' with 'U' to transcribe DNA to RNA
    transcription_table = str.maketrans("T", "U")

    # Use the translation table to convert the DNA sequence to RNA
    return dna_sequence.translate(transcription_table)


def translate_rna(rna_sequence):
    """ Translates RNA codons into an amino acid protein chain """

    codon_table = {
        'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T',
        'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',
        'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
        'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R',
        'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
        'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
        'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S',
        'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L',
        'UAC':'Y', 'UAU':'Y', 'UAA':'', 'UAG':'', 'UGA':''
    }

    # An empty string to accumulate the resulting protein sequence
    protein = ""

    # Loop through the RNA sequence in steps of 3 to read codons
    for i in range(0, len(rna_sequence), 3):
        codon = rna_sequence[i:i+3]

        # Check if the codon is complete (3 nucleotides). If not, print a warning and break the loop.
        if len(codon) < 3:
            print(f"Warning: Incomplete codon '{codon}'. Ignoring.")
            break

        # Look up the amino acid corresponding to the RNA codon in the codon table. If the codon is not found, use "?" as a placeholder.
        amino_acid = codon_table.get(codon, "?")

        # If the amino acid is an empty string, it indicates a stop codon, so we break the loop to end translation.
        if amino_acid == "":
            break
        
        # Add the amino acid to the growing protein sequence
        protein += amino_acid

# Return the final protein sequence after processing all codons
if __name__ == "__main__":
    file_path = "../sample.fasta"

    # try and except block to handle potential file-related errors gracefully
    try:
        print("Starting Master Pipeline...")

        # Read the DNA sequence from the specified FASTA file and store it in the variable 'dna'. The read_fasta function will handle the file reading and
        dna= read_fasta(file_path)

        # Print the length of the loaded DNA sequence to confirm successful reading and provide feedback on the size of the data being processed.
        print(f"Loaded DNA sequence ({len(dna)} base pairs).")

        # Transcribe the DNA sequence to RNA using the transcribe_dna function and store the resulting RNA sequence in the variable 'rna'.
        rna = transcribe_dna(dna)

        # Translate the RNA sequence into a protein sequence using the translate_rna function and store the resulting protein sequence in the variable 'protein_product'.
        protein_product = translate_rna(rna)

        # Print the final protein product to the console, providing a clear output of the result of the entire pipeline. This allows users to see the end result of the transcription and translation processes.
        print("\n--- Pipeline Success ---")
        print("Final Protein Product: ", protein_product)

    # Handle the case where the specified FASTA file is not found, providing a user-friendly error message to help diagnose the issue.
    except FileNotFoundError:
        print(f"Error: The file at '{file_path}' was not found. Check your path!")
