def longest(a1, a2):
    letters = a1 + a2
    arr = []
    for letter in letters:
        if letter not in arr:
            arr.append(letter)
            arr.sort()
    return "".join(arr)





print(longest("aretheyhere", "yestheyarehere"), "aehrsty")
print(longest("loopingisfunbutdangerous", "lessdangerousthancoding"), "abcdefghilnoprstu")
print(longest("inmanylanguages", "theresapairoffunctions"), "acefghilmnoprstuy")