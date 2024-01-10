from collections import namedtuple

open_vowels = ['a', 'e', 'o', 'á', 'é', 'í', 'ó', 'ú']
closed_vowels = [ 'i', 'u', 'ü']
vowels = open_vowels + closed_vowels
simple_consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'z']
double_consonants = ['bs', 'll', 'rr', 'bl', 'cl', 'gl', 'fl', 'kl', 'pl', 'br', 'cr', 'dr', 'fr', 'gr', 'kr', 'pr', 'tr', 'ps', 'ch']


SyllabicGroup = namedtuple("SyllabicGroup", "position string")

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
            groups.append(SyllabicGroup(pos - len(group), group))
            prev_open_vowel = False
            group = letter
        else:
            groups.append(SyllabicGroup(pos - len(group), group))
            prev_open_vowel = False
            group = ''
    
    groups.append(SyllabicGroup(pos +1 - len(group), group))
    return list(filter(lambda g: g.string != '', groups))

def left_consonant(word):
    vgs = vowels_groups(word)
    for ix, vg in enumerate(vgs):
        pos, string = vg
        if pos > 1 and word[pos-2: pos] in double_consonants:
            vgs[ix] = SyllabicGroup(pos-2, word[pos-2: pos] + string)
        elif word[pos-1: pos] in simple_consonants:
            vgs[ix] = SyllabicGroup(pos-1, word[pos-1: pos] + string)
    return vgs

def syllables(word):
    sg = left_consonant(word)
    syls = []
    
    ix_sg = 0
    syl = ''
    for ix_letter in range(len(word)):
        if ix_sg >= len(sg) - 1 or ix_letter < sg[ix_sg + 1].position:
            syl += word[ix_letter]
        else:
            syls.append(syl)
            ix_sg += 1
            syl = word[ix_letter]
    syls.append(syl)
    return syls




        