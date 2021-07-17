import string

def is_pangram(s):
    return "".join(sorted(set([i.lower() for i in s if i.isalpha()]))) == string.ascii_lowercase



pangram = "The quick, brown fox jumps over the lazy dog!"
print(is_pangram(pangram), True)
