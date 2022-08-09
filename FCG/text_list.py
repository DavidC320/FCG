# 9/7/2022

from random import choice

start = (
    "",
    "Hello",
    "something came in the mail today",
    "Where is the garbage can",  #
    "Watch out!",  #
    "I need to tell you something",
    "Have I ever told you a story",
    "There is something in the closet"
)

middle = (
    "",
    "There is something outside",
    "look in the box",
    "Do you see it?",
    "Something very funny",
    "I think it's coming",  #
    "Grandma?",  #
    "There is a secret I haven't told you.",
    "You will see me difrently after this.",
    "Once upon a time in a very distant land.",
    "There was a phesant.",
    "I can hear laughter.",
    "There is creaking every night."
)

end = (
    "It's freddy fazebear",
    "Bazinga",
    "the mail",
    "you like sish soap... right?",
    "I'm just dinking my moik",  #
    "Purple Guy!",  #
    "I'm you!",
    "That's how I met you",
    "Is that the world famous character from the popular indie game developed by Toby Fox, Sans Undertale"
)

codes = (
    "",
)

def grab_text(num):
    
    num_to_list = {
        0 : "str",
        1 : "mid",
        2 : "mid",
        3 : "end",
    }

    list_type = num_to_list.get(num)

    if list_type == "str":
        return choice(start)
    elif list_type == "mid":
        return choice(middle)
    elif list_type == "end":
        return choice(end)