import os
from java.util import Date
from java.text import SimpleDateFormat

#nmConnect(userConfigFile='/oracle/Middleware_Home/user_projects/domains/test_domain/wlst_scripts/userconfigfile.secure', 
#          userKeyFile='/oracle/Middleware_Home/user_projects/domains/test_domain/wlst_scripts/userkeyfile.secure',
#          host='localhost',port='5556', nmType='plain')

#nmConnect(userConfigFile='{{ dommain_user_projects }}/wlst_scripts//userconfigfile.secure', 
#          userKeyFile='{{ dommain_user_projects }}/wlst_scripts/userkeyfile.secure', 
#          host='localhost', port='{{ node_manager_listen_port }}', nmType='plain')
#prps = makePropertiesObject("weblogic.ListenPort=7001")
#nmServerStatus('AdminServer')
#nmStart('AdminServer')
#nmDisconnect()


curTime = SimpleDateFormat("MMM dd, yyyy hh:mm:ss a zzz").format(Date())

connect('weblogic','welcome1')
try:
    cd('/Servers')
    allServers=ls('/Servers', returnMap='true')
    for p_server in allServers:
         if p_server == 'AdminServer':
            continue
         else:
            print "Starting server:" + p_server
            startServer(p_server);
except Exception, e:
    print "Error Occured"

def _startServer(ServerName):

#adminsvrport = "7001"
#admin_url = "t3://localhost:" + adminsvrport
    managed_server_name = ServerName
    direction = path + managed_server_name
    cd(direction)

    serverState = cmo.getState()
    print curTime + " " + managed_server_name + ' initial State: ' + serverState

    if serverState != 'FAILED_NOT_RESTARTABLE' and serverState !='SHUTDOWN':
        try:
            curTime = SimpleDateFormat("MMM dd, yyyy hh:mm:ss a zzz").format(Date())
            print curTime + " " + "Attempting to force shutdown:" + managed_server_name
            cmo.forceShutdown()
            serverState = cmo.getState()
            while (serverState!='SHUTDOWN' and serverState != 'FAILED_NOT_RESTARTABLE'):
                serverState = cmo.getState()
                java.lang.Thread.sleep(5000)
            #print curTime + " " + managed_server_name + ' current State: ' + serverState
        except:
            print "exception"
        #print curTime + " - " + managed_server_name + " - exception while stopping managed server !"
        #dumpStack()
        curTime = SimpleDateFormat("MMM dd, yyyy hh:mm:ss a zzz").format(Date())
        print curTime + " " + "Attempting to start:" + managed_server_name
        cmo.start()
        serverState = cmo.getState()
        while (serverState!='RUNNING'):
            serverState = cmo.getState()
            java.lang.Thread.sleep(5000)
            curTime = SimpleDateFormat("MMM dd, yyyy hh:mm:ss a zzz").format(Date())
            print curTime + " " + managed_server_name + ' current State: ' + serverState
            print curTime +' :Script ran successfully ...' + managed_server_name + " was restarted" 