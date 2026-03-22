# inet_4031_adduser_script
Python script for automating adding users in Linux


# Program Description
This program is created to automate the task of adding users onto a linux operating system. It has the ability to create the users and assign them into groups. Just how a user can use the adduser commands the program uses it as well. By going through a list in a file it is able to use the adduser command to quickly create lots of users.

# Program Operation
In order for the program to work it must take an input from a file, with a specfic format explained below. The program should be run as sudo in order to make sure it has the correct permissions. Here is a command for running the file sudo ./create-users.py < create-users.input with create-users-input being the file that has the users for the create-users.py to create.

## Input file format
The format of the file is that by lines, where each user is one line, with each field seperated with :. An example line is user04:pass04:Last04:First04:group01. Where user04 is the username, pass04 is the password, Last04 and First04 is the last and first name, group01 is the group the user should join. If a user needs to be in muiltple groups they should be sperated by comma no space ex:group01,group02. In order to skip a line add # in front of the line no space. For a user with no groups add a - where the group field is. Each line must by five fields or else the line will get skipped.

## Command Excution
A user can run the code by running the sudo ./create-users.py < create-users.input command. Make sure to run the code with sudo level permissions and make sure that create-users.py is executable. 

## Dry Run
A user can dry run the program in order to make sure the code is correct without having the code be implemented. So the users will not be created. The code will instead print out messages that are useful for troubleshooting and ensuring the user understands the steps the program is taking.
