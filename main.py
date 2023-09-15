from conf import conectar_db
from scripts import obter_vaga

vagaexist = ""
vagadtl = ""

if __name__ == '__main__':

    print("Iniciando processo de espelhamento da base da Gupy")

    conectar_db.conecta_banco()
    conectar_db.limpa_db()
    obter_vaga.obter_dados_vaga()
    conectar_db.desconecta_banco()