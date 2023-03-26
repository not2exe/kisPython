class MealyError(Exception):
    pass


class Shit:
    def __init__(self):
        self.state = 'A'

    def slog(self):
        match self.state:
            case 'A':
                self.state = 'B'
                return 0
            case 'C':
                self.state = 'A'
                return 4
            case 'G':
                self.state = 'B'
                return 9
            case _:
                raise MealyError("slog")

    def tread(self):
        match self.state:
            case 'B':
                self.state = 'C'
                return 1
            case 'C':
                self.state = 'C'
                return 3
            case 'E':
                self.state = 'F'
                return 6
            case 'G':
                self.state = 'H'
                return 8
            case 'H':
                self.state = 'A'
                return 11
            case _:
                raise MealyError("tread")

    def look(self):
        match self.state:
            case 'C':
                self.state = 'D'
                return 2
            case 'D':
                self.state = 'E'
                return 5
            case 'F':
                self.state = 'G'
                return 7
            case 'H':
                self.state = 'B'
                return 10
            case _:
                raise MealyError("look")


def try_tread(obj, val):
    try:
        assert (obj.tread() == val)
    except MealyError:
        pass


def try_look(obj, val):
    try:
        assert (obj.look() == val)
    except MealyError:
        pass


def try_slog(obj, val):
    try:
        assert (obj.slog() == val)
    except MealyError:
        pass


def try_methods(obj, state, tread_val=None, look_val=None, slog_val=None):
    obj.state = state
    try_tread(obj, tread_val)
    try_look(obj, look_val)
    try_slog(obj, slog_val)


def test():
    obj = main()
    try_methods(obj, 'A', slog_val=0)
    try_methods(obj, 'B', tread_val=1)
    try_methods(obj, 'C', 3, 2, 4)
    try_methods(obj, 'D', look_val=5)
    try_methods(obj, 'E', tread_val=6)
    try_methods(obj, 'F', look_val=7)
    try_methods(obj, 'G', slog_val=9, tread_val=8)
    try_methods(obj, 'H', tread_val=11, look_val=10)


def main():
    return Shit()
