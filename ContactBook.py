import json
import getpass
import os

attr_list = ["email", "birthday", "age", "phone_number", "adress", "note"]

file = open("content.json", "r+", 8)
text = json.load(file)

def clear(): return os.system('cls')

class input_system(object):
    def __init__(self):
        self.viewmode()

    def viewmode(self):
        def help():
            print("----------------------")
            print("-----Viewmode-Help----")
            print("(name of entry)             : shows you all Attributes of the entry")
            print("(name of entry) (Attribute) : shows you the specific Attribute of the entry")
            print("contacts                    : shows all contacts that you have")
            print("(Attribute)                 : shows you the Attribute for all entrys")
            print("all                         : shows you all entrys with all Atributes")
            print("Editmode                    : goes into Editmode")
            print("clear                       : clears the terminal")
            print("exit                        : ends the programm")
            print("----------------------")

        while True:
            inp = input(":")
            clear()
            print("-------Viewmode-------")
            inp = inp.split(" ")
            if inp[0].upper() == "EXIT":
                break
            elif inp[0].upper() == "CLEAR":
                clear()
                continue
            elif inp[0].upper() == "PW":
                continue
            elif inp[0].upper() == "ALL":
                for element in text:
                    __key_dic = text[element]
                    if element == "Pw":
                        continue
                    print("---------------")
                    print(element)
                    for x in __key_dic:
                        print(x, ":", __key_dic[x])
                print("---------------")
            elif inp[0].upper() == "CONTACTS" or inp[0].upper() == "CONTACT":
                print("-------------------")
                for element in text:
                    if element == "Pw":
                        continue
                    print(element)
                    print("-------------------")
            elif inp[0].upper() == "EDITMODE":
                clear()
                print("-------Editmode-------")
                self.edit_mode()
                break
            elif inp[0].upper() == "HELP":
                help()
            else:
                try:
                    __key_dic = text[inp[0]] # if input[0] is equal to some name
                    try:
                        __key_dic[inp[1]] # Try if inp[1] is equal to some Attribute
                        print("----------------------")
                        if __key_dic[inp[1]] == "":
                            print(inp[0] + ":" ,"empty")
                        else:
                            print(inp[1] + ":" ,__key_dic[inp[1]])
                        print("----------------------")
                    except: # If inp[1] is not equal to some Attribute
                        # Print every Attribute from the name
                        print("---------------------")
                        print(inp[0] + ":")
                        for x in text[inp[0]]:
                            print(x, ":", __key_dic[x])
                        print("----------------------")
                except: # if input[0] is not equal to some name
                    for x in attr_list:
                        if inp[0] == x: # if input[0] is equal to some Attribute
                            print("----------------------")
                            for element in text: # Go through every name in the list and print out the specific Attribute
                                __key_dic = text[element]
                                if element == "Pw":
                                    continue
                                if __key_dic[inp[0]] != "":
                                    print(element + ":", __key_dic[inp[0]])
                                    print("----------------------")


    def edit_mode(self):
        def dump(name, email, birthday, age, phone_number, adress, note):
            dumped = {name : {
                "email" : email,
                "birthday" : birthday,
                "age" : age,
                "phone_number" : phone_number,
                "adress" : adress,
                "note" : note
            }}
            text.update(dumped)
            file.seek(0)
            json.dump(text, file)
            file.truncate()

        def update():
            file.seek(0)
            json.dump(text, file)
            file.truncate()

        def new_entry(name=0):
            if name == 0:
                name = input("Name:")
            else:
                name = name
            email = input("E-Mail:")
            birthday = input("Birthday:")
            try:
                age = int(input("Age:"))
            except:
                age = None
            phone_number = input("Phone Number:")
            adress = input("Adress:")
            note = input("Note:")
            dump(name, email, birthday, age, phone_number, adress, note)
            clear()
            print("-------Editmode------")

        def user_edit(entry):
            __entry_dic = text[entry]
            print("-------User-Edit-------")
            __inp_text = entry + ":"
            while True:
                inp = input(__inp_text)
                clear()
                print("-------User-Edit-------")
                if inp.upper() == "EXIT":
                    clear()
                    print("-------Editmode-------")
                    break
                elif inp.upper() == "DEL" or inp.upper() == "DELETE":
                    del text[entry]
                    update()
                    clear()
                    print("-------Editmode------")
                    break
                elif inp.upper() == "NEW" or inp.upper() == "NEU":
                    new_entry(entry)
                    clear()
                    print("------Editmode------")
                    break
                elif inp.upper() == "HELP":
                    print("-----------------------")
                    print("-----User-Edit-Help----")
                    print("Attribute : edits the Attribute")
                    print("new       : deletes all entries so that they can be creates again")
                    print("del       : deletes the user with all it's entries")
                    print("exit      : goes out of the user-edit")
                    print("-----------------------")
                else:
                    try:
                        __entry_dic[inp]
                        inp_text = "new " + inp + ":"
                        if inp == "age":
                            try:
                                __new = int(input(inp_text))
                            except:
                                __new = None
                        else:
                            __new = input(inp_text)
                        text[entry][inp] = __new
                        update()
                        clear()
                        print("-------User-Edit-------")
                    except:
                        pass

        def help():
            print("-----------------------")
            print("-----Editmode-Help-----")
            print("new      : creates a new entry")
            print("(name)   : Edit existing entry")
            print("viewmode : goes into viewmode")
            print("exit    : ends the programm")
            print("----------------------")

        while True:
            inp = input(":")
            clear()
            print("-------Editmode-------")
            if inp.upper() == "NEW":
                new_entry()
            elif inp.upper() == "VIEWMODE":
                clear()
                print("-------Viewmode-------")
                self.viewmode()
                break
            elif inp.upper() == "HELP":
                help()
            elif inp.upper() == "EXIT":
                break
            else:
                try:
                    text[inp]
                    clear()
                    user_edit(inp)
                except:
                    pass
                

    def exit():
        file.close()
        clear()


clear()
print("--------------------------")
print("----Welcome to KaiBook----")
print("---------Viewmode---------")
inp = input_system()
input_system.exit()
