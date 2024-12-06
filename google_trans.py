from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def translate_text():
    try:
        source_lang = comb_sor.get()
        target_lang = comb_dest.get()

        src_code = lang_map[source_lang]
        dest_code = lang_map[target_lang]

        text_to_translate = src_txt.get(1.0, END).strip()
        if not text_to_translate:
            dest_txt.delete(1.0, END)
            dest_txt.insert(END, "Please enter text to translate!")
            return

        translator = Translator()
        translated = translator.translate(text_to_translate, src=src_code, dest=dest_code)
        dest_txt.delete(1.0, END)
        dest_txt.insert(END, translated.text)
    except Exception as e:
        dest_txt.delete(1.0, END)
        dest_txt.insert(END, f"Error: {str(e)}")

lang_map = {v.title(): k for k, v in LANGUAGES.items()}
lang_names = sorted(lang_map.keys())

root = Tk()
root.title("TransGenie")
root.geometry("700x750")
root.config(bg="#F7F7F7")

title_label = Label(
    root, 
    text="🌍 VociVerse 🌍", 
    font=("Helvetica", 24, "bold"), 
    bg="#F7F7F7", 
    fg="#34495E"
)
title_label.pack(pady=20)

# Source Text Box
src_label = Label(root, text="Enter Text:", font=("Helvetica", 14), bg="#F7F7F7", fg="#34495E")
src_label.pack(pady=5)
src_txt = Text(root, font=("Helvetica", 14), wrap=WORD, height=10, width=60, bd=2, relief=GROOVE)
src_txt.pack(pady=10)

frame = Frame(root, bg="#F7F7F7")
frame.pack(pady=10)

comb_sor = ttk.Combobox(frame, values=lang_names, font=("Helvetica", 12), state="readonly", width=20)
comb_sor.set("English")
comb_sor.grid(row=0, column=0, padx=10)

translate_btn = Button(
    frame, 
    text="Translate ➡️", 
    font=("Helvetica", 14, "bold"), 
    bg="#2ECC71", 
    fg="white", 
    command=translate_text, 
    relief=RAISED, 
    bd=3
)
translate_btn.grid(row=0, column=1, padx=10)

comb_dest = ttk.Combobox(frame, values=lang_names, font=("Helvetica", 12), state="readonly", width=20)
comb_dest.set("Hindi")
comb_dest.grid(row=0, column=2, padx=10)

dest_label = Label(root, text="Translated Text:", font=("Helvetica", 14), bg="#F7F7F7", fg="#34495E")
dest_label.pack(pady=5)
dest_txt = Text(root, font=("Helvetica", 14), wrap=WORD, height=10, width=60, bd=2, relief=GROOVE)
dest_txt.pack(pady=10)

footer_label = Label(root, text="© 2024 VociVerse", font=("Helvetica", 10), bg="#F7F7F7", fg="#34495E")
footer_label.pack(side=BOTTOM, pady=10)


root.mainloop()
