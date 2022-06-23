# creates function with two parameters
# the function calculates bmi based on a person's weight and height
# the function returns None if weight and/or height are not in a plausible range
def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None
    return weight / height ** 2 
