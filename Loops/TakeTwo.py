#Write a for loop that iterates over the integers from 1 to 100 
#prints the result of multiplying each integer by 2.

for num in range(1, 101):
    print(num * 2)


# challenge store results in list, then print

print("This line is for a visual break in the output")

number_list = []

for num in range(1,101):
    number_list.append(num*2)

print(number_list)