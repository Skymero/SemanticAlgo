#TODO: receive document, video id, and language
# use to translate docs to english
       
       
        with open(f"transcripts/transcript_{item}.txt", "r",encoding='utf-8') as f:
            text = f.read()
            
        src_lang = language
        dest_lang = 'en'
        translator = Translator(from_lang=src_lang, to_lang=dest_lang)
        translation = translator.translate(text)
        
        with open(f"transcripts/transcript_{item}_translated.txt", "w",encoding='utf-8') as file:
            file.write(translation)
                