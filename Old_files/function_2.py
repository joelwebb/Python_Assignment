#! python

def translate_function(string_nucleotides):
    mito_table = CodonTable.unambiguous_dna_by_name["Vertebrate Mitochondrial"]

    aa_seq_string =""
    for i in range(0, len(string_nucleotides), 3):

        codon = string_nucleotides[i:i+3]
        if codon in mito_table.stop_codons:
            break

        aminoacid = mito_table.forward_table[codon]

        aa_seq_string += aminoacid

    return(aa_seq_string)
