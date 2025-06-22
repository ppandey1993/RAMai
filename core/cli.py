import json
import os

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
            print(f"📖 {v['title']}: {v['description']}")
            print(f"🕊️ RamAI bolta hai: {v['example']['ramai_response']}")
            return
    for c in chaupais:
        if any(tag in user_input.lower() for tag in c["tags"]):
            print(f"🪔 Chaupai: {c['text']}")
            print(f"📜 Arth: {c['meaning']}")
            return
    print("🙏 Maaf kijiye, is prashn ka uttar RamAI ke paas abhi nahi hai.")

# Main loop
if _name_ == "_main_":
    visions = load_visions()
    chaupais = load_chaupais()
    print("🚀 RamAI CLI Loaded – Apna prashn puchhiye (exit likhkar bahar nikal sakte hain):\n")
    
    while True:
        user_input = input("💬 Aap: ")
        if user_input.lower() in ['exit', 'quit']:
            print("🙏 Jai Shri Ram! RamAI se milke sukh mila.")
            break
