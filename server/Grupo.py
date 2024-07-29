from socket import *
import threading

class Grupo:

    users = dict() # dict<Nick, Usuario>
    messages = list()

    # pessoal, acho q aqui a gente poderia ter um set com o momento que ela entrou
    # pra definir quem seria o novo admin?

    def __init__(self, name, admin):

        self.name, self.admin = name, admin 
        self.users[admin.getName()] = admin
    
    def rcvAndPropMsg(self, mensagem):

        # Aqui a mensagem será recebida e enviada para todos
        # usuarios com exceçao do q enviou

        mensagemSplitada = mensagem.split('@')

        # propaga a mensagem para todos os usuarios presentes no grupo
        for user in self.users.keys():

            if(user != mensagemSplitada[1]):

                t = threading.Thread(target= self.users[user].receiveMsgGrupo, args=(mensagem, self.name))
                t.start()
    
    def addUser(self, user):
        self.users[user.getName()] = user
    
    def eraseUser(self, user):
        del self.users[user.getName()]

        mensagem = "2@" + user.getName() + "@saiu"

        self.rcvAndPropMsg(mensagem)
    
    def getName(self):
        return self.name
    
    def getAdmin(self):
        return self.admin
    
    
