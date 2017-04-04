#!python

from Bio.Seq import Seq

def Alt_translate(string_nucleotides):

    coding_dna = Seq(string_nucleotides)

    result = string_nucleotides.translate(table="Vertebrate Mitochondrial", to_stop=True)

    AA_Sequence = str(result)

    return(AA_Sequence) 
