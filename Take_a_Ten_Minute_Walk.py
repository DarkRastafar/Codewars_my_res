def is_valid_walk(walk):
    #determine if walk is valid
    counter = 0
    for i in range(0, len(walk)):
       counter += 1

    if counter == 10 and walk[0] == walk[-1]:
        return True, counter
    elif counter == 10 and walk[-1] == walk[1]:
        return True, counter
    else:
        return False, counter




print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']), 'should return True')
print(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']), 'should return False')
print(is_valid_walk(['w']), 'should return False')
print(is_valid_walk(['n','n','n','s','n','s','n','s','n','s']), 'should return False')
print(is_valid_walk(['s', 'n', 'w', 'n', 'n', 's', 'e', 's', 'n', 's']), "should return True")
print(is_valid_walk(['s', 'n', 'w', 'n', 'n', 's', 'e', 's', 'n', 's']), "should return True")
print(is_valid_walk(['n', 'w', 'e', 'w', 'n', 's', 'e', 'w', 'n', 'w']), "should return False")
print(is_valid_walk(['w', 'n', 'w', 'n', 'e', 's', 'e', 's', 'n', 's']), "should return True")
print(is_valid_walk(['e', 'n', 'e', 'w', 'n', 's', 'n', 's', 's', 'w']), "should return True")