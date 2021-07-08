admin_server_url = 't3://' + ADMIN_HOST + ':' + '7001';
connect('{{ weblogic_admin }}', '{{ weblogic_admin_pass }}', url=admin_server_url)
prps = makePropertiesObject("weblogic.ListenPort=8001")
storeUserConfig(CONFIGURATION_HOME + '/domains/' + DOMAIN_NAME + '/wlst_scripts/userconfigfile.secure', CONFIGURATION_HOME + '/domains/' + DOMAIN_NAME + '/wlst_scripts/userkeyfile.secure')

domain_name = DOMAIN_NAME;

edit()
startEdit()
cd('/SecurityConfiguration/'+ DOMAIN_NAME) # go to MBean object
cmo.setNodeManagerUsername('{{ weblogic_admin }}') # change username
cmo.setNodeManagerPassword('{{ weblogic_admin_pass }}') # change password
save()
activate()

machine_listen_addresses=MACHINE_ADDRESS;
for i in range(len(machine_listen_addresses)):
	edit()
	startEdit()
	
	cd('/Servers/soa_server' + repr(i+1) + '/WebServer/soa_server' + repr(i+1)) # go to MBean object
	# for testing
	if i != 0:
		if machine_listen_addresses[0] == machine_listen_addresses[1]:
			set('FrontendHTTPPort', 8003)
		else:
			set('FrontendHTTPPort', 8001)
	else:
			set('FrontendHTTPPort', 8001)
	set('FrontendHost', machine_listen_addresses[i])
	#Server start up memory arguments
	cd('/Servers/soa_server' + repr(i+1) + '/ServerStart/soa_server' + repr(i+1))
	cmo.setArguments('-Xms6G -Xmx6G')
	cd('/');
	
	cd('/Servers/UCM_server' + repr(i+1) + '/WebServer/UCM_server' + repr(i+1)) # go to MBean object
	
	if i != 0:
		if machine_listen_addresses[0] == machine_listen_addresses[1]:
			set('FrontendHTTPPort', 16202);
		else:
			set('FrontendHTTPPort', 16200);
	else:
			set('FrontendHTTPPort', 16200);
	set('FrontendHost', machine_listen_addresses[i])
	#Server start up memory arguments
	cd('/Servers/UCM_server' + repr(i+1) + '/ServerStart/UCM_server' + repr(i+1))
	cmo.setArguments('-Xms512m -Xmx512m')
	cd('/');
	
	cd('/Servers/osb_server' + repr(i+1) + '/WebServer/osb_server' + repr(i+1)) # go to MBean object
	
	if i != 0:
		if machine_listen_addresses[0] == machine_listen_addresses[1]:
			set('FrontendHTTPPort', 8013);
		else:
			set('FrontendHTTPPort', 8011);
	else:
			set('FrontendHTTPPort', 8011);
	set('FrontendHost', machine_listen_addresses[i])
	#Server start up memory arguments
	cd('/Servers/osb_server' + repr(i+1) + '/ServerStart/osb_server' + repr(i+1))
	cmo.setArguments('-Xms512m -Xmx512m')
	cd('/');
	
	cd('/Servers/iui_server' + repr(i+1) + '/WebServer/iui_server' + repr(i+1)) # go to MBean object
	# for testing
	if i != 0:
		if machine_listen_addresses[0] == machine_listen_addresses[1]:
			set('FrontendHTTPPort', 7013);
		else:
			set('FrontendHTTPPort', 7011);
	else:
			set('FrontendHTTPPort', 7011);
	set('FrontendHost', machine_listen_addresses[i])
	#Server start up memory arguments
	cd('/Servers/iui_server' + repr(i+1) + '/ServerStart/iui_server' + repr(i+1))
	cmo.setArguments('-Xms4G -Xmx4G')
	cd('/');
	
	save()
	activate()

