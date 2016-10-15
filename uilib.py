#coding: utf-8
"""
lABEr
=====
The User-Interface for lABEr.
"""

from tkinter import *
import serwork as sw

class ChatUI:
    "The User-Interface for lABEr"
    def __init__(self, cbfunc):
        "Initializes the ChatUI"
        self._tk = Tk()
        self._tk.title("lABEr")
        self._tk.resizable(width=0, height=0)
        self.outputArea = Text(self._tk, width="86", height="20", state="disabled", font=("Calibri",13))
        self._addLine("++++++ lABEr-Char ++++++")
        self.outputArea.place(x=0, y=0)
        self.inputArea = Entry(self._tk, width="85", font=("Calibri",12))
        self.inputArea.place(x=3.5, y=435)
        self.sendenButton = Button(self._tk, text="Senden", command=self._sendData, padx=5, pady=5)
        self.sendenButton.place(y=461, x=630)
        Label(self._tk, text="Benutzername: ").place(y=466, x=3)
        self.userName = Entry(self._tk, width="30", font=("Calibri",11))
        self.userName.place(x=95, y=466)
        Label(self._tk, text="IP des Anderen: ").place(y=466, x=295)
        self.otherIP = Entry(self._tk, width="30", font=("Calibri",11))
        self.otherIP.place(x=380, y=466)
        yourIP = sw.getMyIp()
        if yourIP == "127.0.0.1":
            self._addLine("Du befindest dich zur Zeit entweder nicht im Netzwerk oder nutzt ein nicht kompatibles Linux")
            self._addLine("Dadurch ist es leider nicht moeglich den lABEr-Chat zu nutzen.")
            self.sendenButton['state'] = "disabled"
        else:
            self._addLine("Deine IP ist: " + yourIP)
            self.cbfunc = cbfunc
            self.yourIP = yourIP

    def postMessage(self, usr, msg):
        self._addLine(usr + ": " + msg)

    def _addLine(self, line):
        "Adds a line to the outputArea"
        line = self._emoticonReplace(line)
        self.outputArea['state'] = "normal"
        self.outputArea.insert('end', line + "\n")
        self.outputArea['state'] = "disabled"

    def _emoticonReplace(self, line):
        line = line.replace(":star:", "★")
        line = line.replace(":yes:", "✓")
        line = line.replace(":sun:", "☀")
        line = line.replace(":snow:", "❄")
        line = line.replace(":love:", "❤")
        line = line.replace(":horse:", "♞")
        line = line.replace(":nuclear:", "☢")
        line = line.replace(":sounds:", "♫")
        line = line.replace(":smile:", "☺")
        line = line.replace(":frown:", "☹")
        return line

    def show(self):
        "Shows the ChatWindow"
        self._tk.geometry("693x500")
        self._tk.mainloop()

    def _sendData(self):
        self._addLine(self.userName.get() + ": " + self.inputArea.get())
        self.userName['state'] = "disabled"
        self.cbfunc(self.userName.get(), self.inputArea.get(), [i.strip() for i in list(self.otherIP.get().split(";"))], self.yourIP)
        self.inputArea.delete(0, END)

    def getuser(self):
        return self.userName()

    def gettext(self):
        return inputArea.get()

    def getotherips(self):
        return [i.strip() for i in list(self.otherIP.get().split(";"))]


"""
DOCS:
=====

def callbackfunction(username, message, other_ip, your_ip):
    pass
obj = ChatUI(callbackfunction)


obj.postMessage(username, message)
"""