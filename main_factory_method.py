# -- coding: utf-8 --
"""

Created on: 29/10/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
from __future__ import annotations
from abc import ABC, abstractmethod

class Creator(ABC):
    """
    La clase Creator declara el factory method que se supone que devolverá un
    objeto de una clase de Producto. Las subclases de Creator suelen
    proporcionar la implementación de este método.
    """

    @abstractmethod
    def factory_method(self):
        """
        Tenga en cuenta que el Creator también puede proporcionar alguna
        implementación predeterminada de el factory method.
        :return:
        """
        pass

    def some_operation(self) -> str:
        """
        También tenga en cuenta que, a pesar de su nombre, la responsabilidad
        principal del Creator no está creando productos. Por lo general,
         contiene alguna lógica comercial central que se basa en objetos
          Product, devueltos por el método de fábrica.
        Las subclases pueden cambiar indirectamente esa lógica empresarial
        anulando el factory method y devolver un tipo de producto diferente
        del mismo.

        :return: result
        """

        # llama al factory method para crear un Objeto Product.
        product = self.factory_method()

        #Ahora usamos el product.
        result = f"Creator: The same creator's code has just worked " \
                 f"with {product.operation()}"
        return result


"""
Concrete Creators anula el factory method para cambiar la salida
tipo de producto.
"""

class ConcreteCreator1(Creator):
    """
    Observe que la firma del método sigue utilizando el tipo de
    producto abstracto aunque el producto concreto sea devuelto por el método.
     Este manera el Creador puede permanecer independiente de las clases
      de productos concretos.
    """

    def factory_method(self) -> Product:
        return ConcreteProduct1()

class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()


class Product(ABC):
    """
    La interfaz Product declara las operaciones que todos los productos
     concretos deben implementar.
    """

    @abstractmethod
    def operation(self) -> str:
        pass


"""
Los Productos concretos proporcionan varias implementaciones
 de la interfaz del Producto.
"""

class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"

class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"

def client_code(creator: Creator) -> None:
    """
    El código del cliente trabaja con una instancia de un creador concreto,
    aunque a través de su interfaz base. Mientras el cliente siga trabajando
     con el creador a través de la interfaz base, puede pasarle cualquier
    subclase del creador.
    """

    print(f"Client: I'm not aware of the creator's class, but it "
          f"still works.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())








