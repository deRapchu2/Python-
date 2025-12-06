import pytest #importing to use its functions in testing the input as string 
from unitTest import square
from unitTest import hello
#in real world we can have code that tests our code and automate it 
def main():
    test_positive()  #convention used to conditionally call main 
    test_negative()
    test_zero()

# def test_square():
#     if square(2) != 4:
#         print("Bug detected at 2")
#     if square(3) != 9:
#         print("Bug detected at 3")  #we have written more test than actual code , therefore we have another way for this 
#     #to show errors we can do assert inside this function , therefore there will be an error if otherwise 
#     if square('abc') != 'abcabc':
#         print("String Error")
#     try:
#         assert square(2) ==4 
#     except AssertionError:
#         print("Error in 2")
#     try:   
#         assert square(3) == 9 #shows us the assertion failed and prints the line , this is aired wit error handling 
#     except AssertionError:
#         print("Error was present at 3")
#     try:   
#         assert square(-3) == 9 #shows us the assertion failed and prints the line , this is aired wit error handling 
#     except AssertionError:
#         print("Error was present at -3")
#     try:   
#         assert square(0) == 0 #shows us the assertion failed and prints the line , this is aired wit error handling 
#     except AssertionError:
#         print("Error was present at 0") #but this way we have to write a lot of code to test a 2 line function , therefore we can do 

    #tools to test is pytest , third party that test automatically when setup 
    # Unit testing is testing individual units of program , or functions to check if they do what is designed them to do
    #this can be done in terminal as pytest code_name.py , here it might pass because we have handled exceptions also 

# def test_square():
#     #to test pytest we will do 
#     assert square(2) == 4
#     assert square(3) == 9
#     assert square(-2) == 4
#     #and we will see that error is raised and reason is also shown 
    #it shows the first assertion that fails but we can do diferrentily for returning every error , for that we have to make more functions 
    #therefore we can have seperate for negative and positive 
    #we can also have for valueerror if input is putted as a string 
def test_positive():
    assert square(2) == 4
    assert square(3) == 9
def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9
def test_zero():
    assert square(0) == 0 #if passes it will show 3 passed means that 3 functions have passed to be good 
    #if failed that it will show number of passed and number of failed 
    #we can have files for different types of test and we can run pytest of a whole folder where we have the test files  
def test_str():
    #now if we remove the conversion for user input to int in the main code , we have to test that too   
    #here typeError will be raised 
    with pytest.raises(TypeError):
        square("abc") #now the test will be successful be we have handled the exception here for square("abc") 
    #square("here") #here error will be raised because we have not handled it    
    #testing can only be done on the return value , example would be a program that only prints some string , example 
def test_hello():
    assert hello("niiga") == "hello, niiga" #now we have changed hello from print to return a f string
def test_default_hello(): 
    assert hello() == "hello, World"
if __name__ == "__main__":
    main() #just incase we import this elsewhere2 
