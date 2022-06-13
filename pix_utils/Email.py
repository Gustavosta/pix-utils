#!/usr/bin/env python
#-*- coding:utf -8-*-3

import re
from pix_utils.Base import Base


class Email(Base):
    """
    Classe para validação de emails.
    """

    def validate(self, email):
        """
        Valida um email.
        """

        pattern = re.compile(r'^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$')
        email = str(email).strip().lower()

        if not re.match(pattern, email):
            return False
        
        else:
            return True
    



