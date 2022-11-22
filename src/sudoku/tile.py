
class Tile:

    value = 0
    lock = False

    def __init__(self, value):

        val = int(value)
        if val > 0:
            self.value = val
            self.lock = True
        

    def changeValue(self, newValue):
        if self.lock == False:
            self.value = newValue

    def __str__(self):
        return str(self.value)