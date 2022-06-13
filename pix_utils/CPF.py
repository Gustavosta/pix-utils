#!/usr/bin/env python
#-*- coding:utf -8-*-3

from pix_utils.Base import Base


class CPF(Base):
    """
    Classe para validação de números de CPF.
    """

    def validate(self, cpf):
        """
        Valida um número de CPF.
        """

        cpf = str(cpf).strip().replace('.', '').replace('-', '').replace(' ', '')

        if not len(cpf) == 11:
            return False    

        if cpf in [s * 11 for s in [str(n) for n in range(10)]]:
            return False

        calc = [i for i in range(1, 10)]

        d1= (sum([int(a)*b for a,b in zip(cpf[:-2], calc)]) % 11) % 10
        d2= (sum([int(a)*b for a,b in zip(reversed(cpf[:-2]), calc)]) % 11) % 10

        return str(d1) == cpf[-2] and str(d2) == cpf[-1]


    def mask(self, cpf):
        """
        Máscara um número de CPF.
        """

        cpf = str(cpf).strip().replace('.', '').replace('-', '').replace(' ', '')

        if not self.validate(cpf):
            return False

        else:
            return '{}.{}.{}-{}'.format(cpf[0:3], cpf[3:6], cpf[6:9], cpf[9:])