#Datasource EBSDS configuration
dsName=EBS_DATASOURCE_NAME
dsFileName=EBS_DATASOURCE_FILENAME
dsDatabaseName=EBS_DATASOURCE_DATABASE_NAME
datasourceTarget1=EBS_DATASOURCE_TARGET1
dsJNDIName=EBS_DATASOURCE_JNDINAME
dsDriverName=EBS_DATASOURCE_DRIVER_CLASS
dsURL=EBS_DATASOURCE_URL
dsUserName=EBS_DATASOURCE_USERNAME
dsPassword=EBS_DATASOURCE_PASSWORD
dsTestQuery=EBS_DATASOURCE_TEST_QUERY

edit()
startEdit()
cd('/')
cmo.createJDBCSystemResource(dsName)
cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName)
cmo.setName(dsName)

cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDataSourceParams/' + dsName )
set('JNDINames',jarray.array([String(dsJNDIName)], String))

cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDriverParams/' + dsName )
cmo.setUrl(dsURL)
cmo.setDriverName( dsDriverName )
cmo.setPassword(dsPassword)

cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCConnectionPoolParams/' + dsName )
cmo.setTestTableName(dsTestQuery)
cmo.setMaxCapacity(100)

cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDriverParams/' + dsName + '/Properties/' + dsName )
cmo.createProperty('user')

cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDriverParams/' + dsName + '/Properties/' + dsName + '/Properties/user')
cmo.setValue(dsUserName)

cd('/SystemResources/' + dsName )
if len(machine_listen_addresses) > 1:
	set('Targets',jarray.array([ObjectName('com.bea:Name=soa_cluster,Type=Cluster')], ObjectName))
else:
	set('Targets',jarray.array([ObjectName('com.bea:Name=soa_server1,Type=Server')], ObjectName))
save()
activate()
	
	
#Datasource INVDB configuration
dsName=INVDB_DATASOURCE_NAME
dsFileName=INVDB_DATASOURCE_FILENAME
dsDatabaseName=INVDB_DATASOURCE_DATABASE_NAME
datasourceTarget=INVDB_DATASOURCE_TARGET
dsJNDIName=INVDB_DATASOURCE_JNDINAME
dsDriverName=INVDB_DATASOURCE_DRIVER_CLASS
dsURL=INVDB_DATASOURCE_URL
dsUserName=INVDB_DATASOURCE_USERNAME
dsPassword=INVDB_DATASOURCE_PASSWORD
dsTestQuery=INVDB_DATASOURCE_TEST_QUERY

edit()
startEdit()
cd('/')
cmo.createJDBCSystemResource(dsName)
cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName)
cmo.setName(dsName)

cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDataSourceParams/' + dsName )
set('JNDINames',jarray.array([String(dsJNDIName)], String))

cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDriverParams/' + dsName )
cmo.setUrl(dsURL)
cmo.setDriverName( dsDriverName )
cmo.setPassword(dsPassword)

cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCConnectionPoolParams/' + dsName )
cmo.setTestTableName(dsTestQuery)
cmo.setMaxCapacity(100)
cmo.setWrapTypes(false)

cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDriverParams/' + dsName + '/Properties/' + dsName )
cmo.createProperty('user')

cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDriverParams/' + dsName + '/Properties/' + dsName + '/Properties/user')
cmo.setValue(dsUserName)

cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDataSourceParams/' + dsName )
cmo.setGlobalTransactionsProtocol('None')

cd('/SystemResources/' + dsName )
if len(machine_listen_addresses) > 1:
	set('Targets',jarray.array([ObjectName('com.bea:Name=soa_cluster,Type=Cluster')], ObjectName))
else:
	set('Targets',jarray.array([ObjectName('com.bea:Name=soa_server1,Type=Server')], ObjectName))

save()
activate()

#Datasource INVDBUI configuration
dsName=INVDBUI_DATASOURCE_NAME
dsFileName=INVDBUI_DATASOURCE_FILENAME
dsDatabaseName=INVDB_DATASOURCE_DATABASE_NAME
datasourceTarget=INVDBUI_DATASOURCE_TARGET
dsJNDIName=INVDBUI_DATASOURCE_JNDINAME
dsDriverName=INVDB_DATASOURCE_DRIVER_CLASS
dsURL=INVDB_DATASOURCE_URL
dsUserName=INVDB_DATASOURCE_USERNAME
dsPassword=INVDB_DATASOURCE_PASSWORD
dsTestQuery=INVDB_DATASOURCE_TEST_QUERY

