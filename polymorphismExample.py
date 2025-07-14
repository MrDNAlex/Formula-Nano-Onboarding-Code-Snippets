from abc import ABC, abstractmethod

# Inheritance Example
# Interface Example using Abstract Base Class (ABC)
class Phone(ABC): 
    OS: str
    
    @abstractmethod
    def call(self, number: str) -> str:
        pass
    
    @abstractmethod
    def text(self, number: str, message: str) -> str:
        pass

# IPhone and Android classes IMPLEMENTS from Phone Interface
class IPhone(Phone):
    OS = "iOS"
    
    def call(self, number: str) -> str:
        return f"Calling {number} from iPhone."
    
    def text(self, number: str, message: str) -> str:
        return f"Sending text to {number} from iPhone: {message}"
    
class Android(Phone):
    OS = "Android"
    
    def call(self, number: str) -> str:
        return f"Calling {number} from Android."
    
    def text(self, number: str, message: str) -> str:
        return f"Sending text to {number} from Android: {message}"

# Google Pixel class INHERITS from Android
class GooglePixel(Android):
    
    def browse(self, url: str) -> str:
        return f"Browsing {url} on Google Pixel."

pixel = GooglePixel()
print(pixel.OS)  # Output: "Android"
print(pixel.call("123-456-7890"))  # Output: "Calling 123-456-7890 from Android."
print(pixel.text("123-456-7890", "Hello!"))  # Output: "Sending text to 123-456-7890 from Android: Hello!"
print(pixel.browse("www.example.com"))  # Output: "Browsing www.example.com on Google Pixel."

print("\n")

# Polymorphism Example
class Animal(ABC):
    def speak(self) -> str:
        return "Animal sound"
    
    def eat(self, food: str) -> str:
        return f"Animal is eating {food}."
   
    def sleep(self) -> str:
        return "Animal is sleeping."

# Dog and Cat classes INHERIT from Animal Interface
# They implement the abstract methods defined in Animal
class Dog(Animal):
    def speak(self) -> str:
        return "Woof! Woof!"
    
    def eat(self, food: str) -> str:
        return f"The dog is eating {food}."
    
    def sleep(self) -> str:
        return "The dog is sleeping."
    
class Cat(Animal):
    def speak(self) -> str:
        return "Meow! Meow!"
    
    def eat(self, food: str) -> str:
        return f"The cat is eating {food}."
    
    def sleep(self) -> str:
        return "The cat is sleeping."

animal = Animal()  # This will raise an error since Animal is abstract
dog = Dog() 
cat = Cat()

# Using polymorphism
print(animal.speak()) # Output: "Animal sound"
print(dog.speak())  # Output: "Woof! Woof!"
print(cat.speak())  # Output: "Meow! Meow!"

print(animal.eat("food"))  # Output: "Animal is eating food."
print(dog.eat("bone"))  # Output: "The dog is eating bone."
print(cat.eat("fish"))  # Output: "The cat is eating fish."

print(animal.sleep())  # Output: "Animal is sleeping."
print(dog.sleep())  # Output: "The dog is sleeping."
print(cat.sleep())  # Output: "The cat is sleeping."