#!/usr/bin/env python
# coding: utf-8

# # Extended Chatbot

# This chatbot runs off of a bag-of-words model: in other words, it takes a keyword from the user and tries to determine what the user is talking about, purely based off user input. While this ignores many things about language itself, it is a good place to start for a chatbot and can carry a more extended conversation with the user than prior chatbots seen in the course

# It is through the use of conditionals to determine what the user is talking about based on lists of words. We categorize these lists of words based on subject and feed them into the chatbot. The chatbot will then respond appropriately based on the word the user has entered.

# What makes this chatbot cool: it has a wide range of possible responses and is easy for the user to interact with. Try it below! And check out the Github repo here: 

# In[1]:


import string
import random


# Here we have two different methods to determine if what the user enters is a question or an exclamation

# In[2]:


def is_question(input_string):
    output = False
    if (input_string.find('?') != -1):
      output = True
    else:
        output = False
    return output


# In[3]:


def is_exclam(input_string):
    output = False
    if (input_string.find('!') != -1):
        output = True
    else:
        output = False
    return output


# In[4]:


def greeting():
    print("Chatbot! Enter text to begin a conversation. Have fun!")


# In[ ]:


def exit_msg():
    print("Thank you for trying Chatbot!")


# The method below aims to clean the punctuation off of the sentence that the user enters.

# In[ ]:


def remove_punctuation(input_string):
    out_string = ""
    for x in input_string:
            if x not in string.punctuation:
                out_string += x
    print(out_string)
    return out_string


# In[ ]:


def prepare_text(input_string):
    temp_string = input_string.lower()
    temp_string = remove_punctuation(temp_string)
    out_list = temp_string.split()
    return out_list


# In[ ]:


def respond_echo(input_string, number_of_echoes, spacer):
    echo_output = ""
    if input_string:
        echo_output = (input_string + spacer) * number_of_echoes
    else:
        echo_output = None
    return echo_output


# In[ ]:


def selector(input_list, check_list, return_list):
    output = None
    for x in input_list:
        if x in check_list:
            output = random.choice(return_list)
            break;
    return output


# In[ ]:


def string_concatenator(string1, string2, separator):
    return string1 + separator + string2


# In[ ]:


def list_to_string(input_list, separator):
    output = input_list[0]
    for x in input_list[1:]:
        output = string_concatenator(output, x, separator)
    return output


# In[ ]:


def end_chat(input_list):
    if "quit" in input_list:
        output = True
    else:
        output = False
    return output


# In[ ]:


def is_in_list(list_one, list_two):    
    for element in list_one:
        if element in list_two:
            return True
    return False

def find_in_list(list_one, list_two):
    for element in list_one:
        if element in list_two:
            return element
    return None


# The following is the text that our Chatbot will understand! Note that these are lists of strings.

# In[ ]:


GREETINGS_IN = ['hello', 'hi', 'hey', 'hola', 'welcome', 'bonjour', 'greetings', 'yo']
GREETINGS_OUT = ["Hello!", 'Nice to meet you!',  "Let's chat!", "I'm Chatbot!", "Greetings!"]

COMP_IN = ['python', 'code', 'computer', 'algorithm', 'robot']
COMP_OUT = ["Python is what I'm made of.",             "Did you know I'm made of code!?",             "Computers are so magical",             "Do you think I'll pass the Turing test?"]

PEOPLE_IN = ['alan', 'turing', 'grace', 'hopper', 'john von', 'neumann', 'ada', 'lovelace']
PEOPLE_OUT = ['was awesome!', 'did so many important things!', 'is someone you should look up :).', 'is well known in computer science']
PEOPLE_NAMES = {'turing': 'Alan', 'hopper': 'Grace', 'neumann': 'John von', 'lovelace': 'Ada'}

TOPICS_IN = ['movies', 'tv shows', 'songs', 'music', 'netflix', 'gaming', 'school', 'study', 'video games']
TOPICS_OUT = ["I like ", "I am a fan of ", "I also enjoy"]

JOKES_IN = ['hilarious', 'ha', 'haha', 'lol']
JOKES_OUT = ['ha', 'haha', 'hilarious'] 

EMOTE_IN = [':)', ':(', ':O']
EMOTE_OUT = [':/', ':O', ':P']

