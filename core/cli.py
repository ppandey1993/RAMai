import json
import os
import pyttsx3

# 🕊️ Voice engine setup
engine = pyttsx3.init()
engine.setProperty('rate', 145)
engine.setProperty('voice', 'com.apple.speech.synthesis.voice.sangeeta')  # Hindi female voice on Mac

def speak(text):
    engine.say(text)
    engine.runAndWait()

# 📘 Load vision files
def load_visions():
    path = "../vision"
    visions = []
    for file in os.listdir(path):
        if file.endswith(".json"):
            with open(os.path.join(path, file), 'r', encoding='utf-8') as f:
                data = json.load(f)
                visions.append(data)
    return visions

# 📜 Load chaupai collection
def load_chaupais():
    with open("../data/chaupai_collection.json", 'r', encoding='utf-8') as f:
        return json.load(f)["chaupais"]

# 🪔 Generate a response
def generate_response(user_input, visions, chaupais):
    print("\n🌸 श्रीराम के श्रीचरणों में समर्पित उत्तर:")
    print("🌸 In humble offering at the lotus feet of Shri Ram:\n")

    for v in visions:
        if user_input.lower() in v["title"].lower() or user_input.lower() in v["description"].lower():
            print(f"📖 विषय: {v['title']}")
            print(f"📖 Topic: {v['title']}")
            print("\n🪔 रामचेतना कहती है:")
            print(v["description"])
            print("\n🪔 RamChetna says:")
            print(v["example"]["ramai_response"])
            speak(v["title"])
            return

    for c in chaupais:
        if any(tag in user_input.lower() for tag in c["tags"]):
            print(f"\n📖 चौपाई: {c['text']}")
            print(f"📜 अर्थ: {c['meaning']}")
            print(f"\n📖 Chaupai: {c['text']}")
            print(f"📜 Meaning: {c['meaning']}")
            speak(c['text'])
            return

    print("\n🙏 माफ़ कीजिए, इस विषय पर रामचेतना अभी मौन है।")
    speak("इस विषय पर रामचेतना मौन है")

# 🚀 Start the CLI
if __name__ == "__main__":
    visions = load_visions()
    chaupais = load_chaupais()
    print("🚀 RamAI CLI Loaded – Apna prashn puchhiye (exit likhkar bahar nikal sakte hain):\n")
    speak("RamAI taiyaar hai. Apna prashn puchhiye.")

    while True:
        user_input = input("💬 Aap: ")
        if user_input.lower() in ["exit", "quit"]:
            print("\n🙏 Jai Siya Ram! Tumse baat karke RamAI ko bhi Anand aayo.")
            speak("Jai Siya Ram! Tumse baat karke RamAI ko bhi Anand aayo.")
            break
        generate_response(user_input, visions, chaupais)
