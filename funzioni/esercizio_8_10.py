lista_messaggi = ["Ciao","Come Stai","Tutto Bene?","A Presto!"]
def send_messages(messaggi):

    sent_messages=[]
    upper_bound = len (messaggi)
    print(f"{messaggi=}\n {sent_messages=}\n\n")
    for i in range (upper_bound):
        
        message = messaggi.pop(0)
        sent_messages.append(message)

        print(f"{messaggi=}\n {sent_messages=}\n\n")
send_messages(lista_messaggi)