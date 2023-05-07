class ViajeroFrecuente:
    __nroviajero = 0
    __DNI = ""
    __nombre = ""
    __apellido = ""
    __totalmillas = 0
    def __init__(self,nroviajero=0,DNI="",nombre="",apellido="",totalmillas=0):
         self.__nroviajero = nroviajero
         self.__DNI = DNI
         self.__nombre = nombre
         self.__apellido = apellido
         self.__totalmillas = totalmillas   
        
    
    def retornatotalmillas(self):
        return self.__totalmillas
    def getNum(self):
     return self.__nroviajero
    def __gt__ (self, otroviajero):
       return self.__totalmillas > otroviajero.__totalmillas 
    def __add__ (self, numero):
       self.__totalmillas = self.__totalmillas + numero
       return self
    def __sub__ (self, numero):
       self.__totalmillas = self.__totalmillas - numero
       return self
        
    

