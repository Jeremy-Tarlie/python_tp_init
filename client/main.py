client = {101: 'Dupont', 102: 'Martin', 103: 'Durand'}

def getAllClients(client):
    print("--------------------")
    print("Liste des clients:")
    i = 1
    for key in client:
        print(f"{i}. {client.get(key)} est le client numéro {key}")
        i += 1
    print("--------------------")

def deleteClient(client):
    key = None
    x = input("Entrez le numéro du client à supprimer (id ou nom): ")
    for id, name in client.items():
        if str(id) == x:
            print("--------------------")
            key = id
            print(f"Le client {client.get(key)} a été supprimé")
            del client[int(x)]        
            print("--------------------")
            break
        elif name == x:
            print("--------------------")
            key = [key for key, val in client.items() if val == x]
            print(f"Le client {client.get(key[0])} a été supprimé")
            del client[key[0]]
            print("--------------------")
            break
    return key

def addClient(client):
    name = input("Entrez le nom du client à ajouter: ")
    id = input("Entrez l'id du client à ajouter: ")
    client[int(id)] = name

def updateClient(client):
    key = None
    x = input("Entrez le numéro du client à modifier (id ou nom): ")
    y = input("Vous voulez changer son id ou son nom : ")
    while str(y) not in ['id', 'nom']:
        y = input("Vous voulez changer son id ou son nom (id ou nom uniquement) : ")
        
    for id, name in client.items():
        if str(id) == x and y == 'nom':
            z = input("Entrez le nouveau nom du client: ")
            print("--------------------")
            key = id
            print(f"Le client {client.get(key)} a été modifié")
            client[int(x)] = z
            print("--------------------")
            break
        elif name == x and y == 'nom':
            z = input("Entrez le nouveau nom du client: ")
            print("--------------------")
            key = [key for key, val in client.items() if val == x]
            print(f"Le client {client.get(key[0])} a été modifié")
            client[key[0]] = z
            print("--------------------")
            break
        elif str(id) == x:
            z = input("Entrez le nouvel id du client: ")
            print("--------------------")
            key = id
            print(f"Le client {client.get(key)} a été modifié")
            client[z] = client.get(key)
            del client[int(x)]
            print("--------------------")
            break
        elif name == x:
            z = input("Entrez le nouvel id du client: ")
            print("--------------------")
            key = [key for key, val in client.items() if val == x]
            print(f"Le client {client.get(key[0])} a été modifié")
            client[key[0]] = client.get(key[0])
            del client[key[0]]
            print("--------------------")
            break
    return key


while True:
    print("1. Afficher les clients")
    print("2. Supprimer un client")
    print("3. Ajouter un client")
    print("4. Modifier un client")
    print("5. Quitter")
    choice = input("Entrez votre choix: ")
    if choice == '1':
        getAllClients(client)
    elif choice == '2':
        if deleteClient(client) is None:
            print("--------------------")
            print("Ce client n'existe pas")
            print("--------------------")
    elif choice == '3':
        addClient(client)
    elif choice == '4':
        if updateClient(client) is None:
            print("--------------------")
            print("Ce client n'existe pas")
            print("--------------------")
    elif choice == '5':
        break
    else:
        print("--------------------")
        print("Choix invalide")
        print("--------------------")
