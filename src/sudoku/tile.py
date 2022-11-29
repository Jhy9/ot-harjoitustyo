
class Tile:

    value = 0
    lock = False

    def __init__(self, value):
        val = int(value)
        if val > 0:
            self.value = val
            self.lock = True

    def change_value(self, new_value):
        if self.lock is False:
            self.value = new_value

    def __str__(self):
        return str(self.value)
