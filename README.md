![License](https://img.shields.io/github/license/RAPTOR7762/pklxml)
![PyPi](https://img.shields.io/badge/version-N/A-orange)
![File Extension](https://img.shields.io/badge/file%20extension-.pklxml-blue)

## pklxml

pklxml, short for Python **P**ic**kl**e E**x**tensible **M**arkup **L**anguage Library, is a Python module and as a human-readable alternative to [Pickle](https://docs.python.org/3/library/pickle.html). Instead of saving data as a binary `.pkl` file, it saves data as an XML-based file called `.pklxml`. This makes it a lot more safer. The module uses the LXML module to parse `.pklxml` (XML) files.

The reason why I wanted to make this module is so that we (as humans) can see what has been actually saved. Currently, I have to open `.pkl` files with Qt Creator to decode the binary and usuall, with (no) success.

## Example programme
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
## Contribute

Contribute to this repository if you can! Star my repository! Thanks!
