def main():
    score = int(input("Enter the score for your todays test: "))

    if score >90 and score <= 100: #score being >90 is same as 90<score , we can define range as defined in below code 
        print("YOur score is good")
    elif score <=90 and score >60:
        print("YOur grade is Decent")
    elif score <=60 and score > 33:
        print("BArely passses")
    else:
        print("Leave my tuition")

main()
#this can be replaced by 

score = int(input("Enter your grades: "))

if 90<=score<=100:
    print("Grade: A")
elif 75<=score<90:
    print("Grade: B")
elif 50<=score<75:
    print("Grade: C")
else:
    print("Grade: F") #this can be simplified further as 

if score>=90:
    print("A") #this can be used because this only executes if score >90 and if not it will move further 
elif score>=75:
    print("B")
elif score>= 50:
    print("C")
else:
    print("Fail") 

#even and odd 

#letting the score to be the input number 

if score%2 == 0:
    print("THe score is even")
else:
    print("YOur score is odd")
#this can be also used as 
def iseven(n):
    if n%2 == 0:
        return True
    else:
        return False 
           #all this can be collapsed into 
    return True if n%2 == 0 else False #incase our boolean expression, here n%2 == 0 , has true or false as only answers we dont need to ask questions using conditionals
    #this is even better in 
    return n%2 == 0 

if iseven(score):
    print("Even")
else:
    print("Odd")

