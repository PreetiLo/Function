# numbers_list = [1, 2, 3, 4, 5, 6, 7, 10, -2]
# print (max(numbers_list))

# a=[1,2,3,4,5,6]
# print(len(a))

# def say_hello(name):
#     print ("Hello ", name)
#     print ("Aap kaise ho?")
# say_hello("Aatif")
# say_hello("monika")

# multiple funcation Argument

# def add_numbers(number1,number2):
#     print ("Main do numbers ko add karunga.")
#     print (number1 + number2)
# add_numbers(120, 50)
# num_x = 134   # ye value islie nhi ho rha hai kyonki ye function ke bahar likha hai
# name = "Rinki"
# add_numbers(num_x,name) 

# 

# def say_hello_people(name_x, name_y, name_z, name_a):
#     print ("Namaste ", name_x) 
#     print ("Alah hafiz ", name_y) 
#     print ("Bonjour ", name_z) 
#     print ("Hello ", name_a) 
# say_hello_people("Imitiyaz", "Rishabh", "Rahul", "Vidya")
# say_hello_people("Steve", "Saswata", "Shakrundin", "Rajeev")

# Arbitrary Arguments hum jab tak use krte hai jab hume pta nhi hota hai ki hame kitne number of argument function me dene hai.

# def icecream(*flavours):
#     for flavoure in flavours:
#         print("i love"+flavoure)
# icecream("chocalate","butterscotch","vanilla","strawberry")        

# Default parameter value se yaha humara ye matlab hai ki hum function ko define karte time kisi parameter ko value assign kar dete hai taaki hum function ko bina kisi argument ke call kare to vo default value ko le le.

# def attendance(name,status="absent"):
#     print(name,"is",status," today")
# attendance("kartik","present")
# attendance("sonu")
# attendance("vishal","present")
# attendance("umesh")
