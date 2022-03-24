@dp.message_handler(text = '📿 Bugungi kun')
async def times(message: types.Message):
	send = await message.answer('⏳')
	await asyncio.sleep(2)
	await bot.delete_message(chat_id=message.chat.id, message_id=send.message_id)
	url = 'http://api.pray.zone/v2/times/today.json?city=khiva'
	work = requests.get(url)
	res = work.json()
	img = Image.open('pic/img.png')
	myFont = ImageFont.truetype('mono.ttf', 48)
	I1 = ImageDraw.Draw(img)
	I1.text((50, 50), f"{datetime.datetime.today().day-1}-Ramazon", font=myFont, fill=(255, 0, 0))
	I1.text((50, 100), f"{datetime.datetime.today().day}-Aprel", font=myFont, fill=(255, 0, 0))
	I1.text((10, 200), f"Saxarlik : {res['results']['datetime'][0]['times']['Fajr']}", font=myFont, fill=(255, 0, 0))
	I1.text((10, 300), f"Iftorlik    : {res['results']['datetime'][0]['times']['Sunset']}", font=myFont, fill=(255, 0, 0))
	img.save("pic/img_t.png")
	bomdod = res['results']['datetime'][0]['times']['Fajr']
	quyosh = res['results']['datetime'][0]['times']['Sunrise']
	peshin = res['results']['datetime'][0]['times']['Dhuhr']
	asr = res['results']['datetime'][0]['times']['Asr']
	shom = res['results']['datetime'][0]['times']['Sunset']
	xufton = res['results']['datetime'][0]['times']['Isha']
	await message.reply_photo(photo=open('pic/img_t.png', 'rb'), caption=f"<b>Ramazon oyi muborak bo'lsin</b>\n\nBugun Ramazonning {datetime.datetime.today().day - 1} - kuni\n<b>Bomdod : {bomdod}\nQuyosh :   {quyosh}\nPeshin :     {peshin}\nAsr :            {asr}\nShom :       {shom}\nXufton :     {xufton}</b>", reply_markup=ramazon_btn, parse_mode='html')
