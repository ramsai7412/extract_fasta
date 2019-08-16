import os
import sys
import argparse
#Developed Info
print ("\n*********************************************************************************")
print ("* Python script to subset multi fasta file using ids from another file\t\t*")
print ("* Script Developed by\t:\tRam Sai Nanduri\t\t\t\t\t*")
print ("*********************************************************************************")
##Argument parser
parser = argparse.ArgumentParser(description="Subset Multi Fasta using Ids from another file.")
parser.add_argument("-m", "--multifasta", metavar="multifasta", help="Input multi fasta file", type=str)
parser.add_argument("-i", "--ids", metavar="ids", help="Input sequence Ids file", type=str)
parser.add_argument("-v", "--version", help="Program's version", action='version', version='%(prog)s 1.0')
args = parser.parse_args()

#Reading user input file
in_file = args.multifasta
seq_ids = args.ids
file_path = os.path.abspath(os.path.dirname(in_file))

#reading multifasta file
with open(in_file, "r") as fa:
    lines = fa.read().split('>')
    lines = lines[1:]
    lines = ['>'+ seq for seq in lines]
    ids_seqs = {}

for seqs in lines:
#Extracting sequence Id and sequences as a dict
	seq = seqs.split('\n')
	id_trim = seq[0].split(' ')
	ids_seqs.update({id_trim[0]: seq[1]})

#reading Ids to extract from multi fasta file
with open(seq_ids, "r") as ids:
	seq_id = ids.read().split("\n")

#getting sequences for the selected ids
selected_ids = {a: b for a, b in ids_seqs.items() if a in seq_id}

#Renaming the output file if already exits
if os.path.exists("selected.fasta"):
	os.rename('selected.fasta', 'old_selected.fasta')

#writing sequences for the selected ids to a file
for individual_seq in selected_ids:
	seq1 = selected_ids.get(individual_seq)
	out_file=open(file_path+"/"+"selected.fasta", "a+")
	out_file.write(individual_seq+"\n"+seq1+"\n")
	out_file.close()

print ("\nSuccessfully extracted the sequences from the "+os.path.basename(in_file)+" for the ids provided in the "+os.path.basename(seq_ids))
print ("\nResults are stored in the selected.fasta file\n")