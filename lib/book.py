#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count  # Calls the setter

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        self.validate_page_count(page_count)  # ✅ Correct usage
        self._page_count = page_count

    def validate_page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        elif value <= 0:
            print("page_count must be greater than 0")


    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
