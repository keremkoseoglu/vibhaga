""" Main tester module for Vibhaga """
from os import getcwd, path
from vibhaga.inspector import Container, Inspector

class Tester:
    """ Main tester class """

    def __init__(self):
        self._container = Container(["vibhaga", "test"])

    def test(self):
        self._test_gmicc()
        self._test_gmip()
        self._test_gcicc()
        self._test_gcic()

    def _test_gmicc(self):
        print("Testing get_modules_in_cwd_container")
        modules = Inspector.get_modules_in_cwd_container(self._container)
        for module in modules:
            print("- Found module: " + module)

    def _test_gmip(self):
        print("Testing get_modules_in_path")
        full_path = path.join(getcwd(), "vibhaga", "test")
        modules = Inspector.get_modules_in_path(full_path)
        for module in modules:
            print ("- Found module: " + module)
        print("Testing get_modules_in_path with tester filter")
        modules = Inspector.get_modules_in_path(full_path, ["tester"])
        for module in modules:
            print ("- Found module: " + module)

    def _test_gcicc(self):
        print("Testing get_classes_in_cwd_container")
        classes = Inspector.get_classes_in_cwd_container(self._container)
        for class_name in classes:
            print("- Found class: " + class_name.__module__)

    def _test_gcic(self):
        print("Testing get_classes_in_container")
        classes = Inspector.get_classes_in_container(self._container)
        for class_name in classes:
            print("- Found class: " + class_name.__module__)
