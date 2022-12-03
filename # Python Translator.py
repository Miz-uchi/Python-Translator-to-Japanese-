# Python Translator to Japanese 
#

from googletrans import Translator 

tl =  Translator()

text = input ('Insert your Text:')

res = tl.translate(text,dest='ja')

print(res.text)