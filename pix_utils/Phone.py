#!/usr/bin/env python
#-*- coding:utf -8-*-3

import re


class Phone(object):
    """
    Classe para validação de números de telefone.
    """

    def __init__(self, phone):
        """
        Inicializa a classe.
        """

        self.phone = phone


    def validate(self):
        """
        Valida um número de telefone.
        """

        pattern = re.compile(r'([1-9]{2})(9[1-9])([0-9]{3})([0-9]{4})')
        number = str(self.phone).strip().replace(' ', '').replace('(', '').replace(')', '').replace('-', '')

        if not re.match(pattern, number):
            return False

        else:
            return True


    def mask(self):
        """
        Máscara um número de telefone.
        """

        pattern = re.compile(r'([1-9]{2})(9[1-9])([0-9]{3})([0-9]{4})')
        number = str(self.phone).strip().replace(' ', '').replace('(', '').replace(')', '').replace('-', '')

        if not re.match(pattern, number):
            return False

        else:
            return '({}) {}-{}'.format(number[0:2], number[2:7], number[7:])


