from silabeador import vowels_groups

def test_grupos_vocalicos_basicos():
    assert vowels_groups('constante') == ['o', 'a', 'e']
    assert vowels_groups('psicólogo') == ['i', 'ó', 'o', 'o']

def test_grupos_vocalicos_diptongos_triptongos():
    assert vowels_groups('caucho') == ['au', 'o']
    assert vowels_groups('cigüeña') == ['i', 'üe', 'a']
    assert vowels_groups('evacuáis') == ['e', 'a', 'uái']

def test_grupos_silabicos_hiatos():
    assert vowels_groups("cafeína") == ['a', 'e', 'í', 'a']
    assert vowels_groups("salíais") == ['a', 'í', 'ai']


    