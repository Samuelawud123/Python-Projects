#Name: Samuel Awud
#Date: Jan 10, 2023

#Mid-Lib Game 
"""A program that asks players for few words and 
replace those words on an already written paragraph.

Original Story: Once upon a time, there was a kind and 
adventurous prince named Sam. He embarked on a journey to
rescue a beautiful princess from a fearsome dragon. 
Together, they lived happily for 50 years in Paris."""

print("Welcome to  the Mad-Lib players") 
#print a welcome for the players

adjective = input("Enter an adjective first: ") 
#asks for the adective to describe the prince
name = input("Enter a name: ")
#asks for a name to replace the princes name 
verb = input("Enter a verb: ")
#asks for verb to replace the word embarked
animal = input("Enter animal name: ") 
#asks for the animal to replace the dragon
number = input("Enter a number of your choice: ") 
#asks for a number to replace the number of years
city = input("Enter your favorite city: ") 
#asks for a city to replace Paris

"""We finally plug in these words into the old story 
and print the result"""
print("Once upon a time, there was a kind and",adjective,"\
 prince named",name, ". He",verb, "on a journey to rescue\
 a beautiful princess from a fearsome",animal,". Together, they \
lived happily for",number, "years in",city,".")

"""It was a pretty fun homework where I learned a lot in programming.
It was kind of hard to find the story at first, but I ended up getting
this one from an old book. I tested the program by running the file again
and again on visual studio codes. And I learned how to comment a single line
Bigand multiline comments, I learned how to recieve input the user, how to 
print a line and how to plug in words when printing. For next time, I will
make sure to use a much cleaner variable names since the ones I used were
a little confusing."""