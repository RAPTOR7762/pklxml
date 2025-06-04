![License](https://img.shields.io/github/license/RAPTOR7762/pklxml)
![PyPi](https://img.shields.io/badge/version-v0.2.3-orange)
![File Extension](https://img.shields.io/badge/file%20extension-.pklxml-blue)

## pklxml

pklxml, short for Python **P**ic**kl**e E**x**tensible **M**arkup **L**anguage Library, is a Python module and as a human-readable alternative to [Pickle](https://docs.python.org/3/library/pickle.html). Instead of saving data as a binary `.pkl` file, it saves data as an XML-based file called `.pklxml`. This makes it a lot more safer. The module uses the LXML module to parse `.pklxml` (XML) files.

The reason why I wanted to make this module is so that we (as humans) can see what has been actually saved. Currently, I have to open `.pkl` files with Qt Creator to decode the binary and usually, with (no) success.

## Example programme

List and dictionary example code

```python
from pklxml import dump, load

data = {'name': 'Alice', 'age': 30}
dump(data, 'data.pklxml')

try:
  data = load('data.pklxml')
  print(data)
except OSError:
  data = {}
```

Class example code

```python
from pklxml import dump, load

# Define a simple class (normally this would be in a separate module)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Register the class somewhere importable if needed
# For now, let's pretend it's in 'example_class' for deserialization
Person.__module__ = "examples.example_class"

# Create an instance
alice = Person("Alice", 30)

# Serialize to XML
pklxml.dump(alice, "examples/output_basic.pklxml")

# Deserialize from XML
try:
    restored = pklxml.load("examples/output_basic.pklxml")
    print(f"Restored: {restored.__class__.__name__}({restored.name}, {restored.age})")
except OSError as e:
    print("Failed to load .pklxml file:", e)
```

## Contribute

Contribute to this repository if you can! Star my repository! Thanks!
