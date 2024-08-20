import spacy

# Load the English model
nlp = spacy.load("en_core_web_sm")

# text = "Apple is looking at buying U.K. startup for $1 billion"

file_path = 'transcripts\\transcript_IwBYnjVubW4.txt' 
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

doc = nlp(text)

seen_entities = set()

for ent in doc.ents:
    if ent.label_ != "QUANTITY" and ent.label_ != "MONEY" and ent.label_ != "DATE" and ent.label_ != "TIME" and ent.label_ != "CARDINAL" and ent.label_ != "LANGUAGE" and ent.label_ != "PERCENT" and ent.label_ != "ORDINAL":

        if ent.text not in seen_entities:
            sentence_text = ent.sent.text
            entity_text = doc[ent.start:ent.end].text
            seen_entities.add(entity_text)
            print(f"Non-person entity: {entity_text} | ({ent.label_})")
            print(f"Context: {sentence_text}")
    else:
        continue
