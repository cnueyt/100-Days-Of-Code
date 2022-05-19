# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
sp = 15
mp = 20
lp = 25
ppfsp = 2
ppfmp = 3
ecfap = 1

if size == "S":
    bill = sp
    if add_pepperoni=="Y":
        bill = bill + ppfsp
        if  extra_cheese == "Y":
            bill = bill + ecfap
            print(bill)
    elif add_pepperoni =="N":
        if  extra_cheese == "Y":
            bill = bill + ecfap
            print(bill)
elif size == "M":
    bill = mp
    if add_pepperoni=="Y":
        bill = bill + ppfsp
    else:
        print(bill)
        if  extra_cheese == "Y":
            bill = bill + ecfap
            print(bill)
elif size == "L":
    bill = lp
    if add_pepperoni=="Y":
        bill = bill + ppfsp
    else:
        print(bill)
        if  extra_cheese == "Y":
            bill = bill + ecfap
            print(bill)
else:
    print("please do S or M or L")