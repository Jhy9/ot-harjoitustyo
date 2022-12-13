
class Tile:
    valid_values=[str(0), str(1), str(2), str(3), str(4), str(5), str(6), str(7), str(8), str(9)]
    value = 0
    lock = False

    def __init__(self, value, lock = None):
        if str(value) in self.valid_values:
            val = int(value)
            if val > 0:
                self.value = val
                self.lock = True
        else:
            self.value = 0
        if lock is not None:
            if lock == 0:
                self.lock = False

    def change_value(self, new_value):
        if self.lock is False:
            if str(new_value) in self.valid_values:
                self.value = new_value

    def __str__(self):
        return str(self.value)
