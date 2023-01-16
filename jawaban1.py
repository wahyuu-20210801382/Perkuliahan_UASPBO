# Jelaskan menurut anda apa itu inheritance

class Ojek():

    def __init__(self, nama, transmisi, daerah):
        self.nama = nama
        self.transmisi = transmisi
        self.daerah = daerah

    def cek_id_abang(self):
        print('nama:',self.nama,'\nmotor:',self.transmisi,'\ndaerah:',self.daerah)

class Gojek(Ojek):

    def cek_id_abang(self):
        print('cek aplikasi gojek')


ojek1 = Ojek('WAHYU','automatic','Citra Raya')
ojek2 = Gojek('ELSA','automatic','Pasar Cikupa')

ojek1.cek_id_abang()
ojek2.cek_id_abang()
