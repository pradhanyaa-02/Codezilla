# Codezilla
Contains tasks, projects and learning excercises completed for a technical club, showcasing practical skills, team work and hands-on experience in coding

## Explanation to Tasks
### Task 2: Sum of Digits
This solution is used to find the sum of digits of a number by repeatedly extracting and adding each digit. The sum_of_digits() function takes an integer num and initializes total to 0. Inside a while loop, it uses num % 10 to get the last digit and adds it to total. Then, it removes the last digit by doing integer division num // 10. This process continues until all digits are processed. The final result is the sum of all digits in the number. This method is efficient and works for any non-negative integer input.

### Task 2: Leap Year Checker
This solution is used to check if a given year is a leap year by applying the rules of the Gregorian calendar. A year is a leap year if it is divisible by 400, or if it is divisible by 4 **and not** divisible by 100. The function `leap_year_checker()` uses logical conditions to evaluate these rules. If the condition is true, it prints that the year is a leap year; otherwise, it states it is not. This method ensures correct results for all years, including exceptions like 1900 (not a leap year) and 2000 (leap year). It's a simple and effective solution.

### Task 2: Word Reverse
This solution is used to reverse a given word by iterating through it from the last character to the first. The function `reverse_word()` uses a `for` loop with the range `len(word)-1` to `0`, stepping backward. Each character is added to a new string `reversed_word`, building the reversed version. Finally, it returns the reversed string. This approach manually constructs the reversed word without using built-in reverse functions, helping understand string indexing and loops. However, the code has an error: `reversed_word` is used before being defined. It should be initialized as an empty string before the loop to work correctly.
