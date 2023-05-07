from claseviajerofrecuente import ViajeroFrecuente
import csv
class Controlador:
    __viajeros=[]
    def __init__(self):
        self.__viajeros = []
    def crearLista(self):
        archivo = open("Viajeros.csv")
        reader = csv.reader (archivo,delimiter=";")
        for fila in reader:
            nro=int(fila[0])
            dni=str(fila[1])
            nom=str(fila[2])
            ape=str(fila[3])
            tmil=int(fila[4])
            viajero=ViajeroFrecuente(nro,dni,nom,ape,tmil)
            self.__viajeros.append(viajero)
    
    def mayores (self): 
        i = 0
        max_viajero = max(self.__viajeros)
        m = max_viajero.retornatotalmillas()
        for i in range (len(self.__viajeros)):
            if self.__viajeros[i].retornatotalmillas() == m:
                print ('El viajero con numero {} tiene la maxima cantidad de total de millas que es {} '.format(self.__viajeros[i].getNum(), self.__viajeros[i].retornatotalmillas()))

    def acumularMillas (self):
        numero = 0
        i = 0
        indice = int(input ('Ingrese numero de viajero a acumular millas '))
        while  i < len(self.__viajeros):
            if self.__viajeros[i].getNum() == indice:
                numero = int(input ('Ingrese cantidad de millas a acumular '))
                print ('Actual cantidad de millas: {} '.format(self.__viajeros[i].retornatotalmillas()))
                self.__viajeros[i] = self.__viajeros[i] + numero
                print ('Nueva cantidad de millas del viajero {}: {} '.format(self.__viajeros[i].getNum(), self.__viajeros[i].retornatotalmillas()))
                break
            i+=1
        else : 
            print ('No se encontro ningun viajero con el numero ingresado ')    
            
    def canjearMillas (self):
        numero = 0
        i = 0
        indice = int(input ('Ingrese numero de viajero a canjear millas '))
        while  i < len(self.__viajeros):
            if self.__viajeros[i].getNum() == indice:
                numero = int(input ('Ingrese cantidad de millas a canjear '))
                print ('Actual cantidad de millas: {} '.format(self.__viajeros[i].retornatotalmillas()))
                self.__viajeros[i] = self.__viajeros[i] - numero
                print ('Nueva cantidad de millas del viajero {}: {} '.format(self.__viajeros[i].getNum(), self.__viajeros[i].retornatotalmillas()))
                break
            i+=1
        else : 
            print ('No se encontro ningun viajero con el numero ingresado ')    
                    