
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        return f"Hi, my name is {self.name}, I am {self.age} years old and I am a {self.gender}."


class Member(Person):
    def __init__(self, name, age, gender, membership):
        Person.__init__(self, name, age, gender)
        self.membership = membership

    def introduce(self):
        return f"{super().introduce()} My membership number: {self.membership}."



class Author(Person):
    def __init__(self, name, age, gender, books_written):
        Person.__init__(self, name, age, gender)
        self.books_written = books_written

    def list_books(self):
        return f"Books written: {self.books_written}"



class AuthorMember(Member, Author):
    def __init__(self, name, age, gender, membership, books_written):
        Person.__init__(self, name, age, gender)
        Member.__init__(self, name, age, gender, membership)
        Author.__init__(self, name, age, gender, books_written)

    def introduce(self):
        return f"{super().introduce()} {self.list_books()}"



library_members = [
    AuthorMember("May", 24, "Female", "1083", ["I need coffee", "Where is my will to live"]),
    AuthorMember("Mariia", 29, "Female", "3976", ["How to play sims", "I cant see, where are my glasses"]),
    AuthorMember("Zosia", 19, "Female", "8378", ["All I want is sleep", "Coocking 101"]),
]


for member in library_members:
    print(member.introduce())