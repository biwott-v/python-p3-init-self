#!/usr/bin/env python3

class Dog:
    def __init__(self,name,breed="Mutt"):
        self.breed=breed
        self.name=name
        print(f"print {name} is born")

    def bark(self):
        print("Woof!")