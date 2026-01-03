def DNA_strand(dna):
    return dna.translate(str.maketrans('TAGC','ATCG'))

print(DNA_strand("GCAGTGAGAGTCTAGTG"))