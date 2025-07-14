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


# Polymorphism Example

class Animal(ABC):
    @abstractmethod
    def speak(self) -> str:
        pass
    
    @abstractmethod
    def eat(self, food: str) -> str:
       pass
   
    @abstractmethod
    def sleep(self) -> str:
        pass
    
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
    