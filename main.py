def math_formula_option():
    print('\nMaths formula option:')
    print('a. diameter of a circle')
    print('b. circumference of a circle')
    print('c. volume of a cube')
    print('d. hypotenuse of a right angled triangle')
    print('e. area of a trapezoid')

math_formula_option()

options = input('pick an option from a to f  ')
print(options)

if options == 'a':
    radius = int(input('Enter radius of circle  '))
    diameter = radius * 2
    print(diameter)

elif options == 'b':
    radius = int(input('Enter radius of circle  '))
    circumference = 2 * 22/7 * radius
    print(circumference)

elif options == 'c':
    side = int(input('Enter length of the side  '))
    volume_of_a_cube = side ** 3
    print(volume_of_a_cube)

elif options == 'd':
    opposite = int(input('enter value for opposite  '))
    adjacent = int(input('enter value for adjacent  '))
    hypotenuse = (opposite ** 2) + (adjacent ** 2)
    print(hypotenuse)

elif options == 'e':
    b1 = int(input('enter b1  '))
    b2 = int(input('enter b2  '))
    height = int(input('enter height  '))
    area_of_trapezoid = 0.5 * height * (b1 + b2)
    print(area_of_trapezoid)

else :
    print('Type an option from a to f')