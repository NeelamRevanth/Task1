#Create a string made of the first, middle and last character? 
#Expected Output: Live Tech

# 2. String made of first, middle, and last character
text = "Live Tech"
first_char = text[0]
middle_char = text[len(text)//2]
last_char = text[-1]
result = first_char + middle_char + last_char
print("First, middle, last characters:", result)
