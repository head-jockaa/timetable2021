# coding:utf-8

NHK1_NET = ["NHK1_010", "NHK1_011", "NHK1_012", "NHK1_013", "NHK1_014", "NHK1_015", "NHK1_016", "NHK1_020", "NHK1_030", "NHK1_040", "NHK1_050", "NHK1_060", "NHK1_070", "NHK1_150", "NHK1_160", "NHK1_170", "NHK1_180", "NHK1_190", "NHK1_200", "NHK1_220", "NHK1_230", "NHK1_250", "NHK1_270", "NHK1_310", "NHK1_320", "NHK1_330", "NHK1_340", "NHK1_350", "NHK1_360", "NHK1_370", "NHK1_380", "NHK1_390", "NHK1_400", "NHK1_401", "NHK1_410", "NHK1_420", "NHK1_430", "NHK1_440", "NHK1_450", "NHK1_460", "NHK1_470"]

NHKFM_NET = ["NHKFM_010", "NHKFM_011", "NHKFM_012", "NHKFM_013", "NHKFM_014", "NHKFM_015", "NHKFM_016", "NHKFM_020", "NHKFM_030", "NHKFM_040", "NHKFM_050", "NHKFM_060", "NHKFM_070", "NHKFM_080", "NHKFM_090", "NHKFM_100", "NHKFM_110", "NHKFM_120", "NHKFM_140", "NHKFM_150", "NHKFM_160", "NHKFM_170", "NHKFM_180", "NHKFM_190", "NHKFM_200", "NHKFM_210", "NHKFM_220", "NHKFM_230", "NHKFM_240", "NHKFM_250", "NHKFM_260", "NHKFM_270", "NHKFM_280", "NHKFM_290", "NHKFM_300", "NHKFM_310", "NHKFM_320", "NHKFM_330", "NHKFM_340", "NHKFM_350", "NHKFM_360", "NHKFM_370", "NHKFM_380", "NHKFM_390", "NHKFM_400", "NHKFM_401", "NHKFM_410", "NHKFM_420", "NHKFM_430", "NHKFM_440", "NHKFM_450", "NHKFM_460", "NHKFM_470"]

FM_NET = ["AIRG","AFB","FMI","DATEFM","AFM","RFM","FMF","RADIOBERRY","FMGUNMA","FMNIIGATA","FMTOYAMA","HELLOFIVE","FMFUKUI","FMN","FMAICHI","FMGIFU","KMIX","FMMIE","FMO","KISSFMKOBE","ERADIO","FMSANIN","FMOKAYAMA","HFM","FMY","FM807","FMKAGAWA","JOEUFM","HISIX","FMFUKUOKA","FMS","FMNAGASAKI","FMK","FMOITA","JOYFM","MYUFM","FMOKINAWA"]


