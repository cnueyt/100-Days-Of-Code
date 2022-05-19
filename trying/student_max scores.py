# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
#len kullanmadan listenin uzunluğunu bulalım
x = 0
y = 1
for i in student_scores:
    x +=1

if y < x:
    for i in student_scores:
        if student_scores[y-1]>student_scores[y]:
            print(student_scores)
        elif student_scores[y-1]<student_scores[y]:
            y +=1 



