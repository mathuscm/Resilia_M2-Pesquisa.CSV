def test_var(variavel):
    
    while True:
        try:
            temp = int(variavel)
            break
        except ValueError:
            print('Por favor, digite apenas números')
        pass
    return temp