def get_station_name_tag(s):
	if s == "ＨＢＣラジオ":
		return "HBC"
	elif s == "ＳＴＶラジオ":
		return "STV"
	elif s == "AIR-G&#39;（FM北海道）":
		return "AIRG"
	elif s == "FM NORTH WAVE":
		return "NORTHWAVE"
	elif s == "ＲＡＢ青森放送":
		return "RAB"
	elif s == "エフエム青森":
		return "AFB"
	elif s == "IBCラジオ":
		return "IBC"
	elif s == "エフエム岩手":
		return "FMI"
	elif s == "TBCラジオ":
		return "TBC"
	elif s == "Date fm エフエム仙台":
		return "DATEFM"
	elif s == "ＡＢＳ秋田放送":
		return "ABS"
	elif s == "エフエム秋田":
		return "AFM"
	elif s == "YBC山形放送":
		return "YBC"
	elif s == "Rhythm Station　エフエム山形":
		return "RFM"
	elif s == "RFCラジオ福島":
		return "RFC"
	elif s == "ふくしまFM":
		return "FMF"
	elif s == "TBSラジオ":
		return "TBS"
	elif s == "文化放送":
		return "QRR"
	elif s == "ニッポン放送":
		return "LFR"
	elif s == "InterFM897":
		return "INT"
	elif s == "TOKYO FM":
		return "FMT"
	elif s == "J-WAVE":
		return "FMJ"
	elif s == "ラジオ日本":
		return "JORF"
	elif s == "bayfm78":
		return "BAYFM78"
	elif s == "NACK5":
		return "NACK5"
	elif s == "ＦＭヨコハマ":
		return "YFM"
	elif s == "IBS茨城放送" or s == "LuckyFM 茨城放送":
		return "IBS"
	elif s == "CRT栃木放送":
		return "CRT"
	elif s == "RadioBerry":
		return "RADIOBERRY"
	elif s == "FM GUNMA":
		return "FMGUNMA"
	elif s == "ＢＳＮラジオ":
		return "BSN"
	elif s == "FM NIIGATA":
		return "FMNIIGATA"
	elif s == "ＫＮＢラジオ":
		return "KNB"
	elif s == "ＦＭとやま":
		return "FMTOYAMA"
	elif s == "MROラジオ":
		return "MRO"
	elif s == "エフエム石川":
		return "HELLOFIVE"
	elif s == "FBCラジオ":
		return "FBC"
	elif s == "FM福井":
		return "FMFUKUI"
	elif s == "ＹＢＳラジオ":
		return "YBS"
	elif s == "FM FUJI":
		return "FMFUJI"
	elif s == "SBCラジオ":
		return "SBC"
	elif s == "ＦＭ長野":
		return "FMN"
	elif s == "CBCラジオ":
		return "CBC"
	elif s == "東海ラジオ":
		return "TOKAIRADIO"
	elif s == "ぎふチャン":
		return "GBS"
	elif s == "ZIP-FM":
		return "ZIPFM"
	elif s == "FM AICHI":
		return "FMAICHI"
	elif s == "ＦＭ ＧＩＦＵ":
		return "FMGIFU"
	elif s == "SBSラジオ":
		return "SBS"
	elif s == "K-MIX SHIZUOKA":
		return "KMIX"
	elif s == "レディオキューブ ＦＭ三重":
		return "FMMIE"
	elif s == "ABCラジオ":
		return "ABC"
	elif s == "MBSラジオ":
		return "MBS"
	elif s == "OBCラジオ大阪":
		return "OBC"
	elif s == "FM COCOLO":
		return "CCL"
	elif s == "FM802":
		return "802"
	elif s == "FM大阪":
		return "FMO"
	elif s == "Kiss FM KOBE":
		return "KISSFMKOBE"
	elif s == "ラジオ関西":
		return "CRK"
	elif s == "e-radio FM滋賀":
		return "ERADIO"
	elif s == "KBS京都ラジオ":
		return "KBS"
	elif s == "α-STATION FM京都":
		return "ALPHASTATION"
	elif s == "wbs和歌山放送":
		return "WBS"
	elif s == "BSSラジオ":
		return "BSS"
	elif s == "エフエム山陰":
		return "FMSANIN"
	elif s == "ＲＳＫラジオ":
		return "RSK"
	elif s == "ＦＭ岡山":
		return "FMOKAYAMA"
	elif s == "RCCラジオ":
		return "RCC"
	elif s == "広島FM":
		return "HFM"
	elif s == "ＫＲＹ山口放送":
		return "KRY"
	elif s == "エフエム山口":
		return "FMY"
	elif s == "ＪＲＴ四国放送":
		return "JRT"
	elif s == "FM徳島":
		return "FM807"
	elif s == "RNC西日本放送":
		return "RNC"
	elif s == "エフエム香川":
		return "FMKAGAWA"
	elif s == "RNB南海放送":
		return "RNB"
	elif s == "FM愛媛":
		return "JOEUFM"
	elif s == "RKC高知放送":
		return "RKC"
	elif s == "エフエム高知":
		return "HISIX"
	elif s == "RKBラジオ":
		return "RKB"
	elif s == "KBCラジオ":
		return "KBC"
	elif s == "LOVE FM":
		return "LOVEFM"
	elif s == "CROSS FM":
		return "CROSSFM"
	elif s == "FM FUKUOKA":
		return "FMFUKUOKA"
	elif s == "エフエム佐賀":
		return "FMS"
	elif s == "NBC長崎放送" or s == "NBCラジオ":
		return "NBC"
	elif s == "FM長崎":
		return "FMNAGASAKI"
	elif s == "RKKラジオ":
		return "RKK"
	elif s == "FMKエフエム熊本":
		return "FMK"
	elif s == "OBSラジオ":
		return "OBS"
	elif s == "エフエム大分":
		return "FMOITA"
	elif s == "宮崎放送":
		return "MRT"
	elif s == "エフエム宮崎":
		return "JOYFM"
	elif s == "ＭＢＣラジオ":
		return "MBC"
	elif s == "μＦＭ":
		return "MYUFM"
	elif s == "RBCiラジオ":
		return "RBC"
	elif s == "ラジオ沖縄":
		return "ROK"
	elif s == "FM沖縄":
		return "FMOKINAWA"
	elif s == "ラジオNIKKEI第1":
		return "RN1"
	elif s == "ラジオNIKKEI第2":
		return "RN2"
	elif s == "放送大学":
		return "HOUSOUDAIGAKU"
	return ""
