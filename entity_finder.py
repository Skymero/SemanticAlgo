import spacy
import os

def check_new_filename(new_filename):
    """
    Check if the new filename is valid.
    
    Args:
        new_filename (str): The new filename to check.
    
    Returns:
        bool: True if the filename is valid, False otherwise.
    """
    # Check if the filename is not empty
    if not new_filename:
        print("Error: New filename is empty.")
        return False
    
    # Check if the filename has a valid extension
    if not new_filename.endswith(".txt"):
        print("Error: New filename must have a .txt extension.")
        return False
    
    # Check if the filename already exists
    if os.path.exists(new_filename):
        print("Error: New filename already exists.")
        return False
    
    return True


def entity_finder(doc, transcript_name):
    seen_entities = set()

    with open(transcript_name, "w", encoding='utf-8') as file:
        for ent in doc.ents:
            if ent.label_ != "QUANTITY" and ent.label_ != "MONEY" and ent.label_ != "DATE" and ent.label_ != "TIME" and ent.label_ != "CARDINAL" and ent.label_ != "LANGUAGE" and ent.label_ != "PERCENT" and ent.label_ != "ORDINAL":
                #########################################################
                entity_pos = [token.pos_ for token in ent]

                    # Get the previous token (if it exists)
                if ent.start > 0:
                    prev_token = doc[ent.start - 1]
                    prev_pos = prev_token.pos_
                    prev_word = prev_token.text
                else:
                    prev_pos = None
                    prev_word = None


                    # Get the next token (if it exists)
                if ent.end < len(doc):
                    next_token = doc[ent.end]
                    next_pos = next_token.pos_
                    next_word = next_token.text
                else:
                    next_pos = None
                    next_word = None

                
                #########################################################
                if ent.text not in seen_entities:
                    sentence_text = ent.sent.text
                    entity_text = doc[ent.start:ent.end].text
                    seen_entities.add(entity_text)
                    

                    # if (entity_pos == 'ADJ' or entity_pos == 'NOUN') and len(entity_pos) == 1:
                    #     if prev_pos == 'ADJ' or prev_pos == 'NOUN':
                    #         entity_text = prev_word + ' ' + entity_text
                    #     elif next_pos == 'ADJ' or next_pos == 'NOUN':
                    #         entity_text = entity_text + ' ' + next_word

                    if prev_pos in ['ADJ', 'NOUN', 'PROPN']:
                        entity_text = prev_word + ' ' + entity_text
                    elif next_pos in ['ADJ', 'NOUN', 'PROPN']:
                        entity_text = entity_text + ' ' + next_word
                        

                    file.write(f"Entity POS count: {len(entity_pos)}\n")
                    # print(f"Entity: {entity_text} | ({ent.label_})")
                    # print(f"Entity POS: {entity_pos}")
                    # print(f"Previous Word: {prev_word} | POS: {prev_pos}")
                    # print(f"Next Word: {next_word} | POS: {next_pos}")
                    
                    file.write(f"Entity: {entity_text}\n")
                    file.write(f"Entity POS: {entity_pos}\n")
                    file.write(f"Previous Word: {prev_word} | POS: {prev_pos} \n")
                    file.write(f"Next Word: {next_word} | POS: {next_pos} \n")
                    file.write(f"Context: {sentence_text}\n")


                    file.write(f"\n")
                    # print(f"Context: {sentence_text}")
                    
            else:
                continue

def main():
    # Load the English model
    nlp = spacy.load("en_core_web_lg")

    folder_path = 'C:\\Users\\MartinezR\\SemanticAlgo\\transcripts'
    new_folder_path = 'C:\\Users\\MartinezR\\SemanticAlgo\\entities'

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            new_filename = f'entity_{filename}'
            new_file_path = os.path.join(new_folder_path, new_filename)
            old_filepath = os.path.join(folder_path, filename)

            with open(old_filepath, 'r', encoding='utf-8') as file:
                text = file.read()

            doc = nlp(text)
            if check_new_filename(new_file_path) == True:
                entity_finder(doc, new_file_path)


if __name__ == "__main__":
    main()





# file_path = 'transcripts\\transcript_IwBYnjVubW4.txt' 
# with open(file_path, 'r', encoding='utf-8') as file:
#     text = file.read()

# doc = nlp(text)
