from imports import *
import aiogram

async def sistem_number(number):
    number = (number).replace('е', 'e').replace('k', 'к').replace('к', '000')
    number = int(float(number))

    return number

async def scor_summ(number):
    if int(number) in range(0, 1000):
        number3 = number
    if int(number) in range(1000, 999999):
        number1 = number / 1000
        number2 = round(number1)
        number3 = f'{number2} тыщ'
    if int(number) in range(1000000, 999999999):
        number1 = number / 1000000
        number2 = round(number1)
        number3 = f'{number2} млн'
    if int(number) in range(1000000000, 999999999999):
        number1 = number / 1000000000
        number2 = round(number1)
        number3 = f'{number2} млрд'
    if int(number) in range(1000000000000, 999999999999999):
        number1 = number / 1000000000000
        number2 = round(number1)
        number3 = f'{number2} трлн'
    if int(number) in range(1000000000000000, 999999999999999999):
        number1 = number / 1000000000000000
        number2 = round(number1)
        number3 = f'{number2} квдр'
    if int(number) in range(1000000000000000000, 999999999999999999999):
        number1 = number / 1000000000000000000
        number2 = round(number1)
        number3 = f'{number2} квнт'
    if int(number) in range(1000000000000000000000, 999999999999999999999999):
        number1 = number / 1000000000000000000000
        number2 = round(number1)
        number3 = f'{number2} скст'
    if int(number) in range(1000000000000000000000000, 999999999999999999999999999):
        number1 = number / 1000000000000000000000000
        number2 = round(number1)
        number3 = f'{number2} трикс'
    if int(number) in range(1000000000000000000000000000,999999999999999999999999999999):
        number1 = number / 1000000000000000000000000000
        number2 = round(number1)
        number3 = f'{number2} твинкс'
    if int(number) in range(1000000000000000000000000000000, 999999999999999999999999999999999):
        number1 = number / 1000000000000000000000000000000
        number2 = round(number1)
        number3 = f'{number2} септ'
    if int(number) in range(1000000000000000000000000000000000, 999999999999999999999999999999999999):
        number1 = number / 1000000000000000000000000000000000
        number2 = round(number1)
        number3 = f'{number2} октл'
    if int(number) in range(1000000000000000000000000000000000000, 999999999999999999999999999999999999999):
        number1 = number / 1000000000000000000000000000000000000
        number2 = round(number1)
        number3 = f'{number2} нонл'
    if int(number) in range(1000000000000000000000000000000000000000, 999999999999999999999999999999999999999999):
        number1 = number / 1000000000000000000000000000000000000000
        number2 = round(number1)
        number3 = f'{number2} декал'
    if int(number) in range(1000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999):
        number1 = number / 1000000000000000000000000000000000000000000
        number2 = round(number1)
        number3 = f'{number2} эндк'
    if int(number) in range(1000000000000000000000000000000000000000000000,999999999999999999999999999999999999999999999999):
        number1 = number / 1000000000000000000000000000000000000000000000
        number2 = round(number1)
        number3 = f'{number2} доктл'
    if int(number) in range(1000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999) :
        number1 = number / 1000000000000000000000000000000000000000000000000
        number2 = round(number1)
        number3 = f'{number2} гугл'
    if int(number) in range(1000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999) :
        number1 = number / 1000000000000000000000000000000000000000000000000000
        number2 = round(number1)
        number3 = f'{number2} кинд'
    if int(number) in range(1000000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999999) :
        number1 = number / 1000000000000000000000000000000000000000000000000000000
        number2 = round(number1)
        number3 = f'{number2} трипт'
    if int(number) in range(1000000000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999999999) :
        number1 = number / 1000000000000000000000000000000000000000000000000000000000
        number2 = round(number1)
        number3 = f'{number2} срист'
    if int(number) in range(1000000000000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999999999999):
        number1 = number / 1000000000000000000000000000000000000000000000000000000000000
        number2 = round(number1)
        number3 = f'{number2} манит'
    if int(number) in range(1000000000000000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999999999999999):
        number1 = number / 1000000000000000000000000000000000000000000000000000000000000000
        number2 = round(number1)
        number3 = f'{number2} гвинт'
    if int(number) in range(1000000000000000000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999999999999999999):
        number1 = number / 1000000000000000000000000000000000000000000000000000000000000000000
        number2 = round(number1)
        number3 = f'{number2} ланит'
    if int(number) in range(1000000000000000000000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999999999999999999999):
        number1 = number / 1000000000000000000000000000000000000000000000000000000000000000000000
        number2 = round(number1)
        number3 = f'{number2} октит'
    if int(number) in range(1000000000000000000000000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999999999999999999999999):
        number1 = number / 1000000000000000000000000000000000000000000000000000000000000000000000000
        number2 = round(number1)
        number3 = f'{number2} новит'
    if int(number) in range(1000000000000000000000000000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999999999999999999999999999):
        number1 = number / 1000000000000000000000000000000000000000000000000000000000000000000000000000
        number2 = round(number1)
        number3 = f'{number2} унд'
    if int(number) in range(1000000000000000000000000000000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999999999999999999999999999999):
        number1 = number / 1000000000000000000000000000000000000000000000000000000000000000000000000000000
        number2 = round(number1)
        number3 = f'{number2} конт'
    if int(number) in range(1000000000000000000000000000000000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999999999999999999999999999999999):
        number1 = number / 1000000000000000000000000000000000000000000000000000000000000000000000000000000000
        number2 = round(number1)
        number3 = f'{number2} тент' 
    if int(number) >= 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000:
        number1 = number / 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        number2 = round(number1)
        number3 = f'{number2} фенд'
    if int(number) >= 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000:
        number1 = number / 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        number2 = round(number1)
        number3 = f'{number2} внат'

    return number3

