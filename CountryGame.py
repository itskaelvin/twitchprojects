
countries = dict(
 Canada = 1, 
 China = 2, 
 UK = 3,
 USA = 4,
 Korea = 5
)

answerkey = {
    "Canada" : "OTTAWA",
    "China" : "BEIJING",
    "UK" : "LONDON",
    "USA" : "WASHINGTON D.C.",
    "Korea" : "SEOUL"
}

import random
print(random.choice(list(countries.keys())))
print("Welcome to the Game. Test you knowledge!")
score = 0
for x in range(5):
    c = random.choice(list(countries.keys()))
    print("What is the capital of" + " " + c + "?")
    answer = input("Enter answer:")
    answer = answer.upper()
    print ("Your answer was:" + answer)
    if answer == answerkey[c]:
        score += 1
        print("Correct!")
    else:
        print("Wrong!")
print("Congratulations! You got" + " " + str(score) + " " + "correct!")
