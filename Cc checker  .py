import requests
def random():
    url = 'https://www.colorschemer.com/fetchdata/namso-generator/'
    hed = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
        'cache-control': 'no-cache',
        'content-length': '96',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': '__cfduid=d3a24a72dabe36ac486f5980deaa6341e1619540498; csrftoken=znauXaCZm7n1Hv3bvT9ipjki3UWKD0TPVnIzggoYuGU70SlGfQ4j10sxY6XvZ9cc; _ga=GA1.2.1949207860.1619540538; __gads=ID=572c33422f7e3d2d-2251c5edafa70046:T=1619540585:RT=1619540585:S=ALNI_MZ-SMWJOutkbVxZWYiNTx6RDmb3bQ; ezoadgid_263296=-1; ezoref_263296=; ezoab_263296=mod1; lp_263296=https://www.colorschemer.com/credit-card-generator/; ezovuuid_263296=19b81857-1b71-4d15-680a-17ac24c0b66e; ezCMPCCS=true; _gid=GA1.2.331173167.1619941794; _gat_gtag_UA_1328132_1=1; __qca=P0-1330245701-1619941795445; ezovuuidtime_263296=1619941801; ezopvc_263296=2; ezux_ifep_263296=true; ezux_et_263296=17; ezux_tos_263296=22',
        'origin': 'https://www.colorschemer.com',
        'pragma': 'no-cache',
        'referer': 'https://www.colorschemer.com/bin-generator/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        'sec-ch-ua-mobile': '?1',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Mobile Safari/537.36',
        'x-csrftoken': '23DA4G8umgDzVAefixlfWiZwQp4SWCu0o3bFnMUtuPaFeXwK2uggyZ7LLB5DiLNn',
        'x-requested-with': 'XMLHttpRequest',
    }
    data = {
        'bin': '604578',
        'brand': '',
        'quantity': '20',
        'month': 'random',
        'year': 'random',
        'cvv': '',
        'isDateChecked': 'true',
        'isCvvChecked': 'true',
    }
    req = requests.post(url, headers=hed, data=data).text
    print(req)
    input('press enter to close')
def chose():
    binn = input('Enter the bin:')
    cvv=input('Enter your cvv:(press enter to random)')
    url = 'https://www.colorschemer.com/fetchdata/namso-generator/'
    hed = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
        'cache-control': 'no-cache',
        'content-length': '96',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': '__cfduid=d3a24a72dabe36ac486f5980deaa6341e1619540498; csrftoken=znauXaCZm7n1Hv3bvT9ipjki3UWKD0TPVnIzggoYuGU70SlGfQ4j10sxY6XvZ9cc; _ga=GA1.2.1949207860.1619540538; __gads=ID=572c33422f7e3d2d-2251c5edafa70046:T=1619540585:RT=1619540585:S=ALNI_MZ-SMWJOutkbVxZWYiNTx6RDmb3bQ; ezoadgid_263296=-1; ezoref_263296=; ezoab_263296=mod1; lp_263296=https://www.colorschemer.com/credit-card-generator/; ezovuuid_263296=19b81857-1b71-4d15-680a-17ac24c0b66e; ezCMPCCS=true; _gid=GA1.2.331173167.1619941794; _gat_gtag_UA_1328132_1=1; __qca=P0-1330245701-1619941795445; ezovuuidtime_263296=1619941801; ezopvc_263296=2; ezux_ifep_263296=true; ezux_et_263296=17; ezux_tos_263296=22',
        'origin': 'https://www.colorschemer.com',
        'pragma': 'no-cache',
        'referer': 'https://www.colorschemer.com/bin-generator/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        'sec-ch-ua-mobile': '?1',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Mobile Safari/537.36',
        'x-csrftoken': '23DA4G8umgDzVAefixlfWiZwQp4SWCu0o3bFnMUtuPaFeXwK2uggyZ7LLB5DiLNn',
        'x-requested-with': 'XMLHttpRequest',
    }
    data = {
        'bin': binn,
        'brand': '',
        'quantity': '20',
        'month': 'random',
        'year': 'random',
        'cvv': cvv,
        'isDateChecked': 'true',
        'isCvvChecked': 'true',
    }
    req = requests.post(url, headers=hed, data=data).text
    print(req)
    input('press enter to close')
print('''
   _____            _               _             
  / ____|          | |             | |            
 | |     ___    ___| |__   ___  ___| | _____ _ __ 
 | |    / __|  / __| '_ \ / _ \/ __| |/ / _ \ '__|
 | |____ (__  | (__| | | |  __/ (__|   <  __/ |   
  \_____\___|  \___|_| |_|\___|\___|_|\_\___|_|   
                               PY:@127.1.0.0.1
''')
print('1.I have bin \n2.random bin')
pp=input('enter number:')
if pp == '1':
    chose()
elif pp == '2':
    random()