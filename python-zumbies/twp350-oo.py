class televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2

    def mudar_canal_para_cima(self):
        self.canal += 1

    def mudar_canal_para_baixo(self):
        self.canal -= 1

tv_sala = televisao()
tv_sala.mudar_canal_para_cima()
print(tv_sala.canal)