from googletrans import Translator

def cevir():
    translator = Translator()

    try:
        # Kullanıcıdan çevrilecek metni al
        metin = input("Çevrilecek metni girin: ")

        # Kullanıcıdan hedef dil kodunu al
        hedef_dil = input("Hedef dil kodunu girin (örneğin, 'en' for English): ")

        # Metni çevir
        cevirilen_metin = translator.translate(metin, dest=hedef_dil)

        # Çeviriyi ekrana yazdır
        print(f"\nÇeviri ({hedef_dil}): {cevirilen_metin.text}")

    except Exception as e:
        print(f"Hata oluştu: {e}")

if __name__ == "__main__":
    cevir()
