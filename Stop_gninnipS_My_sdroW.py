def spin_words(sentence):
    arr = sentence.split()
    for word in arr:
        if len(word) >= 5:
            arr.insert(arr.index(word), arr.pop(arr.index(word))[::-1])
    return " ".join(arr)



print(spin_words("Welcome"), "emocleW")
print(spin_words("This is a test"), "This is a test")
print(spin_words("This is another test"), "This is rehtona test")