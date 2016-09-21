# IPND Stage 2 Final Project

# Presents the user with a short text that contains missing words.  The user has
# up do MAX_GUESSES per blank to answer correctly.

# Unlike madlibs, where the placeholder values were variable, we know exactly
# what pattern we are looking for to identify a blank space.  In this case,
# the program expects a blank space with the format ___#___ (i.e. three
# underscores followed by a number in the range 1-10.  There can be multiple
# occurrences of the same numbered blank.  The only assumptions is that the
# first occurrence of each numbered blank appear in order (i.e. 1 before 2 and 2
# before 3 etc).

# Quiz texts and their corresponding answers are provided in text files stored
# in quizes_path and answers_path respectively.  It is assumed that quiz and
# answer file pairs have identical names.


import os # to get the listdir method
import re # to use regular expressions for finding blanks

MAX_GUESSES = 5             # number of guesses for EACH blank
quizes_path = "quizes"      # relative path to the quiz text files
answers_path = "answers"    # relative path to the answer key files

def display_welcome():
    print ("Welcome to the IPND Stage 2 Quizes.\nYou will be given " +
    str(MAX_GUESSES) + ''' guesses to correctly identify the missing word that
    belongs in each blank space (e.g. ___1___).  The answers are not
    case-sensitive.\n''')

# display the available files in the quiz directory
def get_quiz_list(path):
    return os.listdir(path)
    
# prompt the user for their name and to choose from a list of available quizes
def get_user_choices(avail_quizes):
    name = raw_input("Please tell me your name: ")
    
    print ('''\nChoose a quiz by index (i.e. 0, 1, 2 etc.) from the list below: ''')
    print avail_quizes
    choice = raw_input("Choice: ")
    return name, choice

# take a relative path and a file name and return a string containing the text
# read from the file
def get_file_text(path, fname):
    f = open(path + '/' + fname, 'r')
    text = f.read()
    return text

# beginning of program
def take_quiz():
    # welcome and give the user basic instructions
    display_welcome()
   
    # get the list of available quizes 
    file_list = get_quiz_list(quizes_path)

    # get the user name and quiz choice
    user_name, choice = get_user_choices(file_list)
    print 'You chose quiz ' + choice + '. Good luck, ' + user_name + '!\n'
    
    # open the quiz text file and store the text
    quiz = get_file_text(quizes_path, file_list[int(choice)])

    # open the corresponding answer text file and store as a list
    # it is assumed that the answer file is named identically to the
    # quiz file
    answers = get_file_text(answers_path, file_list[int(choice)])
    answers = answers.split(',')
    print quiz    
    
    # get a list of all blanks that match the pattern
    matches = re.findall('___[1-9]___|___10___', quiz)
    num_unique_matches = len(set(matches))

    index = 0 # keep track of which blank / answer pair we are talking about
    while index < num_unique_matches:
        remaining_guesses = MAX_GUESSES
        wrong_guesses = 0
        correct = False
        placeholder = matches[index]

        # let the user guess until they either get it right or they use all of
        # their allotted guesses
        while wrong_guesses < MAX_GUESSES and not correct:
            user_input = raw_input("What word goes in: " + placeholder + "?  ")
            user_input = user_input.lower()
            #check if the answer given is correct and if so replace all
            #instances of this blank with the answer.
            correct_answer = answers[index].strip() # strip removes any leading
            # or trailing whitespace
            correct_answer = correct_answer.lower()
            if user_input == correct_answer:
                correct = True
                quiz = quiz.replace(placeholder, user_input)
                print '\nCorrect!\n'
                print quiz
                index += 1
            else:
                #Otherwise let the user know they got it wrong and report how many
                #chances they have left
                wrong_guesses += 1
                remaining_guesses -= 1
                print '\nIncorrect! You have ' + str(remaining_guesses) + ' guesses remaining.\n'
                print quiz
        if not correct:
            return 'You Lose!\n'
    if correct:
        print "You Win!"
        return quiz
    else:
        return "You Lose!"
    
print take_quiz()       
