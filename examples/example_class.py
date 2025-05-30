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
