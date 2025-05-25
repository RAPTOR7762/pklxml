## Project Metadata

- **Version**: 0.0.1  
- **PyPI**: Not published yet  
- **File Extension**: `.pypxml`

```bash
pip install git+https://github.com/RAPTOR7762/pypxml.git
```
![License](https://img.shields.io/github/license/RAPTOR7762/pypxml)
![Stars](https://img.shields.io/github/stars/RAPTOR7762/pypxml)

## pypxml

pypxml, short for **Py**thon **P**ickle E**x**tensible **M**arkup **L**anguage Library, is a Python module and as a human-readable alternative to [Pickle](https://docs.python.org/3/library/pickle.html). Instead of saving data as a binary `.pkl` file, it saves data as an XML-based file called `.pypxml`. This makes it a lot more safer. The module uses the LXML module to parse `.pypxml` (XML) files.

The reason why I wanted to make this module is so that we (as humans) can easily what has been actually saved. I have to open `.pkl` files with Qt Creator to decode the binary and I (un)successfully managed to decode it.

I'm thinking of publishing this to PyPi, but maybe not so soon.

## Example programme
```python
from pypxml import dump, load

data = {'name': 'Alice', 'age': 30}
dump(data, 'data.pypxml')

loaded_data = load('data.pypxml')
print(loaded_data)
```
## Contribute

Contribute to this repository if you can! Like my repository! Thanks!
