CURRENT_YEAR =2023
METER_TO_FEET = 3.281

firstname = input("Your firstname: ") 
lastname = input("Your lastname: ")
year_born = input("When you were born: ")
height_meter = input("your heaight (meter): ")


answers_list =["yes","no","y","n"]
while True:
	gender_input = input("Are you male (yes/no): ")
	if gender_input in answers_list:
		break

year_born = int(year_born)
age = CURRENT_YEAR - year_born

height_meter = float(height_meter)
height_feet = height_meter * METER_TO_FEET
Sheight_meter = round(height_feet,1)

print("\n---")
print("Your name is " + firstname +" "+ lastname)
print("{2} is {0} year old in {1}". format(age,CURRENT_YEAR,firstname))
print("You are {0} feet tall". format(height_meter))


if gender_input == "yes":
	is_male = True

else:
	is_male = False

if  is_male == True:
	if height_feet > 6.5:
		print("you are", end = " ")

		for i in range(10):
			print("very", end =" ")

		print("tall as a man")	

	elif height_feet >6.0:
		print("you are tall as a man")
	else :
		print("you are short as a man")
	
else:
	if height_feet > 5.7:
		print("you are tall as a girl")

	elif height_feet<5.0:
		print("you are", end = " ")

		i=0
		while i<10:
			print("short", end= " ")
			i=i+1

		print("tall as a girl")	

	else:
		print("you are short as a girl")