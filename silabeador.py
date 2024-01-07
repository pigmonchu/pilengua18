open_vowels = ['a', 'e', 'o', 'á', 'é', 'í', 'ó', 'ú']
closed_vowels = [ 'i', 'u', 'ü']
vowels = open_vowels + closed_vowels

def vowels_groups(word):
    groups = []
    group = ''
    prev_open_vowel = False
    for letter in word:
        if letter in closed_vowels:
            group += letter
        elif letter in open_vowels and not prev_open_vowel:
            group += letter
            prev_open_vowel = True
        elif letter in open_vowels:            
            groups.append(group)
            prev_open_vowel = False
            group = letter
        else:
            groups.append(group)
            prev_open_vowel = False
            group = ''
    
    groups.append(group)
    return list(filter(lambda g: g != '', groups))