from claseviajerofrecuente import ViajeroFrecuente
from controlador import Controlador
from Menu import Menuclass
def test ():
    c=Controlador()
    c.crearLista()
    m=Menuclass()
    m.opciones(c)
if __name__=="__main__":
    test()
    
