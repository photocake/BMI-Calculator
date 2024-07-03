import os

height = input('Please input your height(cm) to contiune...')
weight = input('Please input your weight(kg) to contiune...')
height = float(height) / 100
weight = float(weight)

bmi = weight / height ** 2
if bmi < 18.5:
        print('Your BMI is', bmi, '. You are underweight.')

elif bmi >= 18.5 and bmi < 24:
        print('Your BMI is', bmi, '. You are normal weight.')

elif bmi >= 24 and bmi < 27:
        print('Your BMI is', bmi, '. You are slightly overweight.')

elif bmi >= 27 and bmi < 30:
        print('Your BMI is', bmi, '. You are medium overweight.')

else:
        print('Your BMI is', bmi, '. You are heavily overweight.')

os.system("pause")