Name = input('Name: ')  # define user name
Surname = input('Surname: ')  # define user surname

print('{0} {1}'.format(Name, Surname))  # formatting with "one space" and print out
print('{1}, {0}'.format(Name, Surname))  # formatting with "coma + inverted" and print out
print('{0}  {1}'.format(Name, Surname))  # formatting with "tabulation" and print out