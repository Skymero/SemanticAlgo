import spacy

# Function to identify semantic roles in a text file
def identify_semantic_roles(file_path):
    # Load the spaCy model
    nlp = spacy.load("en_core_web_sm")
    
    # Read the content of the text file
    with open(file_path, 'r') as file:
        text = file.read()
    
    # Process the text with spaCy
    doc = nlp(text)
    
    # Dictionary to hold semantic roles and corresponding tokens
    semantic_roles = {
        'agents': [],
        'themes': [],
        'goals': [],
        'locations': [],
        'sources': [],
        'instruments': [],
        'experiencers': []
    }
    
    # Define possible semantic roles based on dependency labels
    role_labels = {
        'agents': ['nsubj', 'nsubjpass'],
        'themes': ['dobj', 'attr'],
        'goals': ['pobj', 'prep_to'],
        'locations': ['prep_in', 'prep_on', 'prep_at'],
        'sources': ['prep_from'],
        'instruments': ['prep_with'],
        'experiencers': ['nsubj']
    }
    
    # Analyze the document and identify semantic roles
    for token in doc:
        for role, labels in role_labels.items():
            if token.dep_ in labels:
                semantic_roles[role].append(token.text)
    
    return semantic_roles

# Example usage
file_path = 'transcript_bvWRMAU6V-c.txt'  # Path to your text file
semantic_roles = identify_semantic_roles(file_path)

# Print the identified semantic roles
for role, tokens in semantic_roles.items():
    print(f"{role.capitalize()}: {', '.join(tokens)}")
