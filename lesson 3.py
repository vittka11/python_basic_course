#умови
# v1
# n1 = 10
#n2 = 20
#v2
n1,n2=10, 20 # множинне призначення
print(n1 > n2)
print(n1>= n2)
print(n1< n2)
print(n1 <= n2)
print(n1 == n2) #поверне true якщо обидва операнди рівні(однакові
print(n1 != n2) #поверне тру якщо обидва операнди рівні
result = n1 == n2
###
print(1 == 1 and 3 == 3)
print(1 == 1 or 2 == 3)
###
is_valid = false
print(is_valid)
print(not is_valid)
#
# print ("hello" in "hello world")
#
###
# hours = int(input("Enter hours: "))

#v1
if hours >= 12:
   print("PM")
else
    print("AM")

#v2
if 12<+ hours < 24: # hours >+ 12 and hours < 24
    print("PM")
if 0 <+ hours < 12:
    print("AM")
else:
    print("Incorrect hours!")

    ###
    #ввести рейтинг фільму : якщо рейтинг дорівнює 5 або 4 - ок, інакще - погано
    # film_rating = int(input("Enter film rating: ")

number_b = 30
#v1
#if number_b <5:
#   number_a = 10
#else:
#    number_a=20
#v2
number_a = 10 if number_b < 5 else 20
print(number_a)

######
number_b =30
if number_b <5
    if number_b %2 == 0:
        number_a = 10
    else:number_a = 15
else:
    number_a = 20
 number_a = 10 if number_b % 2 == 0 else 15 if number_b < 5 else 20
 print(number_a)



 ###############################
лист список
 #list
 #number =[]
 #numbers1 = list()
 #print(type(numbers))
 #print(type(numbers_1))
 #
 #numbers = [1, 3, 25, 7, 2, 7]
 ###
 ### print(numbers)
 ###
 ### [] -> індексатори
   #### ІНДЕКС ЦЕ ПОРЯДКОВИЙ НОМЕР ЕЛЕМЕНТА


numbers[1] = 11111
print(numbers)

print(len(numbers))
print(numbers[-1])
#
#print(numbers[len(numbers)]) # [6] -> error

###
values =["one", 12, 12.4, True]
print(values)

#
nums:list[int] = [1,3] * 5
print(nums)
 #
 # slices
 numbers = [1, 3, 25, 7, 2, 7]
 print(numbers[:])
 print(numbers[1:])
 print(numbers[1:5])
 print(numbers[:5])
 print (numbers[1:5:2])
print(numbers[::-1])
print(numbers[5::-1])
print(numbers[5:0:-1])

##
users = ()










