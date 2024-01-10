from silabeador import vowels_groups, left_consonant, SyllabicGroup, syllables

def test_grupos_vocalicos_basicos():
    assert vowels_groups('constante') == [SyllabicGroup(1, 'o'), 
                                          SyllabicGroup(5, 'a'), 
                                          SyllabicGroup(8, 'e')]
    assert vowels_groups('psicólogo') == [SyllabicGroup(2, 'i'), 
                                          SyllabicGroup(4, 'ó'), 
                                          SyllabicGroup(6, 'o'), 
                                          SyllabicGroup(8, 'o')]

def test_grupos_vocalicos_diptongos_triptongos():
    assert vowels_groups('caucho') == [SyllabicGroup(1, 'au'), 
                                       SyllabicGroup(5, 'o')]
    assert vowels_groups('cigüeña') == [SyllabicGroup(1, 'i'), 
                                        SyllabicGroup(3, 'üe'), 
                                        SyllabicGroup(6, 'a')]
    assert vowels_groups('evacuáis') == [SyllabicGroup(0, 'e'), 
                                         SyllabicGroup(2, 'a'), 
                                         SyllabicGroup(4, 'uái')]

def test_grupos_vocalicos_hiatos():
    assert vowels_groups("cafeína") == [SyllabicGroup(1, 'a'), 
                                        SyllabicGroup(3, 'e'), 
                                        SyllabicGroup(4, 'í'), 
                                        SyllabicGroup(6, 'a')]
    assert vowels_groups("salíais") == [SyllabicGroup(1, 'a'), 
                                        SyllabicGroup(3, 'í'), 
                                        SyllabicGroup(4, 'ai')]

def test_grupos_vocalicos_mayusculas():
    assert vowels_groups("cAfeÍna") == [SyllabicGroup(1, 'A'), 
                                        SyllabicGroup(3, 'e'), 
                                        SyllabicGroup(4, 'Í'), 
                                        SyllabicGroup(6, 'a')]
    assert vowels_groups("salÍaIs") == [SyllabicGroup(1, 'a'), 
                                        SyllabicGroup(3, 'Í'), 
                                        SyllabicGroup(4, 'aI')]

def test_constante_izquierda_basico():
    assert left_consonant("mala") == [SyllabicGroup(0, 'ma'), 
                                      SyllabicGroup(2, 'la')]
    assert left_consonant("macho") == [SyllabicGroup(0, 'ma'), 
                                       SyllabicGroup(2, 'cho')]
    assert left_consonant("manchar") == [SyllabicGroup(0, 'ma'),
                                         SyllabicGroup(3, 'cha')]

def test_separate_syllables():
    word = "constante"
    assert vowels_groups(word) == [SyllabicGroup(1, 'o'),
                                   SyllabicGroup(5, 'a'),
                                   SyllabicGroup(8, 'e')]
    assert left_consonant(word) == [SyllabicGroup(0, 'co'),
                                    SyllabicGroup(4, 'ta'),
                                    SyllabicGroup(7, 'te')]
    
    assert syllables(word) == ['cons', 'tan', 'te']

def test_create_syllabic_group():
    sg = SyllabicGroup(1, 'o')
    assert sg.position == 1
    assert sg.string == 'o'

'''
def test_constante_izquierda():
    assert left_consonant("compruebo") == ['co', 'prue', 'bo']
'''