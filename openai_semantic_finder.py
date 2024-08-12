import openai
import os

# OPENAI_API_KEY = ''
# client = OpenAI(
#     api_key=os.environ['OPENAI_API_KEY'],
# )

# # Set your OpenAI API key
# openai.api_key = ""



def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# def find_semantic_agents(text):
    # This function is going to ask OpenAI's API to analyze a text and extract information about the roles of people, places, and things mentioned in the text.

    # The 'prompt' is a message that we send to the API to guide it on what we want it to do. It's like a recipe for the API.
    # In this case, the prompt is telling the API to do the following:
    # - Analyze a document that discusses various topics
    # - Identify all semantic roles, including direct and indirect agents, themes, goals, locations, sources, instruments, and experiencers
    # - Generate a list of search terms for each identified semantic role that will help us find more information about those topics

    # After we send the prompt to the API, we need to make a request to the API to get a response.
    # The API will generate a response based on the prompt and the context of the text we gave it.
    # The response will be in the form of a list of search terms for each semantic role that the API identified in the text.

    # The API request looks like this:
    # response = openai.Completion.create(
    #     engine="text-davinci-003",  # This is the name of the model that the API will use to generate the response.
    #     prompt=prompt,  # This is the message that guides the API on what to do.
    #     max_tokens=500,  # This is the maximum number of tokens that the API is allowed to generate in the response.
    #     temperature=0.3,  # This is a parameter that controls how 'creative' the API's response is. Lower values make the API more deterministic, while higher values make it more random.
    # )

    # After we get the response from the API, we can use it to search for more information about the topics mentioned in the text.
    # The API has generated a list of search terms for each semantic role that it identified in the text.
    # We can use these search terms to search for more information about the topics discussed in the text.
    # For example, if the API identified a theme as "climate change", we can use the search term "climate change" to search for more information about that topic.

    # The response from the API will be in the form of a string.
    # We can access this string by calling response.choices[0].text.
    # The [0] is because the API can generate multiple responses, and we are only interested in the first one.
    # The .strip() method is used to remove any leading or trailing whitespace from the response string.
def find_semantic_agents(text):
    openai.api_key = ""
    # client = OpenAI(
    #     api_key=os.environ['OPENAI_API_KEY'],
    # )
    # client = OpenAI()
    
    # Craft the prompt
    prompt = (
        "You are a linguist and an analyst. I have a document that discusses various topics. Please analyze the document and identify all semantic roles, including direct and indirect agents, themes, goals, locations, sources, instruments, and experiencers. Then, generate a list of search terms for each identified semantic role that will help me find more information about those topics."
    )

    # Make the API request
    model = openai.Model("text-davinci-003")
    response = openai.Completion.create(
        prompt=prompt,
        max_tokens=500,  # Adjust according to the text length
        temperature=0.3,  # Lower temperature for more deterministic output
    )


    return response.choices[0].text.strip()

def main():
    # Load the text from a file
    file_path = 'transcripts\\transcript_IwBYnjVubW4.txt'
    text = load_text(file_path)

    # Find semantic agents
    agents = find_semantic_agents(text)

    # Print the results
    print("Semantic Agents and Actions:")
    print(agents)


if __name__ == "__main__":
    main()

