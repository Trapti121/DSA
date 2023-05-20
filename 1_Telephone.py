size=3
client_list = [None] *size

def add_client():
    client_id=int(input("Enter client's id :\n"))
    name=input("Enter client's name :\n")
    telephone = input("Enter client's telephone:\n")
    client_details=[client_id,name,telephone]

    index = client_id % size 
    for i in range(size):
        if client_list[index]==None:
            client_list[index]=client_details
            print("adding data" , index,client_details)
            break
        else:
            index=(index+1)%size

def search_client():
    client_id = int(input("Enter the client id which is to be searched:\n"))
    index = client_id %size
    for i in range(size):
        if client_list[index] != None:
            if client_list[index][0] == client_id:
                print("Client is found at index",index,client_list[index])
                break
        index = (index +1 )%size
    else:
        print("Element not found !")

def delete_client():
    client_id=int(input("Enter the client id which is to be deleted:\n"))
    index=client_id % size
    for i in range(size):
        if client_list[index] != None:
            if client_list[index][0]==client_id:
                client_list[index]=None
                print("Client deleted")
                break
        index=(index +1)%size
    else:
        print("Element is not found")


add_client()
add_client()
add_client()
print("serach client")
search_client()
print("deleted client")
delete_client()
print("search client")
search_client()