#i)
def calculate_area(r):
    area = 3.14*r
    print(f'The area of the circle is {area}')
calculate_area(5)

#ii)
def sum_of_natural_numbers(n):
    sum = 1+2+3+n
    print(f'The sum of natural numbers up to n is {sum}')
sum_of_natural_numbers(4)  

#iii)
numbers = [1,3,5,7,9]

print(numbers)

numbers.append(10)
print(numbers)

#iv)
numbers = [1,3,5,7,9]
new_list = []
for items in numbers:
    if items :
        new_list.append(items)
        new_list.sort()
        print(items)

#v)
student_info = {
    'name': 'Alice',
    'age': 20,
    'grade': 'A',
    'city' : 'New York'
}
print(student_info)
student_info = {
    'age' : '25'
}
updated_age = (student_info['age'])
print(updated_age)

#vi)

