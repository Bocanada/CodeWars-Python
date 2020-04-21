def DNA_strand(dna):
    # code here
    complements = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G',
    }
    return ''.join([complements[c] for c in dna])
