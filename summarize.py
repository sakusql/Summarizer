import tkinter as tk
from tkinter import messagebox
import openai

openai.api_key = 'votre clé api openai'

def summarize():
    article_text = entry.get()
    if article_text:
        try:
            summary = summarize_text(article_text)

            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, summary)
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors du résumé : {e}")
    else:
        messagebox.showwarning("Entrée manquante", "Veuillez entrer un texte ou un lien d'article.")

def summarize_text(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Tu es un assistant qui résume des articles."},
            {"role": "user", "content": f"Peux-tu résumer cet article : {text}"}
        ],
        max_tokens=300,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response['choices'][0]['message']['content']

x = tk.Tk()
x.title("Résumé d'Articles avec ChatGPT")
x.geometry("600x400")
x.configure(bg="#f0f0f0")

label = tk.Label(x, text="Entrez le lien de votre article ou le texte directement", bg="#f0f0f0", font=("Helvetica", 12))
label.pack(pady=10)

entry = tk.Entry(x, width=50, font=("Helvetica", 12))
entry.pack(pady=5)

summarize_button = tk.Button(x, text="Résumer", command=summarize, bg="#4CAF50", fg="white", font=("Helvetica", 12))
summarize_button.pack(pady=10)

result_text = tk.Text(x, height=10, width=60, font=("Helvetica", 12), wrap=tk.WORD)
result_text.pack(pady=10)

x.mainloop()