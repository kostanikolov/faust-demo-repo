class SingletonMeta(type):
    """
    A metaclass for creating Singleton classes.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            # If an instance doesn't exist, create one and store it.
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class SingletonClass(metaclass=SingletonMeta):
    """
    Example class using the Singleton pattern.
    """
    def __init__(self, value):
        self.value = value


# Test the Singleton behavior
if __name__ == "__main__":
    obj1 = SingletonClass("First Instance")
    obj2 = SingletonClass("Second Instance")

    print(f"Object 1 value: {obj1.value}")  # Outputs: First Instance
    print(f"Object 2 value: {obj2.value}")  # Outputs: First Instance

    print(f"Are both objects the same? {'Yes' if obj1 is obj2 else 'No'}")

