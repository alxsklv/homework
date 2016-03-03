import math
print ('Enter your variables\n')
a = float(input("enter coefficient 'a': "))
b = float(input("enter coefficient 'b': "))
c = float(input("enter coefficient 'c': "))

D = math.pow(b, 2) - (4 * a * c)
print('parameter a: {0}\n'
      'parameter b: {1}\n'
      'parameter c: {2}\n'
      'calculated discriminant {3}\n'
      .format (a, b, c, D))  # checking transitional results

if D > 0 and a != 0:  # second condition was added to avoid division on zero
    x1 = (-b - math.sqrt(D))/(2 * a)
    x2 = (-b + math.sqrt(D))/(2 * a)
    print('x1 = {0}\n'
          'x2 = {1}\n'
          .format(x1, x2))

elif D == 0 and a != 0:  # second condition was added to avoid division on zero
    x = - (b/(2*a))
    print('x = ', x)

else:
    print("Result: no solution")