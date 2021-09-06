from data.data import data 

class PortalAdmin:

    def createUser(name):
        if(hash(name) > len(data.user)):
            for i in range(0,len(data.user) - hash(name)):
                data.user.append(0)
        data.user[hash(name)] = {hash(name), name}
        return (name)

    def updateUser(name):
        if(data.user[hash(name)] == 0):
            return 'error'
        data.user[hash(name)] = {hash(name), name}
        return 'OK'

    def deleteUser(name):
        if(data.user[hash(name)] == 0):
            return 'error'
        removed = data.user[hash(name)]
        data.user[hash(name)] = 0
        return removed

    def getUser(name):
        return (data.user[hash(name)])