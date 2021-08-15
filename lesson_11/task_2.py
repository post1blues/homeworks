class Mathematician:
    def square_nums(self, nums):
        return list(map(lambda x: x**2, nums))

    def remove_positives(self, nums):
        return list(filter(lambda x: x < 0, nums))

    def filter_leaps(self, years):
        return list(filter(self._is_leap_year, years))

    def _is_leap_year(self, year):
        if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
            return False
        else:
            return True


m = Mathematician()
print(m.square_nums([7, 11, 5, 4]))
print(m.remove_positives([26, -11, -8, 13, -90]))
print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))