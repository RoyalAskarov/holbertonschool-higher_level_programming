import pickle

class CustomObject:
    """
    A custom Python class to demonstrate serialization and deserialization
    using the pickle module.
    """

    def __init__(self, name: str, age: int, is_student: bool):
        """Initializes the CustomObject with name, age, and student status."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints out the object's attributes in the specified format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the current instance and saves it to the provided filename.
        Returns None if an error occurs during the process.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Loads and returns an instance of CustomObject from the provided filename.
        Returns None if the file is non-existent or malformed.
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, pickle.UnpicklingError, EOFError, Exception):
            return None