import pyttsx3
from PyPDF2 import PdfReader


engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
current_speech_rate = engine.getProperty("rate")
engine.setProperty("rate", 150)
volume = engine.getProperty('volume')
engine.setProperty('volume', 1.0)

start_page = int(input("Enter the page number: "))


with open("C:\\Users\\shaik\\Downloads\\Books\\10. Wireshark.pdf", "rb") as file:
    reader = PdfReader(file)
    total_pages = len(reader.pages)
    print(f"Total Pages: {total_pages}")

    if start_page < 1 or start_page > total_pages:
        print("Invalid page number")
    else:

        for page_num in range(start_page - 1, total_pages):
            page = reader.pages[page_num]
            text = page.extract_text()
            if text:
                print(f"Reading Page {page_num + 1}")
                engine.say(text)
                engine.runAndWait()
