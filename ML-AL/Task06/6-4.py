glossary = {
    'variable': 'A storage location identified by a memory address and an associated symbolic name (an identifier), which contains some known or unknown quantity of information referred to as a value.',
    'function': 'A block of code designed to perform a specific task.',
    'loop': 'A control flow statement that allows code to be executed repeatedly based on a given condition.',
    'dictionary': 'A collection of key-value pairs, where each key must be unique.',
    'newline character': 'A special character that signifies the end of a line of text and the start of a new one.'
}

for word, meaning in glossary.items():
    print(f"{word}:\n{meaning}\n")

for word, meaning in glossary.items():
    print(f"{word}:\n{meaning}\n")

# Add five more terms
glossary['list'] = 'An ordered collection of items.'
glossary['tuple'] = 'An immutable ordered collection of items.'
glossary['set'] = 'An unordered collection of unique items.'
glossary['class'] = 'A blueprint for creating objects.'
glossary['module'] = 'A file containing Python definitions and statements.'

for word, meaning in glossary.items():
    print(f"{word}:\n{meaning}\n")
