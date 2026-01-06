from abc import ABC, abstractmethod

# ---------------------------------------------------------
# GRANDPARENT CLASS — ABSTRACT BASE CLASS
# ---------------------------------------------------------
class Animal(ABC):
    # Constructor: sets shared attributes for all animals
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Abstract method: forces all subclasses to implement make_sound()
    @abstractmethod
    def make_sound(self):
        pass

    # Dunder method #1: readable string representation
    def __str__(self):
        return f"{self.name} ({self.age} yrs)"

    # Overloaded method using *args
    # Allows extra descriptive info to be added
    def describe(self, *args):
        base = f"Animal: {self.name}"
        if args:
            extras = ", ".join(args)
            return f"{base} | {extras}"
        return base


# ---------------------------------------------------------
# PARENT CLASS 1 — MAMMAL
# ---------------------------------------------------------
class Mammal(Animal):
    # Constructor: uses super() to call Animal's __init__
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    # Method unique to mammals
    def walk(self):
        return f"{self.name} is walking."

    # Required abstract method implementation
    def make_sound(self):
        return "generic mammal sound"

    # Dunder method #2: formal string representation
    def __repr__(self):
        return f"Mammal(name={self.name}, fur_color={self.fur_color})"


# ---------------------------------------------------------
# PARENT CLASS 2 — BIRD
# ---------------------------------------------------------
class Bird(Animal):
    # Constructor: uses super() to call Animal's __init__
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    # Method unique to birds
    def fly(self):
        return f"{self.name} is flying."

    # Required abstract method implementation
    def make_sound(self):
        return "generic bird sound"

    # Dunder method #3: formal string representation
    def __repr__(self):
        return f"Bird(name={self.name}, wing_span={self.wing_span})"


# ---------------------------------------------------------
# CHILD CLASS 1 — DOG
# ---------------------------------------------------------
class Dog(Mammal):
    # Constructor: uses super() to call Mammal's __init__
    def __init__(self, name, age, fur_color, breed):
        super().__init__(name, age, fur_color)
        self.breed = breed

    # Method unique to dogs
    def bark(self):
        return "Woof!"

    # Dunder method #4: returns length of dog's name
    def __len__(self):
        return len(self.name)


# ---------------------------------------------------------
# CHILD CLASS 2 — PARROT
# ---------------------------------------------------------
class Parrot(Bird):
    # Constructor: uses super() to call Bird's __init__
    def __init__(self, name, age, wing_span, vocab):
        super().__init__(name, age, wing_span)
        self.vocab = vocab  # number of words the parrot knows

    # Method unique to parrots
    def talk(self):
        return "Hello!"

    # Dunder method #5: returns vocabulary size
    def __len__(self):
        return self.vocab
