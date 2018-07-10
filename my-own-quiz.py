# Opening prompts and selecting game level
def set_game_difficulty():
    print "Let's take a quiz!"
    choosen_level = raw_input("Please type a game difficulty of easy, medium, or hard: ")
    if choosen_level == "easy" or choosen_level == "medium" or choosen_level == "hard":
        print "Let's do a " + choosen_level + " level!"
        print "Your quiz begins below!"
    else:
        print "Please imput a valid answer of easy, medium, or hard."
    return choosen_level

#After selecting which game they woud like to play
def game_questions(choosen_level):
    if choosen_level == "easy":
        quiz = '''A __1__ is created with the def keyword. You specify the inputs a __1__ takes by adding __2__ separated by commas between the parentheses. __1__s by default return __3__ if you don't specify the value to return. __2__ can be standard data types such as string, number, dictionary, tuple, and __4__ or can be more complicated such as objects and lambda functions.'''
    elif choosen_level == "medium":
        quiz = '''We used to dream about this stuff. Now, we get to build it. It's pretty neat. ___1___ was the Chairman and CEO of Apple Inc., a company he founded with ___2___ in ___3___. He was also the CEO of Pixar Animation Studios until it was acquired by the Walt Disney Company in 2007. ___1___ was the Walt Disney Company's largest individual shareholder and a former member of its Board of Directors. He is considered to have been a leading figure in both the computer and entertainment industries. Apple was released ___4___ in 2007. This Product caused a great change in the lives of people. '''
    elif choosen_level == "hard":
        quiz = '''__1___ is a sovereign island nation in East Asia.The 2020 Summer Olympics will be held in a capital of ___1___ : ___2___.This country has very traditional city ___3___ is most popular city among foreign tourists. Food in this country is so good especially ___4___ : raw sliced fish, shellfish or crustaceans on vinger rice. This country is birthplace of ___5___. ___5___ is pretty popular among teenager around the world. This country is facing a declining birth rate and an aging population. People of 65 and above are over ___6___ mollion people in ___1___.'''
    return quiz
        
#Depending on which level they select, the answers of that game are here.
def game_answers(choosen_level):
    if choosen_level == "easy":
        answer = ["function", "parameters", "errors", "numbers"]
    elif choosen_level == "medium":
        answer = ["Steven Paul Jobs", "Steve Wozniak", "1976", "iPhone"]
    elif choosen_level == "hard":
        answer = ["Japan", "Tokyo", "Kyoto", "sushi", "anime", "30"]
    return answer

#Takes the blanks and the word trying to be imputted, sees if it matches
#anything in the list, and returns the blank if the answer isnt right. If it is, it will 
#return the answer
def word_in_pos(answer_number, game_answers):
    word = answer_number
    for word in game_answers:
        if word == "__" + str(answer_number) + "__":
            return word
        else:
            return None

#Fills in the blanks of the question with the user's answer
def answering_questions(question, user_answer, answer_number):
    replaced = []
    game_answers = question.split()
    word = user_answer
    for word in game_answers:
        replacement = word_in_pos(answer_number, game_answers)
        if replacement != None:
            print 'here i am figure it out alone baby cakes'
            word = word.replace(replacement, user_answer)
            replaced.append(word)
        else:
            replaced.append(word)
    final_answer = " ".join(replaced)
    return final_answer

#Quiz operations
def play_game():
    choosen_level = set_game_difficulty()
    question = game_questions(choosen_level)
    solutions = game_answers(choosen_level)
    answers_left = 4
    print "You will get " + str(len(solutions)) + " guesses per problem."
    answer_number = 1
    print question
    while answer_number <= len(solutions):
        user_answer = raw_input("Type your best guess for __"+ str(answer_number) + "__. \n>>")
        index = answer_number - 1
        if user_answer == solutions[index]:
            print "Correct!"
            question = answering_questions(question, user_answer, answer_number)
            print question
            answer_number += 1
        else:
            print "Incorrect. Try again!"
    print "Nice! You Passed the " + choosen_level + " level. You rock!"

play_game()