class Robot:

    def __init__(self, name):
        self.set_name(name)

    def set_name(self, name):
        if name == "Hugo":
            print("Name 'Hugo' unzulässig!")
            self.name = "Marvin"
        else:
            self.name = name


x = Robot("Marvin")
y = Robot("Hugo")
print(x.name, y.name)
