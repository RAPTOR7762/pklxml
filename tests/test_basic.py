import pklxml

# Serialize
data = {'name': 'Alice', 'age': 30, 'skills': ['Python', 'XML']}
pklxml.dump(data, 'output.pklxml')

# Deserialize
restored = pklxml.load('output.pklxml')
print(restored)
