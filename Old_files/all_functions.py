#! python

def get_sequences_from_file(fasta_fn):

    sequence_data_dict = {}

    for record in SeqIO.parse(fasta_fn, "fasta"):

        description = record.description.split()

        species_name = description[1] + " " + description[2]

        sequence_data_dict[species_name] = record.seq

    return(sequence_data_dict)




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




    from Bio.Seq import Seq

    def Alt_translate(string_nucleotides):

        coding_dna = Seq(string_nucleotides)

        result = string_nucleotides.translate(table="Vertebrate Mitochondrial", to_stop=True)

        AA_Sequence = str(result)

        return(AA_Sequence)




        def get_proportion_aa(aa_seq):

            charged = ['R','K','D','E']
            polar = ['Q','N','H','S','T','Y','C','M','W']
            hydrophobic = ['A','I','L','F','V','P','G']
            c_count=0
            p_count=0
            h_count=0

            for aa in str(aa_seq):
                if aa in charged:
                    c_count += 1

                elif aa in polar:
                    p_count += 1

                elif aa in hydrophobic:
                    h_count += 1

            proportion_type = [c_count/len(aa_seq), p_count/len(aa_seq), h_count/len(aa_seq)]

            return proportion_type



            import pandas as pd
            cytb_seqs = get_sequences_from_file("bears_cytb.fasta")

            bear_df = pd.read_csv("https://raw.githubusercontent.com/joelwebb/Python_Assignment/master/bears_data.csv")

            species_list = list(bear_df.species)

            for key, value in cytb_seqs.items():
                aa_seq =Alt_translate(str(value))

                proportion = get_proportion_aa(aa_seq)

                bear_df.loc[bear_df.species==key, 'charged'] = proportion[0]

                bear_df.loc[bear_df.species==key, 'polar'] = proportion[1]

                bear_df.loc[bear_df.species==key, 'hydrophobic'] = proportion[2]




import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sea
import pandas as pd
#x = ["arctos", "thibetanus","ursinus", "americanus", "malayanus", "melanoleuca", "ornatus", "maritimus"]

#y = [203.5,99.7,100,110.5,47.0,118.2,140.7,425.1]

bear_df = pd.DataFrame({'species': ["arctos", "thibetanus","ursinus", "americanus", "malayanus", "melanoleuca", "ornatus", "maritimus"], 'mass':[203.5,99.7,100,110.5,47.0,118.2,140.7,425.1]})
#bar = plt.plot(x, y)

#bar_chart = sea.barplot(x="species", y = "mass", data=bear_df)
sea.barplot(x=bear_df.mass, y=bear_df.species)

#chart = sea.barplot(x='species', y='mass', data=bear_df)


import numpy as num

ind = num.arange(len(bear_df))
p1= plt.bar(ind, bear_df.charged)
p2= plt.bar(ind, bear_df.polar, bottom = bear_df.charged)
p3= plt.bar(ind, bear_df.hydrophobic, bottom = bear_df.charged + bear_df.polar)
plt.xlabel('Ursus Species')
plt.xticks(ind, bear_df.species, rotation=30, horizontalalignment='right')
plt.ylabel('Proportion')
plt.yticks(num.arange(0, 1.1, 0.1))
plt.legend((p1[0], p2[0], p3[0]), ('Charged', 'Polar', 'Hydrophobic'), bbox_to_anchor=(1.01, 1.01))
plt.show()
