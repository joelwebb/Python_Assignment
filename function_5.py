#! python

cytb_seqs = get_sequences_from_file("bears_cytb.fasta")

bear_df = pd.read_csv("bears_data.csv")

species_list = list(bear_df.species)

for key, value in cytb_seqs.items():
    aa_seq =Alt_translate(str(value))

    proportion = get_proportion_aa(aa_seq)

    bear_df.loc[bear_df.species==key, 'charged'] = proportion[0]

    bear_df.loc[bear_df.species==key, 'polar'] = proportion[1]

    bear_df.loc[bear_df.species==key, 'hydrophobic'] = proportion[2] 
