# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

low_name1 = name1.lower()
low_name2 = name2.lower()

count_T1 = low_name1.count("t")
count_T2 = low_name2.count("t")
count_T= count_T1 + count_T2

count_R1 = low_name1.count("r")
count_R2 = low_name2.count("r")
count_R= count_R1 + count_R2

count_U1 = low_name1.count("u")
count_U2 = low_name2.count("u")
count_U= count_U1 + count_U2

count_E1 = low_name1.count("e")
count_E2 = low_name2.count("e")
count_E= count_E1 + count_E2

toplam_true = count_T + count_R + count_U + count_E

count_L1 = low_name1.count("l")
count_L2 = low_name2.count("l")
count_L= count_L1 + count_L2

count_O1 = low_name1.count("o")
count_O2 = low_name2.count("o")
count_O= count_O1 + count_O2

count_V1 = low_name1.count("v")
count_V2 = low_name2.count("v")
count_V= count_V1 + count_V2

countt_E1 = low_name1.count("e")
countt_E2 = low_name2.count("e")
countt_E= countt_E1 + countt_E2

toplam_love = count_L + count_O + count_V + countt_E

str_toplam_true = str(toplam_true)
str_toplam_love = str(toplam_love)

str_total_toplam= int(str_toplam_true + str_toplam_love)

if str_total_toplam <=10 and str_total_toplam >= 90:
    print(f"Your score is {str_total_toplam}, you go together like coke and mentos.")

elif str_total_toplam >= 40 and str_total_toplam <= 50 :
    print(f"Your score is {str_total_toplam}, you are alright together.")

else:
    print(f"Your score is {str_total_toplam}")