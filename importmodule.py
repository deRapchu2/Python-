import sys 

from Python.Module import hello

if len(sys.argv) ==2:
    hello(sys.argv[1]) #the problem here is that in the module that we created the main function is executed therefore no matter our input 
    #the output will be hello niaaami will always be also executed because of last line main() in the module , to prevent this we change last line in the module to if__name__= ...
    #what is does is that the command that is beign run in the terminal , that commands __name__ it equates to __main__ otherwise if imported that commands 
    # __name__ automatically equals to its __program_name__ not the __main__ therefore we can put a condition in the module therefore main() that we define will only run if 
    #the program is itself being run in the command line , therefore the condiiton is : if __name__ == '__main__' : main() 
    #therefore now the functions defined under the condition will only be called if the program is itself being ran in command line


#we can also do , import Module and instead of hello we do Module.hello