def dna_to_rna(dna):
    return dna.translate(str.maketrans("GCAT","GCAU"))

print(dna_to_rna("GATCGGGTACAGTACTAGACAGATAAAACGTCCGGGATTAGC"))
