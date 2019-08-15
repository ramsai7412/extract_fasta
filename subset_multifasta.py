import os
import sys

#Reading user input file
args = sys.argv[1:3]
in_file = args[0]
seq_ids = args[1]
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