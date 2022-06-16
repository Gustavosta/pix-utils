# pix-utils

Módulo para validação de chaves PIX e geração de chaves PIX copia-e-cola

## Instalação

você pode instalar o módulo usando o comando:

```bash
pip install pix-utils
```

## Recursos

Veja alguns dos recursos desta biblioteca:

### Validação de chaves PIX.

Valida o tipo de chave chamando o método `validate`.

```python
from pix_utils import CPF, CNPJ, Email, Phone, Random


print(Phone().validate('11991234567')) # True
print(Email().validate('example@example.com')) # True
print(CPF().validate('12345678901')) # False
print(CNPJ().validate('06.990.590/0001-23')) # True
print(Random().validate('12345678-1234-1234-1234-123456789012')) # True
```

### Formatação de chaves PIX para CPF, CNPJ e telefone.

Máscara chaves PIX de CPF, CNPJ e telefone chamando o método `mask`.

```python
from pix_utils import CPF, CNPJ, Phone


print(CPF().mask('11438374798')) # 114.383.747-98
print(Phone().mask('11991234567')) # (11) 99123-4567
print(CNPJ().mask('06990590000123')) # 06.990.590/0001-23
```

### Geração de códigos para pagamento PIX estático.

Gera códigos de pagamento estáticos de PIX copia-e-cola.

```python
from pix_utils import Code


KEY = '11438374798' # Chave PIX.
NAME = 'John Doe' # Nome do dono do PIX.
CITY = 'Sao Paulo' # Cidade do dono do PIX. Lembre-se de não usar acentos.
VALUE = 10.00 # Valor da transação.
INDENTIFY = '12345678' # Indentificador da transação (opcional).

print(Code(key=KEY, name=NAME, city=CITY, value=VALUE, identifier=INDENTIFY)) 
# 00020126330014BR.GOV.BCB.PIX011111438374798520400005303986540510.005802BR5908John Doe6009Sao Paulo621205081234567863046A00
```

### Indentificar e formatar chave PIX

Automáticamente Indentifica o tipo de chave PIX e a formata.

```python
from pix_utils import Type


print(Type('11438374798')) # (CPF, '114.383.749-98')
print(Type('11991234567')) # (Phone, '(11) 99123-4567')
print(Type('06990590000123')) # (CNPJ, '06.990.590/0001-23')
print(Type('12345678-1234-1234-1234-123456789012')) # (Random, '12345678-1234-1234-1234-123456789012')
print(Type('example@example.com')) # (Email, example@example.com')
```

Você pode ver exemplos de usos [aqui](/examples)

## Licença

[MIT Licence](LICENSE)