edit()
startEdit()
cd('/')
cmo.createJDBCSystemResource(dsName)
cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName)
cmo.setName(dsName)

cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDataSourceParams/' + dsName )
set('JNDINames',jarray.array([String(dsJNDIName)], String))

cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDriverParams/' + dsName )
cmo.setUrl(dsURL)
cmo.setDriverName( dsDriverName )
cmo.setPassword(dsPassword)

cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCConnectionPoolParams/' + dsName )
cmo.setTestTableName(dsTestQuery)
cmo.setMaxCapacity(100)
cmo.setWrapTypes(false)

cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDriverParams/' + dsName + '/Properties/' + dsName )
cmo.createProperty('user')

cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDriverParams/' + dsName + '/Properties/' + dsName + '/Properties/user')
cmo.setValue(dsUserName)

cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDataSourceParams/' + dsName )
cmo.setGlobalTransactionsProtocol('None')

cd('/SystemResources/' + dsName )
if len(machine_listen_addresses) > 1:
	set('Targets',jarray.array([ObjectName('com.bea:Name=iui_cluster,Type=Cluster')], ObjectName))
else:
	set('Targets',jarray.array([ObjectName('com.bea:Name=iui_server1,Type=Server')], ObjectName))

save()
activate()
	
# DBAdapter configuration for APPS don't change these ones
uniqueString         = ''
appName              = 'DbAdapter'
moduleOverrideName   = appName+'.rar'
moduleDescriptorName = 'META-INF/weblogic-ra.xml'
eisName=APPS_EIS_NAME
datasourceTarget1=EBS_DATASOURCE_TARGET1
dsName=EBS_DATASOURCE_JNDINAME

def makeDeploymentPlanVariable(wlstPlan, name, value, xpath, origin='planbased'):
  """Create a varaible in the Plan.
  This method is used to create the variables that are needed in the Plan in order
  to add an entry for the outbound connection pool for the new data source.
  """
 
  try:
    variableAssignment = wlstPlan.createVariableAssignment(name, moduleOverrideName, moduleDescriptorName)
    variableAssignment.setXpath(xpath)
    variableAssignment.setOrigin(origin)
    wlstPlan.createVariable(name, value)
 
  except:
    print('--> was not able to create deployment plan variables successfully')

#uniqueString = str(int(time.time()))	
edit()
startEdit()
cd('/')
# update the deployment plan

print('--> about to update the deployment plan for the DbAdapter')
startEdit()
planPath = Oracle_SOA1_HOME + '/soa/connectors/DbAdapterPlan/Plan.xml'
appPath = get('/AppDeployments/DbAdapter/SourcePath')
print('--> Using plan ' + repr(planPath))
plan = loadApplication(appPath, planPath)
print('--> adding variables to plan')
makeDeploymentPlanVariable(plan, 'ConnectionInstance_' + eisName + '_JNDIName_' + uniqueString, eisName, '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="' + eisName + '"]/jndi-name')
makeDeploymentPlanVariable(plan, 'ConfigProperty_xADataSourceName_'+ dsName + uniqueString, dsName, '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="' + eisName + '"]/connection-properties/properties/property/[name="xADataSourceName"]/value')

print('--> saving plan')
plan.save();
save();
print('--> activating changes')
activate(block='true');
cd('/AppDeployments/DbAdapter/Targets');
print('--> redeploying the DbAdapter')
redeploy(appName, planPath, targets=cmo.getTargets());
print('--> done')


# DBAdapter configuration for INVDB don't change these ones
uniqueString         = ''
appName              = 'DbAdapter'
moduleOverrideName   = appName+'.rar'
moduleDescriptorName = 'META-INF/weblogic-ra.xml'
eisName=INVDB_EIS_NAME
datasourceTarget=INVDB_DATASOURCE_TARGET
dsName=INVDB_DATASOURCE_JNDINAME

#uniqueString = str(int(time.time()))
edit()
startEdit()
cd('/')
# update the deployment plan

