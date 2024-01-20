# Card Sorting Script

Examining Static vs Instance Methods in Python

## Notes on Static Methods: Python vs JavaScript

### Key Differences

1. Decorator vs. Keyword:

    - **Python:** Defines static methods using the `@staticmethod` decorator.
    - **JavaScript:** Uses the `static` keyword directly within the class definition.

2. Class Methods:

    - **Python:** Distinguishes between static methods and class methods using `@staticmethod` and `@classmethod` decorators.
    - **JavaScript:** Doesn't have a separate concept of class methods. Functions defined as `static` are the closest equivalent.

3. Class-Based vs. Prototype-Based:

    - **Python:** Class-based, with classes defining blueprints for creating objects.
    - **JavaScript:** Prototype-based, where classes are essentially syntactic sugar for creating objects with shared prototypes.

4. Inheritance:

    - **Python:** Static methods are not inherited by subclasses.
    - **JavaScript:** Static methods are inherited by subclasses, but they are not shared across instances.

5. Calling Convention:

    - **Both:** Called directly on the class itself, without the need to create an instance.

### Takeaways

- Python's static methods are more isolated and don't access class or instance attributes.
- JavaScript's static methods, due to the prototype-based nature, have implicit access to the class's prototype.
