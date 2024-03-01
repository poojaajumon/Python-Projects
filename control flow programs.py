# control flow programs
#task 1
a=int(input("enter your age"))
if(a>18):
    print("you are eligible")
else:
    print("you are not eligible")



# task2
a=int(input("enter a number"))
if(a>0):
    print("positive")
else:
    print("negative")

#task3
alphabet=input("enter a single alphabet:")
if alphabet.lower() in ['a','e','i','o','u']:
    print(f"{alphabet} is a vowel")
else:
    print(f"{alphabet} is not a vowel")

# task4
for i in range(-10,0):
    print(i)
# task 5
for i in range(200,500,2):
    print(i)

#task 6
num=int(input("enter a number"))
print("the multiples of given number is:")
for i in range (1,100):
    print(num*i,end="")

# task 7
a=[10,20,30,40,50]
print("elements of given list positioned at odd index:")
for i in range (0,len(a),2):
    print(a[i])

# task 8
num=int(input("display multiplication table of "))
for i in range(1,11):
    print(num,'x',i,'=',num*i)

# task 9
word="welcome"
for letter in word:
    if(letter=='c'):
        break
    print(letter)

# task 10
string = "Hello world!"
for char in string:
    if char == "w":
        continue 
    print(char)

