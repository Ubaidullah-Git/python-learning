def dna_to_rna(dna):
    return dna.translate(str.maketrans("GCAT","GCAU"))

def dna_to_rna1(dna):
    return dna.replace('T','U')

print(dna_to_rna("GATCGGGTACAGTACTAGACAGATAAAACGTCCGGGATTAGC"))
print(dna_to_rna1("TGCAGTACTAGATAAAACGTCCGGGATTGC"))
