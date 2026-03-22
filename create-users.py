#!/usr/bin/python3

# INET4031
# Duncan Gillespie
# March,20,2026
# March,21,2026

#import os: imports a python library containing functions that allow python to ineract with the operating system.
#import re: imports a python library containing functions that allow for enhanced functions with strings.
#import sys: imports a python library containing functions that allow for python system specfic parameters.
import os
import re
import sys


def main():
    for line in sys.stdin:

        #Match is searching for the # character, # is being used to tell the program when a line should be skipped. The skipping is done in the if statement below
        match = re.match("^#",line)

        #This function gets rid of whitespace and splits the line into fields to be assigned to users
        fields = line.strip().split(':')

        #This code checks if match is true and skips the line in the file, it checks if the line is 5 fields, any more or less and it is skipped.
        #The line needs to be 5 fields as that is what a user needs
        if match or len(fields) != 5:
            continue

        # fields 0 and 1 are for setting username and passwords of users, gecos is setting the first and last name of the user.
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        # We are splitting this line in case a user needs to be assgined to more than one group.
        groups = fields[4].split(',')

        #This line is a troubleshooting measure and gives the user information as to the status of the program.
        print("==> Creating account for %s..." % (username))

        #This line is adding the command to add a user, with the groups and username of the user, does not assgin a password.
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        #The first time the code is ran the print statement should be uncommented to ensure cmd is correct, 
        #the os.system(cmd) will attempt to create a user if uncommented
        #print(cmd)
        os.system(cmd)

        #This code helps troubleshoot and gives the user an update on what the code is doing.
        print("==> Setting the password for %s..." % (username))

        #This line gets the program through the password checks when creating an account by printing the password twice.
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        #The first time the code is ran the print statement should be uncommented to ensure cmd is correct,
        #The os.system(cmd) will attempt to set the password for a user if uncommented
        #print(cmd)
        os.system(cmd)

        for group in groups:
            #The if statement is looking for the amount of groups to place a user in as it could be more than one
            #If the group is '-' than the program skips assigning it to a specfic group and assigns to it user group
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print(cmd)
                os.system(cmd)

if __name__ == '__main__':
    main()
