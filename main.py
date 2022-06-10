import pytest


def more_than_five(somelist):
    list_2 = []
    for i in somelist:
        if abs(i) > 5:
            list_2.append(i)
    return list_2


# print(more_than_five([1, 28, -90, -3, 20, 456]))


def test_a():
    assert more_than_five([1, 28, -90, -3, 20, 456]) == [28, -90, 20, 456]

# _______________________________________________________


# ____________________________________________
import unittest


def list_range(a, b, c):
    list_1 = []
    for i in range(a, b, c):
        list_1.append(i)
    list_1.reverse()
    return list_1


class Testlist(unittest.TestCase):

    def test_equal(self):
        self.assertEqual(list_range(2, 20, 4), [18, 14, 10, 6, 2])


if __name__ == '__main__':
    unittest.main()
# _____________________________________



import unittest


def month_to_season(month_number):
    season = {1: 'Winter', 2: 'Winter', 3: 'Spring',
              4: 'Spring', 5: 'Spring', 6: 'Summer',
              7: 'Summer', 8: 'Summer', 9: 'Autumn',
              10: 'Autumn', 11: 'Autumn', 12: 'Winter'}
    if month_number in season:
        return season[month_number]
    else:
        print("It's only 12 month in a year")


# month_to_season(2)


class Testlist(unittest.TestCase):

    def test_equal2(self):
        self.assertEqual(month_to_season(2), "Winter")


if __name__ == '__main__':
    unittest.main()
