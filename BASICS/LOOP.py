#Loop is a way of repeating an action until a given condition is met
#for example lets create a list of fruits and using for loop, to print each element of the list.

#create a list called fruits
fruits = ["Apple", "Banana", "Grapes", "Mango"]

#adding loop to print each element of the list "fruits", unless every element is printed
for fruit in fruits:
  print(fruit)   

#RESULT: 
#Apple
#Banana
#Grapes
#Mango
-------------------------------------------------------------------------------------------------------------------
#Indentation is important, anything after for loop statement is part of for loop
for fruit in fruits:
  print(fruit)  #part of for loop
print(fruits)   #not a part of the loop as there is no indentation in front of it.

--------------------------------------------------------------------------------------------------------------------
#example 2: consider a list of scores
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

#first way of printing the total of scores in the student_scores
sum = sum(student_scores)
print(sum) #RESULT: 2068

#Getting the same result with for-loop
sum = 0
for score in student_scores:
    sum += score
print(sum) #RESULT: 2068

----------------------------------------------------------------------------------------------------------------------
#scenario
#find out the biggest number from the following list
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

#declaring variable to record the max number from the list
max_num = 0

#for loop
for score in student_scores:
    if score > max_num:
        max_num = score
print(max_num)

---------------------------------------------------------------------------------------------------------------------------
#LEARNING 2: Using range function with For-Loop
#Syntax : for i in range(a,b)    #i: particular elements #a: starting range and b: ending range, a =< num < b

#example: dislay 1-10 numbers on screen
#Solution:
for num in range(1,11):
  print(num)

#Result: 
1
2
3
4
5
6
7
8
9
10

--------------------------------------------------------------------------------------------------------------------------

