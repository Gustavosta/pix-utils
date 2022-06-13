#!/usr/bin/env python
#-*- coding:utf -8-*-3

from pix_utils.Base import Base


class CNPJ(Base):
    """
    Classe para validação de números de CNPJ.
    """

    def caculate_digit(self, cnpj, is_first_digit: bool = True):
        """
        Calcula o dígito verificador.
        """

        if is_first_digit:
            FACTORIES = [6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9]
        else:
            FACTORIES = [5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9]

        result_sum = 0
        for index, factory in enumerate(FACTORIES):
            result_sum += factory * int(cnpj[index])
        REST = result_sum % 11
        if REST >= 10:
            return 0
        return REST


    def validate(self, cnpj):
        """
        Valida um número de CNPJ.
        """

        cnpj = str(cnpj).strip().replace('.', '').replace('-', '').replace('/', '').replace(' ', '')
        first_digit = cnpj[0]
        
        if not len(cnpj) == 14:
            return False
        if not not all(first_digit == digit for digit in cnpj):
            return False

        first_verification_digit: int = self.caculate_digit(cnpj)
        last_verification_digit: int = self.caculate_digit(cnpj, is_first_digit=False)

        return cnpj[-2:] == f'{first_verification_digit}{last_verification_digit}'


    def mask(self, cnpj):
        """
        Máscara um número de CNPJ.
        """

        cnpj = str(cnpj).strip().replace('.', '').replace('-', '').replace('/', '').replace(' ', '')
        if not self.validate():
            return False

        else:
            return f'{cnpj[0:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}'




