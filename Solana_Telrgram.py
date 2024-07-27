import requests
import time




def time_pg():
    time_pg=time.strftime("%Y-%m-%d   %H:%M.%S", time.localtime())
    return time_pg


print("Start_Script:", time_pg())


def timers():
    try:
        iti =0
        while True:
            iti +=1
            print("Запуск итерацйии", time_pg(), "   Итерация:",iti)
            print("Задержка на 20 минут")
            telegram_sol_()

            time.sleep(1200)

    except OSError:
        print("Error_script_work")


""""#############Binance#########################################################################
print("#####Binance#################################################\033")
url = "https://api.binance.com/api/v3/ticker/price?symbol="

current=('SOLUSDT','BTCUSDT')
iter = 0
for _ in current:
    result=url+current[iter]
    data = requests.get(result)
    iter+=1
    data = data.json()
    #print(data)
    print(f"{data['symbol']} price is {data['price']}")"""

###################BYbit########################################################################

def telegram_sol_():
    urlBubit = "https://api.bybit.com/v5/market/tickers?category=spot&symbol="
    current = ('SOLUSDT', 'BTCUSDT')
    iter_by = 0
    spisok = []
    for _ in current:
        result_by = urlBubit + current[iter_by]
        data = requests.get(result_by)
        datas = data.json()
        iter_by += 1
        result = (f" {datas['result']}")
        # print(result)
        # print(result[43:50],"price is ",result[67:72],"$")
        res = (result[43:50], result[67:72], "$")
        spisok.append(res)

    bot_sms = spisok

    #print(bot_sms)

    ################################################################################
    TOKEN = "7491789551:AAFVK6V4Z7CnCOBS4PoSroBTu76Hx21LEsE"
    chat_id = "-1002076312227"
    message = bot_sms
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url).json()
    #print(requests.get(url).json())


if __name__ == "__main__":
    timers()

