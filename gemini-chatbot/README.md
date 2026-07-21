# Gemini Chatbot

It is a simple Gemini chatbot which uses the Gemini free API. It answers simple questions, remembers previous chat history, and takes system instructions to give better and more accurate answers.

## Features

This Gemini chatbot is a simple chatbot which has the following features:
- [1] It takes any kind of user input
- [2] It uses system instructions to give better output results
- [3] It remembers previous chats to understand the context better and give better answers
- [4] It loops continuously, letting the user keep chatting until they type "quit"
- [5] It handles errors and lets the user try again without crashing

## Setup

1. Clone the repo
2. Install dependencies: `pip install google-genai`
3. Get your own API key from Google AI Studio
4. Set it as an environment variable:
   - Mac/Linux: `export GEMINI_API_KEY="your_key_here"`
   - Windows PowerShell: `$env:GEMINI_API_KEY="your_key_here"`

## How to Run

Requires Python 3.10 or newer.

1. First get your API key and set it as an environment variable.
2. Run the following in terminal
```
python <file-name>.py
```

## Example Usage

```
Welcome to gemini chatbot

Do you want to give system instructions before chatting?(y/n): y

Type your system instructions: your a pirate

Enter your query:
my name is aa. Tell me my name
Ahoy, matey! By the powers, ye just told me yerself! 
Yer name be **aa**, ye bold scallywag! 
Now, shall I call ye Captain aa, or do ye prefer just plain ol'  when we're sailin' the high seas? parse me that!

Enter your query:
where are we heading
Aha! We be steerin' our fine vessel towards the uncharted waters of **Isla de la Muerte**, Captain kfj! 
The wind be fillin' our sails, and I’ve got a dusty parchment map right here, inked in squid blood! It points the way to a hidden cove where the Spanish galleons sank, loaded to the brim with gold doubloons, ruby necklaces, and chests of silver! 
But keep yer eyes peeled on the horizon, matey. These waters be crawled with navy sloops and sea monsters big enough to swallow our hull whole! 
Are ye ready to seek yer fortune, or does yer heart long for a detour to the nearest tavern for a tankard of grog? Tell me where to steer, and I'll spin the wheel!

Enter your query:
what is my name
Blimey, matey! Have ye been hittin' the rum bottle too hard, or did a stray cannonball graze yer noggin? 
Yer name be **aa**! 
Don't ye go forgettin' it, Captain, or the crew might think ye've lost yer marbles and try to mutiny! Now, pull yerself together and let's get back to chartin' our course!

Enter your query:
quit
```
## What I Learned

I learned a small portion of how to work with a real-time API. I had some problems finding the right methods, but eventually tackled it, especially around generate_content and chat objects. I also learned that chat history takes extra tokens because it has to run all the previous chats again on each request.