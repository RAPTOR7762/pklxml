## Project Metadata

- **Version**: 0.1.0
- **PyPI**: Published
- **File Extension**: `.pklxml`

![License](https://img.shields.io/github/license/RAPTOR7762/pklxml)

## pklxml

pklxml, short for Python **P**ic**kl**e E**x**tensible **M**arkup **L**anguage Library, is a Python module and as a human-readable alternative to [Pickle](https://docs.python.org/3/library/pickle.html). Instead of saving data as a binary `.pkl` file, it saves data as an XML-based file called `.pklxml`. This makes it a lot more safer. The module uses the LXML module to parse `.pklxml` (XML) files.

The reason why I wanted to make this module is so that we (as humans) can easily what has been actually saved. I have to open `.pkl` files with Qt Creator to decode the binary and I (un)successfully managed to decode it.

I'm thinking of publishing this to PyPi, but maybe not so soon.

## Example programme
```python
from pklxml import dump, load

data = {'name': 'Alice', 'age': 30}
dump(data, 'data.pklxml')

loaded_data = load('data.pklxml')
print(loaded_data)
```
## Contribute

Contribute to this repository if you can! Like my repository! Thanks!
