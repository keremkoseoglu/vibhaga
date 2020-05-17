""" Module for demo concrete class """
from vibhaga.test.demo_abstract import DemoAbstract


class DemoConcrete(DemoAbstract):
    """ Demo concrete class for testing purposes """

    def __init__(self):
        print("Demo concrete created")

    def demo_abstract_method(self):
        """ Demo abstract method """
        print("DemoConcrete :: demo_abstract_method called")
