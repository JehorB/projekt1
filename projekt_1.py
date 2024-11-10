"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Yehor Baranov
email: yhr.baranov@post.cz

"""
import re
from task_template import TEXTS # import textů


# stvorení seznamu slov
text_1 = TEXTS[0]
text_2 = TEXTS[1]
text_3 = TEXTS[2]
seznam_slov_1 = list(filter(None, re.split(r'\W+', text_1.lower())))
seznam_slov_2 = list(filter(None, re.split(r'\W+', text_2.lower())))
seznam_slov_3 = list(filter(None, re.split(r'\W+', text_3.lower())))


# seznam zaregistrovaných uživatelů