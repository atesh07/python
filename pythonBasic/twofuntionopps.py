class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def showDetails(self):
        print(f"Title : {self.title}")
        print(f"Author : {self.author}")

book1=Book("Python","ehtesham")
book1.showDetails()
        