print('--> about to update the deployment plan for the DbAdapter')
planPath = Oracle_SOA1_HOME + '/soa/connectors/DbAdapterPlan/Plan.xml'
appPath = get('/AppDeployments/DbAdapter/SourcePath')
print('--> Using plan ' + repr(planPath))
plan = loadApplication(appPath, planPath)
print('--> adding variables to plan')
makeDeploymentPlanVariable(plan, 'ConnectionInstance_' + eisName + '_JNDIName_' + uniqueString, eisName, '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="' + eisName + '"]/jndi-name')
makeDeploymentPlanVariable(plan, 'ConfigProperty_DataSourceName_'+ dsName + uniqueString, dsName, '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="' + eisName + '"]/connection-properties/properties/property/[name="dataSourceName"]/value')

print('--> saving plan')
plan.save();
save();
print('--> activating changes')
activate(block='true');
cd('/AppDeployments/DbAdapter/Targets');
print('--> redeploying the DbAdapter')
redeploy(appName, planPath, targets=cmo.getTargets());
print('--> done')

edit()
startEdit()

print 'Creating JMS Server'
cd('/')
print 'Creating JMS Server.'
cmo.createJMSServer('IUIJmsServer')
cd('/JMSServers/IUIJmsServer')
cmo.setTemporaryTemplateResource(None)
cmo.setTemporaryTemplateName(None)
if len(machine_listen_addresses) > 1:
	cmo.addTarget(getMBean('/Servers/soa_cluster'))
else:
	cmo.addTarget(getMBean('/Servers/soa_server1'))

print 'Creating JMS Module'
cd('/')
cmo.createJMSSystemResource('IUIJmsModule')
cd('/JMSSystemResources/IUIJmsModule')
if len(machine_listen_addresses) > 1:
	cmo.addTarget(getMBean('/Servers/soa_cluster'))
else:
	cmo.addTarget(getMBean('/Servers/soa_server1'))

cmo.createSubDeployment('IUISubDeployment')

print 'Creating Connection Factory'
cd('/')
cd('/JMSSystemResources/IUIJmsModule/JMSResource/IUIJmsModule')
cmo.createConnectionFactory('IUIConnectionFactory')
cd('/JMSSystemResources/IUIJmsModule/JMSResource/IUIJmsModule/ConnectionFactories/IUIConnectionFactory')
cmo.setJNDIName('jms/IUIConnectionFactory')
set('SubDeploymentName','IUISubDeployment')
cd('/JMSSystemResources/IUIJmsModule/JMSResource/IUIJmsModule/ConnectionFactories/IUIConnectionFactory/SecurityParams/IUIConnectionFactory')
cmo.setAttachJMSXUserId(false)
cd('/JMSSystemResources/IUIJmsModule/JMSResource/IUIJmsModule/ConnectionFactories/IUIConnectionFactory/ClientParams/IUIConnectionFactory')
cmo.setClientIdPolicy('Restricted')
cmo.setSubscriptionSharingPolicy('Exclusive')
cmo.setMessagesMaximum(10)
cd('/JMSSystemResources/IUIJmsModule/JMSResource/IUIJmsModule/ConnectionFactories/IUIConnectionFactory/TransactionParams/IUIConnectionFactory')
cmo.setXAConnectionFactoryEnabled(true)
cd('/JMSSystemResources/IUIJmsModule/JMSResource/IUIJmsModule/ConnectionFactories/IUIConnectionFactory')
cmo.setDefaultTargetingEnabled(false)

print 'Creating Topic'
cd('/')
cd('/JMSSystemResources/IUIJmsModule/JMSResource/IUIJmsModule')
cmo.createTopic('IUIJmsTopic')
cd('/JMSSystemResources/IUIJmsModule/JMSResource/IUIJmsModule/Topics/IUIJmsTopic')
set('JNDIName','jms/IUIJmsTopic')
set('SubDeploymentName','IUISubDeployment')
cd('/JMSSystemResources/IUIJmsModule/SubDeployments/IUISubDeployment')
cmo.addTarget(getMBean('/JMSServers/IUIJmsServer'))

print 'JMS Resources are Successfully Created'
activate()

