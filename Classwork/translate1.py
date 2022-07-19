from googletrans import Translator,LANGUAGES

translator=Translator()

text=input("Enter the text you want to translate:")
source_src=translator.detect(text)

count=1
for key, value in LANGUAGES.items():
    print(f"{count}) {value}:{key}")
    count += 1

    
dest_src=input("Enter the destination language:")

for key,value in LANGUAGES.items():
    if value==dest_src:
        result=key
        print(result)


translated_text = translator.translate(text, src=source_src.lang, dest =result)
print(translated_text)

print(f"your original text: is:{text}")
print(f"your text is translate in:{LANGUAGES[result]}")
print(f"your translated text: is:{translated_text.text}")
print(f"your text is pronunciation as:{translated_text.pronunciation}")