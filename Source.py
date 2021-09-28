# libraries
import requests

# methods
def inputUser():
    user = input("Digite qual é o nome da conta de backup: ")
    return user

def inputApikey():
    apikey = input("Digite qual é a ApiKey do seu portal: ")
    return apikey

def inputBackupSetID():
    backupsetid = input("Digite qual é o id do seu backup-set: ")
    return backupsetid

def inputStatus():
    status = input("Digite o status (INFO, SUCCESS, WARN, ERROR, OUTDATED, NEVER, NOMON) desejado: ")
    return status

# functions
def menuInput():
    while True:
        a = input("Digite a opção desejada e dê um ENTER: ")
        if a.isnumeric():
            break
        else:
            continue
    return int(a)

def apioption1():
    apikey = inputApikey()
    url = "https://api.backupmanager.info/webservices?method=get-backup-infos&apikey=" + apikey + "&show_stats=true"
    ret = requests.get(url)
    r = ret.text
    return r

def apioption2():
    apikey = inputApikey()
    user = inputUser()
    backup_set_id = inputBackupSetID()
    status = inputStatus()
    url = "https://api.backupmanager.info/webservices?method=get-backup-infos&apikey=" + apikey + "&user=" + user + "&backup_set_id=" + backup_set_id +"&status=" + status
    ret = requests.get(url)
    r = ret.text
    return r

def apioption3():
    user = inputUser()
    backupsetid = inputBackupSetID()
    apikey = inputApikey()
    url = "https://api.backupmanager.info/webservices?method=show-backup-quotas&apikey=" + apikey + "&user=" +user + "&backup_set_id=" + backupsetid
    ret = requests.get(url)
    r = ret.text
    return r

def apioption4():
    apikey = inputApikey()
    user = inputUser()
    backup_set_id = inputBackupSetID()
    url = "https://api.backupmanager.info/webservices?method=show-backup-usage&apikey=" + apikey + "&user=" + user + "&backup_set_id= " + backup_set_id
    ret = requests.get(url)
    r = ret.text
    return r

def apioption5():
    apikey = inputApikey()
    user = inputUser()
    backup_set_id = inputBackupSetID()
    url = "https://api.backupmanager.info/webservices?method=run-backup&apikey=" + apikey + "&user=" + user + "&backup_set_id=" + backup_set_id
    ret = requests.get(url)
    r = ret.text
    return r

def apioption6():
    apikey = inputApikey()
    user = inputUser()
    backup_set_id = inputBackupSetID()
    url = "https://api.backupmanager.info/webservices?method=stop-backup&apikey=" + apikey + "&user=" + user + "&backup_set_id=" + backup_set_id
    ret = requests.get(url)
    r = ret.text
    return r

"""
def apioption7():
    opt = input("Digite o número da opção acima que deseja visualizar a documentação e dê um ENTER: ")
    pass
"""

# program
while True:
    # header
    print("Selecione a opção desejada:")
    print("Consulta de API Backup Manager \nSelecione a opção de API que deseja validar:\n")
    print("1 - Listar o estado geral das tarefas de backup")
    print("2 - Listar as informações gerais dos perfis de backup")
    print("3 - Listar as informações de cotas dos perfis de backup")
    print("4 - Listar as informações de consumo dos perfis de backup")
    print("5 - Iniciar um backup remotamente")
    print("6 - Interromper a inicialização de um backup")
#    print("7 - Documentação")
    print("0 - Fecar programa")

    apioption = menuInput()
    
    if apioption > 0:
        if apioption == 1:
            print(apioption1() + "\n\n\n")
        elif apioption == 2:
            print(apioption2() + "\n\n\n")    
        elif apioption == 3:
            print(apioption3() + "\n\n\n")
        elif apioption == 4:
            print(apioption4() + "\n\n\n")
        elif apioption == 5:
            print(apioption5() + "\n\n\n")
        elif apioption == 6:
            print(apioption6() + "\n\n\n")
    else:
        break
#        elif apioption == 7:
#            apioption7()


print("\nAPI implemented by Pedro Renan Mussato - website: pedromussato.com\n")
# exit