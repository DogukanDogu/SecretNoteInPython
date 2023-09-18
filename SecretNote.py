import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from tkinter import messagebox
import cryptography.fernet

class SecretNote:

    def __init__(self, root):
        global txtSecretNoteTitle, txtSecretNote, txtSecretNoteMasterkey

        root.title("Secret Notes")
        width=421
        height=766
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        imageSecret = PhotoImage(file="SecretNotes/topsecret.png")
        canvas = tk.Canvas(height=200,width=200)
        canvas.create_image(100,100,image=imageSecret)
        lblSecretNoteImage=tk.Label(image=imageSecret)
        canvas.place(x=80,y=20)

        lblSecretNoteTitle=tk.Label(root)
        lblSecretNoteTitle["cursor"] = "sizing"
        ft = tkFont.Font(family='Times',size=12)
        lblSecretNoteTitle["font"] = ft
        lblSecretNoteTitle["fg"] = "#333333"
        lblSecretNoteTitle["justify"] = "center"
        lblSecretNoteTitle["text"] = "Enter Your Title"
        lblSecretNoteTitle.place(x=70,y=170,width=284,height=30)

        txtSecretNoteTitle=tk.Entry(root)
        txtSecretNoteTitle["borderwidth"] = "1px"
        txtSecretNoteTitle["cursor"] = "sizing"
        ft = tkFont.Font(family='Times',size=10)
        txtSecretNoteTitle["font"] = ft
        txtSecretNoteTitle["fg"] = "#333333"
        txtSecretNoteTitle["justify"] = "left"
        txtSecretNoteTitle["text"] = ""
        txtSecretNoteTitle.place(x=70,y=200,width=288,height=30)

        lblSecretNote=tk.Label(root)
        lblSecretNote["cursor"] = "sizing"
        ft = tkFont.Font(family='Times',size=12)
        lblSecretNote["font"] = ft
        lblSecretNote["fg"] = "#333333"
        lblSecretNote["justify"] = "center"
        lblSecretNote["text"] = "Enter Your Secret"
        lblSecretNote.place(x=70,y=240,width=287,height=30)

        txtSecretNote=tk.Text(root)
        txtSecretNote["borderwidth"] = "1px"
        txtSecretNote["cursor"] = "sizing"
        ft = tkFont.Font(family='Times',size=10)
        txtSecretNote["font"] = ft
        txtSecretNote["fg"] = "#333333"
        txtSecretNote.place(x=70,y=280,width=290,height=316)

        lblSecretNoteMasterKey=tk.Label(root)
        lblSecretNoteMasterKey["cursor"] = "sizing"
        ft = tkFont.Font(family='Times',size=10)
        lblSecretNoteMasterKey["font"] = ft
        lblSecretNoteMasterKey["fg"] = "#333333"
        lblSecretNoteMasterKey["justify"] = "center"
        lblSecretNoteMasterKey["text"] = "Enter Master Key"
        lblSecretNoteMasterKey.place(x=70,y=600,width=292,height=35)

        txtSecretNoteMasterkey=tk.Entry(root)
        txtSecretNoteMasterkey["borderwidth"] = "1px"
        txtSecretNoteMasterkey["cursor"] = "sizing"
        ft = tkFont.Font(family='Times',size=10)
        txtSecretNoteMasterkey["font"] = ft
        txtSecretNoteMasterkey["fg"] = "#333333"
        txtSecretNoteMasterkey["justify"] = "left"
        txtSecretNoteMasterkey["text"] = ""
        txtSecretNoteMasterkey.place(x=70,y=640,width=290,height=30)

        btnSaveEndEncrypt=tk.Button(root)
        btnSaveEndEncrypt["bg"] = "#f0f0f0"
        btnSaveEndEncrypt["cursor"] = "sizing"
        ft = tkFont.Font(family='Times',size=10)
        btnSaveEndEncrypt["font"] = ft
        btnSaveEndEncrypt["fg"] = "#000000"
        btnSaveEndEncrypt["justify"] = "center"
        btnSaveEndEncrypt["text"] = "Save&Encrypt"
        btnSaveEndEncrypt.place(x=160,y=680,width=106,height=30)
        btnSaveEndEncrypt["command"] = self.btnSaveEndEncrypt_Click

        btnSaveAndDecrypt=tk.Button(root)
        btnSaveAndDecrypt["bg"] = "#f0f0f0"
        btnSaveAndDecrypt["cursor"] = "sizing"
        ft = tkFont.Font(family='Times',size=10)
        btnSaveAndDecrypt["font"] = ft
        btnSaveAndDecrypt["fg"] = "#000000"
        btnSaveAndDecrypt["justify"] = "center"
        btnSaveAndDecrypt["text"] = "Decrypt"
        btnSaveAndDecrypt.place(x=160,y=720,width=105,height=30)
        btnSaveAndDecrypt["command"] = self.btnSaveAndDecrypt_Click

    def btnSaveEndEncrypt_Click(self):
        title = txtSecretNoteTitle.get()
        secretNote = txtSecretNote.get(1.0,END)

        if title == "" or secretNote == "":
            tk.messagebox.showinfo(message="title , Secret Note and Master Key  is mandatory")
            return

        key = cryptography.fernet.Fernet.generate_key()

        txtSecretNoteMasterkey.insert(0,str(key))

        with open("my_secret.txt","a") as data_file:
            encrypted_text_secret_note = cryptography.fernet.Fernet(key).encrypt(secretNote.encode())
            data_file.write(f"\n{title}\n{encrypted_text_secret_note} ")
            txtSecretNote.delete(0.0,END)
            txtSecretNoteTitle.delete(0,END)

    def btnSaveAndDecrypt_Click(self):
        secretmasterkey = txtSecretNoteMasterkey.get()
        if secretmasterkey == "":
            tk.messagebox.showinfo(message="Master Key is mandatory for decryption")
            return

        with open("my_secret.txt", "r") as data_file:
            contents = data_file.read()

            token = cryptography.fernet.Fernet.decrypt(None,bytes(secretmasterkey, "utf-8"))
            decrypted_text = cryptography.fernet.Fernet(token).decrypt(contents)

            txtSecretNote.insert(0.0,str(decrypted_text))


if __name__ == "__main__":
    root = tk.Tk()
    app = SecretNote(root)
    root.mainloop()
