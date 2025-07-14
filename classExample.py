class Dog:
    # Properties of the Dog class
    name: str
    breed: str
    colour: str
    
    # Constructor for the Dog class
    def __init__ (self, name:str, breed:str, colour:str):
        self.name = name
        self.breed = breed
        self.colour = colour
        
    # Methods of the Dog class
    def bark(self) -> str:
        return "Woof! Woof!"
    
    def eat(self, food: str) -> str:
        return f"{self.name} is eating {food}."

    def fetch(self, item: str) -> str:
        return f"{self.name} fetched the {item}!"

mika = Dog("Mika", "Golden Retriever", "Golden")

print(mika.name)  # Output: "Mika"
print(mika.breed)  # Output: "Golden Retriever" 
print(mika.colour)  # Output: "Golden"
print("\n")
print(mika.bark())  # Output: "Woof! Woof!"
print(mika.eat("dog food"))  # Output: "Mika is eating dog food."
print(mika.fetch("ball"))  # Output: "Mika fetched the ball!"



