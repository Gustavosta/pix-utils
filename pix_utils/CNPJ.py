#!/usr/bin/env python
#-*- coding:utf -8-*-3


class CNPJ(object):
    """
    Classe para validação de números de CNPJ.
    """

    def __init__(self, cnpj):
        """
        Inicializa a classe.
        """

        self.cnpj = cnpj


    def caculate_digit(self, is_first_digit: bool = True):
        """
        Calcula o dígito verificador.
        """

        if is_first_digit:
            FACTORIES = [6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9]
        else:
            FACTORIES = [5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9]

        result_sum = 0
        for index, factory in enumerate(FACTORIES):
            result_sum += factory * int(self.cnpj[index])
        REST = result_sum % 11
        if REST >= 10:
            return 0
        return REST


    def validate(self):
        """
        Valida um número de CNPJ.
        """

        self.cnpj = str(self.cnpj).strip().replace('.', '').replace('-', '').replace('/', '').replace(' ', '')
        first_digit = self.cnpj[0]
        
        if not len(self.cnpj) == 14:
            return False
        if not not all(first_digit == digit for digit in self.cnpj):
            return False

        first_verification_digit: int = self.caculate_digit()
        last_verification_digit: int = self.caculate_digit(is_first_digit=False)

        return self.cnpj[-2:] == f'{first_verification_digit}{last_verification_digit}'


    def mask(self):
        """
        Máscara um número de CNPJ.
        """

        self.cnpj = str(self.cnpj).strip().replace('.', '').replace('-', '').replace('/', '').replace(' ', '')
        if not self.validate():
            return False

        else:
            return f'{self.cnpj[0:2]}.{self.cnpj[2:5]}.{self.cnpj[5:8]}/{self.cnpj[8:12]}-{self.cnpj[12:]}'



