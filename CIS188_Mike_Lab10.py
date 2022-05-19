#CIS188_Mike_Lab10.py
import csv
import passGenerator as pg
''' Your company has set up a new IT system and needs to set random initial passwords for each employee.   '''
count = 0
# You have been provided a CSV file, called employee.csv, with a list of all employees in the company. 
exampleFile = open('.\employees.csv')
employee_data = list(csv.DictReader(exampleFile))
outputfile = open('CIS188_Mike_Lab10_Output.csv', 'w', newline="")
outputDictWriter = csv.DictWriter(outputfile,['fname','lname','email','password'])
outputDictWriter.writeheader()
for row in employee_data:
# Call Random Pw gen and create new list with those objects
    password = pg.gen_pass(16)
    # You need to create a new CSV file which contains the first name, last name, email and a new randomly generated password.  
    outputDictWriter.writerow({'fname':row['fname'],'lname':row['lname'], 'email':row['email'], 'password':password })
    count += 1



