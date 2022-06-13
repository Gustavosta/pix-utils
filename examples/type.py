#!/usr/bin/env python
#-*- coding:utf -8-*-3

from pix_utils import Type


# Vamos indentificar os tipos de chave PIX.
print(Type('11438374798')) # (CPF, '114.383.749-98')
print(Type('11991234567')) # (Phone, '(11) 99123-4567')
print(Type('06990590000123')) # (CNPJ, '06.990.590/0001-23')
print(Type('12345678-1234-1234-1234-123456789012')) # (Random, '12345678-1234-1234-1234-123456789012')
print(Type('example@example.com')) # (Email, example@example.com')


