import pypxml

# Serialize
data = {'name': 'Alice', 'age': 30, 'skills': ['Python', 'XML']}
pysxml.dump(data, 'output.pysxml')

# Deserialize
restored = pysxml.load('output.pysxml')
print(restored)
