class User:
    def __init__(self, first_name, last_name):
        self.first = first_name
        self.last = last_name

    def first_name(self):
        return self.first

    def last_name(self):
        return self.last

    def first_last_name(self):
        return f"Имя: {self.first}, Фамилия: {self.last}"
