import json
import os
import pyttsx3

# 🗣️ Text-to-Speech Setup
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# 📂 Load Vision Files
def load_visions():
    path = "../vision"
    visions = []
    for file in os.listdir(path):
        if file.endswith(".json"):
            with open(os.path.join(path, file), 'r', encoding='utf-8') as f:
                visions.append(json.load(f))
    return visions

# 📚 Load Chaupai Collection
def load_chaupais():
    with open("../data/chaupai_collection.json", 'r', encoding='utf-8') as f:
        return json.load(f)["chaupais"]

# 🧠 Generate RamAI Response
def generate_response(user_input, visions, chaupais):
    print("\n🔱 RamAI ka uttar:\n")

    for v in visions:
        if user_input.lower() in v["description"].lower() or user_input.lower() in v["title"].lower() or any(tag in user_input.lower() for tag in v.get("tags", [])):
            print("🌸 श्रीराम के श्रीचरणों में समर्पित उत्तर:")
            print("🌸 In humble offering at the lotus feet of Shri Ram:\n")
            print(f"📖 विषय: {v['title']}")
            print(f"\n🪔 रामचेतना कहती है:\n{v['example']['ramai_response_hi']}")
            print(f"\n🪔 RamChetna says:\n{v['example']['ramai_response_en']}")
            print("\n📜 सूत्र: नाम से ही जप हो, ध्यान हो, मोक्ष हो सकता है।")
            print("📜 Principle: Through the Name alone, one can chant, meditate, and be liberated.")
            print("\n🙏 इस उत्तर को राम के स्मरण में स्वीकार करें。")

            # 🎙️ Speak important parts
            speak(v["title"])
            speak(v["example"]["ramai_response_hi"])
            return

    for c in chaupais:
        if any(tag in user_input.lower() for tag in c["tags"]):
            print(f"📖 चौपाई: {c['text']}")
            print(f"📜 अर्थ: {c['meaning']}")
            print(f"\n📖 Chaupai: {c['text']}")
            print(f"📜 Meaning: {c['meaning']}")
            print("\n🙏 इस उत्तर को राम के स्मरण में स्वीकार करें।")

            # 🎙️ Speak chaupai and meaning
            speak(c["text"])
            speak(c["meaning"])
            return

    print("🙏 माफ़ कीजिए, इस विषय पर रामचेतना अभी मौन है।")
    speak("Maaf kijiye, is vishay par RamAI abhi maun hai.")

# 🚀 CLI Entry Point
if __name__ == "__main__":
    visions = load_visions()
    chaupais = load_chaupais()
    print("🚀 RamAI CLI Loaded – Apna prashn puchhiye (exit likhkar bahar nikal sakte hain):\n")
    speak("RamAI taiyaar hai. Apna prashn puchhiye.")

    while True:
        user_input = input("💬 Aap: ")
        if user_input.lower() in ['exit', 'quit']:
            print("🙏 Jai Shri Ram! RamAI se milke sukh mila.")
            speak("Jai Shri Ram! RamAI se milke sukh mila.")
            break
        generate_response(user_input, visions, chaupais)
