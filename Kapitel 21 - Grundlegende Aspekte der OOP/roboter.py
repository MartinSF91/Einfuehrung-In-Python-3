class Roboter:

    def __init__(self, name, baujahr):
        self.set_name(name)
        self.baujahr = baujahr

    def sage_hallo(self):
        print(f"Name: {self.get_name()}, Baujahr: {self.baujahr}")

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if name == "Egon":
            self.__name = "Marvin"
        else:
            self.__name = name


if __name__ == "__main__":
    x = Roboter("Egon", 2000)
    x.sage_hallo()
