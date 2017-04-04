#! python


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
