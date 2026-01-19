import tkinter as tk
from tkinter import messagebox
import mysql.connector

# ---------- DATABASE ----------
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="notes_app"
    )

# ---------- MAIN WINDOW ----------
root = tk.Tk()
root.title("Notes Dashboard")
root.geometry("750x500")

# ---------- FUNCTIONS ----------
def fetch_notes():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM notes ORDER BY id DESC")
    data = cursor.fetchall()
    conn.close()
    return data

def refresh_dashboard():
    for w in notes_frame.winfo_children():
        w.destroy()

    notes = fetch_notes()

    for index, note in enumerate(notes):
        btn = tk.Button(
            notes_frame,
            text=note["title"],
            width=22,
            height=4,
            command=lambda n=note: open_editor(n)
        )
        btn.grid(row=index // 3, column=index % 3, padx=10, pady=10)

def open_editor(note=None):
    editor = tk.Toplevel(root)
    editor.title("Note Editor")
    editor.geometry("400x400")

    tk.Label(editor, text="Title").pack()
    title_entry = tk.Entry(editor, width=40)
    title_entry.pack(pady=5)

    tk.Label(editor, text="Content").pack()
    content_text = tk.Text(editor, height=15)
    content_text.pack(pady=5)

    if note:
        title_entry.insert(0, note["title"])
        content_text.insert("1.0", note["content"])

    def save_note():
        title = title_entry.get()
        content = content_text.get("1.0", tk.END).strip()

        if not title:
            messagebox.showwarning("Warning", "Title required")
            return

        conn = get_connection()
        cursor = conn.cursor()

        if note:
            cursor.execute(
                "UPDATE notes SET title=%s, content=%s WHERE id=%s",
                (title, content, note["id"])
            )
        else:
            cursor.execute(
                "INSERT INTO notes (title, content) VALUES (%s, %s)",
                (title, content)
            )

        conn.commit()
        conn.close()
        refresh_dashboard()
        editor.destroy()

    def delete_note():
        if messagebox.askyesno("Delete", "Delete this note?"):
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM notes WHERE id=%s", (note["id"],))
            conn.commit()
            conn.close()
            refresh_dashboard()
            editor.destroy()

    tk.Button(editor, text="Save", command=save_note).pack(side="left", padx=20, pady=10)

    if note:
        tk.Button(editor, text="Delete", command=delete_note).pack(side="right", padx=20, pady=10)

# ---------- UI ----------
top = tk.Frame(root)
top.pack(fill="x", pady=10)

tk.Label(top, text="My Notes", font=("Arial", 18)).pack(side="left", padx=20)
tk.Button(top, text="+ Create Note", command=lambda: open_editor()).pack(side="right", padx=20)

notes_frame = tk.Frame(root)
notes_frame.pack(expand=True)

refresh_dashboard()
root.mainloop()
