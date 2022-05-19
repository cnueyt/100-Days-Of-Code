import math
def paint_can(height, width, cover):
    covercount = math.ceil(((height*width)/cover))
    print(f"height of wall is: {height} \nwidth of wall is: {width}")
    print(f"you need {covercount} cans")

height = float(input("Height: "))
width = float(input ("Width: "))
cover = int(input ("Cover: "))

paint_can(height, width, cover)
print(type(paint_can))






#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇



