import netmiko
import time
import getpass

# This file is where all output is logged
timestamp = time.ctime().replace(':', '.')

# Open file with hosts
hostList = open("hosts.txt").read().splitlines()

# Open file with hosts
cmdsList = open("sshCmds.txt").read().splitlines()

# Check files for data
if not hostList[0]: raise("No hosts in hosts.txt file or unable to read")
if not cmdsList[0]: raise("No commands in sshCmds.txt file or unable to read")

def getCreds():

    while True:
        sshUser = input('\n\nEnter username: ')
        sshPass = getpass.getpass('Enter password: ')
        devType = input('''Device Type? (Enter "?" for list.  Hit enter for generic termserver)
SSH Device Type: ''')
        
        
        if devType == '': devType = 'generic_termserver'
        if devType == '?': devType = ''
        

        
        sshConf = {
        'device_type': devType,
        'ip': hostList[0],
        'username': sshUser,
        'password': sshPass}
        
        print("Testing creds on first host in list: " + hostList[0])
        
        try:
            netmiko.ConnectHandler(**sshConf)
            print("Login success")
            return {'uid': sshUser, 'password': sshPass, 
                    'devType': devType}
            break
    
        except Exception as e:
            print(e)

        else:
            print('Access denied')
    
def runCommands(uid, password, devType):
    
    # Log File
    f = open("sshLog-{}.txt".format(timestamp), "a")
    
    for host in hostList:
        
        sshConf = {
            'device_type': devType,
            'ip': host,
            'username': uid,
            'password': password}
        
        
        net_connect = netmiko.ConnectHandler(**sshConf)
        
        f.write("\n" + host)     
            
        sshOutput = net_connect.send_config_set(cmdsList)
        f.write(sshOutput)
        
        f.write("\n")
    
    f.close()
    


def main():
    
    credsDict = getCreds()
    
    runCommands(credsDict['uid'], credsDict['password'],
                 credsDict["devType"])
    
     

  
if __name__ == "__main__":
    main()