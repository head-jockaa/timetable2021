# coding:utf-8
import os
import math
import datetime
import util
import tvlist
import nhk

base64_special = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","@","$","{","|","}",";","*","_","~","^","`","'"]

def get_station_name(s):
	if s == "G10":
		return "ＮＨＫ総合１・札幌"
	elif s == "G11":
		return "ＮＨＫ総合１・函館"
	elif s == "G12":
		return "ＮＨＫ総合１・旭川"
	elif s == "G13":
		return "ＮＨＫ総合１・帯広"
	elif s == "G14":
		return "ＮＨＫ総合１・釧路"
	elif s == "G15":
		return "ＮＨＫ総合１・北見"
	elif s == "G16":
		return "ＮＨＫ総合１・室蘭"
	elif s == "G22":
		return "ＮＨＫ総合１・青森"
	elif s == "G20":
		return "ＮＨＫ総合１・盛岡"
	elif s == "G17":
		return "ＮＨＫ総合１・仙台"
	elif s == "G18":
		return "ＮＨＫ総合１・秋田"
	elif s == "G19":
		return "ＮＨＫ総合１・山形"
	elif s == "G21":
		return "ＮＨＫ総合１・福島"
	elif s == "G26":
		return "ＮＨＫ総合１・水戸"
	elif s == "G28":
		return "ＮＨＫ総合１・宇都宮"
	elif s == "G25":
		return "ＮＨＫ総合１・前橋"
	elif s == "G23":
		return "ＮＨＫ総合１・東京"
	elif s == "G31":
		return "ＮＨＫ総合１・新潟"
	elif s == "G37":
		return "ＮＨＫ総合１・富山"
	elif s == "G34":
		return "ＮＨＫ総合１・金沢"
	elif s == "G36":
		return "ＮＨＫ総合１・福井"
	elif s == "G32":
		return "ＮＨＫ総合１・甲府"
	elif s == "G30":
		return "ＮＨＫ総合１・長野"
	elif s == "G39":
		return "ＮＨＫ総合１・岐阜"
	elif s == "G35":
		return "ＮＨＫ総合１・静岡"
	elif s == "G33":
		return "ＮＨＫ総合１・名古屋"
	elif s == "G38":
		return "ＮＨＫ総合１・津"
	elif s == "G45":
		return "ＮＨＫ総合１・大津"
	elif s == "G41":
		return "ＮＨＫ総合１・京都"
	elif s == "G40":
		return "ＮＨＫ総合１・大阪"
	elif s == "G42":
		return "ＮＨＫ総合１・神戸"
	elif s == "G44":
		return "ＮＨＫ総合１・奈良"
	elif s == "G43":
		return "ＮＨＫ総合１・和歌山"
	elif s == "G49":
		return "ＮＨＫ総合１・鳥取"
	elif s == "G48":
		return "ＮＨＫ総合１・松江"
	elif s == "G47":
		return "ＮＨＫ総合１・岡山"
	elif s == "G46":
		return "ＮＨＫ総合１・広島"
	elif s == "G50":
		return "ＮＨＫ総合１・山口"
	elif s == "G53":
		return "ＮＨＫ総合１・徳島"
	elif s == "G52":
		return "ＮＨＫ総合１・高松"
	elif s == "G51":
		return "ＮＨＫ総合１・松山"
	elif s == "G54":
		return "ＮＨＫ総合１・高知"
	elif s == "G55":
		return "ＮＨＫ総合１・福岡"
	elif s == "Gkk":
		return "ＮＨＫ総合１・北九州"
	elif s == "G61":
		return "ＮＨＫ総合１・佐賀"
	elif s == "G57":
		return "ＮＨＫ総合１・長崎"
	elif s == "G56":
		return "ＮＨＫ総合１・熊本"
	elif s == "G60":
		return "ＮＨＫ総合１・大分"
	elif s == "G59":
		return "ＮＨＫ総合１・宮崎"
	elif s == "G58":
		return "ＮＨＫ総合１・鹿児島"
	elif s == "G62":
		return "ＮＨＫ総合１・沖縄"
	elif s == "E10":
		return "ＮＨＫＥテレ１・札幌"
	elif s == "E11":
		return "ＮＨＫＥテレ１・函館"
	elif s == "E12":
		return "ＮＨＫＥテレ１・旭川"
	elif s == "E13":
		return "ＮＨＫＥテレ１・帯広"
	elif s == "E14":
		return "ＮＨＫＥテレ１・釧路"
	elif s == "E15":
		return "ＮＨＫＥテレ１・北見"
	elif s == "E16":
		return "ＮＨＫＥテレ１・室蘭"
	elif s == "E22":
		return "ＮＨＫＥテレ１・青森"
	elif s == "E20":
		return "ＮＨＫＥテレ１・盛岡"
	elif s == "E17":
		return "ＮＨＫＥテレ１・仙台"
	elif s == "E18":
		return "ＮＨＫＥテレ１・秋田"
	elif s == "E19":
		return "ＮＨＫＥテレ１・山形"
	elif s == "E21":
		return "ＮＨＫＥテレ１・福島"
	elif s == "E23":
		return "ＮＨＫＥテレ１・東京"
	elif s == "E31":
		return "ＮＨＫＥテレ１・新潟"
	elif s == "E37":
		return "ＮＨＫＥテレ１・富山"
	elif s == "E34":
		return "ＮＨＫＥテレ１・金沢"
	elif s == "E36":
		return "ＮＨＫＥテレ１・福井"
	elif s == "E32":
		return "ＮＨＫＥテレ１・甲府"
	elif s == "E30":
		return "ＮＨＫＥテレ１・長野"
	elif s == "E35":
		return "ＮＨＫＥテレ１・静岡"
	elif s == "E33":
		return "ＮＨＫＥテレ１・名古屋"
	elif s == "E40":
		return "ＮＨＫＥテレ１・大阪"
	elif s == "E49":
		return "ＮＨＫＥテレ１・鳥取"
	elif s == "E48":
		return "ＮＨＫＥテレ１・松江"
	elif s == "E47":
		return "ＮＨＫＥテレ１・岡山"
	elif s == "E46":
		return "ＮＨＫＥテレ１・広島"
	elif s == "E50":
		return "ＮＨＫＥテレ１・山口"
	elif s == "E53":
		return "ＮＨＫＥテレ１・徳島"
	elif s == "E52":
		return "ＮＨＫＥテレ１・高松"
	elif s == "E51":
		return "ＮＨＫＥテレ１・松山"
	elif s == "E54":
		return "ＮＨＫＥテレ１・高知"
	elif s == "E55":
		return "ＮＨＫＥテレ１・福岡"
	elif s == "Ekk":
		return "ＮＨＫＥテレ１・北九州"
	elif s == "E61":
		return "ＮＨＫＥテレ１・佐賀"
	elif s == "E57":
		return "ＮＨＫＥテレ１・長崎"
	elif s == "E56":
		return "ＮＨＫＥテレ１・熊本"
	elif s == "E60":
		return "ＮＨＫＥテレ１・大分"
	elif s == "E59":
		return "ＮＨＫＥテレ１・宮崎"
	elif s == "E58":
		return "ＮＨＫＥテレ１・鹿児島"
	elif s == "E62":
		return "ＮＨＫＥテレ１・沖縄"
	elif s == "STV":
		return "札幌テレビ"
	elif s == "HBC":
		return "ＨＢＣ北海道放送"
	elif s == "UHB":
		return "北海道文化放送"
	elif s == "HTB":
		return "ＨＴＢ"
	elif s == "TVH":
		return "ＴＶｈ"
	elif s == "RAB":
		return "ＲＡＢ青森放送"
	elif s == "ATV":
		return "ＡＴＶ青森テレビ"
	elif s == "ABA":
		return "青森朝日放送"
	elif s == "TVI":
		return "テレビ岩手"
	elif s == "IBC":
		return "ＩＢＣテレビ"
	elif s == "MIT":
		return "めんこいテレビ"
	elif s == "IAT":
		return "岩手朝日テレビ"
	elif s == "MMT":
		return "ミヤギテレビ"
	elif s == "TBC":
		return "ＴＢＣテレビ"
	elif s == "OX":
		return "仙台放送"
	elif s == "KHB":
		return "東日本放送"
	elif s == "ABS":
		return "ABS秋田放送1"
	elif s == "ABS2":
		return "ABS秋田放送2"
	elif s == "AKT":
		return "ＡＫＴ秋田テレビ"
	elif s == "AAB":
		return "秋田朝日放送"
	elif s == "YBC":
		return "山形放送"
	elif s == "TUY":
		return "ＴＵＹ"
	elif s == "SAY":
		return "さくらんぼテレビ"
	elif s == "YTS":
		return "山形テレビ"
	elif s == "FCT":
		return "福島中央テレビ"
	elif s == "TUF":
		return "テレビユー福島"
	elif s == "FTV":
		return "ＦＴＶ福島テレビ"
	elif s == "KFB":
		return "ＫＦＢ福島放送"
	elif s == "NTV":
		return "日テレ"
	elif s == "TBS":
		return "ＴＢＳ"
	elif s == "CX":
		return "フジテレビ"
	elif s == "EX":
		return "テレビ朝日"
	elif s == "EX2":
		return "テレビ朝日２"
	elif s == "TX":
		return "テレビ東京"
	elif s == "TTV":
		return "とちぎテレビ"
	elif s == "GTV":
		return "群馬テレビ"
	elif s == "TVS":
		return "テレ玉"
	elif s == "CTC":
		return "チバテレ"
	elif s == "CTC2":
		return "チバテレ2"
	elif s == "CTC3":
		return "チバテレ3"
	elif s == "MX":
		return "ＴＯＫＹＯ　ＭＸ１"
	elif s == "MX2":
		return "ＴＯＫＹＯ　ＭＸ２"
	elif s == "TVK":
		return "ｔｖｋ"
	elif s == "TENY":
		return "ＴｅＮＹ"
	elif s == "BSN":
		return "ＢＳＮ"
	elif s == "NST":
		return "新潟総合テレビ"
	elif s == "UX":
		return "新潟テレビ２１"
	elif s == "KNB":
		return "ＫＮＢテレビ"
	elif s == "TUT":
		return "チューリップテレビ"
	elif s == "BBT":
		return "富山テレビ放送"
	elif s == "KTK":
		return "テレビ金沢"
	elif s == "MRO":
		return "ＭＲＯ"
	elif s == "ITC":
		return "石川テレビ"
	elif s == "HAB":
		return "ＨＡＢ"
	elif s == "FBC":
		return "福井放送"
	elif s == "FTB":
		return "福井テレビ"
	elif s == "YBS":
		return "山梨放送"
	elif s == "UTY":
		return "ＵＴＹ"
	elif s == "TSB":
		return "ＴＳＢ"
	elif s == "SBC":
		return "ＳＢＣ信越放送"
	elif s == "NBS":
		return "長野放送"
	elif s == "ABN":
		return "長野朝日放送"
	elif s == "CTV":
		return "中京テレビ"
	elif s == "CBC":
		return "ＣＢＣテレビ"
	elif s == "THK":
		return "東海テレビ"
	# 波ダッシュ(U+301C)ではなく全角チルダ(U+FF5E)
	elif s == "NBN":
		return "メ～テレ"
	elif s == "TVA":
		return "テレビ愛知"
	elif s == "GBS":
		return "ぎふチャン"
	elif s == "SDT":
		return "Daiichi-TV"
	elif s == "SBS":
		return "ＳＢＳ"
	elif s == "SUT":
		return "テレビ静岡"
	elif s == "SATV":
		return "静岡朝日テレビ"
	elif s == "MTV":
		return "三重テレビ１"
	elif s == "YTV":
		return "よみうりテレビ"
	elif s == "MBS":
		return "ＭＢＳ毎日放送"
	elif s == "KTV":
		return "関西テレビ"
	elif s == "ABC":
		return "ＡＢＣテレビ"
	elif s == "TVO":
		return "テレビ大阪"
	elif s == "BBC":
		return "ＢＢＣびわ湖放送"
	elif s == "KBS":
		return "ＫＢＳ京都"
	elif s == "SUN":
		return "サンテレビ１"
	elif s == "TVN":
		return "奈良テレビ"
	elif s == "WTV":
		return "ＷＴＶ"
	elif s == "NKT":
		return "日本海テレビ"
	elif s == "BSS":
		return "ＢＳＳテレビ"
	elif s == "TSK":
		return "さんいん中央テレビ１"
	elif s == "TSK2":
		return "さんいん中央テレビ２"
	elif s == "RNC":
		return "ＲＮＣ西日本テレビ"
	elif s == "RSK":
		return "ＲＳＫテレビ"
	elif s == "OHK":
		return "ＯＨＫ"
	elif s == "KSB":
		return "瀬戸内海放送"
	elif s == "TSC":
		return "テレビせとうち"
	elif s == "HTV":
		return "広島テレビ"
	elif s == "RCC":
		return "ＲＣＣテレビ"
	elif s == "TSS":
		return "テレビ新広島"
	elif s == "HOME":
		return "広島ホームテレビ"
	elif s == "KRY":
		return "山口放送１"
	elif s == "TYS":
		return "ｔｙｓテレビ山口"
	elif s == "YAB":
		return "ｙａｂ山口朝日"
	elif s == "JRT":
		return "四国放送"
	elif s == "RNB":
		return "南海放送"
	elif s == "ITV":
		return "あいテレビ"
	elif s == "EBC":
		return "テレビ愛媛"
	elif s == "EAT":
		return "愛媛朝日テレビ"
	elif s == "RKC":
		return "高知放送"
	elif s == "KUTV":
		return "テレビ高知"
	elif s == "KSS":
		return "高知さんさんテレビ"
	elif s == "FBS":
		return "ＦＢＳ福岡放送"
	elif s == "RKB":
		return "ＲＫＢ毎日放送"
	elif s == "TNC":
		return "テレビ西日本"
	elif s == "KBC":
		return "ＫＢＣテレビ"
	elif s == "TVQ":
		return "ＴＶＱ九州放送"
	elif s == "STS":
		return "ＳＴＳサガテレビ"
	elif s == "NIB":
		return "長崎国際テレビ"
	elif s == "NBC":
		return "ＮＢＣ長崎放送"
	elif s == "KTN":
		return "テレビ長崎"
	elif s == "NCC":
		return "ＮＣＣ長崎文化放送"
	elif s == "KKT":
		return "くまもと県民"
	elif s == "RKK":
		return "ＲＫＫ熊本放送"
	elif s == "TKU":
		return "テレビ熊本"
	elif s == "KAB":
		return "ＫＡＢ熊本朝日放送"
	elif s == "TOS":
		return "ＴＯＳテレビ大分"
	elif s == "OBS":
		return "ＯＢＳ大分放送"
	elif s == "OAB":
		return "ＯＡＢ大分朝日放送"
	elif s == "UMK":
		return "テレビ宮崎"
	elif s == "MRT":
		return "ＭＲＴ宮崎放送"
	elif s == "KYT":
		return "鹿児島讀賣テレビ"
	elif s == "KYT3":
		return "鹿児島讀賣テレビ3"
	elif s == "MBC":
		return "ＭＢＣ南日本放送"
	elif s == "KTS":
		return "鹿児島テレビ放送"
	elif s == "KKB":
		return "ＫＫＢ鹿児島放送"
	elif s == "RBC":
		return "ＲＢＣテレビ"
	elif s == "OTV":
		return "沖縄テレビ"
	elif s == "QAB":
		return "琉球朝日放送"
	elif s == "BS1":
		return "ＮＨＫ ＢＳ１"
	elif s == "BSp":
		return "ＮＨＫ ＢＳプレミアム"
	elif s == "BS4":
		return "ＢＳ日テレ"
	elif s == "BS5":
		return "ＢＳ朝日"
	elif s == "BS6":
		return "ＢＳ-ＴＢＳ"
	elif s == "BS7":
		return "ＢＳテレ東"
	elif s == "BS8":
		return "ＢＳフジ"
	elif s == "WW1":
		return "ＷＯＷＯＷプライム"
	elif s == "WW2":
		return "ＷＯＷＯＷライブ"
	elif s == "WW3":
		return "ＷＯＷＯＷシネマ"
	elif s == "WW4":
		return "WOWOWプラス"
	elif s == "SC1":
		return "スター・チャンネル1"
	elif s == "SC2":
		return "スター・チャンネル2"
	elif s == "SC3":
		return "スター・チャンネル3"
	elif s == "BS11":
		return "BS11イレブン"
	elif s == "BS12":
		return "BS12 トゥエルビ"
	elif s == "OU1":
		return "放送大学ex"
	elif s == "GCH":
		return "グリーンチャンネル"
	elif s == "BSA":
		return "BSアニマックス"
	elif s == "SKY":
		return "BSスカパー!"
	elif s == "JS1":
		return "J SPORTS 1"
	elif s == "JS2":
		return "J SPORTS 2"
	elif s == "JS3":
		return "J SPORTS 3"
	elif s == "JS4":
		return "J SPORTS 4"
	elif s == "BSF":
		return "BS釣りビジョン"
	elif s == "JMV":
		return "BS日本映画専門チャンネル"
	elif s == "DCH":
		return "ディズニー・チャンネル"
	elif s == "FK1":
		return "NHK BS4K"
	elif s == "FK4":
		return "BS日テレ 4K"
	elif s == "FK5":
		return "BS朝日 4K"
	elif s == "FK6":
		return "BS-TBS 4K"
	elif s == "FK7":
		return "BSテレ東 4K"
	elif s == "FK8":
		return "BSフジ 4K"
	elif s == "EK1":
		return "NHK BS8K"
	elif s == "FKW":
		return "ＷＯＷＯＷ　４Ｋ"
	elif s == "FKC":
		return "ザ・シネマ 4K"
	elif s == "FKS":
		return "ショップチャンネル 4K"
	elif s == "QVC":
		return "4K QVC"
	return ""

def get_decoder():
	result = []
	f = open("scripts/decoder.js", "r")
	aaa = f.read().split('"')
	result.append(aaa[1])
	result.append(aaa[3])
	result.append(aaa[5])
	f.close()
	return result

def load_hash_array(filename):
	f = open(filename, "r")
	jsfile = f.read()
	f.close()

	BEGIN = 0
	MAINKEY = 1
	MAINKEY_COLON = 2
	HASH_VALUE_KEY = 3
	HASH_VALUE_KEY_COLON = 4
	HASH_VALUE_VALUE = 5
	HASH_VALUE_COMMA = 6
	MAIN_COMMA = 7
	END = 8
	PLAIN_VALUE = 9
	HASH_VALUE_HASH_VALUE_KEY = 10
	HASH_VALUE_HASH_VALUE_KEY_COLON = 11
	HASH_VALUE_HASH_VALUE_VALUE = 12
	HASH_VALUE_HASH_VALUE_COMMA = 13
	ARRAY = 14
	ARRAY_VALUE = 15
	ARRAY_COMMA = 16
	ARRAY_TUPLE1 = 17
	ARRAY_TUPLE1_VALUE = 18
	ARRAY_TUPLE_COMMA = 19
	ARRAY_TUPLE2 = 20
	ARRAY_TUPLE2_ARRAY = 21
	ARRAY_TUPLE2_ARRAY_VALUE = 22
	ARRAY_TUPLE2_ARRAY_COMMA = 23

	mode = BEGIN
	s = ""
	keyname = ""
	keyname2 = ""
	keyname3 = ""
	tuple = ["",[]]
	result = None
	for a in jsfile:
		if mode == BEGIN:
			if a == "[":
				mode = ARRAY
				result = []
			elif a == "{":
				mode = MAINKEY
				s = ""
				result = {}
		elif mode == ARRAY:
			if a == "[":
				mode = ARRAY_TUPLE1
				tuple = ["",[]]
			elif a == "\"":
				mode = ARRAY_VALUE
				s = ""
		elif mode == ARRAY_VALUE:
			if a == "\"":
				mode = ARRAY_COMMA
				result.append(s)
			else:
				s += a
		elif mode == ARRAY_COMMA:
			if a == ",":
				mode = ARRAY
				s = ""
			elif a == "]":
				mode = END

		elif mode == ARRAY_TUPLE1:
			if a == "\"":
				mode = ARRAY_TUPLE1_VALUE
				s = ""
		elif mode == ARRAY_TUPLE1_VALUE:
			if a == "\"":
				mode = ARRAY_TUPLE_COMMA
				tuple[0] = s
			else:
				s += a
		elif mode == ARRAY_TUPLE_COMMA:
			if a == ",":
				mode = ARRAY_TUPLE2
			elif a == "]":
				mode = ARRAY
				result.append(tuple)
		elif mode == ARRAY_TUPLE2:
			if a == "[":
				mode = ARRAY_TUPLE2_ARRAY
				s = ""
		elif mode == ARRAY_TUPLE2_ARRAY:
			if a == "\"":
				mode = ARRAY_TUPLE2_ARRAY_VALUE
				s = ""
		elif mode == ARRAY_TUPLE2_ARRAY_VALUE:
			if a == "\"":
				mode = ARRAY_TUPLE2_ARRAY_COMMA
				tuple[1].append(s)
			else:
				s += a
		elif mode == ARRAY_TUPLE2_ARRAY_COMMA:
			if a == ",":
				mode = ARRAY_TUPLE2_ARRAY
			elif a == "]":
				mode = ARRAY_TUPLE_COMMA

		elif mode == MAINKEY:
			if a == ":":
				mode = MAINKEY_COLON
				keyname = s
			elif a not in [" ","\n","\r","\t"]:
				s += a
		elif mode == MAINKEY_COLON:
			if a == "{":
				mode = HASH_VALUE_KEY
				result[keyname] = {}
				s = ""
			elif a == "\"":
				mode = PLAIN_VALUE
				result[keyname] = ""
				s = ""
		elif mode == HASH_VALUE_KEY:
			if a == "}":
				mode = MAIN_COMMA
			elif a == ":":
				keyname2 = s
				mode = HASH_VALUE_KEY_COLON
			elif a not in [" ","\n","\r","\t"]:
				s += a
		elif mode == HASH_VALUE_KEY_COLON:
			if a == "{":
				mode = HASH_VALUE_HASH_VALUE_KEY
				result[keyname][keyname2] = {}
				s = ""
			elif a == "\"":
				mode = HASH_VALUE_VALUE
				s = ""
		elif mode == HASH_VALUE_VALUE:
			if a == "\"":
				mode = HASH_VALUE_COMMA
				result[keyname][keyname2] = s
			else:
				s += a
		elif mode == HASH_VALUE_HASH_VALUE_KEY:
			if a == "}":
				mode = HASH_VALUE_COMMA
			elif a == ":":
				keyname3 = s
				mode = HASH_VALUE_HASH_VALUE_KEY_COLON
			elif a not in [" ","\n","\r","\t"]:
				s += a
		elif mode == HASH_VALUE_HASH_VALUE_KEY_COLON:
			if a == "\"":
				mode = HASH_VALUE_HASH_VALUE_VALUE
				s = ""
		elif mode == HASH_VALUE_HASH_VALUE_VALUE:
			if a == "\"":
				mode = HASH_VALUE_HASH_VALUE_COMMA
				result[keyname][keyname2][keyname3] = s
			else:
				s += a
		elif mode == PLAIN_VALUE:
			if a == "\"":
				mode = MAIN_COMMA
				result[keyname] = s
			else:
				s += a
		elif mode == HASH_VALUE_COMMA:
			if a == ",":
				mode = HASH_VALUE_KEY
				s = ""
			elif a == "}":
				mode = MAIN_COMMA
		elif mode == HASH_VALUE_HASH_VALUE_COMMA:
			if a == ",":
				mode = HASH_VALUE_HASH_VALUE_KEY
				s = ""
			elif a == "}":
				mode = HASH_VALUE_COMMA
		elif mode == MAIN_COMMA:
			if a == ",":
				mode = MAINKEY
				s = ""
			elif a == "}":
				mode = END
	return result

def split_chunk(str):
	splited = []
	chunk = ""
	for s in str:
		if s == ":":
			chunk = splited[-1]
			splited.pop(-1)
		chunk += s
		if s == "." or s == ",":
			splited.append(chunk)
			chunk = ""
	splited.append(chunk)
	return splited

def decode_string(str):
	result = ""
	is_abc_mode = False
	is_kanji = False
	is_backslash = False
	code = 0
	for c in str:
		if is_backslash and c == 'n':
			result += "<br>"
			is_backslash = False
			continue
		if c == '\\':
			is_backslash = True
			continue
		if is_abc_mode:
			if c == '>':
				is_abc_mode = False
			else:
				result += c
		elif is_kanji:
			code = code * 64 + base64_special.index(c)
			if code < decoder1_range:
				result += decoder[0][code]
			elif code < decoder1_range + decoder2_range:
				result += decoder[1][(code - decoder1_range)*2] + decoder[1][(code - decoder1_range)*2+1]
			else:
				result += decoder[2][(code - decoder1_range - decoder2_range)*3] + decoder[2][(code - decoder1_range - decoder2_range)*3+1] + decoder[2][(code - decoder1_range - decoder2_range)*3+2]
			is_kanji = False
		elif c == '<':
			is_abc_mode = True
		elif c in base64_special:
			is_kanji = True
			code = base64_special.index(c)
		else:
			result += c
	return result

def decompressProgramChunk(month, day, tv, chunk_string):
	keysta = ""
	if tv in tvlist.NHK_NET:
		keysta = "G23"
	elif tv in tvlist.ETV_NET:
		keysta = "E23"
	elif tv in tvlist.NTV_NET:
		keysta = "NTV"
	elif tv in tvlist.TBS_NET:
		keysta = "TBS"
	elif tv in tvlist.CX_NET:
		keysta = "CX"
	elif tv in tvlist.EX_NET or tv == "EX2":
		keysta = "EX"
	elif tv in tvlist.TX_NET:
		keysta = "TX"
	elif tv == "CTC2" or tv == "CTC3":
		keysta = "CTC"
	elif tv == "MTV2":
		keysta = "MTV"
	elif tv == "SUN2":
		keysta = "SUN"
	elif tv == "NB2":
		keysta = "BS1"
	elif tv == "BN2":
		keysta = "BS4"
	elif tv == "FK4":
		keysta = "BS4"
	elif tv == "FK5":
		keysta = "BS5"
	elif tv == "FK6":
		keysta = "BS6"
	elif tv == "FK7":
		keysta = "BS7"
	elif tv == "FK8":
		keysta = "BS8"

	keystas_table = []
	keysta_string = ""

	if month in original_timetables and day in original_timetables[month]:
		if tv.startswith("sG") and tv[1:] in original_timetables[month][day]:
			if tv == "sG23":
				keysta_string = original_timetables[month][day]["G23"]
			else:
				keysta_string = decompressProgramChunk(month, day, tv[1:], original_timetables[month][day][tv[1:]])
		elif tv.startswith("sE") and tv[1:] in original_timetables[month][day]:
			if tv == "sE23":
				keysta_string = original_timetables[month][day]["E23"]
			else:
				keysta_string = decompressProgramChunk(month, day, tv[1:], original_timetables[month][day][tv[1:]])
		elif tv == "ABS2" and "ABS" in original_timetables[month][day]:
			keysta_string = decompressProgramChunk(month, day, "ABS", original_timetables[month][day]["ABS"])
		elif tv == "TSK2" and "TSK" in original_timetables[month][day]:
			keysta_string = decompressProgramChunk(month, day, "TSK", original_timetables[month][day]["TSK"])
		elif tv == "KYT3" and "KYT" in original_timetables[month][day]:
			keysta_string = decompressProgramChunk(month, day, "KYT", original_timetables[month][day]["KYT"])
		elif keysta in original_timetables[month][day]:
			keysta_string = original_timetables[month][day][keysta]

	splitedColon = keysta_string.split(":")
	keystas_table = split_chunk(splitedColon[0])

	if chunk_string == "":
		return []

	result = []
	chunks = split_chunk(chunk_string)
	for c in chunks:
		splitedColon2 = c.split(":")
		chunk = splitedColon2[0]

		splited_by_space = (chunk[-1] == ",")
		chunk = chunk[:-1]

		if len(chunk) <= 2:
			for k in keystas_table:
				if chunk == k[:2]:
					result.append(k)
		elif "*" in chunk:
			splited = chunk.split("*")
			for k in keystas_table:
				hit = False
				if splited[0] == k[:2]:
					hit = True
					for idx in reversed(range(len(k))):
						if not (k[idx] >= '0' and k[idx] <= '9') and k[idx] != '.' and k[idx] != ',':
							result.append(k[:idx+1] + splited[1] + k[-1])
							break
				if hit:
					break
		elif "-" in chunk:
			splited = chunk.split("-")
			start = False
			for k in keystas_table:
				if splited[0] == k[:2]:
					start = True
				if start:
					result.append(k)
				if splited[1] == k[:2]:
					break;
		elif "^" in chunk:
			keysta_sub_string = ""
			if tv.startswith("sG") and "sG23" in original_timetables[month][day]:
				keysta_sub_string = original_timetables[month][day]["sG23"]
			elif tv.startswith("sE") and "sE23" in original_timetables[month][day]:
				keysta_sub_string = original_timetables[month][day]["sE23"]
			splitedColon_sub = keysta_sub_string.split(":")
			keystas_sub_table = split_chunk(splitedColon_sub[0])
			for k in keystas_sub_table:
				if chunk[:2] == k[:2]:
					result.append(k)
					break
		else:
			result.append(chunk + ("," if splited_by_space else "."))

	if len(splitedColon2) == 1:
		return "".join(result)
	else:
		return "".join(result) + ":" + splitedColon2[1]

def getYesterdayDate(year, month, day):
	today = datetime.date((int)(year), (int)(month), (int)(day))
	yesterday = today - datetime.timedelta(1)
	year2 = str(yesterday.year)
	if yesterday.month < 10:
		month2 = "0" + str(yesterday.month)
	else:
		month2 = str(yesterday.month)
	if yesterday.day < 10:
		day2 = "0" + str(yesterday.day)
	else:
		day2 = str(yesterday.day)
	return year2 + month2 + day2

def getTomorrowDate(year, month, day):
	today = datetime.date((int)(year), (int)(month), (int)(day))
	tomorrow = today + datetime.timedelta(days=1)
	year2 = str(tomorrow.year)
	if tomorrow.month < 10:
		month2 = "0" + str(tomorrow.month)
	else:
		month2 = str(tomorrow.month)
	if tomorrow.day < 10:
		day2 = "0" + str(tomorrow.day)
	else:
		day2 = str(tomorrow.day)
	return year2 + month2 + day2

def read_chunk(chunk):
	TYPES = 0
	TITLE = 1
	CATEGORY = 2
	SUB_CATEGORY = 3
	CHAPTER = 4
	DESC = 5
	SPACE = 6
	INTERVAL = 7

	mode = TYPES
	s = ""
	title_id = 0
	types = []
	category = ""
	sub_category = ""
	chapter_id = None
	desc_id = 0
	interval = 0
	splited_by_space = False
	for c in chunk[2:]:
		if mode == TYPES and c == '?':
			# 番組情報なし(categoryを空文字とする)
			break
		elif mode == TYPES and c >= '0' and c<= '9':
			mode = TITLE
			s = ""
		elif mode == TITLE and not (c >= '0' and c<= '9'):
			title_id = int(s)
			mode = CATEGORY
		elif mode == CHAPTER and c >= '0' and c<= '9':
			mode = DESC
			s = ""
		elif mode == DESC and not (c >= '0' and c<= '9'):
			mode = SPACE
			desc_id = int(s)
			splited_by_space = (c == ',')
			continue
		elif mode == SPACE and c == ':':
			mode = INTERVAL
			s = ""
			continue

		if mode == TYPES:
			types.append(type_names[c]["icon"])
		elif mode == TITLE:
			s += c
		elif mode == CATEGORY:
			if c == "A":
				category = "100"
			elif c == "B":
				category = "101"
			elif c == "C":
				category = "102"
			elif c == "D":
				category = "103"
			elif c == "E":
				category = "104"
			elif c == "F":
				category = "105"
			elif c == "G":
				category = "106"
			elif c == "H":
				category = "107"
			elif c == "I":
				category = "108"
			elif c == "J":
				category = "109"
			elif c == "K":
				category = "110"
			elif c == "L":
				category = "111"
			elif c == "M":
				category = "112"
			elif c == "N":
				category = "113"
			elif c == "O":
				category = "114"
			elif c == "P":
				category = "115"
			mode = SUB_CATEGORY
		elif mode == SUB_CATEGORY:
			if c == "A":
				sub_category = "100"
			elif c == "B":
				sub_category = "101"
			elif c == "C":
				sub_category = "102"
			elif c == "D":
				sub_category = "103"
			elif c == "E":
				sub_category = "104"
			elif c == "F":
				sub_category = "105"
			elif c == "G":
				sub_category = "106"
			elif c == "H":
				sub_category = "107"
			elif c == "I":
				sub_category = "108"
			elif c == "J":
				sub_category = "109"
			elif c == "K":
				sub_category = "110"
			elif c == "L":
				sub_category = "111"
			elif c == "M":
				sub_category = "112"
			elif c == "N":
				sub_category = "113"
			elif c == "O":
				sub_category = "114"
			elif c == "P":
				sub_category = "115"
			mode = CHAPTER
		elif mode == CHAPTER:
			if chapter_id == None:
				chapter_id = 0
			chapter_id = chapter_id * 50 + abc_list.index(c)
		elif mode == DESC:
			s += c
		elif mode == INTERVAL:
			s += c

	if mode == DESC:
		desc_id = int(s)
	elif mode == INTERVAL:
		interval = int(s)

	return category + sub_category, types, title_id, chapter_id, desc_id, interval, splited_by_space

def output_html(year, month, day, area, stations):
	found = False
	for station in stations:
		if station in timetables[month][day]:
			found = True
			break
	if not found:
		return

	dir_path = "restore" + year + "/" + month + "/" + day
	if not os.path.isdir(dir_path):
		os.makedirs(dir_path)
	file_path = dir_path + "/" + year + "_" + month + "_" + day + "_" + area + ".html"
	outfile = open(file_path, "w")

	today_string = str((int)(month)) + "月 " + str((int)(day)) + "日"
	outfile.write('<html><head><meta charset="utf-8" /><title>' + today_string + '</title></head><body>\n')
	for station in stations:
		if not station in timetables[month][day]:
			continue
		outfile.write('<div class="cell-station cell-top" title="' + get_station_name(station) + '">\n')
		idx = 0
		isFirst = True
		for chunk in timetables[month][day][station]:
			yearmonthday = year + month + day
			hour = str(base60.index(chunk[0]))
			if isFirst and (int)(hour) >= 20:
				yearmonthday = getYesterdayDate(year, month, day)
			elif (int)(hour) >= 24:
				hour = "0" + str((int)(hour)-24)
				yearmonthday = getTomorrowDate(year, month, day)
			elif len(hour) == 1:
				hour = "0" + str(hour)
			minute = str(base60.index(chunk[1]))
			if len(minute) == 1:
				minute = "0" + str(minute)

			category, types, title_id, chapter_id, desc_id, interval, splited_by_space = read_chunk(chunk)

			if interval != 0:
				height = (interval*3) - 3
			elif isFirst and (int)(hour) >= 20:
				t1 = "0500"
				t2 = util.time_decode_base60(timetables[month][day][station][idx+1])
				height = (util.get_interval(t1,t2) * 3) - 3
			else:
				t1 = util.time_decode_base60(timetables[month][day][station][idx])
				t2 = util.time_decode_base60(timetables[month][day][station][idx+1])
				height = (util.get_interval(t1,t2) * 3) - 3
			idx += 1

			types_string = ""
			for t in types:
				if t == "PS":
					types_string += "【PPS】"
				elif t == "契":
					types_string += "【契】"
				elif t == "幕":
					types_string += "(字幕版)"
				elif t == "R15":
					types_string += "[R15+]"
				elif t == "22.2ch":
					types_string += "[22.2]"
				elif t == "5.1ch":
					types_string += "[5.1]"
				else:
					types_string += "[" + t + "]"

			full_title = decode_string(titles[title_id][0])
			if splited_by_space:
				full_title += " "
			if chapter_id != None:
				full_title += decode_string(titles[title_id][1][chapter_id])

			if category == "":
				# 番組情報はありません
				outfile.write('  <div class="cell-schedule" style="height: ' + str(height) + 'px;"></div>\n')
			else:
				outfile.write('  <div class="cell-schedule cell-genre-' + category + ' system-cell-schedule-head-' + yearmonthday + hour + minute + '" style="height: ' + str(height) + 'px;">\n')
				outfile.write('    <span class="schedule-title">' + full_title + types_string + '</span>\n');
				outfile.write('    <span class="schedule-summary">' + decode_string(descriptions[desc_id]) + '</span>\n');
				outfile.write('  </div>\n')

			isFirst = False

		outfile.write('</div>\n')
	outfile.write('</body></html>\n')
	outfile.close()

def output_html_ouj(year, month, day):
	if not "OU2" in timetables[month][day]:
		return

	dir_path = "restore" + year + "/" + month + "/" + day
	if not os.path.isdir(dir_path):
		os.makedirs(dir_path)
	file_path = dir_path + "/" + year + "_" + month + "_" + day + "_OUJ.html"
	outfile = open(file_path, "w")

	today_string = "month=" + str((int)(month)) + "&date=" + str((int)(day))
	outfile.write('<html><head><meta charset="utf-8" /></head><body><a href=\'/hp/bangumi2/bangumi.php?' + today_string + '\'></a>\n')
	outfile.write('<TABLE class=\'tbl-ct-program\'></TABLE>\n')
	outfile.write('<TABLE class=\'tbl-ct-program\'>\n')
	for chunk in timetables[month][day]["OU2"]:
		hour = str(base60.index(chunk[0]))
		if len(hour) == 1:
			hour = "0" + str(hour)
		minute = str(base60.index(chunk[1]))
		if len(minute) == 1:
			minute = "0" + str(minute)

		category, types, title_id, chapter_id, desc_id, interval, splited_by_space = read_chunk(chunk)

		full_title = decode_string(titles[title_id][0])
		if splited_by_space:
			full_title += " "
		if chapter_id != None:
			full_title += decode_string(titles[title_id][1][chapter_id])

		outfile.write('<TR><TD>\n')
		outfile.write('<span class=\'time-program\'>' + hour + ':' + minute + '</span>\n')
		outfile.write('<dl>\n')
		outfile.write('<dt>' + full_title + '</dt>\n')
		outfile.write('<dd>' + decode_string(descriptions[desc_id]).lstrip("「").rstrip("」") + '</dd>\n')
		outfile.write('</dl>\n')
		outfile.write('</TD></TR>\n')

	outfile.write('</TABLE>\n')
	outfile.write('</body></html>\n')
	outfile.close()

def output_html_mxtv(year, month, day):
	if not "MX2" in timetables[month][day]:
		return

	dir_path = "restore" + year + "/" + month + "/" + day
	if not os.path.isdir(dir_path):
		os.makedirs(dir_path)
	file_path = dir_path + "/" + year + "_" + month + "_" + day + "_MX.html"
	outfile = open(file_path, "w")

	today_string = year + "年 " + str((int)(month)) + "月" + str((int)(day)) + "日"
	outfile.write('<html><head><meta charset="utf-8" /><title>' + today_string + '</title></head><body><table>\n')
	for chunk in timetables[month][day]["MX2"]:
		hour = str(base60.index(chunk[0]))
		minute = str(base60.index(chunk[1]))
		if len(minute) == 1:
			minute = "0" + str(minute)

		category, types, title_id, chapter_id, desc_id, interval, splited_by_space = read_chunk(chunk)

		types_string = ""
		for t in types:
			if t == "新":
				types_string += '<span class="icon_new">新</span>'
			elif t == "再":
				types_string += '<span class="icon_re">再</span>'
			elif t == "終":
				types_string += '<span class="icon_end">終</span>'
			elif t == "字":
				types_string += '<span class="icon_jimaku">字</span>'
			elif t == "二":
				types_string += '<span class="icon_2kakokugo">二</span>'
			elif t == "解":
				types_string += '<span class="icon_kaisetsu">解</span>'
			elif t == "デ":
				types_string += '<span class="icon_data">デ</span>'
			elif t == "生":
				types_string += '<span class="icon_live">生</span>'

		full_title = decode_string(titles[title_id][0])
		if splited_by_space:
			full_title += " "
		if chapter_id != None:
			full_title += decode_string(titles[title_id][1][chapter_id])

		outfile.write('<tr><td class="program_set tb_set_mx2">\n')
		outfile.write('<div class="time">' + hour + ':' + minute + '</div>\n')
		outfile.write('<strong>' + full_title + '</strong>\n')
		outfile.write('<div class="about">' + decode_string(descriptions[desc_id]) + '</div>\n')
		outfile.write(types_string + '\n')
		outfile.write('</td></tr>\n')

	outfile.write('</table></body></html>\n')
	outfile.close()

def output_html_mietv(year, month, day):
	if not "MTV2" in timetables[month][day]:
		return

	dir_path = "restore" + year + "/" + month + "/" + day
	if not os.path.isdir(dir_path):
		os.makedirs(dir_path)
	file_path = dir_path + "/" + year + "_" + month + "_" + day + "_MTV.html"
	outfile = open(file_path, "w")

	today_string = str((int)(month)) + "月" + str((int)(day)) + "日"
	outfile.write('<html><head><meta charset="utf-8" /></head><body><span class="current">' + today_string + '</span><div id="ch2"><table>\n')
	idx = 0
	for chunk in timetables[month][day]["MTV2"]:
		if "MTV" in timetables[month][day] and chunk in timetables[month][day]["MTV"]:
			break
		hour = str(base60.index(chunk[0]))
		if len(hour) == 1:
			hour = "0" + str(hour)
		minute = str(base60.index(chunk[1]))
		if len(minute) == 1:
			minute = "0" + str(minute)

		category, types, title_id, chapter_id, desc_id, interval, splited_by_space = read_chunk(chunk)

		types_string = ""
		for t in types:
			types_string += "【" + t + "】"

		full_title = decode_string(titles[title_id][0])
		if splited_by_space:
			full_title += " "
		if chapter_id != None:
			full_title += decode_string(titles[title_id][1][chapter_id])

		outfile.write('<tr>\n')
		outfile.write('<td>' + str((int)(hour)) + ':' + minute + '</td>\n')
		outfile.write('<td><p class="title">' + full_title + types_string + '</p>')
		outfile.write('<p>' + decode_string(descriptions[desc_id]) + '</p></td>\n')
		outfile.write('</tr>\n')
		idx += 1

	if idx != 0:
		a = util.time_decode_base60( timetables[month][day]["MTV2"][idx][:2] )
		outfile.write('<tr>\n')
		outfile.write('<td>' + a[:2] + ':' + a[2:] + '</td>\n')
		outfile.write('</tr>\n')

	outfile.write('</table></body></html>\n')
	outfile.close()

def output_html_suntv(year, month, day):
	if not "SUN2" in timetables[month][day]:
		return

	dir_path = "restore" + year + "/" + month + "/" + day
	if not os.path.isdir(dir_path):
		os.makedirs(dir_path)
	file_path = dir_path + "/" + year + "_" + month + "_" + day + "_SUN.html"
	outfile = open(file_path, "w")

	today_string = str((int)(month)) + "月" + str((int)(day)) + "日"
	outfile.write('<html><head><meta charset="utf-8" /></head><body><a href=date1>' + today_string + '</a>\n')
	idx = 0
	for chunk in timetables[month][day]["SUN2"]:
		if "SUN" in timetables[month][day] and chunk in timetables[month][day]["SUN"]:
			idx += 1
			continue
		hour = str(base60.index(chunk[0]))
		if len(hour) == 1:
			hour = "0" + str(hour)
		minute = str(base60.index(chunk[1]))
		if len(minute) == 1:
			minute = "0" + str(minute)

		category, types, title_id, chapter_id, desc_id, interval, splited_by_space = read_chunk(chunk)

		types_string = ""
		for t in types:
			if t == "新":
				types_string += '<span class=\'prg-icon-new\'>新</span>'
			elif t == "再":
				types_string += '<span class=\'prg-icon-re\'>再</span>'
			elif t == "終":
				types_string += '<span class=\'prg-icon-end\'>終</span>'
			elif t == "字":
				types_string += '<span class=\'prg-icon-sub\'>字</span>'
			elif t == "二":
				types_string += '<span class=\'prg-icon-lang\'>二</span>'
			elif t == "解":
				types_string += '<span class=\'prg-icon-cmnt\'>解</span>'
			elif t == "手":
				types_string += '<span class=\'prg-icon-sign\'>手</span>'
			elif t == "S":
				types_string += '<span class=\'prg-icon-ss\'>SS</span>'
			elif t == "吹":
				types_string += '<span class=\'prg-icon-dubb\'>吹</span>'
			elif t == "多":
				types_string += '<span class=\'prg-icon-sec\'>多</span>'
			elif t == "前":
				types_string += '<span class=\'prg-icon-fp\'>前</span>'
			elif t == "後":
				types_string += '<span class=\'prg-icon-lp\'>後</span>'

		full_title = decode_string(titles[title_id][0])
		if splited_by_space:
			full_title += " "
		if chapter_id != None:
			full_title += decode_string(titles[title_id][1][chapter_id])

		a = util.time_decode_base60( timetables[month][day]["SUN2"][idx][:2] )
		b = util.time_decode_base60( timetables[month][day]["SUN2"][idx+1][:2] )
		interval = util.get_interval(a,b) * 5

		outfile.write('<div class=\'box sv2\' style=height:' + str(interval) + 'px>\n')
		outfile.write('<span class=\'st-time\'>' + hour + ':' + minute + '</span>\n')
		outfile.write(types_string + '\n')
		outfile.write('<span class=\'st-title\'>' + full_title + '</span>\n')
		outfile.write('<p class=\'st-detail\'>' + decode_string(descriptions[desc_id]) + '</p>\n')
		outfile.write('</div>\n')
		idx += 1

	outfile.write('</body></html>\n')
	outfile.close()

def output_html_nhk(year, month, day, nhk_area):
	area = nhk.convertToTvkingdomArea(nhk_area)
	if not "sG"+area in timetables[month][day] and not "sE"+area in timetables[month][day]:
		return

	dir_path = "restore" + year + "/" + month + "/" + day
	if not os.path.isdir(dir_path):
		os.makedirs(dir_path)
	file_path = dir_path + "/" + year + "_" + month + "_" + day + "_NHK" + nhk_area + ".html"
	outfile = open(file_path, "w")

	chunks = []
	for i in [0,2,4,6,7,8,9,10,11]:
		chunks.append({"column":i, "top":0, "height":1600, "chunk":""})
	if not "sG"+area in timetables[month][day]:
		chunks.append({"column":1, "top":0, "height":1600, "chunk":""})
	if not "sE"+area in timetables[month][day]:
		chunks.append({"column":3, "top":0, "height":1600, "chunk":""})
	if not "NB2" in timetables[month][day]:
		chunks.append({"column":5, "top":0, "height":1600, "chunk":""})

	idx = 0
	height = 0
	if "sG"+area in timetables[month][day]:
		for c in timetables[month][day]["sG"+area]:
			if c not in timetables[month][day]["G"+area]:
				splited = c.split(":")
				if len(splited) == 1:
					interval = util.get_interval(util.time_decode_base60(timetables[month][day]["sG"+area][idx]), util.time_decode_base60(timetables[month][day]["sG"+area][idx+1]))
				else:
					interval = (int)(splited[1])
				h_m = (int)(util.time_decode_base60(c))
				minute = math.floor(h_m/100)*60+(h_m%100) -255
				if minute-height != 0:
					chunks.append({"column":1, "top":height, "height":minute-height, "chunk":""})
					height += minute-height
				chunks.append({"column":1, "top":height, "height":interval, "chunk":c})
				height += interval
			idx += 1
		chunks.append({"column":1, "top":height, "height":1600-height, "chunk":""})

	idx = 0
	height = 0
	if "sE"+area in timetables[month][day]:
		for c in timetables[month][day]["sE"+area]:
			if c not in timetables[month][day]["E"+area]:
				splited = c.split(":")
				if len(splited) == 1:
					interval = util.get_interval(util.time_decode_base60(timetables[month][day]["sE"+area][idx]), util.time_decode_base60(timetables[month][day]["sE"+area][idx+1]))
				else:
					interval = (int)(splited[1])
				h_m = (int)(util.time_decode_base60(c))
				minute = math.floor(h_m/100)*60+(h_m%100) -255
				if minute-height != 0:
					chunks.append({"column":3, "top":height, "height":minute-height, "chunk":""})
					height += minute-height
				chunks.append({"column":3, "top":height, "height":interval, "chunk":c})
				height += interval
			idx += 1
		chunks.append({"column":3, "top":height, "height":1600-height, "chunk":""})

	idx = 0
	height = 0
	if "NB2" in timetables[month][day]:
		for c in timetables[month][day]["NB2"]:
			if c not in timetables[month][day]["BS1"]:
				splited = c.split(":")
				if len(splited) == 1:
					interval = util.get_interval(util.time_decode_base60(timetables[month][day]["NB2"][idx]), util.time_decode_base60(timetables[month][day]["NB2"][idx+1]))
				else:
					interval = (int)(splited[1])
				h_m = (int)(util.time_decode_base60(c))
				minute = math.floor(h_m/100)*60+(h_m%100) -255
				if minute-height != 0:
					chunks.append({"column":5, "top":height, "height":minute-height, "chunk":""})
					height += minute-height
				chunks.append({"column":5, "top":height, "height":interval, "chunk":c})
				height += interval
			idx += 1
		chunks.append({"column":5, "top":height, "height":1600-height, "chunk":""})

	chunks_sorted = sorted(chunks, key=lambda x:(x["top"],x["column"]))

	outfile.write('<html><head><meta charset="utf-8" /></head><body><div area="' + nhk_area + '" date="' + year + month + day + '"><button>現在の時刻</button>\n')

	for chunk in chunks_sorted:

		category, types, title_id, chapter_id, desc_id, interval, splited_by_space = read_chunk(chunk["chunk"])

		types_string = ""
		for t in types:
			if t == "解":
				types_string += '<img src="' + nhk.IMG_COMMENT + '">'
			elif t == "S":
				types_string += '<img src="' + nhk.IMG_STEREO + '">'
			elif t == "SS":
				types_string += '<img src="' + nhk.IMG_SS + '">'
			elif t == "二":
				types_string += '<img src="' + nhk.IMG_BILINGUAL + '">'
			elif t == "多":
				types_string += '<img src="' + nhk.IMG_MULTISOUND + '">'
			elif t == "字":
				types_string += '<img src="' + nhk.IMG_SUB + '">'
			elif t == "手":
				types_string += '<img src="' + nhk.IMG_SIGN + '">'
			elif t == "デ":
				types_string += '<img src="' + nhk.IMG_DATA + '">'
			elif t == "双":
				types_string += '<img src="' + nhk.IMG_INTER + '">'
			elif t == "再":
				types_string += '<img src="' + nhk.IMG_RE + '">'

		full_title = decode_string(titles[title_id][0])
		if splited_by_space:
			full_title += " "
		if chapter_id != None:
			full_title += decode_string(titles[title_id][1][chapter_id])
		if "終" in types:
			full_title += "［終］"

		outfile.write('<td data-v="" colspan="1" rowspan="' + str(chunk["height"]) + '">\n');
		if chunk["chunk"] != "":
			m = util.time_decode_base60(chunk["chunk"])
			hour_int = math.floor((int)(m)/100)
			if hour_int < 12:
				hour = "午前" + str(hour_int)
			elif hour_int < 24:
				hour = "午後" + str(hour_int-12)
			else:
				hour = "午前" + str(hour_int-24)
			minute = str(m)[-2:]
			outfile.write('<p class="time">' + hour + ':' + minute + '</p>\n')
			outfile.write('<p><a class="to-dtl">' + full_title + '</a></p>' + types_string + '\n')
			outfile.write('<div class="arrow">' + decode_string(descriptions[desc_id]) + '</div>\n')
		outfile.write('</td>\n')

	outfile.write('</div></body></html>\n')
	outfile.close()

def output_html_bs4(days):
	hit = [False,False,False,False,False,False,False]
	hit_one = False
	idx = 0
	for d in days:
		if d.month < 10:
			month = "0" + str(d.month)
		else:
			month = str(d.month)
		if d.day < 10:
			day = "0" + str(d.day)
		else:
			day = str(d.day)
		if month in timetables and day in timetables[month] and "BN2" in timetables[month][day]:
			hit[idx] = True
			hit_one = True
		idx += 1
	if not hit_one:
		return

	file_path = "restore" + year + "/" + month + "/" + year + "_" + str(days[0].isocalendar()[1]) + "week_bs141.html"
	outfile = open(file_path, "w")
	outfile.write('<html><head><meta charset="utf-8" /></head><body>\n')
	outfile.write('</body></html>\n')
	outfile.close()

	chunks = []
	chunks.append({"column":0, "top":0, "height":60*30, "chunk":""})
	chunks.append({"column":8, "top":0, "height":60*30, "chunk":""})
	for i in [1,2,3,4,5,6,7]:
		if not hit[i-1]:
			chunks.append({"column":i, "top":0, "height":60*30, "chunk":""})

	for d in range(7):
		if days[d].day < 10:
			day = "0" + str(days[d].day)
		else:
			day = str(days[d].day)
		idx = 0
		height = 0
		if hit[d]:
			for c in timetables[month][day]["BN2"]:
				if c not in timetables[month][day]["BS4"]:
					splited = c.split(":")
					if len(splited) == 1:
						interval = util.get_interval(util.time_decode_base60(timetables[month][day]["BN2"][idx]), util.time_decode_base60(timetables[month][day]["BN2"][idx+1]))
					else:
						interval = (int)(splited[1])
					h_m = (int)(util.time_decode_base60(c))
					minute = math.floor(h_m/100)*60+(h_m%100)
					if minute-height != 0:
						chunks.append({"column":d+1, "top":height, "height":minute-height, "chunk":""})
						height += minute-height
					chunks.append({"column":d+1, "top":height, "height":interval, "chunk":c})
					height += interval
				idx += 1
			chunks.append({"column":d+1, "top":height, "height":60*30-height, "chunk":""})

	chunks_sorted = sorted(chunks, key=lambda x:(x["top"],x["column"]))

	file_path = "restore" + year + "/" + month + "/" + year + "_" + str(days[0].isocalendar()[1]) + "week_bs142.html"
	outfile = open(file_path, "w")
	outfile.write('<html><head><meta charset="utf-8" /></head><body>\n')

	for chunk in chunks_sorted:
		category, types, title_id, chapter_id, desc_id, interval, splited_by_space = read_chunk(chunk["chunk"])

		types_string = ""
		for t in types:
			if t == "新":
				types_string += '<div class="programschedule-icon icon-new"></div>'
			elif t == "終":
				types_string += '<div class="programschedule-icon icon-end"></div>'
			elif t == "前":
				types_string += '<div class="programschedule-icon icon-fpart"></div>'
			elif t == "後":
				types_string += '<div class="programschedule-icon icon-lpart"></div>'
			elif t == "生":
				types_string += '<div class="programschedule-icon icon-live"></div>'
			elif t == "再":
				types_string += '<div class="programschedule-icon icon-repeat"></div>'
			elif t == "二":
				types_string += '<div class="programschedule-icon icon-bilingual"></div>'
			elif t == "多":
				types_string += '<div class="programschedule-icon icon-multiplex"></div>'
			elif t == "S":
				types_string += '<div class="programschedule-icon icon-stereo"></div>'
			elif t == "SS":
				types_string += '<div class="programschedule-icon icon-ss"></div>'
			elif t == "字":
				types_string += '<div class="programschedule-icon icon-caption"></div>'
			elif t == "デ":
				types_string += '<div class="programschedule-icon icon-data"></div>'
			elif t == "双":
				types_string += '<div class="programschedule-icon icon-bidirectional"></div>'

		full_title = decode_string(titles[title_id][0])
		if splited_by_space:
			full_title += " "
		if chapter_id != None:
			full_title += decode_string(titles[title_id][1][chapter_id])

		outfile.write('<td rowspan="' + str(chunk["height"]) + '">\n')
		if chunk["chunk"] != "":
			m = util.time_decode_base60(chunk["chunk"])
			outfile.write('<div programschedule-item__starttime">\n          ' + m[:2] + '：' + m[-2:] + '\n</div>\n')
			outfile.write('<div class="programschedule-item__icon">' + types_string + '</div>\n')
			outfile.write('<div class="programschedule-item__title">' + full_title + '</div>\n')
		outfile.write('</td>\n')

	outfile.write('</body></html>\n')
	outfile.close()



if __name__ == "__main__":
	global timetables, original_timetables, station_names, decoder
	global decoder1_range, decoder2_range, decoder3_range

	year = "2021"
	abc_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x"]
	base60 = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x"]

	decoder = get_decoder()
	decoder1_range = len(decoder[0])
	decoder2_range = (int)(len(decoder[1]) / 2)
	decoder3_range = (int)(len(decoder[2]) / 3)

	type_names = load_hash_array("scripts/type_names.js")
	original_timetables = load_hash_array("scripts/timetables.js")
	titles = load_hash_array("scripts/titles.js")
	descriptions = load_hash_array("scripts/descriptions.js")

	timetables = {}
	for month in original_timetables:
		timetables[month] = {}
		for day in original_timetables[month]:
			timetables[month][day] = {}
			for station in original_timetables[month][day]:
				result = decompressProgramChunk(month, day, station, original_timetables[month][day][station])
				timetables[month][day][station] = split_chunk(result)

	for month in timetables:
		for day in timetables[month]:
			print(year+"-"+month+"-"+day)
			output_html(year, month, day, "10", ["HBC","E10","G10","STV","HTB","TVH","UHB"])
			output_html(year, month, day, "11", ["HBC","E11","G11","STV","HTB","TVH","UHB"])
			output_html(year, month, day, "12", ["HBC","E12","G12","STV","HTB","TVH","UHB"])
			output_html(year, month, day, "13", ["HBC","E13","G13","STV","HTB","TVH","UHB"])
			output_html(year, month, day, "14", ["HBC","E14","G14","STV","HTB","TVH","UHB"])
			output_html(year, month, day, "15", ["HBC","E15","G15","STV","HTB","TVH","UHB"])
			output_html(year, month, day, "16", ["HBC","E16","G16","STV","HTB","TVH","UHB"])
			output_html(year, month, day, "22", ["RAB","E22","G22","ABA","ATV"])
			output_html(year, month, day, "20", ["G20","E20","TVI","IAT","IBC","MIT"])
			output_html(year, month, day, "17", ["TBC","E17","G17","MMT","KHB","OX"])
			output_html(year, month, day, "18", ["G18","E18","ABS","ABS2","AAB","AKT"])
			output_html(year, month, day, "19", ["G19","E19","YBC","YTS","TUY","SAY"])
			output_html(year, month, day, "21", ["G21","E21","FCT","KFB","TUF","FTV"])
			output_html(year, month, day, "26", ["G26","E23","NTV","EX","TBS","TX","CX","G23"])
			output_html(year, month, day, "28", ["G28","E23","TTV","NTV","TBS","CX","EX","TX","G28"])
			output_html(year, month, day, "25", ["G25","E23","GTV","NTV","TBS","CX","EX","TX","G25"])
			output_html(year, month, day, "29", ["G23","E23","TVS","NTV","EX","TBS","TX","CX"])
			output_html(year, month, day, "27", ["G23","E23","CTC","NTV","EX","TBS","TX","CX"])
			output_html(year, month, day, "23", ["G23","E23","NTV","EX","TBS","TX","CX","MX"])
			output_html(year, month, day, "24", ["G23","E23","TVK","NTV","EX","TBS","TX","CX"])
			output_html(year, month, day, "31", ["G31","E31","TENY","UX","BSN","NST"])
			output_html(year, month, day, "32", ["G32","E32","YBS","UTY"])
			output_html(year, month, day, "30", ["G30","E30","TSB","ABN","SBC","NBS"])
			output_html(year, month, day, "37", ["KNB","E37","G37","TUT","BBT"])
			output_html(year, month, day, "34", ["G34","E34","KTK","HAB","MRO","ITC"])
			output_html(year, month, day, "36", ["G36","E36","FBC","FTB"])
			output_html(year, month, day, "39", ["THK","E33","G39","CTV","CBC","NBN","GBS"])
			output_html(year, month, day, "35", ["G35","E35","SDT","SATV","SBS","SUT"])
			output_html(year, month, day, "33", ["THK","E33","G33","CTV","CBC","NBN","TVA"])
			output_html(year, month, day, "38", ["THK","E33","G38","CTV","CBC","NBN","MTV"])
			output_html(year, month, day, "45", ["G45","E40","BBC","MBS","ABC","KTV","YTV"])
			output_html(year, month, day, "41", ["G41","E40","MBS","KBS","ABC","KTV","YTV"])
			output_html(year, month, day, "40", ["G40","E40","MBS","ABC","TVO","KTV","YTV"])
			output_html(year, month, day, "42", ["G42","E40","SUN","MBS","ABC","KTV","YTV"])
			output_html(year, month, day, "44", ["G44","E40","MBS","ABC","KTV","TVN","YTV"])
			output_html(year, month, day, "43", ["G43","E40","MBS","WTV","ABC","KTV","YTV"])
			output_html(year, month, day, "49", ["NKT","E49","G49","BSS","TSK","TSK2"])
			output_html(year, month, day, "48", ["NKT","E48","G48","BSS","TSK","TSK2"])
			output_html(year, month, day, "47", ["G47","E47","RNC","KSB","RSK","TSC","OHK"])
			output_html(year, month, day, "46", ["G46","E46","RCC","HTV","HOME","TSS"])
			output_html(year, month, day, "50", ["G50","E50","TYS","KRY","YAB"])
			output_html(year, month, day, "53", ["JRT","E53","G53"])
			output_html(year, month, day, "52", ["G52","E52","RNC","KSB","RSK","TSC","OHK"])
			output_html(year, month, day, "51", ["G51","E51","RNB","EAT","ITV","EBC"])
			output_html(year, month, day, "54", ["G54","E54","RKC","KUTV","KSS"])
			output_html(year, month, day, "55", ["KBC","E55","G55","RKB","FBS","TVQ","TNC","Ekk","Gkk"])
			output_html(year, month, day, "61", ["G61","E61","STS"])
			output_html(year, month, day, "57", ["G57","E57","NBC","NIB","NCC","KTN"])
			output_html(year, month, day, "56", ["G56","E56","RKK","KKT","KAB","TKU"])
			output_html(year, month, day, "60", ["G60","E60","OBS","TOS","OAB"])
			output_html(year, month, day, "59", ["G59","E59","UMK","MRT"])
			output_html(year, month, day, "58", ["MBC","E58","G58","KYT","KYT3","KKB","KTS"])
			output_html(year, month, day, "62", ["G62","E62","RBC","QAB","OTV"])
			output_html(year, month, day, "bs1", ["BS1","BSp","BS4","BS5","BS6","BS7","BS8"])
			output_html(year, month, day, "bs2", ["WW1","WW2","WW3","SC1","SC2","SC3","BS11","BS12","OU1"])
			output_html(year, month, day, "bs3", ["GCH","BSA","SKY","JS1","JS2","JS3","JS4"])
			output_html(year, month, day, "bs4", ["BSF","WW4","JMV","DCH"])
			output_html(year, month, day, "bs4k8k_1", ["FK1","FK4","FK5","FK6","FK7","FK8"])
			output_html(year, month, day, "bs4k8k_2", ["EK1","FKW","FKC","FKS","QVC"])
			output_html(year, month, day, "23_EX2", ["EX2"])
			output_html(year, month, day, "23_MX2", ["MX2"])
			output_html(year, month, day, "27_CTC2", ["CTC2"])
			output_html(year, month, day, "27_CTC3", ["CTC3"])
			output_html_ouj(year, month, day)
			#output_html_mxtv(year, month, day)
			output_html_mietv(year, month, day)
			output_html_suntv(year, month, day)
			for nhk_area in nhk.nhk_areas:
				output_html_nhk(year, month, day, nhk_area)


	d = datetime.date(2021, 1, 1)
	days = []
	for i in range(d.weekday()):
		days.append(datetime.date(2020, 12, 31))
	while d != datetime.date(2022, 1, 1):
		days.append(d)
		if d.weekday() == 6:
			output_html_bs4(days)
			days = []
		d += datetime.timedelta(days=1)
	output_html_bs4(days)
