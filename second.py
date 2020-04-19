#!/usr/bin/env python3

import os
import sys
import datetime
from datetime import date;

## Take input from user
## 2 inputs - their birth date
## Enter month, day and year
## Answer is <day of the week> 


def get_input_from_user():
 month = input("Enter month number ");
 day = input("Enter day number ");
 year = input ("Enter year number ");
 return int(month), int(day), int(year);



def main():
 m,d,y = get_input_from_user();
 print("From user, I got {}/{}/{}".format(m,d,y));
 daynumber =  date(y,m,d).weekday()
 #print(daynumber);

 if daynumber == 0:
  print ("Monday");
 if daynumber == 1:
  print ("Tuesday");
 if daynumber == 2:
  print ("Wednesday");
 if daynumber == 3:
  print ("Thursday");
 if daynumber == 4:
  print ("Friday");
 if daynumber == 5:
  print ("Saturday");
 if daynumber == 6:
  print ("Sunday");
 
  
 
main();
