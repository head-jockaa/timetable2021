# coding:utf-8
import util

def checkContent(html, year, month, day):
	if not "<a href=date1>" + str((int)(month)) + "月" + str((int)(day)) + "日" in html:
		print(year + "_" + month + "_" + day + "_SUN.htmlの内容が間違っています")

def extractTodays(html):
	splited = html.split("<a href=date")
	return splited[1]

# extractTodaysで切り分けたhtmlを与える
def splitByItem(html):
	splited = html.split("class='box sv2")
	splited.pop(0)
	return splited

# splitByItemで切り分けたhtmlを与える
def extractStartTime(html):
	splited1 = html.split("<span class='st-time'>")
	splited2 = splited1[1].split("</span>")
	return splited2[0].replace(":","")

# splitByItemで切り分けたhtmlを与える
def extractIcons(html):
	splited1 = html.split("</script>")
	types = []
	if "prg-icon-new" in splited1[0]:
		types.append(util.append_type_name("新"))
	if "prg-icon-re" in splited1[0]:
		types.append(util.append_type_name("再"))
	if "prg-icon-end" in splited1[0]:
		types.append(util.append_type_name("終"))
	if "prg-icon-sub" in splited1[0]:
		types.append(util.append_type_name("字"))
	if "prg-icon-lang" in splited1[0]:
		types.append(util.append_type_name("二"))
	if "prg-icon-cmnt" in splited1[0]:
		types.append(util.append_type_name("解"))
	if "prg-icon-sign" in splited1[0]:
		types.append(util.append_type_name("手"))
	if "prg-icon-ss" in splited1[0]:
		types.append(util.append_type_name("SS"))
	if "prg-icon-dubb" in splited1[0]:
		types.append(util.append_type_name("吹"))
	if "prg-icon-sec" in splited1[0]:
		types.append(util.append_type_name("多"))
	if "prg-icon-fp" in splited1[0]:
		types.append(util.append_type_name("前"))
	if "prg-icon-lp" in splited1[0]:
		types.append(util.append_type_name("後"))
	return types

# splitByItemで切り分けたhtmlを与える
def extractTitle(html):
	splited1 = html.split("<span class='st-title'>")
	if len(splited1) == 1:
		return ""
	else:
		splited2 =  splited1[1].split("</span>")
		if "<a " in splited2[0]:
			splited3 = splited2[0].split(">")
			splited4 = splited3[1].split("</a")
			return util.sanitize(splited4[0])
		else:
			return util.sanitize(splited2[0])

# splitByItemで切り分けたhtmlを与える
def extractDescription(html):
	title_name = extractTitle(html)
	if title_name == "KOBE元気!いきいき!!体操":
		return "◇神戸市福祉局と連携し、高齢者の運動不足・ストレス解消のための介護予防体操プログラムやフレイル予防の取り組みを紹介!健康にまつわるミニ講座も。"
	elif title_name == "東京マーケットワイド":
		return "毎日の株価の動きを東証Arrowsスタジオから実況中継。ストックボイスが誇る経済キャスター陣と多彩なゲストを迎え、株・為替・商品・海外市場の動きをリアルタイムで解説"

	splited1 = html.split("</script>")
	splited2 = splited1[0].split("<p class='st-detail'>")
	if len(splited2) == 1:
		return ""
	else:
		splited3 =  splited2[1].split("</p>")
		return util.sanitize(splited3[0].replace("<span class='st-number'>","").replace("<span class='st-detailtxt'>","").replace("</span>",""))

# splitByItemで切り分けたhtmlを与える
def getInterval(html):
	splited1 = html.split("style=height:")
	splited2 = splited1[1].split("px")
	return round((int)(splited2[0]) / 5)

def getCategoryCode(title_name):
	if "体操" in title_name:
		return "110111"
	elif "マーケット" in title_name:
		return "100104"
	elif title_name == "衆院選" or title_name == "市長選":
		return "100108"
	elif title_name == "兵庫県議会中継":
		return "100109"
	elif title_name == "5時に夢中!":
		return "102100"
	else:
		return "115115"
