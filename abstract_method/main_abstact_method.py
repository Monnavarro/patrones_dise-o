# -- coding: utf-8 --
"""

Created on: 29/10/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""

from __future__ import annotations
from abc import ABC, abstractmethod

"""
 La interfaz fábrica abstracta declara un grupo de métodos que
 devuelven distintos productos abstractos. Estos productos se
 denominan familia y están relacionados por un tema o concepto
 de alto nivel. Normalmente, los productos de una familia
 pueden colaborar entre sí. Una familia de productos puede
 tener muchas variantes, pero los productos de una variante
 son incompatibles con los productos de otra.
"""

class AbstractFactory(ABC):

    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:

        """
         Las fábricas concretas producen una familia de productos que
 pertenecen a una única variante. La fábrica garantiza que los
 productos resultantes sean compatibles. Las firmas de los
 métodos de las fábricas concretas devuelven un producto
 abstracto mientras que dentro del método se instancia un
 producto concreto.
        """

class WinFactory(AbstractFactory):

    def create_button(self) -> Button:
        return WinButton()

    def create_checkbox(self) -> Checkbox:
        return WinCheckbox()

    """
     Cada fábrica concreta tiene una variante de producto
 correspondiente.
    """
class MacFactory(AbstractFactory):

    def create_button(self) -> Button:
        return MacBotton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()

    """
     Cada producto individual de una familia de productos debe
 tener una interfaz base. Todas las variantes del producto
 deben implementar esta interfaz.
    """
class Button(ABC):

    @abstractmethod
    def paint(self) -> str:
        pass

    """
     Los productos concretos son creados por las fábricas
 concretas correspondientes.
    """
class WinButton(Button):

    def paint(self) -> str:
        return "Representa un botón en estilo Windows."

class MacBotton(Button):

    def paint(self) -> str:
        return "Representa una casilla en estilo macOS."


"""
 Aquí está la interfaz base de otro producto. Todos los
 productos pueden interactuar entre sí, pero sólo entre
 productos de la misma variante concreta es posible una
 interacción adecuada.
"""
class Checkbox(ABC):

    @abstractmethod
    def paint(self) -> None:  # useful_function_b
        """
         El producto B es capaz de hacer lo suyo...
        """
        pass


    @abstractmethod
    def paint(self, collaborator: Button) -> None:
        """
        ...pero también puede colaborar con el ProductoA.

        La Fábrica Abstracta se asegura de que todos los productos que
        crea son de la misma variante y, por tanto, compatibles.
        """
        pass

"""
Los productos concretos son creados por sus concretas Fábricas
"""
























