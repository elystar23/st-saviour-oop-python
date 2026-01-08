import unittest
from animal import Animal, Mammal, Bird, Dog, Parrot

# ---------------------------------------------------------
# TEST SUITE FOR LAB 4 — PART 3
# ---------------------------------------------------------
class TestAnimals(unittest.TestCase):

    # setUp() runs before every test
    # Creates sample objects to test with
    def setUp(self):
        self.dog = Dog("Buddy", 5, "Brown", "Beagle")
        self.parrot = Parrot("Kiwi", 2, 12.5, 30)

    # -----------------------------------------------------
    # 1. POLYMORPHISM TEST
    # Uses isinstance() to confirm Dog and Parrot
    # are BOTH subclasses of Animal
    # -----------------------------------------------------
    def test_polymorphism(self):
        self.assertTrue(isinstance(self.dog, Animal))
        self.assertTrue(isinstance(self.parrot, Animal))

    # -----------------------------------------------------
    # 2. INHERITANCE TEST
    # Confirms that child classes inherited methods
    # from their parent classes (walk, fly)
    # -----------------------------------------------------
    def test_inherited_methods(self):
        # Dog inherits walk() from Mammal
        self.assertEqual(self.dog.walk(), "Buddy is walking.")

        # Parrot inherits fly() from Bird
        self.assertEqual(self.parrot.fly(), "Kiwi is flying.")

    # -----------------------------------------------------
    # 3. LIST USAGE TEST
    # Demonstrates list usage + polymorphism
    # by looping through different animal types
    # -----------------------------------------------------
    def test_list_usage(self):
        animals = [self.dog, self.parrot]  # list of mixed types

        # Collect sounds from each animal
        sounds = [a.make_sound() for a in animals]

        # Confirm list works and contains expected values
        self.assertEqual(len(animals), 2)
        self.assertIn("generic mammal sound", sounds)
        self.assertIn("generic bird sound", sounds)

    # -----------------------------------------------------
    # 4. ABSTRACT CLASS TEST (+5 BONUS)
    # Confirms Animal cannot be instantiated directly
    # because it contains an @abstractmethod
    # -----------------------------------------------------
    def test_abstract_class(self):
        with self.assertRaises(TypeError):
            Animal("Ghost", 100)  # should fail


# Runs the test suite
if __name__ == "__main__":
    unittest.main()