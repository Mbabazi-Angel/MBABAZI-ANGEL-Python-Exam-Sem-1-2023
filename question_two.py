#i)
class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return(f'{self.title},{self.author}{self.pages}') 
Book1 = Book('title',  'author',  'pages')#create an instance
print(Book1)

#ii)
class EBook:
    def __init__(self,title,author,pages,format):
        self.title = title
        self.author = author
        self.pages = pages
        self.format = format
    def __str__(self):
        return(f'{self.title},{self.author}, {self.pages}, {self.format}') 
EBook1 = EBook('title',  'author', 'pages', 'format')
print(EBook1)

#iii)
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def __str__(self):
        return(f'{self.title}, {self.author}')  
Book2 = Book('title', 'author')
print(Book2)      
        