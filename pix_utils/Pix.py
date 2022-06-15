#!/usr/bin/env python
#-*- coding:utf -8-*-3

from binascii import crc_hqx
from decimal import Decimal
from typing import Optional
from decimal import ROUND_HALF_UP, Decimal


def Code(key: str, name: str, city: str, value: float = None, identifier: Optional[str] = None):
    """
    Essa função serve para criar uma string de código PIX copia e cola
    estático, para geração de pagamentos.
    """
    
    def get_payload():
        """
        Retorna o indicador de formato do payload.
        """

        return "000201"


    def get_merchant_account(key: str):
        """
        Retorna a informação da conta do comerciante.
        """

        GUI = "0014BR.GOV.BCB.PIX"
        string = "01{l:02d}{k}".format(l=len(key), k=key)
        result = GUI + string

        if len(result) > 99:
            raise ValueError("PIX key is too long.")

        return "26{l:02d}{r}".format(l=len(result), r=result)


    def get_merchant_category():
        """
        Retorna o código da categoria do comerciante.
        """

        return '52040000'


    def get_transaction_currency():
        """
        Retorna o código da moeda da transação.
        """

        return '5303986'


    def get_transaction_value(value: Decimal):
        """
        Retorna o valor da transação.
        """

        if value <= Decimal('0.00'):
            raise ValueError("Only positive decimals allowed.")

        string = str(value)
        return f"54{'{:02d}'.format(len(string))}{string}"


    def get_country():
        """
        Retorna o código do país.
        """

        return '5802BR'


    def get_merchant_name(name: str):
        """
        Retorna o nome do comerciante.
        """

        if len(name) > 25:
            raise ValueError(
                "Recipient name must be less than 25 characters long.")
        return f"59{'{:02d}'.format(len(name))}{name}"


    def get_merchant_city(city: str):
        """
        Retorna a cidade do comerciante.
        """

        if len(city) > 15:
            raise ValueError("Max of 15 characters for city name.")
        return f"60{'{:02d}'.format(len(city))}{city}"


    def get_additional_data_field_template(identifier: Optional[str] = None):
        """
        Retorna o template do campo de dados adicionais.
        """

        if not identifier:
            identifier = '***'

        if len(identifier) > 25:
            raise ValueError("Only indentifiers with length less than 25 "
                            "characters are allowed.")

        txid = f"05{'{:02d}'.format(len(identifier))}{identifier}"
        return f"62{'{:02d}'.format(len(txid))}{txid}"


    def get_crc16(payload: str):
        """
        Retorna o CRC16 do payload.
        """

        checksum = crc_hqx(bytes(payload + '6304', 'ascii'), 0xFFFF)
        return hex(checksum)[2:].upper()


    def round_decimal(value: Decimal):
        """
        Arredonda um valor decimal.
        """

        value = Decimal(value)
        return Decimal(value.quantize(Decimal('.01'), rounding=ROUND_HALF_UP))


    transaction_value: str
    if value is not None:
        value = Decimal(value)
        transaction_value = get_transaction_value(round_decimal(value))
    else:
        transaction_value = ''

    payload = "{pfi}{mai}{mcc}{tc}{tv}{cc}{mn}{mc}{adft}".format(
        pfi=get_payload(),
        mai=get_merchant_account(key),
        mcc=get_merchant_category(),
        tc=get_transaction_currency(),
        tv=transaction_value,
        cc=get_country(),
        mn=get_merchant_name(name),
        mc=get_merchant_city(city),
        adft=get_additional_data_field_template(identifier),
    )

    crc = get_crc16(payload)
    return payload + f"6304{crc}"




