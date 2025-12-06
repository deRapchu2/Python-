students = [                                                            #list of dictionaries , dictionary for each student 
    {"name": "Taha" , "House" : "kanlibagh", "Glasses": "Yes"},         # 3 keys and therefore three definitions 
    {"name": "Mohtashim" , "House" : "Sopore", "Glasses": "No"},
    {"name": "Shaarif" , "House" : "Sopore", "Glasses": "Yes"},
    {"name": "Zaid" , "House" : "Sangri", "Glasses": "Yes"},
    {"name": "Momin" , "House" : "kanlibagh", "Glasses": None}
]

for student in students:
    print(student["name"], student["House"], student["Glasses"], sep = ", ") #for each student in the list of students give me his name , house and glasses condition 
    print(student)                                                            #here we see that each student here is a dictionary and above we print the value present in student dictionary 
                                                                              #at the index "name", and "House", "Glasses"

    for key in student:                                                       #each student is a dictionary 
        print(key)                                                            #keys present in each student dictionaty 
        print(student[key])                                                   # here we will print values present in each student dictionary