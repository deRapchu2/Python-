#Unit tests are statements that we write inside our code to check its validity on outliers , special cases and general cases too 
def main():
    x = input("what is X: ")
    #print("x sqaured is", square(x))
    name = input("Enter your name")
    print(hello(name))

def square(n):
    return n*n 
#here we can also check for now negative numbers and zero and other some cases to make this robust 
def hello(to = 'World'):
    return f"hello, {to}"
if __name__ == "__main__":
    main() #this is to safely import this in another files  