# using property class
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    # getter
    def get_temperature(self):
        print("Getting value...")
        return self._temperature

    # setter
    def set_temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value

    # deleter
    def del_temperature(self):
        print("Deleting value...")
        del self._temperature

    # creating a property object
    temperature = property()
    temperature = temperature.getter(get_temperature)
    temperature = temperature.setter(set_temperature)
    temperature = temperature.deleter(del_temperature)

human = Celsius(37)
print(human.temperature)
print(human.to_fahrenheit())
human.temperature = -300
del human.temperature