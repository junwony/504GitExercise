def base_count(sequence):
    base_count_dict = dict()
    for base in sequence:
        if base not in base_count_dict:
            base_count_dict[base] = 1
        else:
            base_count_dict[base] += 1
    return base_count_dict

def base_fraction(base_count_dict):
    print('freqs')
    total = float(sum([base_count_dict[base] for base in base_count_dict.keys()]))
    for base in base_count_dict.keys():
        print(base + ':' + str(base_count_dict[base]/total))

base_fraction(base_count('ATCTGACGCGCGCCGC'))
