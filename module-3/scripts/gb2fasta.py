import os
import sys
from Bio import SeqIO

def read_genbank_and_write_fasta(input_directory, output_file):
    protein_sequences = []
    folder_names = []  # Store the folder names

    # Recursively search for .gbk files in the input directory and its subdirectories
    for root, dirs, files in os.walk(input_directory):
        for file_counter, file_name in enumerate(files, 1):
            if file_name.endswith(".gbk") and "region" in file_name.lower():
                genbank_file = os.path.join(root, file_name)
                gene_counter = 1  # Initialize the gene counter for each GenBank file

                # Store the folder name containing the GenBank files
                folder_name = os.path.basename(root)
                folder_names.append(folder_name)

                # Read the GenBank file
                for record in SeqIO.parse(genbank_file, "genbank"):
                    # Iterate over each feature in the record
                    for feature in record.features:
                        # Check if the feature is a CDS
                        if feature.type == "CDS":
                            # Extract the protein sequence
                            protein_sequence = feature.qualifiers.get("translation", [""])[0]

                            # Increment the gene counter within each GenBank file
                            gene_header = f">{folder_name}bgc{file_counter}_gene{gene_counter}"
                            gene_counter += 1
                            protein_sequences.append(gene_header)
                            protein_sequences.append(protein_sequence)

    # Write protein sequences to the output file in FASTA format
    with open(output_file, "w") as outfile:
        for sequence in protein_sequences:
            outfile.write(sequence + "\n")

    # Print the folder names for reference
    print("Processed folders:", ", ".join(folder_names))

# Check if the correct number of arguments is provided
if len(sys.argv) < 3:
    print("Usage: python script.py input_directory output_file")
    sys.exit(1)

# Get the input directory and output file from command-line arguments
input_directory = sys.argv[1]
output_file = sys.argv[2]

# Read GenBank files and write protein sequences to a FASTA file
read_genbank_and_write_fasta(input_directory, output_file)

