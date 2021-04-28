
import random
import time

def codeloop():                #this is placed inside a function so you can call it again)
	
	
	progress = 0
	end = 1
	wait = 10

	while (progress < end):
		required_char = chr(random.randint(1,26)+96)
		print("type " + required_char)
		input_char = input("->")
		if input_char == required_char:
			progress += 1
			print("current progress is " + str(progress) + "/" + str(end))
		else:
			print("try again")
			progress = 0
			print("current progress is " + str(progress) + "/" + str(end))
		time.sleep(random.randint(0,3))


	print("program finished 1/3")

	random_check = 0
	tries = 0
	random_threshold = 90
	standard_string = "Dear RJ, are you absolutely positively, one hundred percent sure that you want to really do this, and there is no other thing that would be better to do?"

	while(random_check < random_threshold):
		required_char = chr(random.randint(1,26)+96)
		char_location = random.randint(0,len(standard_string)-1)
		modified_string = standard_string[:char_location] + required_char + standard_string[char_location:]
		print(modified_string)
		input_char = input("->")
		if input_char == required_char:
			random_check= random.randint(1,99) + tries
			print(random_check) 
			tries += 1
		else:
			print("Good choice")
			return 1
		time.sleep(random.randint(0,5))



	print("within now and 45 seconds the code will appaer on the screen")
	time.sleep(random.randint(0,45))
	print("the code is: kerlqkjzfcizvjrljadfaksdfjakldsfjawerqweqtopweithrjsiodhfs")
	return 0

codeloop()

