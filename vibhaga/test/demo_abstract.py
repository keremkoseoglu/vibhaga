""" Module for demo abstract class """
from abc import ABC, abstractmethod


class DemoAbstract(ABC):
    """ Demo abstract class for testing purposes """

    @abstractmethod
    def demo_abstract_method(self):
        """ Demo abstract method """

    def demo_method(self):
        """ Demo concrete method """
        pass
