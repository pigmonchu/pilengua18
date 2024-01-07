from silabeador import vowels_groups

def test_grupos_vocalicos_basicos():
    assert vowels_groups('constante') == ['o', 'a', 'e']
    assert vowels_groups('psicólogo') == ['i', 'ó', 'o', 'o']

def test_grupos_vocalicos_diptongos_triptongos():
    assert vowels_groups('caucho') == ['au', 'o']
    assert vowels_groups('cigüeña') == ['i', 'üe', 'a']


    