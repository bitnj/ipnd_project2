# IPND Stage 2 Final Project

# Neil Seas - 2016

# Presents the user with a short text that contains missing words.  The user has
# up do MAX_GUESSES per blank to answer correctly.

# Unlike madlibs, where the placeholder values were variable, we know exactly
# what pattern we are looking for to identify a blank space.  In this case,
# the program expects a blank space with the format ___#___ (i.e. three
# underscores followed by a number in the range 1-10.  There can be multiple
# occurrences of the same numbered blank.  The only assumptions is that the
# first occurrence of each numbered blank appear in order (i.e. 1 before 2 and 2
# before 3 etc).  Blanks of the same number are filled in with the same value
# and at the same time.

# To keep the code neater and more easily allow for additional quizes the quiz
# texts and their corresponding answers are provided in text files stored in
# quizes_path and answers_path respectively.  It is assumed that quiz and answer
# file pairs have identical names.

# Some Google searching was done to get details on methods I assumed would
# exist, but for which I did not know the exact name.  E.g. os.listdir(),
# sorted(), and findall(), set().


import os # to get the listdir method
import re # to use regular expressions for finding blanks

MAX_GUESSES = 5             # upper bound of guesses for EACH blank
quizes_path = "quizes"      # relative path to the quiz text files
answers_path = "answers"    # relative path to the answer key files
regEx = '___[1-9]___|___10___]' # search pattern for blanks

# provides user with brief instructions
def display_welcome():
    print ("Welcome to the IPND Stage 2 Quizes.\n\nYou will be given " +
    str(MAX_GUESSES) + ''' guesses to correctly identify the missing word that
    belongs in each blank space (e.g. ___1___).  The answers are not
    case-sensitive.\n''')

# get available quiz levels
def get_levels(path):
    return sorted(os.listdir(path))
    
# prompt the user for their name and to choose from a list of available quizes
def get_user_choices(levels):
    name = raw_input("Please enter your name: ")
    
    # choose difficulty level
    level = -1
    while level not in range(0, len(levels)):
        print '''\nChoose a difficulty level (by index) from the list: \n'''
        print levels
        level = int(raw_input("Choice: ")) - 1

    # choose limit on incorrect guesses
    guesses = -1
    while guesses not in range(1, MAX_GUESSES):
        print '''\nHow many incorrect guesses per blank do you want?\n'''
        print "Possible choices (1-" + str(MAX_GUESSES) + ")\n"
        guesses = int(raw_input("Choice: "))
    return name, level, guesses

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

    # populates the difficulty_levels list
    difficulty_levels = get_levels(quizes_path)

    # get the user name and quiz choice
    user_name, choice, guesses = get_user_choices(difficulty_levels)
    print 'You chose difficulty level: ' + difficulty_levels[choice] + '. Good luck, ' + user_name + '!\n'
    
    # open the quiz text file and store the text
    fname = difficulty_levels[choice]
    quiz = get_file_text(quizes_path, fname)

    # open the corresponding answer text file and store as a list
    # it is assumed that the answer file is named identically to the
    # quiz file
    answers = get_file_text(answers_path, fname)
    answers = answers.split(',')
    print quiz    
    
    # get a sorted list of all blanks that match our pattern
    matches = re.findall(regEx, quiz)
    matches = list(sorted(set(matches)))
    num_unique_matches = len(set(matches))

    index = 0 # keep track of which blank / answer pair we are talking about
    while index < num_unique_matches:
        remaining_guesses = guesses
        wrong_guesses = 0
        correct = False
        placeholder = matches[index]

        # let the user guess until they either get it right or they use all of
        # their allotted guesses
        while wrong_guesses < guesses and not correct:
            user_input = (raw_input("What word goes in: " + placeholder + "? ")).lower()
            #check if the answer given is correct and if so replace all
            #instances of this blank with the answer.
            correct_answer = (answers[index].strip()).lower()
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
        # if you get here you hit your guess limit without getting it correct
        if not correct:
            return 'Too many incorrect guesses! Better luck next time.\n'
    print "You Win!\n"
    return quiz
        
print take_quiz()       
