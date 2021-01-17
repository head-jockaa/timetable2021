# coding:utf-8
import util

def checkContent(html, year, month, day):
	if not year + "年 " + str((int)(month)) + "月" + str((int)(day)) + "日" in html:
		print(year + "_" + month + "_" + day + "_MX.htmlの内容が間違っています")

# html全体を与える
def splitByItem(html):
	splited = html.split("<td class=\"program_set tb_set_mx2")
	splited.pop(0)
	return splited

# splitByItemで切り分けたhtmlを与える
def extractStartTime(html):
	splited1 = html.split("<div class=\"time\">")
	if len(splited1) == 1:
		return ""
	else:
		splited2 = splited1[1].split("</div>")
		result = splited2[0].replace(":","")
		if len(result) == 3:
			result = "0" + result
		return result

# splitByItemで切り分けたhtmlを与える
def extractIcons(html):
	splited1 = html.split("</td>")
	types = []
	if "icon_new" in splited1[0]:
		types.append(util.append_type_name("新"))
	if "icon_re" in splited1[0]:
		types.append(util.append_type_name("再"))
	if "icon_end" in splited1[0]:
		types.append(util.append_type_name("終"))
	if "icon_jimaku" in splited1[0]:
		types.append(util.append_type_name("字"))
	if "icon_2kakokugo" in splited1[0]:
		types.append(util.append_type_name("二"))
	if "icon_kaisetsu" in splited1[0]:
		types.append(util.append_type_name("解"))
	if "icon_data" in splited1[0]:
		types.append(util.append_type_name("デ"))
	if "icon_live" in splited1[0]:
		types.append(util.append_type_name("生"))
	return types

# splitByItemで切り分けたhtmlを与える
def extractTitle(html):
	splited1 = html.split("<strong>")
	splited2 =  splited1[1].split("</strong>")
	return util.sanitize(splited2[0])

# splitByItemで切り分けたhtmlを与える
def extractDescriptions(html):
	splited1 = html.split("</td>")
	splited2 = splited1[0].split("<div class=\"about\">")
	if len(splited2) == 1:
		return ""
	else:
		splited3 = splited2[1].split("</div>")
		return util.sanitize(splited3[0])

def getCategoryCode(title_name):
	if "ニュース" in title_name or "NEWS" in title_name:
		return "100100"
	elif "天気" in title_name:
		return "100101"
	elif "マーケット" in title_name or "MARKET" in title_name:
		return "100104"
	elif "都知事" in title_name:
		return "100109"
	elif "野球" in title_name:
		return "101101"
	elif "テニス" in title_name or "Good Luck!" in title_name:
		return "101104"
	elif "WWE" in title_name:
		return "101105"
	elif "競馬" in title_name:
		return "101110"
	elif "宝塚" in title_name or "CM INDEX" in title_name:
		return "102100"
	elif "特殊詐欺" in title_name:
		return "102102"
	elif "健康バラエティ" in title_name:
		return "102103"
	elif "ショッピング" in title_name:
		return "102104"
	elif "洋上の楽園クルーズ" in title_name:
		return "102105"
	elif "ドラマ" in title_name or "どらま" in title_name or "東京コンフィデンシャル" in title_name or "恋とか愛とか" in title_name or  "桜井真の3つの遺産" in title_name or "ドクターSAKI" in title_name:
		return "103100"
	elif "マイアミ5" in title_name:
		return "103101"
	elif "ミュージック" in title_name or "music" in title_name or "MUSIC" in title_name or "ドリラボ" in title_name:
		return "104100"
	elif "都響" in title_name:
		return "104102"
	elif "ハワイアン" in title_name:
		return "104105"
	elif "HKT" in title_name or "69号室の住人" in title_name or "東京開運散歩" in title_name:
		return "105102"
	elif "よしもと" in title_name:
		return "105103"
	elif "日本グレートスポット紀行" in title_name:
		return "105105"
	elif "PFF" in title_name:
		return "106100"
	elif "キネマ麹町" in title_name:
		return "106101"
	elif "シティーハンター" in title_name:
		return "107100"
	elif "アドベンチャー・タイム" in title_name:
		return "107101"
	elif "とちぎ" in title_name:
		return "108101"
	elif "アートにエールを" in title_name or "日本ふるさと百景" in title_name or "ごりやくさん" in title_name:
		return "108104"
	elif "F.C.TOKYO COLORS" in title_name:
		return "108106"
	elif "大使館" in title_name:
		return "108107"
	elif "釣り" in title_name:
		return "110100"
	elif "わたしの芸術劇場" in title_name or "Tokyo Photo Library" in title_name or "アート・ステージ" in title_name:
		return "110102"
	elif "NAPAC" in title_name:
		return "110105"
	else:
		return "115115"
