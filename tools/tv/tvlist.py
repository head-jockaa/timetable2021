# coding:utf-8

NHK_NET = ["G10", "G11", "G12", "G13", "G14", "G15", "G16", "G17", "G18", "G19", "G20", "G21", "G22", "G25", "G26", "G28", "G30", "G31", "G32", "G33", "G34", "G35", "G36", "G37", "G38", "G39", "G40", "G41", "G42", "G43", "G44", "G45", "G46", "G47", "G48", "G49", "G50", "G51", "G52", "G53", "G54", "G55", "G56", "G57", "G58", "G59", "G60", "G61", "G62", "Gkk"]
ETV_NET = ["E10", "E11", "E12", "E13", "E14", "E15", "E16", "E17", "E18", "E19", "E20", "E21", "E22", "E30", "E31", "E32", "E33", "E34", "E35", "E36", "E37", "E40", "E46", "E47", "E48", "E49", "E50", "E51", "E52", "E53", "E54", "E55", "E56", "E57", "E58", "E59", "E60", "E61", "E62", "Ekk"]
NTV_NET = ["YTV", "CTV", "STV", "RAB", "ABS", "TVI", "YBC", "MMT", "FCT", "YBS", "TENY", "TSB", "SDT", "KNB", "KTK", "FBC", "RNC", "HTV", "NKT", "KRY", "JRT", "RNB", "RKC", "FBS", "NIB", "KKT", "KYT"]
TBS_NET = ["MBS", "CBC", "HBC", "ATV", "IBC", "TUY", "TBC", "TUF", "UTY", "BSN", "SBC", "SBS", "TUT", "MRO", "RSK", "RCC", "BSS", "TYS", "ITV", "KUTV", "RKB", "NBC", "RKK", "OBS", "MRT", "MBC", "RBC"]
CX_NET = ["KTV", "THK", "UHB", "AKT", "MIT", "SAY", "OX", "FTV", "NST", "NBS", "SUT", "BBT", "ITC", "FTB", "OHK", "TSS", "TSK", "EBC", "KSS", "TNC", "STS", "KTN", "TKU", "KTS", "OTV"]
EX_NET = ["ABC", "NBN", "HTB", "ABA", "AAB", "IAT", "YTS", "KHB", "KFB", "UX", "ABN", "SATV", "HAB", "KSB", "HOME", "YAB", "EAT", "KBC", "NCC", "KAB", "OAB", "KKB", "QAB"]
TX_NET = ["TVO", "TVA", "TVH", "TSC", "TVQ"]

NON_NTV_NET = ["RBC", "STS", "OTV", "QAB", "TOS", "UMK"]
NON_TBS_NET = ["ABS", "YBS", "FBC", "JRT", "AKT", "FTB", "STS", "AAB"]
NON_CX_NET = ["RAB", "YBS", "KRY", "JRT", "ATV", "UTY", "TYS", "ABA", "YAB", "TOS", "UMK"]
NON_EX_NET = ["YBS", "KNB", "FBC", "NKT", "JRT", "RKC", "UTY", "TUT", "BSS", "KUTV", "MRT", "BBT", "FTB", "TSK", "KSS", "STS", "UMK"]
NON_TX_NET = ["RAB", "ABS", "TVI", "YBC", "MMT", "FCT", "YBS", "TENY", "TSB", "SDT", "KNB", "KTK", "FBC", "HTV", "NKT", "KRY", "JRT", "RNB", "RKC", "NIB", "KKT", "KYT", "ATV", "IBC", "TUY", "TBC", "TUF", "UTY", "BSN", "SBC", "SBS", "TUT", "MRO", "RCC", "BSS", "TYS", "ITV", "KUTV", "NBC", "RKK", "OBS", "MRT", "MBC", "RBC", "AKT", "MIT", "SAY", "OX", "FTV", "NST", "NBS", "SUT", "BBT", "ITC", "FTB", "TSS", "TSK", "EBC", "KSS", "STS", "KTN", "TKU", "KTS", "OTV", "ABA", "AAB", "IAT", "YTS", "KHB", "KFB", "UX", "ABN", "SATV", "HAB", "HOME", "YAB", "EAT", "NCC", "KAB", "OAB", "KKB", "QAB", "TOS", "UMK", "MTV", "GBS", "KBS", "BBC", "TVN", "WTV", "BS7", "FK7"]
OTHER_NET = ["MX", "MX2", "TVK", "TVS", "CTC", "CTC2", "CTC3", "GTV", "TTV", "MTV", "GBS", "SUN", "KBS", "BBC", "TVN", "WTV"]


