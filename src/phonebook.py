class Phonebook:

    def __init__(self):
        self.entries = {'POLICIA': '190'}

    def add(self, name, number):
        """

        :param name: name of person in string
        :param number: number of person in string
        :return: 'Nome invalido' or 'Numero invalido' or 'Numero adicionado'
        """
        if '#' in name or '@' in name or '!' in name or '$' in name or '%' in name:
            return 'Nome invalido'

        if len(number) == 0:
            return 'Numero invalido'

        if name not in self.entries:
            self.entries[name] = number
            return 'Numero adicionado'

        return 'Nome já existe'

    def lookup(self, name):
        """
        :param name: name of person in string
        :return: return number of person with name
        """

        if name in self.entries:
            return self.entries[name]
        else:
            if '#' in name or '@' in name or '!' in name or '$' in name or '%' in name:
                return 'Nome invalido'
        return 'Nome não encontrado'

    def get_names(self):
        """

        :return: return all names in phonebook
        """
        return self.entries.keys()

    def get_numbers(self):
        """

        :return: return all numbers in phonebook
        """
        return self.entries.values()

    def clear(self):
        """
        Clear all phonebook
        :return: return 'phonebook limpado'
        """
        self.entries = {}
        return 'phonebook limpado'

    def search(self, search_name):
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search
        """
        result = []
        for name, number in self.entries.items():
            if search_name in name:
                result.append({name, number})
        return result

    def get_phonebook_sorted(self):
        """

        :return: return phonebook in sorted order
        """
        return sorted(self.entries.items())

    def get_phonebook_reverse(self):
        """

        :return: return phonebook in reverse sorted order
        """
        return sorted(self.entries.items(), reverse=True)

    def delete(self, name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'
        """

        if name in self.entries:
            self.entries.pop(name)
            return 'Numero deletado'
        return 'Numero não existe'

    def get_name_by_number(self, number):
        """
        :param name: name of person in string
        :return: return number of person with name
        """

        if number not in self.entries.values():
            return 'Numero não encontrado'
        return list(self.entries.keys())

    def update(self, name, number):

        if name in self.entries:
            self.entries[name] = number
            return 'Numero alterado'
        return 'Nome não encontrado'
