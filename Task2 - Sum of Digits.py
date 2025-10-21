def sum_of_digits(num):
     total = 0
     while(num > 0):
         digit = num % 10
         total = total + digit
         num = num // 10
     return total

N = int(input("Enter a number:"))
sum = sum_of_digits(N)
print("The total sum of digits is: ", sum)











    








