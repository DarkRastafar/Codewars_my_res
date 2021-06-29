def count_smileys(arr):
    counter = 0
    a, m, n = (":", ";"), (")", "D"), ("-", "~")
    for smiles in arr:
        if len(smiles) < 3:
            if smiles[0] in a and smiles[-1] in m:
                counter += 1
        else:
            if smiles[0] in a and smiles[1] in n and smiles[-1] in m:
                counter += 1
    return counter




print(count_smileys([]), 0)
print(count_smileys([':D',':~)',';~D',':)']), 4)
print(count_smileys([':)',':(',':D',':O',':;']), 2)
print(count_smileys([';]', ':[', ';*', ':$', ';-D']), 1)