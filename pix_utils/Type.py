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
    
    if CPF(value).validate() == True:
        return 'CPF', CPF(value).mask()

    if Phone(value).validate() == True:
        return 'Telefone', Phone(value).mask()

    if Random(value).validate() == True:
        return 'Aleatória', Random(value).mask()

    if Email(value).validate() == True:
        return 'Email', Email(value).mask()

    if CNPJ(value).validate() == True:
        return 'CNPJ', CNPJ(value).mask()

    return False



