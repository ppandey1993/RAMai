import json
import os
import pyttsx3

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 140)  # Speed
engine.setProperty('volume', 1.0)  # Max volume

# Optionally set a voice that supports Hindi (depends on OS)
voices = engine.getProperty('voices')
for voice in voices:
    if 'hi' in voice.languages or 'Hindi' in voice.name:
        engine.setProperty('voice', voice.id)
        break

def speak_response(title, description, response):
    full_text = f"{title}. {description}. RamAI bolta hai: {response}. Jai Shri Ram."
    engine.say(full_text)
    engine.runAndWait()

def speak_chaupai(text, meaning):
    full_text = f"Chaupai: {text}. Arth: {meaning}. Jai Shri Ram."
    engine.say(full_text)
    engine.runAndWait()

# Load vision files
def load_visions():
    path = "../vision"
    visions = []
    for file in os.listdir(path):
        if file.endswith(".json"):
            with open(os.path.join(path, file), 'r', encoding='utf-8') as f:
                visions.append(json.load(f))
    return visions

# Load chaupai collection
def load_chaupais():
    with open("../data/chaupai_collection.json", 'r', encoding='utf-8') as f:
        return json.load(f)["chaupais"]

# Respond to input
def generate_response(user_input, visions, chaupais):
    print("\n🔱 RamAI ka uttar:\n")
    for v in visions:
        if user_input.lower() in v["description"].lower() or user_input.lower() in v["title"].lower():
            print(f"📖 विषय: {v['title']}")
            print(f"\n🪔 रामचेतना कहती है:\n{v['description']}")
            print(f"\n🕊️ RamAI bolta hai: {v['example']['ramai_response']}")
            print("\n🙏 इस उत्तर को राम के स्मरण में स्वीकार करें।")
            speak_response(v['title'], v['description'], v['example']['ramai_response'])
            return

    for c in chaupais:
        if any(tag in user_input.lower() for tag in c["tags"]):
            print(f"📖 चौपाई: {c['text']}")
            print(f"📜 अर्थ: {c['meaning']}")
            print(f"\n📖 Chaupai: {c['text']}")
            print(f"📜 Meaning: {c['meaning']}")
            print("\n🙏 इस उत्तर को राम के स्मरण में स्वीकार करें।")
            speak_chaupai(c['text'], c['meaning'])
            return

    print("🙏 माफ़ कीजिए, इस विषय पर रामचेतना अभी मौन है।")
    engine.say("Maaf kijiye, is vishay par Ram Chetna abhi maun hai.")
    engine.runAndWait()

# Main loop
if __name__ == "__main__":
    visions = load_visions()
    chaupais = load_chaupais()
    print("🚀 RamAI CLI Loaded – Apna prashn puchhiye (exit likhkar bahar nikal sakte hain):\n")
    while True:
        user_input = input("💬 Aap: ")
        if user_input.lower() in ['exit', 'quit']:
            print("🙏 Jai Shri Ram! RamAI se milke sukh mila.")
            engine.say("Jai Shri Ram! RamAI se milke sukh mila.")
            engine.runAndWait()
            break
        generate_response(user_input, visions, chaupais)
