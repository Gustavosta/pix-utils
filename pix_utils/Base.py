from abc import ABC


class Base(ABC):
    """
    Classe base para todos os modelos.
    """

    def __init__(self, *args, **kwargs):
        """
        Inicializa o modelo.
        """

        self.__dict__.update(kwargs)
