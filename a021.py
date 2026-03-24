list=input("").split(" ")
if list[1]=="+":
    print(int(list[0])+int(list[2]))
elif list[1]=="-":
    print(int(list[0])-int(list[2]))
elif list[1]=="*":
    print(int(list[0])*int(list[2]))
elif list[1]=="/":
    print(int(list[0])//int(list[2]))
