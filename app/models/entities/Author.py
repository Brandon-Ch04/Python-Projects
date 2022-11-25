class Author():
    
    def __init__(self,id,last_name,name,birth_date=None):
        self.id = id
        self.last_name = last_name
        self.name = name
        self.birth_date = birth_date
 
    def full_name(self):
        return f"{self.last_name}, {self.name}"
