#نمرات دانشجویا کامپیوتر
# A نمرات بین 17 تا 20 با حرف 
# B نمرات بین 12 تا 17 با 
# C نمرات بین 10 تا 12 با 
# F نمرات بین 0 تا 10 با 
#_____________________________________________
score=int(input("enter your score:"))
if score>=17 and score<=20:
    print("great!you got A")
elif score>=12 and  score<=17:
    print("good! you got B")
elif score>=10 and score<=12:
    print("not bad, you need to more try!you got C ")
elif score>=0 and score<=10:
    print("ops!you failed!you got F")
else:
    ("try again!smth went wrong...")
