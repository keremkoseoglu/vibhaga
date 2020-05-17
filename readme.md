# Vibhaga

Vibhaga is a dynamic module / class inspector for Python. If you want to dynamically load concrete classes derived from an abstract class, this tool can help.

## Installation

```
pip install git+https://github.com/keremkoseoglu/vibhaga.git
```

## Code samples

We'll assume that you want to inspect the following package structure:
- vibhaga
  - test
    - demo_abstract.py (contains class DemoAbstract)
    - demo_concrete.py (contains class DemoConcrete)

```python
Inspector.get_modules_in_cwd_container(Container(["vibhaga", "test"]))
```

Returns:
- demo_abstract (string)
- demo_concrete (string)

```python
Inspector.get_modules_in_path(path.join(getcwd(), "vibhaga", "test"))
```

Returns:
- demo_abstract (string)
- demo_concrete (string)

```python
Inspector.get_classes_in_cwd_container(Container(["vibhaga", "test"]))
```

Returns:
- vibhaga.test.demo_abstract (class)
- vibhaga.test.demo_concrete (class)

```python
Inspector.get_classes_in_container(Container(["vibhaga", "test"]))
```

Returns:
- vibhaga.test.demo_abstract (class)
- vibhaga.test.demo_concrete (class)

Check vibhaga.test.tester for more details.