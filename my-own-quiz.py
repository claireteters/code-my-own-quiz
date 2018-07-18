# Opening prompts and selecting game level
def set_game_difficulty():
    print "Let's take a quiz about the hit TV series, 'The Office'!\n"
    choosen_level = raw_input("Please type a game difficulty of easy, medium, or hard: ")
    while choosen_level not in ("easy", "medium", "hard"):
        choosen_level = raw_input("Please imput a valid answer of easy, medium, or hard: \n")
    print "Let's do the " + choosen_level + " level!\n"
    print "Your quiz begins below!\n"
    return choosen_level

def game_questions(choosen_level):
#will fire after selecting which game they woud like to play. 
# choosen_level: equal to which quiz level the user selects
#returns: which level the user selected and would like to play
    quiz = choosen_level
    global quiz
    if choosen_level == "easy":
        quiz = '''In The Office, there are numerous characters to keep track of. __1__ is the boss of the Scranton branch of Dunder Mifflin. __1__'s number one assistant to the regional manager is __2__, who is also a beet farmer on the side. __3__ is the receptionist who is regularly visited by __4__ who is completely in love with __3__, which makes for an excelent story line throughout the show.'''
    elif choosen_level == "medium":
        quiz = '''In The Office, Michael makes a call to the office screaming about how he __1__ on his George Foreman Grill because he likes to wake up to the smell of bacon in the morning. Dwight decides to save the day by going to his house to get him, and while doing so, __2__ into a pole giving himself a __3__. We know this because later in the day, he starts showing symptoms like typing the same word multiple times on his computer screen, and not knowing hes raising his hand durring a __4__.'''
    elif choosen_level == "hard":
        quiz = '''On the episode "Goodbye Michael" of The Office, the group __1__ to him. Michael is caught off gaurd by this and whispers to himself, " __2__ ". They tell him that he has worked there for so long, that it's like watching the movie 'Die Hard' __3__ times. Meredith gets a solo saying you hit me with your __4__, and Creed says I __5__ you when you __6__. They all join together near the end and tell Michael, remember to __7__!'''
    return quiz
        
#Depending on which level they select, the answers of that game are here. 
#choosen_level: equal the answers that the game will accept depending on which level was choosen by the user.
#returns: after the game level is choosen, the list of answers for that particular level will be returned
def game_answers(choosen_level):
    answer = choosen_level
    global answer
    if choosen_level == "easy":
        answer = ["Michael", "Dwight", "Pam", "Jim"]
    elif choosen_level == "medium":
        answer = ["stepped", "crashes", "concussion", "meeting"]
    elif choosen_level == "hard":
        answer = ["sings", "something is happening", "eighty thousand", "car", "watch", "sleep", "call"]
    return answer

#Goes through the quiz being taken and makes each word an individual string,
#checks each string for underscores and the quiz question number the user is answering,
#then returns the quiz question number that the user is going to answer. If the 
#underscores and quiz question number are not found, nothing happens. 
# answer_number: the variable equal to which specific question they are answering... ex. 1, 2, 3
#split_question: takes the quiz words split into strings and goes through the paragraph to find 
#two underscores, quiz question number, and two underscrores following. 
#returns: if no two underscores, quiz question number, and two underscrores are found, None will return
def word_in_pos(answer_number, split_question):
    number = answer_number
    for number in split_question:
        if number == "__" + str(answer_number) + "__":
            return number
        elif number == "__" + str(answer_number) + "__.":
            return number
        elif number == "__" + str(answer_number) + "__,":
            return number
        elif number == "__" + str(answer_number) + "__!":
            return number
    return None 

#Fills in the place of the quiz question number that the user is answering
#with the correct answer of the question being asked. The underscores remain there.
#question: the question the user chose based on the level they wanted to play. 
#answer_number: finds the output of the function above (word_in_pos) and accepts which question number the user is answering. 
# user_answer: replaces answer_number with the user imput of their correct answer to that particular question number.
#returns: the question with the answer in replace of the two underscores, quiz question number, and two underscrores
def answering_questions(question, user_answer, answer_number):
    question_with_answer = ""
    split_question = question.split()
    number_in_question = word_in_pos(answer_number, split_question)
    if number_in_question != None:
        question_with_answer = question.replace(number_in_question, user_answer)
    return question_with_answer

#Quiz operations. This function starts the game!
def play_game():
    choosen_level = set_game_difficulty()
    question = game_questions(choosen_level)
    solutions = game_answers(choosen_level)
    print question
    answer_number = 1
    while answer_number <= len(solutions):
        user_answer = raw_input("Type your best guess for __"+ str(answer_number) + "__. \n>>")
        index = answer_number - 1
        if user_answer == solutions[index]:
            print "Correct!\n"
            question = answering_questions(question, user_answer, answer_number)
            print question
            answer_number += 1
        else:
            print "Incorrect. Try again!\n"
    print "Nice! You passed the " + choosen_level + " level. You rock!"

play_game()