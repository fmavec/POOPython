class Lavadora:

    def __init__(self):
        pass

    def lavar(self, temperatura='caliente'):
        self._llenar_tanque(temperatura)
        self._anadir_jabon()
        self._lavar()
        self._enjuagar()
        self._centrifugar()
    
    def _llenar_tanque(self, temperatura):
        print(f'Llenando tanque de agua a temperatura {temperatura}')
    
    def _anadir_jabon(self):
        print('Añade el jabon')

    def _lavar(self):
        print('Lavando')

    def _enjuagar(self):
        print('Enjuagando')

    def _centrifugar(self):
        print('Centrifugando')


if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar()