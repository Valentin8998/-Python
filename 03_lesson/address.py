class Address:
    def __init__(self, index, city, street, home, kw):
        self.index = index
        self.city = city
        self.street = street
        self.home = home
        self.kw = kw

    def __str__(self):
        return (
            f"{self.index}, {self.city},"
            f"{self.street}, {self.home} - {self.kw}"
            )
