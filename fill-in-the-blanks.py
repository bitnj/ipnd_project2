# IPND Stage 2 Final Project

# Fill in the blank quiz using code adapted from mad_libs.py.  The user will be
# be presented with a paragraph containing blank spaces that need to be filled
# in with the correct answer.  Five attempts will be given to get each blank
# correct.  If the user gets five incorrect answers in a row the quiz must be
# restarted.  The blanks are labeled 1 through n, where blanks with the same
# number are filled in with the same answer.  Answers are NOT case sensitive.
# If a correct answer is given the entire quiz text, with that answer (and all
# previous correct answers) is displayed.

MAX_GUESSES = 5

# Quiz texts
quiz1_text = '''A ___1___ is created with the def keyword. You specify the inputs a 
___1___ takes by adding ___2___ separated by commas between the parentheses. 
___1___s by default return ___3___ if you don't specify the value to return. 
___2___ can be standard data types such as string, number, dictionary, tuple,
and ___4___ or can be more complicated such as objects and lambda functions.\n\n'''

#
quiz2_text = '''A ___1___ is noice! A ___2___ is better! A ___3___ is the best \n\n'''

#
quiz3_text = 'Jack and Jill went up the ___1___'

# list of possible quiz texts
quizes = [quiz1_text, quiz2_text, quiz3_text]

# Placeholders and answers 
quiz1_blanks  = ["___1___", "___2___", "___3___", "___4___"]
quiz1_answers = ["function", "arguments", "None", "List"]

quiz2_blanks = ["___1___", "___2___", "___3___"]
quiz2_answers = ["foo", "bar", "baz"]

quiz3_blanks = ["___1___"]
quiz3_answers = ["beanstalk"]

# beginning of program
def take_quiz():
    # welcome message and prompt for user name
    
    # give brief instructions and ask for quiz selection
    
    choice = raw_input("Choose a quiz: 1, 2, or 3\n\n")
    
    print 'You chose quiz ' + choice + '. Good luck!\n\n'
    quiz = quizes[int(choice) - 1]
    print quiz
    
    index = 0 # keep track of which blank / answer pair we are talking about
    for e in quiz1_blanks:
        rem_guesses = MAX_GUESSES
        guesses = 0
        correct_ans = False
        while guesses < MAX_GUESSES and not correct_ans:
            user_input = raw_input("What word goes in: " + e + "?  ")
            #check if the answer given is correct and if so replace all
            #instances of this blank with the answer.
            answer = quiz1_answers[index]
            if answer == user_input:
                correct_ans = True
                quiz = quiz.replace(e, user_input)
                print 'Correct!\n'
                print quiz
                index += 1
            else:
                #Otherwise let the user know they got it wrong and report how many
                #chances they have left
                guesses += 1
                rem_guesses -= 1
                print 'Incorrect! You have ' + str(rem_guesses) + ' guesses remaining.\n\n'
                print quiz
        if not correct_ans:
            return 'You Lose!\n'
    if correct_ans:
        print "You Win!"
        return quiz
    else:
        return "You Lose!"
    
print take_quiz()       
