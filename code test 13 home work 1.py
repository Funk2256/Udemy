class Name():
    def __init__(self, first_name, last_name):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.full_name = first_name.title() + " " + last_name.title()
        self.initials = first_name.title()[0] + "." + last_name.title()[0]




a1 = Name('JohN', 'SMITH')

print(a1.initials)