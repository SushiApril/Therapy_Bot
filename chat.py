import openai
from keys import  chat_gpt_key
def gen(message):
    openai.api_key = chat_gpt_key

    mes = """Read the following tweets and reply in the format 'You sound xxx' where xxx is what the person sounds like for example "you sound mad", 'you sound stressed '. You can be as descriptive as you would like """
    messages = [{"role": "system", "content": mes },]

    messages.append({"role": "user", "content": message},)
    chat = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo", messages = messages
            )
    reply = chat.choices[0].message.content
    return reply
