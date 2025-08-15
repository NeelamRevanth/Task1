#. So, Python sees that there is 16 stored in the numberOne variable and 4 stored in the numberTwo variable. It adds these up and stores the result in the answer variable.  
#You can also mix the two, variables and hard-code numbers:  
#answer = numberOne + numberTwo + 20  
#answer = 10 * numberOne + (numberTwo + 20)  
#answer = numberOne + 20 + numberTwo – 10


# 9. Using variables and hardcoded numbers
numberOne = 16
numberTwo = 4
answer = numberOne + numberTwo
print("Sum of variables:", answer)
answer = numberOne + numberTwo + 20
print("Variables + 20:", answer)
answer = 10 * numberOne + (numberTwo + 20)
print("Mixed precedence:", answer)
answer = numberOne + 20 + numberTwo - 10
print("Final expression:", answer)
