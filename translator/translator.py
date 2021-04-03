# To Print all the languages that google
# translator supports
import googletrans
  
  
print(googletrans.LANGUAGES)

#pip install translate


from translate import Translator
translator= Translator(to_lang="German")
translation = translator.translate("Good Morning!")
print translation
