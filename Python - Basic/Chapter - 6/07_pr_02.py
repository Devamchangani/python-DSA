sub1 = int(input("Enter first subject marks\n"))
sub2 = int(input("Enter second subject marks\n"))
sub3 = int(input("Enter third subject marks\n"))

if(sub1<33 and sub2<33 and sub3<33):
    print("you are fail")
elif(sub1+sub2+sub3)/3 <40:
    print("you are fail due to total percentage less then 40")   
else:
    print("Congratulation! you are passed the exam")    