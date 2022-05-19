# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1= input("What is your name? \n").lower()
name2= input("What is their name? \n").lower()
# 🚨 Don't change the code above 👆
t =0
r=0
u=0
e =0

for i in name1+name2:
    if i == "t":
        t += 1
    elif i == "r":
        t += 1
    elif i == "u":
        u +=1
    elif i =="e":
        e +=1
a=str(t+r+u+e)
l = 0
o = 0
v = 0
e = 0
for i in name1+name2:
    if i == "l":
        l += 1
    elif i == "o":
        o += 1
    elif i == "v":
        v +=1
    elif i =="e":
        e +=1
b=str(l+o+v+e)
c = int(a+b)

if c < 10 or c >90:
    print(f"your score is {c}, you go together like coke and mentos")
elif c<50 and c>40:
    print(f"Your score is {c}, you are alright together.")
else:
    print(f"Your score is {c}.")

#Write your code below this line 👇


