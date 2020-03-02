#Import necessary package.
import sys

#Author: Alex Damon
#Date: 02/07/20
#Project Name: Employee Database
#This Python project, made in Visual Studio, simulates an employee database.
#The variables include an employees' name, number, department, and job title.
#When the program is run, the user is prompted to enter this information.
#When there are no more employees to enter, the user can type "exit" to print the contents.

#Main function
def main():

    #Initialize variables
    employeeName = ''
    employeeNumber = ''
    employeeDept = ''
    employeeTitle = ''
    employeeNumCounter = 0
    addEmployee = True

    #Lists to store information.
    nameList = []
    numberList = []
    deptList = []
    titleList = []

    #Program title
    print('Employee Database\n-----------------\n')

    #Function call so our program will start.
    startProgram(nameList, numberList, deptList, titleList, employeeNumCounter, addEmployee)

#Function that holds all of our user input functions.
def startProgram(nameList, numberList, deptList, titleList, employeeNumCounter, addEmployee):
    #We do this so input processes will repeat as long as needed.
    while addEmployee is True:
        #Input functions
        employeeName = inputName(nameList, numberList, deptList, titleList, employeeNumCounter)
        employeeNumber = inputNumber(numberList)
        employeeDept = inputDept(deptList)
        employeeTitle = inputTitle(titleList)

#Function to input employee name.
def inputName(nameList, numberList, deptList, titleList, employeeNumCounter):
    employeeName = input('Please enter an employee name or type "exit": ')
    #If user types "exit"
    if employeeName == 'exit' or employeeName == '"exit"':
        del employeeName
        #delete the string.
        print()       
        printContents(nameList, numberList, deptList, titleList, employeeNumCounter)
        #End program
        sys.exit(0)
    else:
        #Otherwise add string to last position in the list.
        nameList.append(employeeName)

#Function to input employee number.
def inputNumber(numberList):
        while True:
            #Tests for condition.
            try:
                employeeNumber = int(input('Please enter an employee number: '))
                #Triggered if input is valid.
                break
            except ValueError:
                #let user know they have made a mistake.
                print('\nError: Only numeric characters accepted. E.g. 12345\n')
        #Otherwise add string to last position in the list.
        numberList.append(employeeNumber)

#Function to input employee department.       
def inputDept(deptList):
        #Continue with user prompts.
        employeeDept = input('Please enter an employee department: ')
        deptList.append(employeeDept)

#Function to input employee title.
def inputTitle(titleList):
        #Continue with user prompts.
        employeeTitle = input('Please enter an employee job title: ')
        titleList.append(employeeTitle)  
        print('\n')

#Function to print out employee information.
def printContents(nameList, numberList, deptList, titleList, employeeNumCounter):
    #Mapping out the list positions.
    for a1, b1, c1, d1 in zip(nameList, numberList, deptList, titleList):
        #Increase employee number after each iteration.
        employeeNumCounter += 1; 
        #Print out contents.
        print('Employee', employeeNumCounter, '\n----------')
        print('Name:', a1)
        print('Number:', b1)
        print('Dept:', c1)
        print('Title:', d1, '\n')
  
#Call to main.
main()
