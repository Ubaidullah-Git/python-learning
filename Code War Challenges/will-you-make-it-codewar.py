def zero_fuel(distance_to_pump, mpg, fuel_left):
    return True if distance_to_pump <= mpg * fuel_left else False

distance_to_pump = 100
mpg = 40
fuel_left = 2.57
print(zero_fuel(distance_to_pump,mpg,fuel_left))
