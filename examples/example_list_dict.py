import pklxml

# Serialize
data = {'name': 'Alice', 'age': 30, 'skills': ['Python', 'XML']}
pklxml.dump(data, 'output.pklxml')

# Deserialize
try:
  data = pklxml.load('output.pklxml')
  print(restored)
except OSError:
  data = {}
