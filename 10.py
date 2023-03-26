class MealyError(Exception):
    pass


class Mealy:
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


def test():
    o = main()
    cases = {
        'A': {'slog': 0, 'tread': MealyError, 'look': MealyError},
        'B': {'slog': MealyError, 'tread': 1, 'look': MealyError},
        'C': {'slog': 4, 'tread': 3, 'look': 2},
        'D': {'slog': MealyError, 'tread': MealyError, 'look': 5},
        'E': {'slog': MealyError, 'tread': 6, 'look': MealyError},
        'F': {'slog': MealyError, 'tread': MealyError, 'look': 7},
        'G': {'slog': 9, 'tread': 8, 'look': MealyError},
        'H': {'slog': MealyError, 'tread': 11, 'look': 10}
    }
    for initial_state in cases:
        for method in cases[initial_state]:
            o.state = initial_state
            if type(cases[initial_state][method]) is int:
                assert getattr(o, method)() == cases[initial_state][method]
            else:
                try:
                    getattr(o, method)()
                except MealyError:
                    pass


def main():
    return Mealy()


test()
