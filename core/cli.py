import json
import os

# Global language setting (default is Hindi)
language = "hi"

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
    global language

    if user_input.strip().lower() == "lang: en":
        language = "en"
        print("\n🌐 Language set to English.\n")
        return
    elif user_input.strip().lower() == "lang: hi":
        language = "hi"
        print("\n🌐 भाषा हिंदी में बदल गई है।\n")
        return

    print("\n🔱 RamAI ka uttar:\n")

    # Check in vision files
    for v in visions:
        if user_input.lower() in v.get("title", "").lower() or user_input.lower() in v.get("description", "").lower():
            if language == "hi":
                print(f"🌸 श्रीराम के श्रीचरणों में समर्पित उत्तर:\n")
                print(f"📖 विषय: {v['title']}")
                print(f"🪔 रामचेतना कहती है:\n{v['description']}")
                print(f"\n📜 सूत्र: {v['example']['ramai_response']}")
                print("\n🙏 इस उत्तर को राम के स्मरण में स्वीकार करें।")
            else:
                print(f"🌸 In humble offering at the lotus feet of Shri Ram:\n")
                print(f"📖 Topic: {v.get('title_en', v['title'])}")
                print(f"🪔 RamChetna says:\n{v.get('description_en', v['description'])}")
                print(f"\n📜 Principle: {v['example'].get('ramai_response_en', v['example']['ramai_response'])}")
                print("\n🙏 Accept this in remembrance of Ram.")
            return

    # Check in chaupai collection
    for c in chaupais:
        if any(tag in user_input.lower() for tag in c["tags"]):
            if language == "hi":
                print(f"📖 चौपाई: {c['text']}")
                print(f"📜 अर्थ: {c['meaning']}")
                print("\n🙏 इस उत्तर को राम के स्मरण में स्वीकार करें।")
            else:
                print(f"📖 Chaupai: {c['text']}")
                print(f"📜 Meaning: {c.get('meaning_en', c['meaning'])}")
                print("\n🙏 Accept this in remembrance of Ram.")
            return

    # Default response
    if language == "hi":
        print("🙏 माफ़ कीजिए, इस प्रश्न का उत्तर RamAI के पास अभी नहीं है।")
    else:
        print("🙏 Sorry, RamAI does not yet have an answer for this query.")

# Main loop
if __name__ == "__main__":
    visions = load_visions()
    chaupais = load_chaupais()
    print("🚀 RamAI CLI Loaded – Apna prashn puchhiye (use 'lang: en' or 'lang: hi' to switch language):\n")
    while True:
        user_input = input("💬 Aap: ")
        if user_input.lower() in ['exit', 'quit']:
            print("🙏 Jai Shri Ram! RamAI se milke sukh mila.")
            break
        generate_response(user_input, visions, chaupais)
