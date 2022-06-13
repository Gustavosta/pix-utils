#!/usr/bin/env python
#-*- coding:utf -8-*-3

import re


class Random(object):
    """
    Classe para validação de chaves PIX aleatórias UUID.
    """

    def __init__(self, random):
        """
        Inicializa a classe.
        """

        self.random = random


    def validate(self):
        """
        Valida uma chave PIX aleatória UUID.
        """

        pattern = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')
        random = str(self.random).strip().lower()

        if not re.match(pattern, random):
            return False

        else:
            return True
    

