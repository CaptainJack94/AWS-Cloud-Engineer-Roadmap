import json

def moderate_message(text):
    if "spam" in text.lower():
        return "BLOCKED"
    return "CLEAN"

with open('data.json', 'r') as my_file:
    chat_log = json.load(my_file)

print(f"{'STATUS':10} | {'USERNAME':10} | MESSAGE") 
print("-" * 40)
   
for chat in chat_log:
    username = chat["username"]
    message = chat["message"]
    moderation_result = moderate_message(message)
    print(f"{moderation_result:10} | {username:10} | {message}")