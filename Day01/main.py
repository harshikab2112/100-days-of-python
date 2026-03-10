print("🎵 Welcome to the Band Name Generator! 🎵")
print("Let's create a cool band name for you.\n")

city = input("🌍 Which city did you grow up in? ").strip().title()
pet = input("🐾 What is the name of your pet? (or your future pet) ").strip().title()

band_name = f"{city} {pet}"

print("\n🎸 Generating your band name...")
print("✨ Your band name could be:", band_name, "✨")
print("\nHope you liked it! 🤘")
