#!/usr/bin/env python
#-*- coding:utf -8-*-3

import re


class Email(object):
    """
    Classe para validação de emails.
    """

    def __init__(self, email):
        """
        Inicializa a classe.
        """

        self.email = email


    def validate(self):
        """
        Valida um email.
        """

        pattern = re.compile(r'^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$')
        email = str(self.email).strip().lower()

        if not re.match(pattern, email):
            return False
        
        else:
            return True
    

