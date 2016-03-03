import math

R = int(input('Enter the radius: '))  # enter the radius of your circle using keyboard

L = 2 * math.pi * R  # circle length calculation

S = math.pi * math.pow(R, 2)  # circle square calculation

print('The length of your circle is: {0} '
      '\nThe square of your circle is: {1}'
      .format(round(L, 2), round(S, 2)))  # rounding to 2 digits after coma and output