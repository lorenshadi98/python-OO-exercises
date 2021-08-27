"""Python serial number generator."""


# from _typeshed import StrPath


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """Generates a number from give start"""
        self.start = self.next = start

    def generate(self):
        """Increments the start number by one"""
        self.next += 1
        return self.next - 1

    def reset(self):
        """resets number back to start"""
        self.next = self.start
