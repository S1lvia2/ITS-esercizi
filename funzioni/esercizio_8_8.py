def make_album(artist, title):
    album:dict = {"artist": artist, "title": title}   
    return album

while True:
    artist:str = str(input("Artist: "))
    title:str = str(input("Title: "))

    album = make_album(artist, title)
    print(album)


















# esercizio 8.10

# lista_messaggi= ["Ciao","Come stai?", "tutto bene ","a presto"]
# def send_message(messaggi): 

#     sent_message = []
#     upper_bound = len(messaggi)
#     print(f"{messaggi=}\n {sent_message}\n\n")
#     for i in range (upper_bound): 

#         message = messaggi.pop(0)
#         sent_messages.append(message)

#         print(f"{messaggi}\n{sent_message}\n\n")

# send_messages(lista_messaggi)





# lista_messaggi = ["Ciao","Come Stai","Tutto Bene?","A Presto!"]
# def send_messages(messaggi):

#     sent_messages=[]
#     upper_bound = len (messaggi)
#     print(f"{messaggi=}\n {sent_messages=}\n\n")
#     for i in range (upper_bound):
        
#         message = messaggi.pop(0)
#         sent_messages.append(message)

#         print(f"{messaggi=}\n {sent_messages=}\n\n")
# send_messages(lista_messaggi)