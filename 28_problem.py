n=input("Which class: ")
w=input("Which pass: ")
if(w=="mothly"):
    if(n=="sleeper"):
        print(100*0.1)
    elif(n=="3AC"):
        print(200*0.1)
    elif(n=="2AC"):
        print(300*0.1)
    elif(n=="1AC"):
        print(400*0.1)
elif(w=="onetime"):
    if(n=="sleeper"):
        print(100)
    elif(n=="3AC"):
        print(200)
    elif(n=="2AC"):
        print(300)
    elif(n=="1AC"):
        print(400)
