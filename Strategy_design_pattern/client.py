from factory import Factory


if __name__ == '__main__':
    Factory = Factory()
    method = Factory.select_method(input('select method to solve problem: '))
    method.rain_water_tapping()
    method = Factory.select_method(input('select method to solve problem: '))
    method.rain_water_tapping()
    method = Factory.select_method(input('select method to solve problem: '))
    method.rain_water_tapping()