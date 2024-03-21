import customtkinter
import tkinter
import whois
import socket
import webbrowser


root = customtkinter.CTk()

root.title("Mars Scanner V0.1")
root.geometry("640x480")
root.resizable(False, False)
customtkinter.set_appearance_mode("dark")

MAIN_COLOUR_ORANGE = "#E3850E"
DEFAULT_COLOUR_BLACK = "#242424"

def raiseDomainLookup():
    domainLookupFrame.tkraise()

def raisePortScanner():
    portScannerFrame.tkraise()

def raiseCredits():
    creditsFrame.tkraise()

def repository():
    webbrowser.open("https://github.com/MarsssDEV/Mars-ToolBox")

lMenuFrame = customtkinter.CTkFrame(root, width=140, height=480, corner_radius=0, fg_color=DEFAULT_COLOUR_BLACK, border_width=1, border_color="#404040")
lMenuFrame.place(x=0, y=0)

titleLabel = customtkinter.CTkLabel(lMenuFrame, width=130, height=30, text="TOOLS", font=("helvetica", 16))
titleLabel.place(relx=0.01, rely=0.025)

domainLookupBtn = customtkinter.CTkButton(lMenuFrame, text="Domain Lookup", fg_color=DEFAULT_COLOUR_BLACK, corner_radius=5, text_color="#fff", width=140, height=30, border_width=1, border_color=MAIN_COLOUR_ORANGE, hover_color=MAIN_COLOUR_ORANGE, command=raiseDomainLookup)
domainLookupBtn.place(relx=0, rely=0.125)

portScannerBtn = customtkinter.CTkButton(lMenuFrame, text="Port Scanner", fg_color=DEFAULT_COLOUR_BLACK, corner_radius=5, text_color="#fff", width=140, height=30, border_width=1, border_color=MAIN_COLOUR_ORANGE, hover_color=MAIN_COLOUR_ORANGE, command=raisePortScanner)
portScannerBtn.place(relx=0, rely=0.19)

linksBtn = customtkinter.CTkLabel(lMenuFrame, width=130, height=30, text="LINKS", font=("helvetica", 16))
linksBtn.place(relx=0.01, rely=0.705)

creditsBtn = customtkinter.CTkButton(lMenuFrame, text="Credits", fg_color=DEFAULT_COLOUR_BLACK, corner_radius=5, text_color="#fff", width=140, height=30, border_width=1, border_color=MAIN_COLOUR_ORANGE, hover_color=MAIN_COLOUR_ORANGE, command=raiseCredits)
creditsBtn.place(relx=0, rely=0.805)

githubBtn = customtkinter.CTkButton(lMenuFrame, text="Repository", fg_color=DEFAULT_COLOUR_BLACK, corner_radius=5, text_color="#fff", width=140, height=30, border_width=1, border_color=MAIN_COLOUR_ORANGE, hover_color=MAIN_COLOUR_ORANGE, command=repository)
githubBtn.place(relx=0, rely=0.870)



#DOMAIN LOOKUP

def domainLookup():
    domain = domainEntry.get()
    info = whois.whois(domain)
    infoToStr = str(info)
    f = open("domainResults.txt",'a')
    f.write(infoToStr)
    f.write("\n")
    f.close()


domainLookupFrame = customtkinter.CTkFrame(root, width=498, height=480, corner_radius=0, fg_color=DEFAULT_COLOUR_BLACK, border_width=1, border_color="#404040")
domainLookupFrame.place(x=142, y=0)

domainLookupTitle = customtkinter.CTkLabel(domainLookupFrame, width=130, height=30, text="DOMAIN LOOKUP", font=("helvetica", 20))
domainLookupTitle.place(relx=0.35, rely=0.01)

domainEntryLabel = customtkinter.CTkLabel(domainLookupFrame, width=130, height=30, text="DOMAIN:", font=("helvetica", 20))
domainEntryLabel.place(relx=0.15, rely=0.11)

domainEntry = customtkinter.CTkEntry(domainLookupFrame, width=200, height=30)
domainEntry.place(relx=0.4, rely=0.11)

domainEntryBtn = customtkinter.CTkButton(domainLookupFrame, text="LOOKUP DOMAIN", fg_color=DEFAULT_COLOUR_BLACK, corner_radius=5, text_color="#fff", width=240, height=30, border_width=1, border_color=MAIN_COLOUR_ORANGE, hover_color=MAIN_COLOUR_ORANGE, command=domainLookup)
domainEntryBtn.place(relx=0.25, rely=0.21)





#port scanner
def portscanner():

    socket.setdefaulttimeout(0.01)
    ip = portScannerEntry.get()
    for port in range(1, 6500 + 1):
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if not tcp.connect_ex((ip, port)):
            f = open("portResults.txt",'a')
            f.write(f"{ip}:{port} OPEN \n")
            f.close()
            tcp.close()

portScannerFrame = customtkinter.CTkFrame(root, width=498, height=480, corner_radius=0, fg_color=DEFAULT_COLOUR_BLACK, border_width=1, border_color="#404040")
portScannerFrame.place(x=142, y=0)

portScannerTitle = customtkinter.CTkLabel(portScannerFrame, width=130, height=30, text="PORT SCANNER", font=("helvetica", 20))
portScannerTitle.place(relx=0.35, rely=0.01)

portScannerLabel = customtkinter.CTkLabel(portScannerFrame, width=130, height=30, text="PORT:", font=("helvetica", 20))
portScannerLabel.place(relx=0.15, rely=0.11)

portScannerEntry = customtkinter.CTkEntry(portScannerFrame, width=200, height=30)
portScannerEntry.place(relx=0.4, rely=0.11)

portScannerEntryBtn = customtkinter.CTkButton(portScannerFrame, text="LOOKUP PORT", fg_color=DEFAULT_COLOUR_BLACK, corner_radius=5, text_color="#fff", width=240, height=30, border_width=1, border_color=MAIN_COLOUR_ORANGE, hover_color=MAIN_COLOUR_ORANGE, command=portscanner)
portScannerEntryBtn.place(relx=0.25, rely=0.21)






#CREDITS!!!!
creditsFrame = customtkinter.CTkFrame(root, width=498, height=480, corner_radius=0, fg_color=DEFAULT_COLOUR_BLACK, border_width=1, border_color="#404040")
creditsFrame.place(x=142, y=0)

creditsTitle = customtkinter.CTkLabel(creditsFrame, width=130, height=30, text="CREDITS", font=("helvetica", 20))
creditsTitle.place(relx=0.35, rely=0.01)

creditsPara = customtkinter.CTkLabel(creditsFrame, width=130, height=30, text="This tool was completely created by mars.py . \n The tool serves as a mini web-testing kit \n with features like a port scanner and a \n domain lookup. Join his Discord server below!", font=("helvetica", 16))
creditsPara.place(relx=0.175, rely=0.11)

discordLink = customtkinter.CTkLabel(creditsFrame, width=130, height=30, text="https://discord.gg/9RRnqJGJaY")
discordLink.place(relx=0.3, rely=0.49) 



root.mainloop()