# #TODO: receive document, video id, and language
# # use to translate docs to english
       
       
#         with open(f"transcripts/transcript_{item}.txt", "r",encoding='utf-8') as f:
#             text = f.read()
            
#         src_lang = language
#         dest_lang = 'en'
#         translator = Translator(from_lang=src_lang, to_lang=dest_lang)
#         translation = translator.translate(text)
        
#         with open(f"transcripts/transcript_{item}_translated.txt", "w",encoding='utf-8') as file:
#             file.write(translation)

import spacy
import os
import langdetect
from spacy.language import Language
from langdetect import detect
from googletrans import Translator
import requests
from time import sleep

# Set the extension outside the function
spacy.tokens.Doc.set_extension("translated_text", default=None, force=True)

@Language.component("translate_to_english")
def translate_to_english(doc):
    #print("UNTRANSLATED: " + doc.text)
    
    translator = Translator()
    max_retries = 3
    for attempt in range(max_retries):
        try:
            language = detect(doc.text)
            print(f"language: {language}")
            translated = translator.translate(doc.text, src=language, dest="en")
            # Set the translated text to the extension
            doc._.translated_text = translated.text
            
            break
        except requests.exceptions.RequestException as e:
            print(f"Network error: {e}")
            if attempt < max_retries - 1:
                print("Retrying...")
                sleep(2)  # Wait for 2 seconds before retrying
            else:
                print("Translation service is not available.")
                doc._.translated_text = None
        except Exception as e:
            print(f"Translation failed: {e}")
            doc._.translated_text = None
            break

    return doc
text = "estamos viajando el viernes para la playa y despues de fiesta para santurce."
nlp = spacy.load("en_core_web_lg")

if "translate_to_english" not in nlp.pipe_names:
    nlp.add_pipe("translate_to_english", last=True)

doc = nlp(text)

if doc._.translated_text:
    print("TRANSLATED: " + doc._.translated_text)
else:
    print("Translation not available.")






