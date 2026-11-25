ism = "Aziz"
yosh = 19
ball = 85

if yosh >= 18 and ball >= 80:
  holat = "Qabul qilindi"
elif yosh >= 18:
  holat = "Zaxirada"
else:
  holat = "Yosh mos emas"

print(f"{ism} ({yosh} yosh) — {holat}")

gpa = float(input())
if gpa>=4.5:
  print(f"{ism} - Yuqori stipendiya")
elif gpa>=3.5:
  print(f"{ism} - Oddiy stipendiya")
else:
  print(f"{ism} - Stipendiya tayinlanmadi")


kitob = input()
kunlar = int(input())
if kunlar<=0:
  print("O'z vaqtida qaytarildi")
elif kunlar >=1 and kunlar <=5:
  print(f"{kunlar} kechikkani uchun {kunlar*2000} so'm jarima")
else:
  print(f"{kunlar} kechikish uchun {10000 + (kunlar-5)*5000} so'm jarima")


parol = input()
isdigit = False;
for i in parol:
  if i.isdigit():
    isdigit = True
if len(parol)<8:
  print("Zaif parol: kamida 8 belgi bolishi kerak")
elif not isdigit:
  print("kamida 1 ta raqam qoshing")
else:
  print("Kuchli parol, omadingni bersin!")