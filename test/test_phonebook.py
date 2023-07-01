from src.phonebook import Phonebook

class TestPhonebook:

    def test_add_invalid_name(self):
        name = 'Thi@go'
        number = '12345678'
        resultado_esperado = 'Nome invalido'
        phonebook = Phonebook()
        resultado = phonebook.add(name=name, number=number)
        assert resultado_esperado == resultado

    def test_add_invalid_number(self):
        name = 'Thiago'
        number = ''
        resultado_esperado = 'Numero invalido'
        phonebook = Phonebook()
        resultado = phonebook.add(name=name, number=number)
        assert resultado_esperado == resultado

    def test_add_existing_contact(self):
        name = 'POLICIA'
        number = '190'
        resultado_esperado = 'Nome já existe'
        phonebook = Phonebook()
        resultado = phonebook.add(name=name, number=number)
        assert resultado_esperado == resultado

    def test_add_number(self):
        name = 'Thiago'
        number = '12345678'
        resultado_esperado = 'Numero adicionado'
        phonebook = Phonebook()
        resultado = phonebook.add(name=name, number=number)
        assert resultado_esperado == resultado

    def test_lookup_invalid_name(self):
        name = 'T#iago'
        resultado_esperado = 'Nome invalido'
        phonebook = Phonebook()
        resultado = phonebook.lookup(name=name)
        assert resultado_esperado == resultado

    def test_lookup_inexistent_name(self):
        name = 'SAMU'
        resultado_esperado = 'Nome não encontrado'
        phonebook = Phonebook()
        resultado = phonebook.lookup(name=name)
        assert resultado_esperado == resultado

    def test_lookup_name(self):
        name = 'POLICIA'
        resultado_esperado = '190'
        phonebook = Phonebook()
        resultado = phonebook.lookup(name=name)
        assert resultado_esperado == resultado

    def test_get_names(self):
        resultado_esperado = ['POLICIA']
        phonebook = Phonebook()
        resultado = phonebook.get_names()
        assert resultado_esperado == (list(resultado))

    def test_get_number(self):
        resultado_esperado = ['190']
        phonebook = Phonebook()
        resultado = phonebook.get_numbers()
        assert resultado_esperado == (list(resultado))

    def test_clear(self):
        resultado_esperado = 'phonebook limpado'
        phonebook = Phonebook()
        resultado = phonebook.clear()
        assert resultado_esperado == resultado

    def test_search_name(self):
        name = 'POL'
        resultado_esperado = [{'190', 'POLICIA'}]
        phonebook = Phonebook()
        resultado = phonebook.search(search_name=name)
        assert resultado_esperado == resultado

    def test_invalid_search_name(self):
        name = 'SAM'
        resultado_esperado = []
        phonebook = Phonebook()
        resultado = phonebook.search(search_name=name)
        assert resultado_esperado == resultado

    def test_sorted_telephone_list(self):
        resultado_esperado = [('BOMBEIRO', '193'), ('MEDICO', '192'), ('POLICIA', '190')]
        name = 'BOMBEIRO'
        number = '193'
        name2 = 'MEDICO'
        number2 = '192'
        phonebook = Phonebook()
        phonebook.add(name=name, number=number)
        phonebook.add(name=name2, number=number2)
        resultado = phonebook.get_phonebook_sorted()
        assert resultado_esperado == resultado

    def test_reversed_telephone_list(self):
        resultado_esperado = [('POLICIA', '190'), ('MEDICO', '192'), ('BOMBEIRO', '193')]
        name = 'BOMBEIRO'
        number = '193'
        name2 = 'MEDICO'
        number2 = '192'
        phonebook = Phonebook()
        phonebook.add(name=name, number=number)
        phonebook.add(name=name2, number=number2)
        resultado = phonebook.get_phonebook_reverse()
        assert resultado_esperado == resultado

    def test_delete_name(self):
        name = 'POLICIA'
        resultado_esperado = 'Numero deletado'
        phonebook = Phonebook()
        resultado = phonebook.delete(name=name)
        assert resultado_esperado == resultado

    def test_delete_invalid_name(self):
        name = 'SAMU'
        resultado_esperado = 'Numero não existe'
        phonebook = Phonebook()
        resultado = phonebook.delete(name=name)
        assert resultado_esperado == resultado

    def test_get_name_by_number(self):
        number = '190'
        resultado_esperado = ['POLICIA']
        phonebook = Phonebook()
        resultado = phonebook.get_name_by_number(number=number)
        assert resultado_esperado == resultado

    def test_get_invalid_name_by_number(self):
        number = '200'
        resultado_esperado = 'Numero não encontrado'
        phonebook = Phonebook()
        resultado = phonebook.get_name_by_number(number=number)
        assert resultado_esperado == resultado

    def test_update_number(self):
        name = 'POLICIA'
        number = '192'
        resultado_esperado = 'Numero alterado'
        phonebook = Phonebook()
        resultado = phonebook.update(name=name, number=number)
        assert resultado_esperado == resultado

    def test_persist_update_number(self):
        name = 'POLICIA'
        number = '192'
        resultado_esperado = ['192']
        phonebook = Phonebook()
        phonebook.update(name=name, number=number)
        resultado = phonebook.get_numbers()
        assert resultado_esperado == (list(resultado))

    def test_update_invalid_number(self):
        name = 'SAMU'
        number = '193'
        resultado_esperado = 'Nome não encontrado'
        phonebook = Phonebook()
        resultado = phonebook.update(name=name, number=number)
        assert resultado_esperado == resultado
