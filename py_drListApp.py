#1st argv:script, 2nd argv:weblogic username, 3rd argv:weblogic pwd, 4th argv:appName

print('----------Validating the parameters.')
if len(sys.argv) < 4 :
  print('Please provide sufficient parameters!')
  exit();

print('The parameters provided are:')
username=sys.argv[1]
print('username     =    '+username)
password=sys.argv[2]
print('password     =    '+password)
app=sys.argv[3]
print('app          =    '+app)
print('\n')


print('----------Connect to the WebLogic AdminServer')
connect(username,password,'http://weblogic-weblogic-dr.apps.cluster-a3e9.a3e9.sandbox567.opentlc.com:80')
print('\n')

print('----------Deploy application to the WebLogic server')
deplymentsList=cmo.getAppDeployments()
print('AppList ---- ')
print(deplymentsList)


exit()