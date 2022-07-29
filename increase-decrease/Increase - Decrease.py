#code to solve the puzzle :
#Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - 
#the directions he got are a little confusing. He starts on the ground floor (floor 0) and then follows the instructions one character at a time.
#An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.
#https://adventofcode.com/2015/day/1

def increase_decrease(s):
    """
    :type s: str
    :rtype: int
    """
    int_val = 0
    for i in range(len(s)):
        if i > 0 and s[i] == ')':
            int_val -= 1
        elif i > 0 and s[i] == '(':
            int_val += 1
        else:
            int_val += 1
    return int_val

input_str = input("Enter a string: ")
print(f"The floor santa ends on is: {increase_decrease(input_str)}")