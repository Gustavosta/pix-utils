#!/usr/bin/env python
#-*- coding:utf -8-*-3

from pix_utils.CPF import CPF
from pix_utils.Phone import Phone
from pix_utils.Random import Random
from pix_utils.Email import Email
from pix_utils.CNPJ import CNPJ


def Type(value):
    """
    Valida um número de CPF, telefone, email, CNPJ ou chave PIX aleatória.
    """
    
    if CPF().validate(value) == True:
        return 'CPF', CPF().mask(value)

    if Phone().validate(value) == True:
        return 'Phone', Phone().mask(value)

    if Random().validate(value) == True:
        return 'Random', Random().mask(value)

    if Email().validate(value) == True:
        return 'Email', Email().mask(value)

    if CNPJ().validate(value) == True:
        return 'CNPJ', CNPJ().mask(value)

    return False



