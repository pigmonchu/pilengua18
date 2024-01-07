from silabeador import vowels_groups

def test_grupos_vocalicos_basicos():
    assert vowels_groups('constante') == ['o', 'a', 'e']
    assert vowels_groups('psicólogo') == ['i', 'ó', 'o', 'o']
