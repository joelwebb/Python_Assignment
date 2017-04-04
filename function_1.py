#! python

def get_sequences_from_file(fasta_fn):

    sequence_data_dict = {}

    for record in SeqIO.parse(fasta_fn, "fasta"):

        description = record.description.split()

        species_name = description[1] + " " + description[2]

        sequence_data_dict[species_name] = record.seq

    return(sequence_data_dict)
