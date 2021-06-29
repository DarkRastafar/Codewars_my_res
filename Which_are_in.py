
def in_array(array1, array2):
    result = []
    for i in range(len(array1)):
        for word in array2:
            if array1[i] in word and array1[i] not in result:
                result.append(array1[i])

    return sorted(result)



a1 = ["live", "arp", "strong"] 
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
print(in_array(a1, a2))
a1 = ["arp", "mice", "bull"] 
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
print(in_array(a1, a2))