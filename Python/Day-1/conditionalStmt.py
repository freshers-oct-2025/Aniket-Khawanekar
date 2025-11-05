if(6>5):
    print("6 पाँच से बड़ा है")

x=5
if(x!=5):
    print("x 5 के बराबर नहीं है")
else:
    print("x 5 के बराबर है")

s=input("add expression")
if(s=="😛"):
    print("you are smiling")
elif(s=="😞"):
    print("you are sad")
elif(s=="😠"):
    print("you are angry")
else:
    print("unknown expression")

num=int(input("Enter a number"))


match(num):
    case 1:
        print("entered one")
    case 2:
        print("entered two")
    case 3:
        print("entered three")
    case 4:
        print("entered four")
    case 5:
        print("entered five")
    case _:
        print("number is out of range")



        