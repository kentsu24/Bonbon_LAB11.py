grade = 1
passed = 0
list = []
student_num = 1
while grade != 0:
    grade = int(input(f"input the grade of the student {student_num} : "))
    if grade < 40 or grade > 100:
        print("invalid grade") 
        break
    else:
        list.append(grade)
        student_num +=1
        if grade >= 75:
           passed += 1
            
    add_grade = input("do you want to add grade? (continue/done) : ")

    if (add_grade.lower() == "continue"):
      continue
    elif (add_grade.lower() == "done"):
     sum_list = sum(list)
     average = (sum_list / len(list))
     average = round(average, 2)
    
     passing = (passed/len(list)*100)
     passing = round(passing, 2)
    
     print(f"Average grade: {average:.2f}")
     print(f"Students Passed: {passed}")
     print (f"Passing %: {passing:.2f}%")
    
     break
    else: 
     print("error: invalid qoute")
     break
    
     
         
    
    

    


      
 
    
