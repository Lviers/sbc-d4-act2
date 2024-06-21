from random import randint

hayang,kulob = 0,1 #make it more efficient by copying sir's code


ako = int(input("Humpyang makulong mahayang! : "))#merge

c1,c2,c3 = randint(0, 1),randint(0, 1),randint(0, 1) #make it more efficient by copying sir's code


print(f"Ako: {'kulob' if ako == kulob else 'hayang'}"), print(f"C1: {'kulob' if c1 == kulob else 'hayang'}"),print(f"C2: {'kulob' if c2 == kulob else 'hayang'}"), print(f"C3: {'kulob' if c3 == kulob else 'hayang'}")
#print(f"C1: {'kulob' if c1 == kulob else 'hayang'}") #less line more efficient??
#print(f"C2: {'kulob' if c2 == kulob else 'hayang'}")
#print(f"C3: {'kulob' if c3 == kulob else 'hayang'}")

if (ako, c1, c2, c3 ) == (hayang, kulob, kulob, kulob):    #make it more efficient by making it shorter
    print("You win!")                                      #1st test if (ako, c1,c2,c3  == hayang, kulob, kulob, kulob) etc. output doesn't work 
elif (ako, c1, c2, c3, ) == (hayang, kulob, kulob, kulob): #even though it has no any errors.
    print("You win!")                                      #2nd test = success as you can see at the left side
elif (ako, c1, c2, c3, ) == (kulob, hayang, kulob, kulob):
    print("C1 wins!")
elif (ako, c1, c2, c3, ) == (hayang, kulob, hayang, hayang):
    print("C1 wins!")
elif (ako, c1, c2, c3, ) == (kulob, hayang, kulob, kulob):
    print("C1 wins!")
elif (ako, c1, c2, c3, ) == (kulob, kulob, hayang, kulob):
    print("C2 wins!")
elif (ako, c1, c2, c3, ) == (kulob, kulob, hayang, kulob):
    print("C2 wins!")
elif (ako, c1, c2, c3, ) == (kulob, kulob, kulob, hayang):
    print("C2 wins!")
elif (ako, c1, c2, c3, ) == (kulob, kulob, kulob, hayang):
    print("C2 wins!")
else:
    print("Draw!")

