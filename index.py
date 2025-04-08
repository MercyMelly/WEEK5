# QUESTION ONE

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self._year = year # so as to hide year attribute

    def getYear(self):
        return self._year
class Ebook(Book):
    def __init__(self, title, author, year, fileSize,format):
        super().__init__(title, author, year)
        self.fileSize = fileSize
        self.format = format

    def displayInfo(self):
        print(f"Title: {self.title}", f"BY: {self.author}", f"Year: {self._year}", f"File Size: {self.fileSize}MB",f"Format: {self.format}")

book1 = Book("Percy Jackson","Rick Riordan", 1925)
book2 = Book("Harry Potter", "J.K. Rowling", 1997)
book3 = Book("The Hobbit", "J.R.R. Tolkien", 1937)
ebook = Ebook("Harry Potter", "J.K. Rowling", 1997, 5, "EPUB")

print(book1.title)
print(book2.author)
print(book3._year)
print(ebook.displayInfo())


# QUESTION TWO

class Animal:
    def __init__(self,name,color,speak):
        self.name = name
        self.color = color
    def speak(self):
        print("Animal sound")    
class cat(Animal):
    def speak(self):
        return ("meow")        
class dog(Animal):
    def speak(self):
        return ("bark")
class sheep(Animal):
    def speak(self):
        return ("baa")   
class hen(Animal):
    def speak(self):
        return ("cluck")     
                
cat1 = cat("cat","black","meow")
dog1 = dog("dog","brown","bark")
sheep1 = sheep("sheep","white","baa")
hen1 = hen("hen","yellow","cluck")
print(cat1.speak())
print(dog1.speak())
print(sheep1.speak())
print(hen1.speak())
print(cat1.color)
print(dog1.name)
print(sheep1.color)
print(hen1.name)