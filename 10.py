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


def try_tread(obj, state, val=None):
    obj.state = state
    try:
        assert (obj.tread() == val)
    except MealyError:
        pass


def try_look(obj, state, val=None):
    obj.state = state
    try:
        assert (obj.look() == val)
    except MealyError:
        pass


def try_slog(obj, state, val=None):
    obj.state = state
    try:
        assert (obj.slog() == val)
    except MealyError:
        pass


def test():
    obj = main()
    try_tread(obj, 'A')
    try_look(obj, 'A')
    try_slog(obj, 'A', 0)
    try_look(obj, 'B')
    try_slog(obj, 'B')
    try_tread(obj, 'B', 1)
    try_look(obj, 'C', 2)
    try_slog(obj, 'C', 4)
    try_tread(obj, 'C', 3)
    try_look(obj, 'D', 5)
    try_slog(obj, 'D')
    try_tread(obj, 'D')
    try_look(obj, 'E')
    try_slog(obj, 'E')
    try_tread(obj, 'E', 6)
    try_look(obj, 'F', 7)
    try_slog(obj, 'F')
    try_tread(obj, 'F')
    try_look(obj, 'G')
    try_slog(obj, 'G', 9)
    try_tread(obj, 'G', 8)
    try_look(obj, 'H', 10)
    try_slog(obj, 'H')
    try_tread(obj, 'H', 11)


def main():
    return Shit()
