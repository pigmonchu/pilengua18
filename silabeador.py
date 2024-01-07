open_vowels = ['a', 'e', 'o', 'á', 'é', 'í', 'ó', 'ú']
closed_vowels = [ 'i', 'u', 'ü']
vowels = open_vowels + closed_vowels

def vowels_groups(word):
    # return list(filter(lambda l: l in vowels, word))
    groups = []
    group = ''
    for letter in word:
        if letter in vowels:
            group += letter
        else:
            groups.append(group)
            group = ''
    
    groups.append(group)
    return list(filter(lambda g: g != '', groups))