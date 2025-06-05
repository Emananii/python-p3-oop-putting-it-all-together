#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        self.validate_size(size)
        self._size = size

    def validate_size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        
    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")