# JmsAdapter configuration
uniqueString         = ''
appName              = 'JmsAdapter'
moduleOverrideName   = appName+'.rar'
moduleDescriptorName = 'META-INF/weblogic-ra.xml'
eisName='eis/wls/IUITopic'
connectionFactoryLoc='jms/IUIConnectionFactory'

def makeDeploymentPlanVariable(wlstPlan, name, value, xpath, origin='planbased'):
  """Create a varaible in the Plan.
  This method is used to create the variables that are needed in the Plan in order
  to add an entry for the outbound connection pool for the new data source.
  """
 
  try:
    variableAssignment = wlstPlan.createVariableAssignment(name, moduleOverrideName, moduleDescriptorName)
    variableAssignment.setXpath(xpath)
    variableAssignment.setOrigin(origin)
    wlstPlan.createVariable(name, value)
 
  except:
    print('--> was not able to create deployment plan variables successfully')

edit()
startEdit()
cd('/')
# update the deployment plan

print('--> about to update the deployment plan for the JmsAdapter')
startEdit()
planPath = Oracle_SOA1_HOME + '/soa/connectors/JmsAdapterPlan/Plan.xml'
appPath = get('/AppDeployments/JmsAdapter/SourcePath')
print('--> Using plan ' + repr(planPath))
plan = loadApplication(appPath, planPath)
print('--> adding variables to plan')

makeDeploymentPlanVariable(plan, 'ConnectionInstance_eis/wls/IUITopic_JNDIName_' + uniqueString, eisName, '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="oracle.tip.adapter.jms.IJmsConnectionFactory"]/connection-instance/[jndi-name="' + eisName + '"]/jndi-name')
makeDeploymentPlanVariable(plan, 'ConfigProperty_ConnectionFactoryLocation_Value_' + uniqueString, connectionFactoryLoc, '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="oracle.tip.adapter.jms.IJmsConnectionFactory"]/connection-instance/[jndi-name="' + eisName + '"]/connection-properties/properties/property/[name="ConnectionFactoryLocation"]/value')
makeDeploymentPlanVariable(plan, 'ConfigProperty_IsTopic_Value_' + uniqueString, 'true', '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="oracle.tip.adapter.jms.IJmsConnectionFactory"]/connection-instance/[jndi-name="' + eisName + '"]/connection-properties/properties/property/[name="IsTopic"]/value')
print('--> saving plan')
plan.save();
save();
print('--> activating changes')
activate(block='true');
cd('/AppDeployments/JmsAdapter/Targets');
print('--> redeploying the JmsAdapter')
print(appName, planPath)
redeploy(appName, planPath, targets=cmo.getTargets());
print('--> done')


edit()
startEdit()

print 'Creating Email JMS JDBC Store'
cd('/')
cmo.createJDBCStore('EmailJmsJDBCStore')
cd('/JDBCStores/EmailJmsJDBCStore')
cmo.setDataSource(getMBean('/SystemResources/INVDB'))
cmo.setPrefixName('INSPY')
if len(machine_listen_addresses) > 1:
	set('Targets',jarray.array([ObjectName('com.bea:Name=soa_cluster,Type=Cluster')], ObjectName))
else:
	set('Targets',jarray.array([ObjectName('com.bea:Name=soa_server1,Type=Server')], ObjectName))

print 'Creating JMS Server'
cd('/')
cmo.createJMSServer('EmailJmsServer')
cd('/JMSServers/EmailJmsServer')
cmo.setTemporaryTemplateResource(None)
cmo.setTemporaryTemplateName(None)
cmo.setPersistentStore(getMBean('/JDBCStores/EmailJmsJDBCStore'))
if len(machine_listen_addresses) > 1:
	cmo.addTarget(getMBean('/Servers/soa_cluster'))
else:
	cmo.addTarget(getMBean('/Servers/soa_server1'))

print 'Creating JMS Module'
cd('/')
cmo.createJMSSystemResource('EmailJmsModule')
cd('/JMSSystemResources/EmailJmsModule')
if len(machine_listen_addresses) > 1:
	cmo.addTarget(getMBean('/Servers/soa_cluster'))
