from google import genai
from google.genai import types

client = genai.Client()

print('\nWelcome to gemini chatbot\n')

if(input('Do you want to give system instructions before chatting?(y/n): ') == 'y'):
    sys_msg = input('Type your system instructions: ')
else:
    sys_msg = 'Your a good knowledgeable person who is giving answers to what you are being asked.'


chat = client.chats.create(
    model = "gemini-3.5-flash",
    config = types.GenerateContentConfig(
        system_instruction= sys_msg
    )
)

while True:
    mssg = input('\nEnter your query:\n')

    if mssg == 'quit' or mssg == 'Quit':
        break
    
    try:
        response = chat.send_message(mssg)

        print(response.text)
    except Exception as e:
        print(f'Something went wrong {e}\n Try again.')




