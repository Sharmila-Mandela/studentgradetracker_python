condition=True
while  condition is True:
    print("Enter Marks Obtained in 6 Subjects: ")
    markOne = int(input())
    markTwo = int(input())
    markThree = int(input())
    markFour = int(input())
    markFive = int(input())
    markSix= int(input())
    tot = markOne+markTwo+markThree+markFour+markFive+markSix
    avg = tot/6


    if avg>=85 and avg<=100:
      print("Total score:",tot)
      print("Your Grade is O")
      print("PASS")
    elif avg>=75 and avg<=84:
      print("Total score:",tot)
      print("Your Grade is A")
      print("PASS")
    elif avg>=66 and avg<=74:
      print("Total score:",tot)
      print("Your Grade is B")
      print("PASS")
    elif avg>=57 and avg<=65:
      print("Total score:",tot)
      print("Your Grade is C ")
      print("PASS")

    elif avg>=47 and avg<=56:
      print("Total score:",tot)
      print("Your Grade is D")
      print("PASS")
    elif avg>=35 and avg<=46:
      print("Total score:",tot)
      print("Your Grade is E")
      print("PASS")
    elif avg<=34:
      print("Total score:",tot)
      print("Your Grade is F")
      print("FAIL")
    else :
      print("INVALID INPUT")

    yorno =input("continue calculating the grades(y/n)")
    if(yorno =='n'):
          condition=False
 