else:
	cmo.addTarget(getMBean('/Servers/soa_server1'))
cmo.createSubDeployment('EmailSubDeployment')

print 'Creating Connection Factory'
cd('/')
cd('/JMSSystemResources/EmailJmsModule/JMSResource/EmailJmsModule')
cmo.createConnectionFactory('EmailConnectionFactory')
cd('/JMSSystemResources/EmailJmsModule/JMSResource/EmailJmsModule/ConnectionFactories/EmailConnectionFactory')
cmo.setJNDIName('jms/EmailConnectionFactory')
set('SubDeploymentName','EmailSubDeployment')
cd('/JMSSystemResources/EmailJmsModule/JMSResource/EmailJmsModule/ConnectionFactories/EmailConnectionFactory/SecurityParams/EmailConnectionFactory')
cmo.setAttachJMSXUserId(false)
cd('/JMSSystemResources/EmailJmsModule/JMSResource/EmailJmsModule/ConnectionFactories/EmailConnectionFactory/ClientParams/EmailConnectionFactory')
cmo.setClientIdPolicy('Restricted')
cmo.setSubscriptionSharingPolicy('Exclusive')
cmo.setMessagesMaximum(10)
cd('/JMSSystemResources/EmailJmsModule/JMSResource/EmailJmsModule/ConnectionFactories/EmailConnectionFactory/TransactionParams/EmailConnectionFactory')
cmo.setXAConnectionFactoryEnabled(true)
cd('/JMSSystemResources/EmailJmsModule/JMSResource/EmailJmsModule/ConnectionFactories/EmailConnectionFactory')
cmo.setDefaultTargetingEnabled(false)

print 'Creating Queue'
cd('/')
cd('/JMSSystemResources/EmailJmsModule/JMSResource/EmailJmsModule')
cmo.createQueue('EmailJmsQueue')
cd('/JMSSystemResources/EmailJmsModule/JMSResource/EmailJmsModule/Queues/EmailJmsQueue')
set('JNDIName','jms/EmailJmsQueue')
set('SubDeploymentName','EmailSubDeployment')
cd('/JMSSystemResources/EmailJmsModule/SubDeployments/EmailSubDeployment')
cmo.addTarget(getMBean('/JMSServers/EmailJmsServer'))

print 'JMS Resources are Successfully Created'
activate()


#Data Source Capacity Configuration
dsName='SOADataSource'
cd('/')

cd('config:/JDBCConnectionPools/'+dsName)
cmo.setXASetTransactionTimeout(1)

#for JTA Transaction
edit()
startEdit()
cd('/JTA/' + DOMAIN_NAME)
cmo.setTimeoutSeconds(3600)
save()
activate()

##Creating sample users in DefaultAuthenticator ##
print 'CREATE SAMPLE USERS'
edit()
startEdit(-1,-1,'false')
serverConfig()
cd('/SecurityConfiguration/'+domain_name+'/Realms/myrealm/AuthenticationProviders/DefaultAuthenticator')

print 'create group AP_INSPYRUS_EBS'
ap_group = 'AP_INSPYRUS_EBS'
cmo.createGroup(ap_group,ap_group)

print 'create group AP_MGR_INSPYRUS_EBS'
ap_mgr_group = 'AP_MGR_INSPYRUS_EBS'
cmo.createGroup(ap_mgr_group,ap_mgr_group)

user = 'ap.processor@ebs.inspyrus.com'    
password = 'InspyrusDemo1'
print 'create user: ',user
cmo.createUser(user,password,user)
cmo.addMemberToGroup(ap_group,user)

user = 'requester@ebs.inspyrus.com'
print 'create user: ',user
cmo.createUser(user,password,user)
cmo.addMemberToGroup(ap_group,user)

user = 'manager@ebs.inspyrus.com'
print 'create user: ',user
cmo.createUser(user,password,user)
cmo.addMemberToGroup(ap_group,user)
cmo.addMemberToGroup(ap_mgr_group,user)

edit()
undo(defaultAnswer='y', unactivatedChanges='true')
stopEdit('y')

shutdown(block='true')