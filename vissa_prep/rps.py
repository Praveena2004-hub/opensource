Vignesh,Charan=input().split()
if Vignesh==Charan:
    print("NULL")
elif(Vignesh=="R" and Charan=="S")or(Vignesh=="S" and Charan=="P")or(Vignesh=="P" and Charan=="R"):
    print("Vignesh")
else:
    print("Charan")
