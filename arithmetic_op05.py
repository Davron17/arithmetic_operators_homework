#Create a variable called 'number' with data type int.
number=int(input())
#Create a variable called 'answer' and assign the remainder of the division of number by 3 to it.
answer=number//100+number%10*100+(number-number//100*100)//10*10
#Print 'answer'.
print(answer)