def get_station_name_tag(s):
	if s == "ＮＨＫ総合１・札幌":
		return "G10"
	elif s == "ＮＨＫ総合１・函館":
		return "G11"
	elif s == "ＮＨＫ総合１・旭川":
		return "G12"
	elif s == "ＮＨＫ総合１・帯広":
		return "G13"
	elif s == "ＮＨＫ総合１・釧路":
		return "G14"
	elif s == "ＮＨＫ総合１・北見":
		return "G15"
	elif s == "ＮＨＫ総合１・室蘭":
		return "G16"
	elif s == "ＮＨＫ総合１・青森":
		return "G22"
	elif s == "ＮＨＫ総合１・盛岡":
		return "G20"
	elif s == "ＮＨＫ総合１・仙台":
		return "G17"
	elif s == "ＮＨＫ総合１・秋田":
		return "G18"
	elif s == "ＮＨＫ総合１・山形":
		return "G19"
	elif s == "ＮＨＫ総合１・福島":
		return "G21"
	elif s == "ＮＨＫ総合１・水戸":
		return "G26"
	elif s == "ＮＨＫ総合１・宇都宮":
		return "G28"
	elif s == "ＮＨＫ総合１・前橋":
		return "G25"
	elif s == "ＮＨＫ総合１・東京":
		return "G23"
	elif s == "ＮＨＫ総合１・新潟":
		return "G31"
	elif s == "ＮＨＫ総合１・富山":
		return "G37"
	elif s == "ＮＨＫ総合１・金沢":
		return "G34"
	elif s == "ＮＨＫ総合１・福井":
		return "G36"
	elif s == "ＮＨＫ総合１・甲府":
		return "G32"
	elif s == "ＮＨＫ総合１・長野":
		return "G30"
	elif s == "ＮＨＫ総合１・岐阜":
		return "G39"
	elif s == "ＮＨＫ総合１・静岡":
		return "G35"
	elif s == "ＮＨＫ総合１・名古屋":
		return "G33"
	elif s == "ＮＨＫ総合１・津":
		return "G38"
	elif s == "ＮＨＫ総合１・大津":
		return "G45"
	elif s == "ＮＨＫ総合１・京都":
		return "G41"
	elif s == "ＮＨＫ総合１・大阪":
		return "G40"
	elif s == "ＮＨＫ総合１・神戸":
		return "G42"
	elif s == "ＮＨＫ総合１・奈良":
		return "G44"
	elif s == "ＮＨＫ総合１・和歌山":
		return "G43"
	elif s == "ＮＨＫ総合１・鳥取":
		return "G49"
	elif s == "ＮＨＫ総合１・松江":
		return "G48"
	elif s == "ＮＨＫ総合１・岡山":
		return "G47"
	elif s == "ＮＨＫ総合１・広島":
		return "G46"
	elif s == "ＮＨＫ総合１・山口":
		return "G50"
	elif s == "ＮＨＫ総合１・徳島":
		return "G53"
	elif s == "ＮＨＫ総合１・高松":
		return "G52"
	elif s == "ＮＨＫ総合１・松山":
		return "G51"
	elif s == "ＮＨＫ総合１・高知":
		return "G54"
	elif s == "ＮＨＫ総合１・福岡":
		return "G55"
	elif s == "ＮＨＫ総合１・北九州":
		return "Gkk"
	elif s == "ＮＨＫ総合１・佐賀":
		return "G61"
	elif s == "ＮＨＫ総合１・長崎":
		return "G57"
	elif s == "ＮＨＫ総合１・熊本":
		return "G56"
	elif s == "ＮＨＫ総合１・大分":
		return "G60"
	elif s == "ＮＨＫ総合１・宮崎":
		return "G59"
	elif s == "ＮＨＫ総合１・鹿児島":
		return "G58"
	elif s == "ＮＨＫ総合１・沖縄":
		return "G62"
	elif s == "ＮＨＫＥテレ１・札幌":
		return "E10"
	elif s == "ＮＨＫＥテレ１・函館":
		return "E11"
	elif s == "ＮＨＫＥテレ１・旭川":
		return "E12"
	elif s == "ＮＨＫＥテレ１・帯広":
		return "E13"
	elif s == "ＮＨＫＥテレ１・釧路":
		return "E14"
	elif s == "ＮＨＫＥテレ１・北見":
		return "E15"
	elif s == "ＮＨＫＥテレ１・室蘭":
		return "E16"
	elif s == "ＮＨＫＥテレ１・青森":
		return "E22"
	elif s == "ＮＨＫＥテレ１・盛岡":
		return "E20"
	elif s == "ＮＨＫＥテレ１・仙台":
		return "E17"
	elif s == "ＮＨＫＥテレ１・秋田":
		return "E18"
	elif s == "ＮＨＫＥテレ１・山形":
		return "E19"
	elif s == "ＮＨＫＥテレ１・福島":
		return "E21"
	elif s == "ＮＨＫＥテレ１・東京":
		return "E23"
	elif s == "ＮＨＫＥテレ１・新潟":
		return "E31"
	elif s == "ＮＨＫＥテレ１・富山":
		return "E37"
	elif s == "ＮＨＫＥテレ１・金沢":
		return "E34"
	elif s == "ＮＨＫＥテレ１・福井":
		return "E36"
	elif s == "ＮＨＫＥテレ１・甲府":
		return "E32"
	elif s == "ＮＨＫＥテレ１・長野":
		return "E30"
	elif s == "ＮＨＫＥテレ１・静岡":
		return "E35"
	elif s == "ＮＨＫＥテレ１・名古屋":
		return "E33"
	elif s == "ＮＨＫＥテレ１・大阪":
		return "E40"
	elif s == "ＮＨＫＥテレ１・鳥取":
		return "E49"
	elif s == "ＮＨＫＥテレ１・松江":
		return "E48"
	elif s == "ＮＨＫＥテレ１・岡山":
		return "E47"
	elif s == "ＮＨＫＥテレ１・広島":
		return "E46"
	elif s == "ＮＨＫＥテレ１・山口":
		return "E50"
	elif s == "ＮＨＫＥテレ１・徳島":
		return "E53"
	elif s == "ＮＨＫＥテレ１・高松":
		return "E52"
	elif s == "ＮＨＫＥテレ１・松山":
		return "E51"
	elif s == "ＮＨＫＥテレ１・高知":
		return "E54"
	elif s == "ＮＨＫＥテレ１・福岡":
		return "E55"
	elif s == "ＮＨＫＥテレ１・北九州":
		return "Ekk"
	elif s == "ＮＨＫＥテレ１・佐賀":
		return "E61"
	elif s == "ＮＨＫＥテレ１・長崎":
		return "E57"
	elif s == "ＮＨＫＥテレ１・熊本":
		return "E56"
	elif s == "ＮＨＫＥテレ１・大分":
		return "E60"
	elif s == "ＮＨＫＥテレ１・宮崎":
		return "E59"
	elif s == "ＮＨＫＥテレ１・鹿児島":
		return "E58"
	elif s == "ＮＨＫＥテレ１・沖縄":
		return "E62"
	elif s == "札幌テレビ":
		return "STV"
	elif s == "ＨＢＣ北海道放送":
		return "HBC"
	elif s == "北海道文化放送":
		return "UHB"
	elif s == "ＨＴＢ":
		return "HTB"
	elif s == "ＴＶｈ":
		return "TVH"
	elif s == "ＲＡＢ青森放送":
		return "RAB"
	elif s == "ＡＴＶ青森テレビ":
		return "ATV"
	elif s == "青森朝日放送":
		return "ABA"
	elif s == "テレビ岩手":
		return "TVI"
	elif s == "ＩＢＣテレビ":
		return "IBC"
	elif s == "めんこいテレビ":
		return "MIT"
	elif s == "岩手朝日テレビ":
		return "IAT"
	elif s == "ミヤギテレビ":
		return "MMT"
	elif s == "ＴＢＣテレビ":
		return "TBC"
	elif s == "仙台放送":
		return "OX"
	elif s == "東日本放送":
		return "KHB"
	elif s == "ABS秋田放送1":
		return "ABS"
	elif s == "ABS秋田放送2":
		return "ABS2"
	elif s == "ＡＫＴ秋田テレビ":
		return "AKT"
	elif s == "秋田朝日放送":
		return "AAB"
	elif s == "山形放送":
		return "YBC"
	elif s == "ＴＵＹ":
		return "TUY"
	elif s == "さくらんぼテレビ":
		return "SAY"
	elif s == "山形テレビ":
		return "YTS"
	elif s == "福島中央テレビ":
		return "FCT"
	elif s == "テレビユー福島":
		return "TUF"
	elif s == "ＦＴＶ福島テレビ":
		return "FTV"
	elif s == "ＫＦＢ福島放送":
		return "KFB"
	elif s == "日テレ":
		return "NTV"
	elif s == "ＴＢＳ":
		return "TBS"
	elif s == "フジテレビ":
		return "CX"
	elif s == "テレビ朝日":
		return "EX"
	elif s == "テレビ朝日２":
		return "EX2"
	elif s == "テレビ東京":
		return "TX"
	elif s == "とちぎテレビ":
		return "TTV"
	elif s == "群馬テレビ":
		return "GTV"
	elif s == "テレ玉":
		return "TVS"
	elif s == "チバテレ":
		return "CTC"
	elif s == "チバテレ2":
		return "CTC2"
	elif s == "チバテレ3":
		return "CTC3"
	elif s == "ＴＯＫＹＯ　ＭＸ１":
		return "MX"
	elif s == "ＴＯＫＹＯ　ＭＸ２":
		return "MX2"
	elif s == "ｔｖｋ":
		return "TVK"
	elif s == "ＴｅＮＹ":
		return "TENY"
	elif s == "ＢＳＮ":
		return "BSN"
	elif s == "新潟総合テレビ":
		return "NST"
	elif s == "新潟テレビ２１":
		return "UX"
	elif s == "ＫＮＢテレビ":
		return "KNB"
	elif s == "チューリップテレビ":
		return "TUT"
	elif s == "富山テレビ放送":
		return "BBT"
	elif s == "テレビ金沢":
		return "KTK"
	elif s == "ＭＲＯ":
		return "MRO"
	elif s == "石川テレビ":
		return "ITC"
	elif s == "ＨＡＢ":
		return "HAB"
	elif s == "福井放送":
		return "FBC"
	elif s == "福井テレビ":
		return "FTB"
	elif s == "山梨放送":
		return "YBS"
	elif s == "ＵＴＹ":
		return "UTY"
	elif s == "ＴＳＢ":
		return "TSB"
	elif s == "ＳＢＣ信越放送":
		return "SBC"
	elif s == "長野放送":
		return "NBS"
	elif s == "長野朝日放送":
		return "ABN"
	elif s == "中京テレビ":
		return "CTV"
	elif s == "ＣＢＣテレビ":
		return "CBC"
	elif s == "東海テレビ":
		return "THK"
	# 波ダッシュ(U+301C)ではなく全角チルダ(U+FF5E)
	elif s == "メ～テレ":
		return "NBN"
	elif s == "テレビ愛知":
		return "TVA"
	elif s == "ぎふチャン":
		return "GBS"
	elif s == "Daiichi-TV":
		return "SDT"
	elif s == "ＳＢＳ":
		return "SBS"
	elif s == "テレビ静岡":
		return "SUT"
	elif s == "静岡朝日テレビ":
		return "SATV"
	elif s == "三重テレビ１":
		return "MTV"
	elif s == "よみうりテレビ":
		return "YTV"
	elif s == "ＭＢＳ毎日放送":
		return "MBS"
	elif s == "関西テレビ":
		return "KTV"
	elif s == "ＡＢＣテレビ":
		return "ABC"
	elif s == "テレビ大阪":
		return "TVO"
	elif s == "ＢＢＣびわ湖放送":
		return "BBC"
	elif s == "ＫＢＳ京都":
		return "KBS"
	elif s == "サンテレビ１":
		return "SUN"
	elif s == "奈良テレビ":
		return "TVN"
	elif s == "ＷＴＶ":
		return "WTV"
	elif s == "日本海テレビ":
		return "NKT"
	elif s == "ＢＳＳテレビ":
		return "BSS"
	elif s == "さんいん中央テレビ１":
		return "TSK"
	elif s == "さんいん中央テレビ２":
		return "TSK2"
	elif s == "ＲＮＣ西日本テレビ":
		return "RNC"
	elif s == "ＲＳＫテレビ":
		return "RSK"
	elif s == "ＯＨＫ":
		return "OHK"
	elif s == "瀬戸内海放送":
		return "KSB"
	elif s == "テレビせとうち":
		return "TSC"
	elif s == "広島テレビ":
		return "HTV"
	elif s == "ＲＣＣテレビ":
		return "RCC"
	elif s == "テレビ新広島":
		return "TSS"
	elif s == "広島ホームテレビ":
		return "HOME"
	elif s == "山口放送１":
		return "KRY"
	elif s == "ｔｙｓテレビ山口":
		return "TYS"
	elif s == "ｙａｂ山口朝日":
		return "YAB"
	elif s == "四国放送":
		return "JRT"
	elif s == "南海放送":
		return "RNB"
	elif s == "あいテレビ":
		return "ITV"
	elif s == "テレビ愛媛":
		return "EBC"
	elif s == "愛媛朝日テレビ":
		return "EAT"
	elif s == "高知放送":
		return "RKC"
	elif s == "テレビ高知":
		return "KUTV"
	elif s == "高知さんさんテレビ":
		return "KSS"
	elif s == "ＦＢＳ福岡放送":
		return "FBS"
	elif s == "ＲＫＢ毎日放送":
		return "RKB"
	elif s == "テレビ西日本":
		return "TNC"
	elif s == "ＫＢＣテレビ":
		return "KBC"
	elif s == "ＴＶＱ九州放送":
		return "TVQ"
	elif s == "ＳＴＳサガテレビ":
		return "STS"
	elif s == "長崎国際テレビ":
		return "NIB"
	elif s == "ＮＢＣ長崎放送":
		return "NBC"
	elif s == "テレビ長崎":
		return "KTN"
	elif s == "ＮＣＣ長崎文化放送":
		return "NCC"
	elif s == "くまもと県民":
		return "KKT"
	elif s == "ＲＫＫ熊本放送":
		return "RKK"
	elif s == "テレビ熊本":
		return "TKU"
	elif s == "ＫＡＢ熊本朝日放送":
		return "KAB"
	elif s == "ＴＯＳテレビ大分":
		return "TOS"
	elif s == "ＯＢＳ大分放送":
		return "OBS"
	elif s == "ＯＡＢ大分朝日放送":
		return "OAB"
	elif s == "テレビ宮崎":
		return "UMK"
	elif s == "ＭＲＴ宮崎放送":
		return "MRT"
	elif s == "鹿児島讀賣テレビ":
		return "KYT"
	elif s == "鹿児島讀賣テレビ3":
		return "KYT3"
	elif s == "ＭＢＣ南日本放送":
		return "MBC"
	elif s == "鹿児島テレビ放送":
		return "KTS"
	elif s == "ＫＫＢ鹿児島放送":
		return "KKB"
	elif s == "ＲＢＣテレビ":
		return "RBC"
	elif s == "沖縄テレビ":
		return "OTV"
	elif s == "琉球朝日放送":
		return "QAB"
	elif s == "ＮＨＫ ＢＳ１":
		return "BS1"
	elif s == "ＮＨＫ ＢＳプレミアム":
		return "BSp"
	elif s == "ＢＳ日テレ":
		return "BS4"
	elif s == "ＢＳ朝日":
		return "BS5"
	elif s == "ＢＳ-ＴＢＳ":
		return "BS6"
	elif s == "ＢＳテレ東":
		return "BS7"
	elif s == "ＢＳフジ":
		return "BS8"
	elif s == "ＷＯＷＯＷプライム":
		return "WW1"
	elif s == "ＷＯＷＯＷライブ":
		return "WW2"
	elif s == "ＷＯＷＯＷシネマ":
		return "WW3"
	elif s == "WOWOWプラス":
		return "WW4"
	elif s == "スター・チャンネル1":
		return "SC1"
	elif s == "スター・チャンネル2":
		return "SC2"
	elif s == "スター・チャンネル3":
		return "SC3"
	elif s == "BS11イレブン":
		return "BS11"
	elif s == "BS12 トゥエルビ":
		return "BS12"
	elif s == "放送大学ex":
		return "OU1"
	elif s == "放送大学on":
		return "OU2"
	elif s == "グリーンチャンネル":
		return "GCH"
	elif s == "BSアニマックス":
		return "BSA"
	elif s == "BSスカパー!":
		return "SKY"
	elif s == "J SPORTS 1":
		return "JS1"
	elif s == "J SPORTS 2":
		return "JS2"
	elif s == "J SPORTS 3":
		return "JS3"
	elif s == "J SPORTS 4":
		return "JS4"
	elif s == "BS釣りビジョン":
		return "BSF"
	elif s == "BS日本映画専門チャンネル":
		return "JMV"
	elif s == "ディズニー・チャンネル":
		return "DCH"
	elif s == "NHK BS4K":
		return "FK1"
	elif s == "BS日テレ 4K":
		return "FK4"
	elif s == "BS朝日 4K":
		return "FK5"
	elif s == "BS-TBS 4K":
		return "FK6"
	elif s == "BSテレ東 4K":
		return "FK7"
	elif s == "BSフジ 4K":
		return "FK8"
	elif s == "NHK BS8K":
		return "EK1"
	elif s == "ＷＯＷＯＷ　４Ｋ":
		return "FKW"
	elif s == "ザ・シネマ 4K":
		return "FKC"
	elif s == "ショップチャンネル 4K":
		return "FKS"
	elif s == "4K QVC":
		return "QVC"
	return ""