UCSD_IN = ['ucsd', 'uc san diego', 'UCSD']
UCSD_OUT = ["Wow! You go to "]

FEELING_IN = ['amazing', 'wonderful', 'glorious', 'fantastic', 'magical', 'significant', 'very']
FEELING_OUT = ["I know, right?"]

PL_IN = ['matlab', 'Java', 'C++', 'C', 'Haskell', 'C#']
PL_OUT = ["I am not written in "]

UNKNOWN = ['...', 'Okay', 'Huh?', 'Yeah!', 'Thanks!', 'I try sometimes!' 'I did not understand, try again?']

QUESTION = 'Try Googling it?'

EXCLAM = "!!!"


# Here is the main function that runs our Chatbot!

# In[ ]:


def chat():
    # Display greeting
    greeting()
    
    #Set chat to True so it will be able to run
    chat = True
    while chat:
        
        # Get a message from the user
        msg = input('INPUT :\t')
        out_msg = None

        # Check if the input is a question
        question = is_question(msg)
        
        exclam = is_exclam(msg)

        # Prepare the input message
        msg = prepare_text(msg)

        # Check for an end msg 
        if end_chat(msg):
            out_msg = 'Thanks for talking with me!'
            chat = False

        # Check for a selection of topics that we have defined to respond to
        #   Here, we will check for a series of topics that we have designed to answer to
        if not out_msg:

            # Initialize to collect a list of possible outputs
            outs = []

            # Check if the input looks like a greeting, add a greeting output if so
            outs.append(selector(msg, GREETINGS_IN, GREETINGS_OUT))

            # Check if the input looks like a computer thing, add a computer output if so
            outs.append(selector(msg, COMP_IN, COMP_OUT))

            # Check if the input mentions a person that is specified, add a person output if so
            if is_in_list(msg, PEOPLE_IN):
                name = find_in_list(msg, PEOPLE_IN)
                outs.append(list_to_string([PEOPLE_NAMES[name], name.capitalize(),
                                            selector(msg, PEOPLE_IN, PEOPLE_OUT)], ' '))

            # Check if the input looks like a joke, add a repeat joke output if so
            outs.append(respond_echo(selector(msg, JOKES_IN, JOKES_OUT), 3, ''))

            # Check if the input contains a language
            if is_in_list(msg, PL_IN):
                outs.append(list_to_string([selector(msg, PL_IN, PL_OUT), find_in_list(msg, PL_IN)], ' '))
                
            if is_in_list(msg, FEELING_IN):
                outs.append(list_to_string([selector(msg, FEELING_IN, FEELING_OUT), find_in_list(msg, FEELING_IN)], ' '))

            # Check if the input contains a certain topic:
            if is_in_list(msg, TOPICS_IN):
                outs.append(list_to_string([selector(msg, TOPICS_IN, TOPICS_OUT), find_in_list(msg, TOPICS_IN)], ' '))

            # Check if the input contains a certain emote:
            if is_in_list(msg, EMOTE_IN):
                outs.append(list_to_string([selector(msg, EMOTE_IN, EMOTE_OUT), find_in_list(msg, EMOTE_IN)], ' '))
            
            # Check if the input contains a reference to UCSD:
            if is_in_list(msg, UCSD_IN):
                outs.append(list_to_string([selector(msg, UCSD_IN, UCSD_OUT), find_in_list(msg, UCSD_IN)], ' '))
            
            # We could have selected multiple outputs from the topic search above (if multiple return possible outputs)
            #   We also might have appended None in some cases, meaning we don't have a reply
            #   To deal with this, we are going to randomly select an output from the set of outputs that are not None
            options = list(filter(None, outs))
            if options:
                out_msg = random.choice(options)

        # If we don't have an output yet, but the input was a question, return msg related to it being a question
        if not out_msg and question:
            out_msg = QUESTION
        
        # If we don't have an output yet, but the input was an exclamation, return a message related
        if not out_msg and exclam:
            out_msg = EXCLAM

        # Catch-all to say something if msg not caught & processed so far
        if not out_msg:
            out_msg = random.choice(UNKNOWN)

        print('CHATBOT SAYS:', out_msg)


# In[ ]:


# Talk to our chatbot
chat()


# In[ ]:


exit_msg()

