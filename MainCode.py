Project_list = ["Project Allocation System",
               "Data Encryption",
               "Image Encryption",
               "Next Generation Databases",
               "Random Password Generator",
               "HTTP Server using Multithreading in Java"]

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0

print("Do you want to select a project : "
      "If Yes Press 1"
      "If NO Press 0")
n = int(input("Enter your decision : "))

print("Press 1 for choosing " + Project_list[0])
print("Press 2 for choosing " + Project_list[1])
print("Press 3 for choosing " + Project_list[2])
print("Press 4 for choosing " + Project_list[3])
print("Press 5 for choosing " + Project_list[4])
print("Press 6 for choosing " + Project_list[5])


while n==1:

    Result = int(input("Enter your choice : "))

    if(Result == 1):
        if(count1 < 3):
           count1 = count1 + 1
           print("Your Project is : ", Project_list[0])
        else:
            print("Project Already taken")

    if(Result == 2):
        if(count2 <3):
            count2 = count2 + 1
            print("Your Project is : ", Project_list[1])
        else:
            print("Project Already taken")

    if(Result == 3):
        if (count3 < 3):
            count3 = count3 + 1
            print("Your Project is : ",Project_list[2])
        else:
            print("Project Already taken")

    if(Result == 4):
        if (count4 < 3):
            count4 = count4 + 1
            print("Your Project is : ",Project_list[3])
        else:
            print("Project Already taken")

    if(Result == 5):
        if (count5 < 3):
            count5 = count5 + 1
            print("Your Project is : ",Project_list[4])
        else:
            print("Project Already taken")

    if(Result == 6):
        if (count6 < 3):
            count6 = count6 + 1
            print("Your Project is : ",Project_list[5])
        else:
            print("Project Already taken")

    print("Do you want to continue? "
          "If YES Press 1 ")
    n = int(input())
