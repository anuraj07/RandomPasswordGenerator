# import random;
# def generate_password():
#     lowerChars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#     upperChars = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#     numericalChars = ['0','1','2','3','4','5','6','7','8','9']
#     specialChars = ['!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[',']','^','_','`','{','|','}','~']
#
#     for x in range(5):
#         password = random.choice(lowerChars)+random.choice(upperChars)+random.choice(numericalChars)+random.choice(specialChars)
#         password = password+password
#         print(password)
#
#     #return password
#
# if __name__ == '__main__':
#     print("Your randomly generated Password is: ",generate_password())



import random
import pyperclip
from tkinter import *
from tkinter.ttk import *

root = Tk()
var = IntVar()
var1 = IntVar()

root.title("Random Password Generator")

root.mainloop()