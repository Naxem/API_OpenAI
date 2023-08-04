import chatgpt
import sys

def mainF():
    chatgpt.start_assisant()
    chatgpt.create_message(user_input)
    chatgpt.chatgptF()

if len(sys.argv) > 1:
    user_input = sys.argv[1]
    mainF()