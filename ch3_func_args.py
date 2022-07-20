def user_info(name, age, city):
    '''This function prints name, age, and city from 
    an argument provided to the function.'''
    
    print(f"{name} is {age} years old, from {city}.")
    
    
user_info("Janet", 58, "Oklahoma City")
#23 is New York years old, from 56.
user_info(23, "New York", 56) 
'''23 is New York years old, from 56.'''

def user_info_default_args(name, age = 0, city = "Tucson"):
    print(f"{name} is {age} years old, from {city}.")


user_info_default_args("Micah")
"""
You don't need to follow the positional order of the argument.
You can adjust that and provide it as you want.
As long as you have a default specified for anything you're not providing,
you will be able to overwrite the values of the defaults that you do provide and any arguments that are required,
of course you'll need to provide as well.
"""
user_info_default_args(age=56, name="Kadeem")


# *args
"""
*args
contents: allows for unlimited variables to be passed into a function without defining them ahead of time

def add(*args):
    print(sum(args))


add(2,3,4)
add(3,2,4,2,5,3)
"""

# **kwargs
"""
**kwargs
contents allows for unlimited keyword arguments to be passed into a function without defining them ahead of time

def application(**kwargs):
    print(**kwargs)
"""

# Combining arg types
"""
All three argument types can be used in a single function. They must be used in order: formal positional arguments, *args, **kwargs

def application(fname, lname, email, company, *args, **kwargs):
    print(f"{fname} {lname} works at {company}. Her email is {email}.")
    
    
application("Jess", "Ingrass", "mail @ mail.com", "TeachCode.org", 75000, hire_date = "September 2010")
    
"""


def application(fname, lname, email, company, *args, **kwargs):
    print(f"{fname} {lname} works at {company}. Her email is {email}.")
    
    
application("Jess", "Ingrass", "mail @ mail.com", "TeachCode.org", 75000, hire_date = "September 2010")


