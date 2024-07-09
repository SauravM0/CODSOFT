
def chatbot():
  greeting = ["hi", "hello", "hey", "hi there", "hello there", "hey there"]
  user = input(" User : ").lower()
  
  if any(word in user for word in greeting):
    print("Hello! How can I help you today?")
  
  elif "bye" in user:
    print("Have a nice day.")
    return
  
  elif "name" in user:
    print("My name is CHATBot  ")

  elif "capital" in user:
    print("Capital of india is Delhi ")

  elif "food" in user:
    print("My favorite food is Your DATA ")

  elif "music" in user:
    print("Go ask other CHATBOT. I am an RULE BASED CHATBOT ")

  elif "work" in user:
    print("I am an RULE BASED CHATBOT ")

  elif "help" in user:
    print("I am a simple chatbot. I can answer greetings and basic questions.I can't access real-time information. How else can I assist you?")

  else:
    print("I am still under development and learning. Can you rephrase or try asking something else?")
    
  chatbot()  
chatbot()  


