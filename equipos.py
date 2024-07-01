class Equipos():
    def __init__(self,id:str,code:str,name:str,group:str):
        self.id=id
        self.code=code
        self.name=name
        self.group=group 

    def __str__(self):
        return f"{self.code}"
    

    