class Person:
    def __init__(self, name, age, gender):
        # Initialize the attributes of the person: name, age, and gender
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        # Print a message introducing the person with their name, age, and gender
        print(f"Hello, my name is {self.name}. I am {self.age} years old and {self.gender}.")

# CreatING an instance of the Person class
person1 = Person("Magnus", 30, "male")

# Call the introduce method to display the person's information
person1.introduce()
