#!/usr/bin/env python
#-*- coding:utf -8-*-3

from CPF import CPF
from Phone import Phone
from Random import Random
from Email import Email
from CNPJ import CNPJ


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