async def advertising_utils(number, message):

    text = f'''
ИГРОВОЙ БОТ ПАПРИК 🌶

💠 КРИПТО ВАЛЮТА
- Иметься 4 крипто валюты а точнее такие как ETHEREUM 🟣, BITCOIN 🟠, LITECOIN ⚪️, MAKER 🔵. Все они работают по настоящему курсу.

🎰 КАЗИНО
- У нас казино которого нету не в одном из русскоязычных игровых ботов , оно особенно тем, что игра идёт не с ботом, а между играми.

👶 УРОВНИ И ЗАДАНИЯ
- В боте у тебя не будет сразу доступ ко всему, для начала тебе прийдётся пройти начальные задания для получения уровня, чем больше уровень, тем больше возможностей

🌅 АВАТАРКИ
- В боте вы сможете поставить любую аватарку , гифку себе на баланс . Начиная от своей Аватарки с тг, и заканчивая любой гифкой/видео с интернета

🛰 МАЙНИНГ ФЕРМА
- В боте есть Майнинг ферма , с которой вы можете зарабатывать каждую секунду , а доход зависит от уровня дома 

🤝 ПЕРЕПРОДАЖИ
- В боте можно перепродавать ресурсы игрокам , и с помощью этого заработать довольно неплохие деньги

📊 ЭКОНОМИКА
- В боте Отличная экономика, что даёт понять что обнуление будут раз в несколько месяцев

👶 ИНСТРУКЦИЯ
- В боте имеется даже инструкция для новых игроков, с помощью который вы сможете ознакомиться с ботом и его функционалом и она вам поможет прокачаться в боте

👾 БОТ - @paprikgamebot
💭 ЧАТ - @paprikchat
'''

    if number == 1:

        return await message.answer( parse_mode='html')
    
    elif number == 2:

        add = cursor.execute('SELECT * FROM users').fetchall()


        number_user_on = 0
        number_user_off = 0
        all_number = 0
        await message.answer('🔈 Реклама началась, ждите результатов...')

        for user in add:
            all_number += 1
            try:
                await message.bot.send_message(user[0], text, parse_mode='html')
                number_user_on += 1
                # await message.answer(f'✅ На ID: <code>{user[0]}</code>. Пришло сообщение', parse_mode='html')
            except:
                number_user_off += 1
                # await message.answer(f'⛔️ На ID: <code>{user[0]}</code>. Не пришло сообщение', parse_mode='html')
            
            if all_number in [1000, 2500, 5000, 10000, 20000, 40000, 80000, 160000, 320000]:
                await message.answer(f"🔉 Уже отправленых сообщений: {'{:,}'.format(all_number).replace(',','.')} шт.")
        text2 = f'''
📢 Результаты рекламы:

✅ Количество получателей: <code>{'{:,}'.format(number_user_on).replace(',','.')} игроков</code>
⛔️ Количество не получивших: <code>{'{:,}'.format(number_user_off).replace(',','.')} игроков</code>
        '''
        await message.answer(f'<b>🔊 РЕКЛАМА:</b>', parse_mode='html')
        await message.answer(text, parse_mode='html')
        await message.answer(text2, parse_mode='html')