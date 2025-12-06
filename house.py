Name = input("Enter your name: ")

if Name == "Harry":
    print("Griffindor")
elif Name == "Hermoine":
    print("Griffindor")
elif Name == "Ron":
    print("Griinfffotodot")
else:
    print("Not griffeindotrian") #This can be replaces by 

if Name == "Harry" or Name == "Hermoine" or Name == "Ron":
    print("Griffindor")
else:
    print("Not griffeindotrian")# even better is match like switch 

match Name:
    case "Harry":
        print("Griffindor")
    case "Hermoine":
        print("Griffindor")
    case "Ron":
        print("Griffindor")
    case "Draco":
        print("SLyherin")
    case _:    #default case 
        print("Who?") 

match Name:
    case "Harry"| "Hermoine" | "Ron" :
        print("Griffindor")
    case "Draco":
        print("SLyherin")
    case _:    #default case 
        print("Who?") 

