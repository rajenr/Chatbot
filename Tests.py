#!/usr/bin/env python
# coding: utf-8

# In[15]:


def is_question(input_string):
    output = False
    if (input_string.find('?') != -1):
      output = True
    else:
        output = False
    return output


# In[16]:


def is_exclam(input_string):
    output = False
    if (input_string.find('!') != -1):
        output = True
    else:
        output = False
    return output


# In[20]:


assert callable(is_question)
assert isinstance(is_question('abc'), bool)
assert is_question('what?') == True
assert is_question('what') == False


# In[21]:


assert callable(is_exclam)
assert isinstance(is_exclam('abc'), bool)
assert is_exclam('wow!') == True
assert is_exclam('wow') == False

