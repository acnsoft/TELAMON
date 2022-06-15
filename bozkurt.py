from datetime import datetime
import socket
import os
import argparse


parser = argparse.ArgumentParser()


now = datetime.now()

current_time = now.strftime("%H:%M:%S")


COLORS = {\
"black":"\u001b[30;1m",
"red": "\u001b[31;1m",
"green":"\u001b[32m",
"yellow":"\u001b[33;1m",
"blue":"\u001b[34;1m",
"magenta":"\u001b[35m",
"cyan": "\u001b[36m",
"white":"\u001b[37m",
"yellow-background":"\u001b[43m",
"black-background":"\u001b[40m",
"cyan-background":"\u001b[46;1m",
}


def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text





oner = "[[blue]]Önerilen[[white]]"
onerilen = colorText(oner)

vrenkli = "[[red]]-[[green]]Beta[[white]]"
vrenklibas = colorText(vrenkli)

print(f"""
 ______             _                       
(____  \           | |                  _   
 ____)  ) ___ _____| |  _ _   _  ____ _| |_ 
|  __  ( / _ (___  ) |_/ ) | | |/ ___|_   _)
| |__)  ) |_| / __/|  _ (| |_| | |     | |_ 
|______/ \___(_____)_| \_)____/|_|      \__)

                                    {vrenklibas}
                                                    
""")



parser.add_argument("-s", "--scan", help='to scan ip/website has any open port', action="store_true" )
parser.add_argument("-sA", "--scanall", help='to scan some ports of an ip/website', action="store_true" )
parser.add_argument("target", help='an ip or a website', type=str)
args = parser.parse_args()




s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Target = args.target



if args.scan:
    x = int(input("Port >"))
    Port = x
    print(f"""
            
 ______             _                       
(____  \           | |                  _   
 ____)  ) ___ _____| |  _ _   _  ____ _| |_ 
|  __  ( / _ (___  ) |_/ ) | | |/ ___|_   _)
| |__)  ) |_| / __/|  _ (| |_| | |     | |_ 
|______/ \___(_____)_| \_)____/|_|      \__)

                                    {vrenklibas}

            
|----------------------------------------------------------------|
|                                                                |
|  Site :  {Target}                                            
|                                                                |
|  Başlama Tarihi : {current_time}                                 
|                                                                |  
|----------------------------------------------------------------|   
            """)

            

    try:
        s.connect((Target , Port))
        print("[+] Port AÇIK>> "+str(Port))
    except:
        print("[-] Port KAPALI>> "+str(Port))

if args.scanall:

    min = int(input("En düşük port >"))
    max = int(input("En büyük port >"))

    print("")

    for Port in range(min, max + 1):
        try:
            s.connect((Target , Port))
            print("[+] Port AÇIK>> "+str(Port))
            
        except:
            print("[-] Port KAPALI>> "+str(Port))
