def first_non_repeating_letter(string):
    if string: 
        for i in list(string):
            if list(string.lower()).count(i.lower()) == 1:
                return i
        return ''
    else:
        return ''








print(first_non_repeating_letter('a'))
print(first_non_repeating_letter('stress'))
print(first_non_repeating_letter('moonmen'))


print(first_non_repeating_letter(''))
print(first_non_repeating_letter('abba'))
print(first_non_repeating_letter('aa'))


print(first_non_repeating_letter('~><#~><'), '#')
print(first_non_repeating_letter('hello world, eh?'), 'w')


print(first_non_repeating_letter('sTreSS'), 'T')
print(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'), ',')