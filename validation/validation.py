data_valid = False

while data_valid == False:
  grade1 = input("Type your first grade:")
  try:
    grade1 = float(grade1)
  except:
     print ("Invalid input. Only numbers are allowed. Decimals should be separated by a dot. ")
     continue
  if (grade1 < 0 or grade1 >10):
    print("Grade should be between 1 and 10.")
    continue 
  else:
      data_valid = True
      
data_valid = False  

while data_valid == False:
  grade2 = input("Enter your second grade:")
  try:
    grade2 = float(grade2)
  except:
      print("Invalid input. Only numbers are allowed. Decimals should be separated by a dot. ")
      continue
  if (grade2 < 0 or grade2 >10):
    print("Grade should be between 1 and 10.")
    continue 
    
  else:
      data_valid = True
data_valid = False
 
while data_valid == False:
  total_classes=input("Type total number of classes:")
  try:
    total_classes= int(total_classes)
  except:
      print("Invalid input. Only numbers are allowed. ")
      continue
      
  if (total_classes <=0):
    print("Classes can't be less or equal to zero")
    continue 
    
  else:
   data_valid = True    
   
data_valid = False
   
while data_valid == False:
   absence =input("Type total number of absence:")
   try:
    absence = int(absence)
   except:
      print("Invalid input. Only numbers are allowed. ")
      continue
      
   if(absence < 0 or absence > total_classes):
     print("Absence can't be less than zero or greater than the total classes. ")
     continue 
     
   else:
    data_valid = True

avg_grade =(grade1 + grade2)/2
attendance =(total_classes-absence)/total_classes 

print("Average grade :", round (avg_grade, 2))
print ("Attendance rate:", str(round (attendance *100))+"%")

if avg_grade >=6:
  if attendance >=0.8:
    print("You have passed")
  else:
    print("Student has failed due to attendance less than 80%")
     
elif attendance >=0.8:
   print ("Student has failed due to average grade of less than 6.0")
else:
   print ("The student has failed due to average grade and attendance rate of less than 6.0 and 80% respectively ")
       
    
    




