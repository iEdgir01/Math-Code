import copy

def print_all_sum_rec(target, current_sum, start, output, result):
 if current_sum == target:
   output.append(copy.copy(result))

 for i in range(start, target):
   temp_sum = current_sum + i
   if temp_sum <= target:
     result.append(i)
     print_all_sum_rec(target, temp_sum, i, output, result)
     result.pop()
   else:
     return

def print_all_sum(target):
 output = []
 result = []
 print_all_sum_rec(target, 0, 1, output, result)
 return output

def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
       return userInput 
       break 

n = inputNumber("Enter the value you would like to calculate the total sum of: ")
res = print_all_sum(n)

def get_nested_length(list):
     
    size = 0
     
    for item in list:
      
        if type(item) == list:  
            
            size += get_nested_length(item)
        else:
         size+=1
    return size
 
#calling the upper define method 
print("The total way to Sum for" ,(n))
print("is" ,get_nested_length(res))