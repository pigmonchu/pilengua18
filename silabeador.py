from collections import namedtuple

open_vowels = ['a', 'e', 'o', 'á', 'é', 'í', 'ó', 'ú']
closed_vowels = [ 'i', 'u', 'ü']
vowels = open_vowels + closed_vowels

SillabicGroup = namedtuple("SillabicGroup", "position string")

def vowels_groups(word):
    groups = []
    group = ''
    prev_open_vowel = False
    for pos, letter in enumerate(word):
        compare_letter = letter.lower()
        if compare_letter in closed_vowels:
            group += letter
        elif compare_letter in open_vowels and not prev_open_vowel:
            group += letter
            prev_open_vowel = True
        elif compare_letter in open_vowels:            
            groups.append(SillabicGroup(pos - len(group), group))
            prev_open_vowel = False
            group = letter
        else:
            groups.append(SillabicGroup(pos - len(group), group))
            prev_open_vowel = False
            group = ''
    
    groups.append(SillabicGroup(pos +1 - len(group), group))
    return list(filter(lambda g: g.string != '', groups))

def left_consonant(word):
    vg = vowels_groups(word)
