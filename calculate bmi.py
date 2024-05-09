def calculate_bmi(weight, height):
    """
    Returns the body mass index and its category
    """
    # Calculate BMI
    bmi = weight / height ** 2
    bmi = round(bmi, 1)

    # Determine BMI category
    if bmi <= 18.5:
        result = 'underweight'
    elif 18.5 < bmi <= 25:
        result = 'normal weight'
    elif 25 < bmi <= 29.9:
        result = 'overweight'
    else:
        result = 'obesity'

    return bmi, result

if __name__ == '__main__':
    weight = float(input('Enter your weight in kilograms: '))
    height = float(input('Enter your height in meters: '))

    # Call function to calculate BMI
    bmi, category = calculate_bmi(weight, height)

    # Print BMI and its category
    print('Your BMI is {bmi}, which indicates {category}.')
