import json
import os

# Default language
language = "bi"  # Options: 'hi', 'en', 'bi'

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

# Generate response based on language
def print_response(title_hi, title_en, desc_hi, desc_en, sutra_hi, sutra_en):
    print("\n🌸 श्रीराम के श्रीचरणों में समर्पित उत्तर:")
    print("🌸 In humble offering at the lotus feet of Shri Ram:\n")

    if language in ["hi", "bi"]:
        print(f"📖 विषय: {title_hi}")
    if language in ["en", "bi"]:
        print(f"📖 Topic: {title_en}\n")

    if language in ["hi", "bi"]:
        print("🪔 रामचेतना कहती है:")
        print(desc_hi)
    if language in ["en", "bi"]:
        print("🪔 RamChetna says:")
        print(desc_en)

    if language in ["hi", "bi"]:
        print(f"\n📜 सूत्र: {sutra_hi}")
    if language in ["en", "bi"]:
        print(f"📜 Principle: {sutra_en}")

    print("\n🙏 इस उत्तर को राम के स्मरण में स्वीकार करें।")

# CLI response logic
def generate_response(user_input, visions, chaupais):
    for v in visions:
        if any(tag in user_input.lower() for tag in v.get("tags", [])):
            print_response(
                v["title"],
                v.get("title_en", v["title"]),
                v["description"],
                v.get("description_en", v["description"]),
                v["example"]["ramai_response"],
                v["example"].get("ramai_response_en", v["example"]["ramai_response"])
            )
            return

    for c in chaupais:
        if any(tag in user_input.lower() for tag in c["tags"]):
            if language in ["hi", "bi"]:
                print(f"\n📖 चौपाई: {c['text']}")
                print(f"📜 अर्थ: {c['meaning']}")
            if language in ["en", "bi"]:
                print(f"\n📖 Chaupai: {c['text']}")
                print(f"📜 Meaning: {c.get('meaning_en', c['meaning'])}")
            print("\n🙏 इस उत्तर को राम के स्मरण में स्वीकार करें।")
            return

    print("\n🙏 माफ़ कीजिए, इस विषय पर रामचेतना अभी मौन है।")

# Main CLI loop
if __name__ == "__main__":
    visions = load_visions()
    chaupais = load_chaupais()
    print("🚀 RamAI CLI Loaded – Apna prashn puchhiye (exit likhkar bahar nikal sakte hain):\n")

    while True:
        user_input = input("💬 Aap: ")
        if user_input.lower() in ['exit', 'quit']:
            print("🙏 Jai Shri Ram! RamAI se milke sukh mila.")
            break

        # Handle language switch
        if user_input.lower().startswith("lang:"):
            lang_input = user_input.split(":")[1].strip()
            if lang_input in ["en", "hi", "bi"]:
                language = lang_input
                print(f"✅ Language changed to: {language.upper()}")
            else:
                print("⚠️ Unsupported language. Use 'en', 'hi', or 'bi'.")
            continue

        generate_response(user_input, visions, chaupais)
