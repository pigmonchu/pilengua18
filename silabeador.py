vowels = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú', 'ü']

def vowels_groups(word):
    return list(filter(lambda l: l in vowels, word))