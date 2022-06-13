#!/usr/bin/env python
#-*- coding:utf -8-*-3

from pix_utils import CPF, CNPJ, Email, Phone, Random


cpf = CPF()
cnpj = CNPJ()
email = Email()
phone = Phone()
random = Random()

# Valida um número de Telefone
print(phone.validate('11991234567')) # True

# Valida um Email
print(email.validate('example@example.com')) # True

# Valida um CPF
print(cpf.validate('12345678901')) # False

# Valida um CNPJ
print(cnpj.validate('06.990.590/0001-23')) # True

# Valida uma chave PIX aleatória
print(random.validate('12345678-1234-1234-1234-123456789012')) # True



