class Cat:
    def __init__(self, name='', gender='', age=0):
        self.name = name
        self.gender = gender
        self.age = age

    def init_from_dict(self, cats_dict):
        self.name = cats_dict.get("name")
        self.gender = cats_dict.get("gender")
        self.age = cats_dict.get("age")
        
