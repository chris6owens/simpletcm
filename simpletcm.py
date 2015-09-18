#!/usr/bin/python
# I don't care because I'm on Windows, but leaving this here to remind me when I move to linux

import sys, re

def addcase(sn,title,project,notes):
  fh_cases_a=open("cases.txt","at")
  fh_cases_a.write("<case>\n")
  fh_cases_a.write("<sn=\""+sn+"\">\n")
  fh_cases_a.write("<title=\""+title+"\">\n")
  fh_cases_a.write("<project=\""+project+"\">\n")
  fh_cases_a.write("<notes>"+notes+"</notes>\n")
  fh_cases_a.write("<\case>\n\n")
  fh_cases_a.close()  
  print ("Added test case "+sn+"\n")
  return "OK"

def searchcases(searchstring):
  result_list=[]
  print("Searching for "+searchstring)
  fh_cases_r=open("cases.txt","rt")
  for line in fh_cases_r:
    result=re.match("<sn=\"(\d+)\"\>",line) # Look for the sn lines for each test cases
    if result:
      current_case_sn=int(result.group(1)) # Keep track of the current sn as we look through the file
      # print("Currently searching case "+str(current_case_sn))
    result=re.search(searchstring,line) # Look for the searchstring in each line from the case file
    if result:
      result_list.append(current_case_sn)
      # print("Current list of results: "+str(result_list))
  fh_cases_r.close()  
  print ("Finished searching\n")
  return result_list

def dbck():
  global highest_case_sn
  print ("Checking databases")
  fh_cases_r=open("cases.txt","rt")
  for line in fh_cases_r:
    result=re.match("<sn=\"(\d+)\"\>",line) # Look for the sn lines for each test cases
    if result:
      if (int(result.group(1))>highest_case_sn): # If it finds an sn value higher than the current one, use the higher
        highest_case_sn=int(result.group(1))
  fh_cases_r.close()

print ("Command: "+sys.argv[1])
highest_case_sn=0 # Looking through the test case database to find the highest SN currently in use
dbck() # Run the database check, including getting the top indices for all tables
highest_case_sn=highest_case_sn+1 # Then increment the indices for any new cases added this session.  
# If anyone other than me ever edits this code they can change this to the more python-standard variable += 1

if (str(sys.argv[1])=="addcase"):
  if (len(sys.argv) == 5): # command and three actual parameters plus the program name
    result=addcase(str(highest_case_sn),sys.argv[2],sys.argv[3],sys.argv[4])
    print("Result: "+result)
  else:
    print ("Usage: simpletcm addcase title projectname notes")

if (str(sys.argv[1])=="searchcases"):
  if (len(sys.argv) == 3): # command and one actual parameter plus the program name
    searchresults=searchcases(sys.argv[2])
    print(searchresults)
  else:
    print ("Usage: simpletcm searchcases searchstring")


# check for command line parameters
# tcm addcase
# tcm getcase
# tcm searchcases
# tcm deletecase
# tcm regex_edit (for changing just one field in a testcase etc)
# tcm generate_testplan(type)
# tcm delete_testplan
# tcm add_run
# tcm add_run_result
# tcm display_run
# tcm delete_run
# tcm add_project
# tcm delete_project

# Case properties: 
#   last updated (timestamp) for marking results obsolete
#   Last pass result
#   Last fail result
#   Temporarily invalid flag
#   Case inactive/archive flag
#   Title
#   Prerequisites/notes/links
#   Steps
#   Project associated with

# Plan properties:
#   List of cases
#   Title
#   Project associated with
#   Notes
#   Plan inactive/archive flag

# Run properties:
#   Title
#   Notes
#   Plan
#   Timestamp
#   numpass & numfail
#   Run inactive/archive flag

# Project properties
#   Title
#   Description/Notes
#   Project inactive/archive flag
