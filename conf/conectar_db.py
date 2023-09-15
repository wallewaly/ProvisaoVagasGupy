# This file is responsible to define the DB Connection and its required data

import mysql.connector

contcadastros = 0


if __name__ != '__main__':

    def conecta_banco():

        global cnx, cursor

        print("Conectando banco de dados")

        cnx = mysql.connector.connect(user='', 
                                    password='',
                                    host='',
                                    database='',
                                    use_pure=False)

        cursor = cnx.cursor()

    def desconecta_banco():

        global cnx, cursor

        print("Desconectando banco de dados")

        cursor.close()

        cnx.close()

    def limpa_db():

        global cnx, cursor

        print("Limpando tabelas do banco de dados")

        query = """TRUNCATE dadosgerais"""

        cursor.execute(query)

        cnx.commit()

    def alimenta_db_vagas(data,page):

        contcadastros = ""

        print("Carregando dados da página",page,"da Gupy para o banco de dados.")

        query = """INSERT INTO dadosgerais 
                    (`id`,`code`, `name`, `currstatus`,`prevstatus`,`numvacancies`,`numclosed`, `reason`, `client`, `contracttype`, `CDC`,`ADPManager`, `ImedLeader`,`Base`, `remoteworking`,`createdAt`, `updatedAt`, `publishedAt`,`cancelAt`,`closedAt`,`approvedAt`,`disapprovedAt`,`lastFreezeDate`,`lastUnfreezeDate`,`AddressLatitude`,`AddressLongitude`,`AddressCity`)
                    VALUES {} """.format(str(data).strip('[]').replace("'NULL'", 'NULL'))

        cursor.execute(query)

        cnx.commit()
else:
    print("Este script não pode ser executado diretamente")