# Hooriya Amjad, ENDG 233 Block 3

value_one = int(input('Enter first integer value: '))           # read first integer value input
operator_one = input('Enter first operator: ')                  # read first operator input
value_two = int(input('Enter second integer value: '))          # read second integer value input
operator_two = input('Enter second operator: ')                 # read second operator input
value_three = int(input('Enter third integer value: '))         # read third integer value input

# block one code, operator one addition input
if operator_one == '+':
    if operator_two == '+':                                     # operator one add, operator two add 
        final_ans = (value_one + value_two + value_three)       # calculate final answer 
    elif operator_two == '-':                                   # operator one add, operator two subtract
        final_ans = (value_one + value_two - value_three)       # calculate final answer
    elif operator_two == '*':                                   # operator one add, operator two multiply
        final_ans = (value_one + (value_two * value_three))     # calculate final answer
    elif operator_two == '/':                                   # operator one add, operator two divide 
        final_ans = (value_one + (value_two // value_three))    # calculate final answer

# block two code, operator one subtract
elif operator_one == '-':
    if operator_two == '+':                                     # operator one subtract, operator two add 
        final_ans = (value_one - value_two + value_three)       # calculate final answer
    elif operator_two == '-':                                   # operator one subtract, operator two subtract
        final_ans = (value_one - value_two - value_three)       # calculate final answer
    elif operator_two == '*':                                   # operator one subtract, operator two multiply
        final_ans = (value_one - (value_two * value_three))     # calculate final answer
    elif operator_two == '/':                                   # operator one subtract, operator two divide
        final_ans = (value_one - (value_two // value_three))    # calculate final answer

# block three code, operator one multiply
elif operator_one == '*':
    if operator_two == '+':                                     # operator one multiply, operator two add 
        final_ans = ((value_one * value_two) + value_three)     # calculate final answer
    elif operator_two == '-':                                   # operator one multiply, operator two subtract
        final_ans = ((value_one * value_two) - value_three)     # calculate final answer
    elif operator_two == '*':                                   # operator one multiply, operator two multiply
        final_ans = (value_one * value_two * value_three)       # calculate final answer
    elif operator_two == '/':                                   # operator one multiply, operator two divide
        final_ans = (value_one * value_two // value_three)      # calculate final answer

# block four code, operator one divide
elif operator_one == '/':
    if operator_two == '+':                                     # operator one divide, operator two add 
        final_ans = ((value_one // value_two) + value_three)    # calculate final answer
    elif operator_two == '-':                                   # operator one divide, operator two subtract
        final_ans = ((value_one // value_two) - value_three)    # calculate final answer
    elif operator_two == '*':                                   # operator one divide, operator two multiply
        final_ans = (value_one // value_two * value_three)      # calculate final answer
    elif operator_two == '/':                                   # operator one divide, operator two divide
        final_ans = (value_one // value_two // value_three)     # calculate final answer
        
# print entered expression and final answer
print('Entered expression:', value_one, operator_one, value_two, operator_two, value_three)
print('Your final answer:', final_ans, '\n')
