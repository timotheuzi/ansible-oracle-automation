
cd('/')
cmo.createJDBCSystemResource('INV_DB_MOBILE')

cd('/JDBCSystemResources/INV_DB_MOBILE/JDBCResource/INV_DB_MOBILE')
cmo.setName('INV_DB_MOBILE')

cd('/JDBCSystemResources/INV_DB_MOBILE/JDBCResource/INV_DB_MOBILE/JDBCDataSourceParams/INV_DB_MOBILE')
set('JNDINames',jarray.array([String('jndi/inv_db_mobile')], String))

cd('/JDBCSystemResources/INV_DB_MOBILE/JDBCResource/INV_DB_MOBILE/JDBCDriverParams/INV_DB_MOBILE')
cmo.setUrl('jdbc:oracle:thin:@192.168.0.38:1521:xe')
cmo.setDriverName('oracle.jdbc.xa.client.OracleXADataSource')
setEncrypted('Password', 'Password_1526337744273', '/oracle/Middleware_Home/user_projects/domains/test_domain/Script1526337693730Config', '/oracle/Middleware_Home/user_projects/domains/test_domain/Script1526337693730Secret')

cd('/JDBCSystemResources/INV_DB_MOBILE/JDBCResource/INV_DB_MOBILE/JDBCConnectionPoolParams/INV_DB_MOBILE')
cmo.setTestTableName('SQL SELECT 1 FROM DUAL\r\n')

cd('/JDBCSystemResources/INV_DB_MOBILE/JDBCResource/INV_DB_MOBILE/JDBCDriverParams/INV_DB_MOBILE/Properties/INV_DB_MOBILE')
cmo.createProperty('user')

cd('/JDBCSystemResources/INV_DB_MOBILE/JDBCResource/INV_DB_MOBILE/JDBCDriverParams/INV_DB_MOBILE/Properties/INV_DB_MOBILE/Properties/user')
cmo.setValue('inspy_ap')

cd('/JDBCSystemResources/INV_DB_MOBILE/JDBCResource/INV_DB_MOBILE/JDBCDataSourceParams/INV_DB_MOBILE')
cmo.setGlobalTransactionsProtocol('TwoPhaseCommit')

cd('/SystemResources/INV_DB_MOBILE')
set('Targets',jarray.array([ObjectName('com.bea:Name=iui_server1,Type=Server')], ObjectName))

activate()

startEdit()

