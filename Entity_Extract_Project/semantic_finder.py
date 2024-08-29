# import spacy

# # Function to identify semantic roles in a text file
# def identify_semantic_roles(file_path):
#     # Load the spaCy model
#     nlp = spacy.load("en_core_web_sm")
    
#     # Read the content of the text file
#     with open(file_path, 'r') as file:
#         text = file.read()
    
#     # Process the text with spaCy
#     doc = nlp(text)
    
#     # Dictionary to hold semantic roles and corresponding tokens
#     semantic_roles = {
#         'agents': [],
#         'themes': [],
#         'goals': [],
#         'locations': [],
#         'sources': [],
#         'instruments': [],
#         'experiencers': []
#     }
    
#     # Define possible semantic roles based on dependency labels
#     role_labels = {
#         'agents': ['nsubj', 'nsubjpass'],
#         'themes': ['dobj', 'attr'],
#         'goals': ['pobj', 'prep_to'],
#         'locations': ['prep_in', 'prep_on', 'prep_at'],
#         'sources': ['prep_from'],
#         'instruments': ['prep_with'],
#         'experiencers': ['nsubj']
#     }
    
#     # Analyze the document and identify semantic roles
#     for token in doc:
#         for role, labels in role_labels.items():
#             if token.dep_ in labels:
#                 semantic_roles[role].append(token.text)
    
#     return semantic_roles

# spacy.cli.download("en_core_web_sm")
# # Example usage
# file_path = 'transcripts\\transcript_HXXoO0FwUKQ.txt'  # Path to your text file
# semantic_roles = identify_semantic_roles(file_path)

# # Print the identified semantic roles
# for role, tokens in semantic_roles.items():
#     print(f"{role.capitalize()}: {', '.join(tokens)}")
import spacy

# Function to identify semantic roles in a text file
def identify_semantic_roles(file_path):
    # Load the spaCy model
    nlp = spacy.load("en_core_web_sm")
    
    # Read the content of the text file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Process the text with spaCy
    doc = nlp(text)
    
    # Dictionary to hold semantic roles and corresponding tokens
    semantic_roles = {
        'direct_agents': [],
        'indirect_agents': [],
        'themes': [],
        'goals': [],
        'locations': [],
        'sources': [],
        'instruments': [],
        'experiencers': []
    }
    
    # Define custom rules to identify semantic roles
    for token in doc:
        # Direct Agent: Subject of the sentence
        if token.dep_ in ('nsubj', 'nsubjpass'):
            semantic_roles['direct_agents'].append(token.text)
        
        # Indirect Agent: Indirect object (often follows 'to' or 'for')
        if token.dep_ == 'dative' or (token.dep_ == 'pobj' and token.head.text in ['to', 'for']):
            semantic_roles['indirect_agents'].append(token.text)
        
        # Theme: Direct object
        if token.dep_ in ('dobj', 'attr'):
            semantic_roles['themes'].append(token.text)
        
        # Goal: Prepositional object with 'to' or 'for'
        if token.dep_ == 'pobj' and token.head.text in ['to', 'for']:
            semantic_roles['goals'].append(token.text)
        
        # Location: Prepositional object with locative prepositions
        if token.dep_ == 'pobj' and token.head.text in ['in', 'on', 'at']:
            semantic_roles['locations'].append(token.text)
        
        # Source: Prepositional object with 'from'
        if token.dep_ == 'pobj' and token.head.text == 'from':
            semantic_roles['sources'].append(token.text)
        
        # Instrument: Prepositional object with 'with'
        if token.dep_ == 'pobj' and token.head.text == 'with':
            semantic_roles['instruments'].append(token.text)
        
        # Experiencer: Subject experiencing the action (usually a human)
        if token.dep_ == 'nsubj' and token.ent_type_ == 'PERSON':
            semantic_roles['experiencers'].append(token.text)

    # Refactor the semantic roles dictionary to have unique lists of tokens for each role
    # Use a dictionary comprehension to create a new dictionary with the same keys as the original dictionary
    # For each key-value pair in the original dictionary, create a new key-value pair in the new dictionary 
    # with the same key and the corresponding value converted to a list
    semantic_roles = {role: list(tokens) for role, tokens in semantic_roles.items()}

    
    return semantic_roles

# Example usage
file_path = 'transcripts\\transcript_IwBYnjVubW4.txt'  # Path to your text file
semantic_roles = identify_semantic_roles(file_path)

# Print the identified semantic roles
for role, tokens in semantic_roles.items():
    print(f"{role.capitalize().replace('_', ' ')}: {', '.join(tokens)}")
