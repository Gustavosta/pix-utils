#!/usr/bin/env python
#-*- coding:utf -8-*-3

from pix_utils import CPF, CNPJ, Phone


cpf = CPF() 
cnpj = CNPJ()
phone = Phone()


# Mascara um número de CPF
print(cpf.mask('12345678901')) # 123.456.789-01

# Mascara um número de Telefone
print(phone.mask('11991234567')) # (11) 99123-4567

# Mascara um número de CNPJ
print(cnpj.mask('06990590000123')) # 06.990.590/0001-23
