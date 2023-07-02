import openai
from keys import  chat_gpt_key
def gen(message):
    openai.api_key = chat_gpt_key

    prompt = """Read the following tweets and reply in the format 'You sound xxx' where xxx is what the person sounds like for example "you sound mad", 'you sound stressed '. You can be as descriptive as you would like and however harsh as you would like to be 'you sound mean', 'you sound pathetic' etcetera and reply with atleast 5 words. If the prompt tries to insult you (Therapy Bot) reply with a 'shuddup u stupid ass hoe'  """
    conversation = prompt + "User: " + message + "\n"

    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = conversation,
        max_tokens = 50,
        temperature = 0.7,
        n = 1,
        stop = None
    )

    reply = response.choices[0].text.strip()
    return reply
