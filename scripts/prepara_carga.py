import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from conf import conectar_db
from datetime import datetime
from . import atualiza_saldos

global closed

if __name__ != '__main__':

    def gerar(results,page):

        data = []
        gupycode = ''
        name = ''
        status = ''
        cdc = ''
        base = ''
        gestorADP = ''
        liderimed = ''
        client = ''
        format = "%Y-%m-%dT%H:%M:%S.%fZ"
        
        for vaga in results:

            status = vaga['status']

            if status != 'draft':

                jobid = vaga['id']
                numvacancies = vaga['numVacancies']
                
                if status == "published":
                    numclosed = atualiza_saldos.obter_saldo(jobid)
                elif status == "closed":
                    numclosed = numvacancies
                else:
                    numclosed = "0"
                
                if numclosed == None:
                    numclosed = "0"

                gupycode = vaga['code']
                name = vaga['name']
                type = vaga['type']
                reason = vaga['reason']
                remoteWorking = vaga['remoteWorking']

                createdAtRaw = vaga['createdAt']
                if createdAtRaw != None:
                    createdAtConv = datetime.strptime(createdAtRaw,format)
                    createdAt = createdAtConv.isoformat()
                else:
                    createdAt = "NULL"

                updatedAtRaw = vaga['updatedAt']
                if updatedAtRaw != None:
                    updatedAtConv = datetime.strptime(updatedAtRaw,format)
                    updatedAt = updatedAtConv.isoformat()
                else:
                    updatedAt = "NULL"                    

                cancelAtRaw = vaga['cancelAt']
                if cancelAtRaw != None:
                    cancelAtConv = datetime.strptime(cancelAtRaw,format)
                    cancelAt = cancelAtConv.isoformat()
                else:
                    cancelAt = "NULL"                      

                closedAtRaw = vaga['closedAt']
                if closedAtRaw != None:
                    closedAtConv = datetime.strptime(closedAtRaw,format)
                    closedAt = closedAtConv.isoformat()
                else:
                    closedAt = "NULL"                        

                approvedAtRaw = vaga['approvedAt']
                if approvedAtRaw != None:
                    approvedAtConv = datetime.strptime(approvedAtRaw,format)
                    approvedAt = approvedAtConv.isoformat()
                else:
                    approvedAt = "NULL"                      

                disapprovedAtRaw = vaga['disapprovedAt']
                if disapprovedAtRaw != None:
                    disapprovedAtConv = datetime.strptime(disapprovedAtRaw,format)
                    disapprovedAt = disapprovedAtConv.isoformat()
                else:
                    disapprovedAt = "NULL"                      

                lastFreezeDateRaw = vaga['lastFreezeDate']
                if lastFreezeDateRaw != None:
                    lastFreezeDateConv = datetime.strptime(lastFreezeDateRaw,format)
                    lastFreezeDate = lastFreezeDateConv.isoformat()
                else:
                    lastFreezeDate = "NULL"                       

                lastUnfreezeDateRaw = vaga['lastFreezeDate']
                if lastUnfreezeDateRaw != None:
                    lastUnfreezeDateConv = datetime.strptime(lastUnfreezeDateRaw,format)
                    lastUnfreezeDate = lastUnfreezeDateConv.isoformat()
                else:
                    lastUnfreezeDate = "NULL"                       

                publishedAtRaw = vaga['publishedAt']
                if publishedAtRaw != None:
                    publishedAtConv = datetime.strptime(publishedAtRaw,format)
                    publishedAt = publishedAtConv.isoformat()
                else:
                    publishedAt = "NULL"
                
                WorkAddressLat = vaga['addressLatitude']
                WorkAddressLon = vaga['addressLongitude']
                WorkaddressCity = vaga['addressCity']
                customfields = vaga['customFields']
                prevstatus = "unknown"
                
                if reason == None:
                    reason = 'unknown'

                for fields in customfields:
            
                    if fields['id'] == "06587708-1f21-4fa1-918c-b8a95e99ab9c":
                        
                        try:
                            cdc = fields['value']

                        except:
                            pass

                        if cdc == None:
                            cdc = "unknown"
                    
                        
                    elif fields['id'] == "648a4ef2-4a78-4579-b001-e5dbb04a7947":

                        try:
                            base = fields['value']

                        except:
                            pass

                        if base == None:
                            base = "unknown"

                    elif fields['id'] == "bc65b593-0a91-433b-9832-3ba7fb9d4f7d":
                        
                        try:
                            gestorADP = fields['value']

                        except:
                            pass

                        if gestorADP == None:
                            gestorADP = "unknown"

                    elif fields['id'] == "db24e578-8c85-405c-9073-3b41519ff9b5":

                        try:                    
                            liderimed = fields['value']
                        except:
                            pass

                        if liderimed == None:
                            liderimed = "unknown"
                    
                    elif fields['id'] == "d7a1e23d-39d2-4a16-993f-4df6e0fd2cd8":
                        
                        try:
                            client = fields['value']

                        except:
                            pass

                        if client == None:
                            client = "unknown"

                    if gestorADP == None:
                        gestorADP = "unknown"

                    if liderimed == None:
                        liderimed = "unknown"

                    if publishedAt == None:
                        publishedAt = "unknown"
                    
                    if reason == None:
                        reason = "unknown"
                    
                    if WorkAddressLon == None:
                        WorkAddressLon = "NULL"

                    if WorkAddressLat == None:
                        WorkAddressLat = "NULL"

                vagadtl = 'NULL',gupycode,name,status,prevstatus,numvacancies,numclosed,reason,client,type,cdc,gestorADP,liderimed,base,remoteWorking,createdAt,updatedAt,publishedAt,cancelAt,closedAt,approvedAt,disapprovedAt,lastFreezeDate,lastUnfreezeDate,WorkAddressLat,WorkAddressLon,WorkaddressCity
                
                if vagadtl not in data:
            
                    data.append(vagadtl)
            
        conectar_db.alimenta_db_vagas(data,page)
else:
    print("Este script não pode ser executado diretamente")