def to_jaden_case(string):
    arr = string.split()
    result = []
    for word in arr:
        if "'" in word:
            result.append(word.capitalize()) 
        else:
            result.append(word.title())
    return " ".join(result)

    # print(test)
    print(quote)

quote = "How can mirrors be real if our eyes aren't real"
to_jaden_case(quote)