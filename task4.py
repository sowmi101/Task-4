Tamil = int(input("Enter your mark:"))
English = int(input("Enter your mark:"))
Maths = int(input("Enter your mark:"))
Science = int(input("Enter your mark:"))
Social = int(input("Enter your mark:"))
Max_mark = 100
Min_mark = 40
if(Tamil > English and English > Maths and Maths > Science and Science > Social):
           Max_mark = Tamil
elif(English > Maths and Maths > Science and Science > Social):
           Max_mark = English
elif(Maths > Science and Science > Social):
           Max_mark = Maths
elif(Science > Social):
           Max_mark = Science
else:
           Max_mark = Social

if(Tamil < English and English < Maths and Maths < Science and Science < Social):
           Min_mark = Tamil
elif(English < Maths and Maths < Science and Science < Social):
           Min_mark = English
elif(Maths < Science and Science < Social):
           Min_mark = Maths
elif(Science < Social):
           Min_mark = Science
else:
           Min_mark = Social

print("Your Maximum Mark:",Max_mark)
print("Your Minimum Mark:",Min_mark)