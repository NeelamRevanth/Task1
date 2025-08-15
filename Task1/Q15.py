#. Create a program to with the given variables and provide the datatypes according to the given values.  
#FirstName = “Raja”; 
#LastName = “Shekhar”; 
#PhoneNumber = “9703971577”; 
#Email = “raj@peramsons.com”; 
#JavaMarks = 70 
#PythonMarks = 90 
#Database = 90 
#WebDevelopment = 90 
#TotalMarks = 340 
#Average = 85.00

# Given variables
FirstName = "Raja"                # str
LastName = "Shekhar"               # str
PhoneNumber = "9703971577"         # str (even though it looks like a number, phone numbers are stored as strings)
Email = "raj@peramsons.com"        # str
JavaMarks = 70                     # int
PythonMarks = 90                   # int
Database = 90                      # int
WebDevelopment = 90                # int
TotalMarks = 340                   # int
Average = 85.00                     # float

# Printing values with their data types
print("FirstName:", FirstName, "| Type:", type(FirstName))
print("LastName:", LastName, "| Type:", type(LastName))
print("PhoneNumber:", PhoneNumber, "| Type:", type(PhoneNumber))
print("Email:", Email, "| Type:", type(Email))
print("JavaMarks:", JavaMarks, "| Type:", type(JavaMarks))
print("PythonMarks:", PythonMarks, "| Type:", type(PythonMarks))
print("Database:", Database, "| Type:", type(Database))
print("WebDevelopment:", WebDevelopment, "| Type:", type(WebDevelopment))
print("TotalMarks:", TotalMarks, "| Type:", type(TotalMarks))
print("Average:", Average, "| Type:", type(Average))
