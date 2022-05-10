def more_than_five(somelist):
    list_2 = []
    for i in somelist:
        if abs(i) > 5:
            list_2.append(i)
    return list_2


print(more_than_five([1, 28, -90, -3, 20, 456]))



def number_stop(somelist):
    for i in somelist:
        if i == 139:
            break
        if i % 2 != 0:
            print(i, end=" ")


list_1 = [1, 28, -90, 44, 60, 5, 9, 80, 139, -3, 20, 456]
number_stop(list_1)


def list_range(a, b, c):
    list_1 = []
    for i in range(a, b, c):
        list_1.append(i)
    list_1.reverse()
    return list_1


print(list_range(2, 20, 4))


def month_to_season(month_number):
    season = {1: 'Winter', 2: 'Winter', 3: 'Spring',
              4: 'Spring', 5: 'Spring', 6: 'Summer',
              7: 'Summer', 8: 'Summer', 9: 'Autumn',
              10: 'Autumn', 11: 'Autumn', 12: 'Winter'}
    if month_number in season:
        print(season[month_number])
    else:
        print("It's only 12 month in a year")

month_to_season(2)

