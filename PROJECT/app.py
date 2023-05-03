from tkinter import *
from chat import get_response, bot_name
f = "Arial 14"
b = "Arial 13 bold"
LightBlue = "#055c9d"
StrongerBlue = "#68bbe3"
BG_B = "#0E86D4"
TC = "#FFFFFF"

class Chatbot:

    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("C.S. Chatbot Application for JBU by Pamela Carta")
        self.window.resizable(width=True, height=False)
        self.window.configure(width=470, height=550, bg=StrongerBlue)

        head_label = Label(self.window, bg=LightBlue, fg=TC, text="Chat with Cies now!\n Type 'quit' to end session.", font=b, pady=0)
        head_label.place(relwidth=1)

        line = Label(self.window, width=450, bg=LightBlue)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        self.text_widget = Text(self.window, width=20, height=2, bg=StrongerBlue, fg=TC, font=f, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)
        bottom_label = Label(self.window, bg=LightBlue, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg=TC, font=f)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)
        send_button = Button(bottom_label, text="Send", font=b, width=20, bg=BG_B, fg=TC, command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")

    def _insert_message(self, msg, sender):
        if msg == "quit":
            exit()
        if msg == "QUIT":
            exit()
        if msg == "Quit":
            exit()
        if not msg:
            return

        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        msg2 = f"{bot_name}: {get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)


if __name__ == "__main__":
    app = Chatbot()
    app.run()