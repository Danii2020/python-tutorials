from googletrans import Translator

translator = Translator()

while True:
    src_word = input("Ingresa la frase o palabra: ")
    if src_word == 'q':
        break
    dest_lang = input("Ingresa el idioma a traducir en siglas: ")
    if dest_lang == 'q':
        break
    translation = translator.translate(text=src_word, dest=dest_lang)
    print(f"{src_word} -> {translation.text}")

