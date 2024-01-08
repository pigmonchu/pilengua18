from silabeador import vowels_groups, left_consonant, SillabicGroup

def test_grupos_vocalicos_basicos():
    assert vowels_groups('constante') == [SillabicGroup(1, 'o'), 
                                          SillabicGroup(5, 'a'), 
                                          SillabicGroup(8, 'e')]
    assert vowels_groups('psicólogo') == [SillabicGroup(2, 'i'), 
                                          SillabicGroup(4, 'ó'), 
                                          SillabicGroup(6, 'o'), 
                                          SillabicGroup(8, 'o')]

def test_grupos_vocalicos_diptongos_triptongos():
    assert vowels_groups('caucho') == [SillabicGroup(1, 'au'), 
                                       SillabicGroup(5, 'o')]
    assert vowels_groups('cigüeña') == [SillabicGroup(1, 'i'), 
                                        SillabicGroup(3, 'üe'), 
                                        SillabicGroup(6, 'a')]
    assert vowels_groups('evacuáis') == [SillabicGroup(0, 'e'), 
                                         SillabicGroup(2, 'a'), 
                                         SillabicGroup(4, 'uái')]

def test_grupos_vocalicos_hiatos():
    assert vowels_groups("cafeína") == [SillabicGroup(1, 'a'), 
                                        SillabicGroup(3, 'e'), 
                                        SillabicGroup(4, 'í'), 
                                        SillabicGroup(6, 'a')]
    assert vowels_groups("salíais") == [SillabicGroup(1, 'a'), 
                                        SillabicGroup(3, 'í'), 
                                        SillabicGroup(4, 'ai')]

def test_grupos_vocalicos_mayusculas():
    assert vowels_groups("cAfeÍna") == [SillabicGroup(1, 'A'), 
                                        SillabicGroup(3, 'e'), 
                                        SillabicGroup(4, 'Í'), 
                                        SillabicGroup(6, 'a')]
    assert vowels_groups("salÍaIs") == [SillabicGroup(1, 'a'), 
                                        SillabicGroup(3, 'Í'), 
                                        SillabicGroup(4, 'aI')]

def test_constante_izquierda_basico():
    assert left_consonant("mala") == [SillabicGroup(0, 'ma'), 
                                      SillabicGroup(2, 'la')]
    assert left_consonant("macho") == [SillabicGroup(0, 'ma'), 
                                       SillabicGroup(2, 'cho')]


def test_create_sillabic_group():
    sg = SillabicGroup(1, 'o')
    assert sg.position == 1
    assert sg.string == 'o'

'''
def test_constante_izquierda():
    assert left_consonant("compruebo") == ['co', 'prue', 'bo']
'''