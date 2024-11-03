class Robot():
    
    def __init__(self, name):
        self.name = name
        
    def set_name(self, name):
        if name == "Hugo":
            self.name == "Marvin"
        else:
            self.name = name
        

x = Robot("Marvin")
y = Robot("Hugo")
print(x.name, y.name)