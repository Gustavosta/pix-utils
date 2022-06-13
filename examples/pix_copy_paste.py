#!/usr/bin/env python
#-*- coding:utf -8-*-3

from pix_utils import Code


KEY = '11438374798' # Chave PIX.
NAME = 'John Doe' # Nome do dono do PIX.
CITY = 'Sao Paulo' # Cidade do dono do PIX. Lembre-se de não usar acentos.
VALUE = 10.00 # Valor da transação.
INDENTIFY = '12345678' # Indentificador da transação (opcional).


print(Code(KEY, NAME, CITY, VALUE, INDENTIFY)) # 00020126330014BR.GOV.BCB.PIX011111438374798520400005303986540510.005802BR5908John Doe6009Sao Paulo621205081234567863046A00
