jsファイルの作り方
==

次の２つを実行してJSファイルを作成します。  
pythonコマンドはバージョン3系です。  

```
python 11_radio_title.py
python 12_radio_table.py
python 13_radio_encode.py
```

`11_radio_title.py` では先に `radio_titles_raw.js` および `radio_descriptions_raw.js` を作成します。この時、出現頻度の高い物に対しては、できるだけ桁数の小さいIDを与えます。  
`12_radio_table.py` で `timetables.js` を作成します。  
最後に `13_radio_encode.py` で容量を2/3に縮めた `radio_titles.js` および `radio_descriptions.js` を作成します。

JSファイルに取り込み済みのデータについては、次を実行して最低限のHTMLを復元する事もできます。

```
python 10_radio_restore.py
```

HTMLファイルの配置方法
==

HTMLの取得方法は各自に任せます。  
以下に示すURLおよび保存先は2021年1月1日の例なので、目的の日付へと適宜読み替えてください。

* NHK番組表

※ サイトには過去1ヶ月の番組表が残っています。番組内容が変わる可能性があるので、翌日以降になってからのデータ取得が望ましいです。  
※ 地域ごとに細かい違いがあるので、全ての地域をチェックしましょう。  
※ 動的生成された結果のHTMLを得る必要があります。地域や日付を切り替える場合はプルダウンメニューを操作せず、URLから直接アクセスします。それによってHTML内に `area="010" date="20210101"` などの文字列が含まれ、あとで誤り確認に利用できます。

| 地域 | URL | 保存先 |
| --- | --- | --- |
| 札幌 | `https://www.nhk.jp/timetable/010/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK010.html` |
| 函館 | `https://www.nhk.jp/timetable/011/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK011.html` |
| 旭川 | `https://www.nhk.jp/timetable/012/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK012.html` |
| 帯広 | `https://www.nhk.jp/timetable/013/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK013.html` |
| 釧路 | `https://www.nhk.jp/timetable/014/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK014.html` |
| 北見 | `https://www.nhk.jp/timetable/015/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK015.html` |
| 室蘭 | `https://www.nhk.jp/timetable/016/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK016.html` |
| 青森 | `https://www.nhk.jp/timetable/020/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK020.html` |
| 盛岡 | `https://www.nhk.jp/timetable/030/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK030.html` |
| 仙台 | `https://www.nhk.jp/timetable/040/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK040.html` |
| 秋田 | `https://www.nhk.jp/timetable/050/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK050.html` |
| 山形 | `https://www.nhk.jp/timetable/060/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK060.html` |
| 福島 | `https://www.nhk.jp/timetable/070/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK070.html` |
| 水戸 | `https://www.nhk.jp/timetable/080/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK080.html` |
| 宇都宮 | `https://www.nhk.jp/timetable/090/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK090.html` |
| 前橋 | `https://www.nhk.jp/timetable/100/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK100.html` |
| さいたま | `https://www.nhk.jp/timetable/110/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK110.html` |
| 千葉 | `https://www.nhk.jp/timetable/120/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK120.html` |
| 東京 | `https://www.nhk.jp/timetable/130/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK130.html` |
| 横浜 | `https://www.nhk.jp/timetable/140/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK140.html` |
| 新潟 | `https://www.nhk.jp/timetable/150/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK150.html` |
| 富山 | `https://www.nhk.jp/timetable/160/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK160.html` |
| 金沢 | `https://www.nhk.jp/timetable/170/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK170.html` |
| 福井 | `https://www.nhk.jp/timetable/180/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK180.html` |
| 甲府 | `https://www.nhk.jp/timetable/190/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK190.html` |
| 長野 | `https://www.nhk.jp/timetable/200/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK200.html` |
| 岐阜 | `https://www.nhk.jp/timetable/210/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK210.html` |
| 静岡 | `https://www.nhk.jp/timetable/220/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK220.html` |
| 名古屋 | `https://www.nhk.jp/timetable/230/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK230.html` |
| 津 | `https://www.nhk.jp/timetable/240/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK240.html` |
| 大津 | `https://www.nhk.jp/timetable/250/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK250.html` |
| 京都 | `https://www.nhk.jp/timetable/260/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK260.html` |
| 大阪 | `https://www.nhk.jp/timetable/270/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK270.html` |
| 神戸 | `https://www.nhk.jp/timetable/280/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK280.html` |
| 奈良 | `https://www.nhk.jp/timetable/290/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK290.html` |
| 和歌山 | `https://www.nhk.jp/timetable/300/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK300.html` |
| 鳥取 | `https://www.nhk.jp/timetable/310/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK310.html` |
| 松江 | `https://www.nhk.jp/timetable/320/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK320.html` |
| 岡山 | `https://www.nhk.jp/timetable/330/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK330.html` |
| 広島 | `https://www.nhk.jp/timetable/340/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK340.html` |
| 山口 | `https://www.nhk.jp/timetable/350/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK350.html` |
| 徳島 | `https://www.nhk.jp/timetable/360/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK360.html` |
| 高松 | `https://www.nhk.jp/timetable/370/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK370.html` |
| 松山 | `https://www.nhk.jp/timetable/380/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK380.html` |
| 高知 | `https://www.nhk.jp/timetable/390/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK390.html` |
| 福岡 | `https://www.nhk.jp/timetable/400/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK400.html` |
| 北九州 | `https://www.nhk.jp/timetable/401/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK401.html` |
| 佐賀 | `https://www.nhk.jp/timetable/410/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK410.html` |
| 長崎 | `https://www.nhk.jp/timetable/420/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK420.html` |
| 熊本 | `https://www.nhk.jp/timetable/430/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK430.html` |
| 大分 | `https://www.nhk.jp/timetable/440/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK440.html` |
| 宮崎 | `https://www.nhk.jp/timetable/450/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK450.html` |
| 鹿児島 | `https://www.nhk.jp/timetable/460/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK460.html` |
| 沖縄 | `https://www.nhk.jp/timetable/470/radio/20210101/daily/all/` | `./radio2021/01/01/2021_01_01_NHK470.html` |

* 民放ラジオ局の番組表

※ 放送予定が変わる可能性もあるので、当日深夜のデータ取得が望ましいです。  

| ラジオ局 | URL | 保存先 |
| --- | --- | --- |
| HBCラジオ | `https://radiko.jp/index/HBC/` | `./radio2021/01/01/2021_01_01_HBC.html` |
| STVラジオ | `https://radiko.jp/index/STV/` | `./radio2021/01/01/2021_01_01_STV.html` |
| AIR-G (FM北海道) | `https://radiko.jp/index/AIR-G/` | `./radio2021/01/01/2021_01_01_AIR-G.html` |
| FM NORTH WAVE | `https://radiko.jp/index/NORTHWAVE/` | `./radio2021/01/01/2021_01_01_NORTHWAVE.html` |
| RAB青森放送 | `https://radiko.jp/index/RAB/` | `./radio2021/01/01/2021_01_01_RAB.html` |
| エフエム青森 | `https://radiko.jp/index/AFB/` | `./radio2021/01/01/2021_01_01_AFB.html` |
| IBCラジオ | `https://radiko.jp/index/IBC/` | `./radio2021/01/01/2021_01_01_IBC.html` |
| エフエム岩手 | `https://radiko.jp/index/FMI/` | `./radio2021/01/01/2021_01_01_FMI.html` |
| TBCラジオ | `https://radiko.jp/index/TBC/` | `./radio2021/01/01/2021_01_01_TBC.html` |
| Date fm (エフエム仙台) | `https://radiko.jp/index/DATEFM/` | `./radio2021/01/01/2021_01_01_DATEFM.html` |
| ABS秋田放送 | `https://radiko.jp/index/ABS/` | `./radio2021/01/01/2021_01_01_ABS.html` |
| エフエム秋田 | `https://radiko.jp/index/AFM/` | `./radio2021/01/01/2021_01_01_AFM.html` |
| YBC山形放送 | `https://radiko.jp/index/YBC/` | `./radio2021/01/01/2021_01_01_YBC.html` |
| Rhythm Station (エフエム山形) | `https://radiko.jp/index/RFM/` | `./radio2021/01/01/2021_01_01_RFM.html` |
| RFCラジオ福島 | `https://radiko.jp/index/RFC/` | `./radio2021/01/01/2021_01_01_RFC.html` |
| ふくしまFM | `https://radiko.jp/index/FMF/` | `./radio2021/01/01/2021_01_01_FMF.html` |
| TBSラジオ | `https://radiko.jp/index/TBS/` | `./radio2021/01/01/2021_01_01_TBS.html` |
| 文化放送 | `https://radiko.jp/index/QRR/` | `./radio2021/01/01/2021_01_01_QRR.html` |
| ニッポン放送 | `https://radiko.jp/index/LFR/` | `./radio2021/01/01/2021_01_01_LFR.html` |
| InterFM897 | `https://radiko.jp/index/INT/` | `./radio2021/01/01/2021_01_01_INT.html` |
| TOKYO FM | `https://radiko.jp/index/FMT/` | `./radio2021/01/01/2021_01_01_FMT.html` |
| J-WAVE | `https://radiko.jp/index/FMJ/` | `./radio2021/01/01/2021_01_01_FMJ.html` |
| ラジオ日本 | `https://radiko.jp/index/JORF/` | `./radio2021/01/01/2021_01_01_JORF.html` |
| bayfm78 | `https://radiko.jp/index/BAYFM78/` | `./radio2021/01/01/2021_01_01_BAYFM78.html` |
| NACK5 | `https://radiko.jp/index/NACK5/` | `./radio2021/01/01/2021_01_01_NACK5.html` |
| FMヨコハマ | `https://radiko.jp/index/YFM/` | `./radio2021/01/01/2021_01_01_YFM.html` |
| LuckyFM (茨城放送) | `https://radiko.jp/index/IBS/` | `./radio2021/01/01/2021_01_01_IBS.html` |
| CRT栃木放送 | `https://radiko.jp/index/CRT/` | `./radio2021/01/01/2021_01_01_CRT.html` |
| RadioBerry | `https://radiko.jp/index/RADIOBERRY/` | `./radio2021/01/01/2021_01_01_RADIOBERRY.html` |
| FM GUNMA | `https://radiko.jp/index/FMGUNMA/` | `./radio2021/01/01/2021_01_01_FMGUNMA.html` |
| BSNラジオ | `https://radiko.jp/index/BSN/` | `./radio2021/01/01/2021_01_01_BSN.html` |
| FM NIIGATA | `https://radiko.jp/index/FMNIIGATA/` | `./radio2021/01/01/2021_01_01_FMNIIGATA.html` |
| KNBラジオ | `https://radiko.jp/index/KNB/` | `./radio2021/01/01/2021_01_01_KNB.html` |
| FMとやま | `https://radiko.jp/index/FMTOYAMA/` | `./radio2021/01/01/2021_01_01_FMTOYAMA.html` |
| MROラジオ | `https://radiko.jp/index/MRO/` | `./radio2021/01/01/2021_01_01_MRO.html` |
| HELLO FIVE (エフエム石川) | `https://radiko.jp/index/HELLOFIVE/` | `./radio2021/01/01/2021_01_01_HELLOFIVE.html` |
| FBCラジオ | `https://radiko.jp/index/FBC/` | `./radio2021/01/01/2021_01_01_FBC.html` |
| FM福井 | `https://radiko.jp/index/FMFUKUI/` | `./radio2021/01/01/2021_01_01_FMFUKUI.html` |
| YBSラジオ | `https://radiko.jp/index/YBS/` | `./radio2021/01/01/2021_01_01_YBS.html` |
| FM FUJI | `https://radiko.jp/index/FM-FUJI/` | `./radio2021/01/01/2021_01_01_FM-FUJI.html` |
| SBCラジオ | `https://radiko.jp/index/SBC/` | `./radio2021/01/01/2021_01_01_SBC.html` |
| FM長野 | `https://radiko.jp/index/FMN/` | `./radio2021/01/01/2021_01_01_FMN.html` |
| CBCラジオ | `https://radiko.jp/index/CBC/` | `./radio2021/01/01/2021_01_01_CBC.html` |
| 東海ラジオ | `https://radiko.jp/index/TOKAIRADIO/` | `./radio2021/01/01/2021_01_01_TOKAIRADIO.html` |
| ぎふチャン | `https://radiko.jp/index/GBS/` | `./radio2021/01/01/2021_01_01_GBS.html` |
| ZIP-FM | `https://radiko.jp/index/ZIP-FM/` | `./radio2021/01/01/2021_01_01_ZIP-FM.html` |
| FM AICHI | `https://radiko.jp/index/FMAICHI/` | `./radio2021/01/01/2021_01_01_FMAICHI.html` |
| FM GIFU | `https://radiko.jp/index/FMGIFU/` | `./radio2021/01/01/2021_01_01_FMGIFU.html` |
| SBSラジオ | `https://radiko.jp/index/SBS/` | `./radio2021/01/01/2021_01_01_SBS.html` |
| K-MIX SHIZUOKA | `https://radiko.jp/index/K-MIX/` | `./radio2021/01/01/2021_01_01_K-MIX.html` |
| レディオキューブ (FM三重) | `https://radiko.jp/index/FMMIE/` | `./radio2021/01/01/2021_01_01_FMMIE.html` |
| ABCラジオ | `https://radiko.jp/index/ABC/` | `./radio2021/01/01/2021_01_01_ABC.html` |
| MBSラジオ | `https://radiko.jp/index/MBS/` | `./radio2021/01/01/2021_01_01_MBS.html` |
| OBCラジオ大阪 | `https://radiko.jp/index/OBC/` | `./radio2021/01/01/2021_01_01_OBC.html` |
| FM COCOLO | `https://radiko.jp/index/CCL/` | `./radio2021/01/01/2021_01_01_CCL.html` |
| FM802 | `https://radiko.jp/index/802/` | `./radio2021/01/01/2021_01_01_802.html` |
| FM大阪 | `https://radiko.jp/index/FMO/` | `./radio2021/01/01/2021_01_01_FMO.html` |
| Kiss FM KOBE | `https://radiko.jp/index/KISSFMKOBE/` | `./radio2021/01/01/2021_01_01_KISSFMKOBE.html` |
| ラジオ関西 | `https://radiko.jp/index/CRK/` | `./radio2021/01/01/2021_01_01_CRK.html` |
| e-radio (FM滋賀) | `https://radiko.jp/index/E-RADIO/` | `./radio2021/01/01/2021_01_01_E-RADIO.html` |
| KBS京都ラジオ | `https://radiko.jp/index/KBS/` | `./radio2021/01/01/2021_01_01_KBS.html` |
| α-STATION (FM京都) | `https://radiko.jp/index/ALPHA-STATION/` | `./radio2021/01/01/2021_01_01_ALPHA-STATION.html` |
| wbs和歌山放送 | `https://radiko.jp/index/WBS/` | `./radio2021/01/01/2021_01_01_WBS.html` |
| BSSラジオ | `https://radiko.jp/index/BSS/` | `./radio2021/01/01/2021_01_01_BSS.html` |
| エフエム山陰 | `https://radiko.jp/index/FM-SANIN/` | `./radio2021/01/01/2021_01_01_FM-SANIN.html` |
| RSKラジオ | `https://radiko.jp/index/RSK/` | `./radio2021/01/01/2021_01_01_RSK.html` |
| FM岡山 | `https://radiko.jp/index/FM-OKAYAMA/` | `./radio2021/01/01/2021_01_01_FM-OKAYAMA.html` |
| RCCラジオ | `https://radiko.jp/index/RCC/` | `./radio2021/01/01/2021_01_01_RCC.html` |
| 広島FM | `https://radiko.jp/index/HFM/` | `./radio2021/01/01/2021_01_01_HFM.html` |
| KRY山口放送 | `https://radiko.jp/index/KRY/` | `./radio2021/01/01/2021_01_01_KRY.html` |
| エフエム山口 | `https://radiko.jp/index/FMY/` | `./radio2021/01/01/2021_01_01_FMY.html` |
| JRT四国放送 | `https://radiko.jp/index/JRT/` | `./radio2021/01/01/2021_01_01_JRT.html` |
| FM徳島 | `https://radiko.jp/index/FM807/` | `./radio2021/01/01/2021_01_01_FM807.html` |
| RNC西日本放送 | `https://radiko.jp/index/RNC/` | `./radio2021/01/01/2021_01_01_RNC.html` |
| エフエム香川 | `https://radiko.jp/index/FMKAGAWA/` | `./radio2021/01/01/2021_01_01_FMKAGAWA.html` |
| RNB南海放送 | `https://radiko.jp/index/RNB/` | `./radio2021/01/01/2021_01_01_RNB.html` |
| FM愛媛 | `https://radiko.jp/index/JOEU-FM/` | `./radio2021/01/01/2021_01_01_JOEU-FM.html` |
| RKC高知放送 | `https://radiko.jp/index/RKC/` | `./radio2021/01/01/2021_01_01_RKC.html` |
| Hi-Six (エフエム高知) | `https://radiko.jp/index/HI-SIX/` | `./radio2021/01/01/2021_01_01_HI-SIX.html` |
| RKBラジオ | `https://radiko.jp/index/RKB/` | `./radio2021/01/01/2021_01_01_RKB.html` |
| KBCラジオ | `https://radiko.jp/index/KBC/` | `./radio2021/01/01/2021_01_01_KBC.html` |
| LOVE FM | `https://radiko.jp/index/LOVEFM/` | `./radio2021/01/01/2021_01_01_LOVEFM.html` |
| CROSS FM | `https://radiko.jp/index/CROSSFM/` | `./radio2021/01/01/2021_01_01_CROSSFM.html` |
| FM FUKUOKA | `https://radiko.jp/index/FMFUKUOKA/` | `./radio2021/01/01/2021_01_01_FMFUKUOKA.html` |
| エフエム佐賀 | `https://radiko.jp/index/FMS/` | `./radio2021/01/01/2021_01_01_FMS.html` |
| NBC長崎放送 | `https://radiko.jp/index/NBC/` | `./radio2021/01/01/2021_01_01_NBC.html` |
| FM長崎 | `https://radiko.jp/index/FMNAGASAKI/` | `./radio2021/01/01/2021_01_01_FMNAGASAKI.html` |
| RKKラジオ | `https://radiko.jp/index/RKK/` | `./radio2021/01/01/2021_01_01_RKK.html` |
| FMKエフエム熊本 | `https://radiko.jp/index/FMK/` | `./radio2021/01/01/2021_01_01_FMK.html` |
| OBSラジオ | `https://radiko.jp/index/OBS/` | `./radio2021/01/01/2021_01_01_OBS.html` |
| エフエム大分 | `https://radiko.jp/index/FM_OITA/` | `./radio2021/01/01/2021_01_01_FM_OITA.html` |
| 宮崎放送 | `https://radiko.jp/index/MRT/` | `./radio2021/01/01/2021_01_01_MRT.html` |
| エフエム宮崎 | `https://radiko.jp/index/JOYFM/` | `./radio2021/01/01/2021_01_01_JOYFM.html` |
| MBCラジオ | `https://radiko.jp/index/MBC/` | `./radio2021/01/01/2021_01_01_MBC.html` |
| μFM | `https://radiko.jp/index/MYUFM/` | `./radio2021/01/01/2021_01_01_MYUFM.html` |
| RBCiラジオ | `https://radiko.jp/index/RBC/` | `./radio2021/01/01/2021_01_01_RBC.html` |
| ラジオ沖縄 | `https://radiko.jp/index/ROK/` | `./radio2021/01/01/2021_01_01_ROK.html` |
| FM沖縄 | `https://radiko.jp/index/FM_OKINAWA/` | `./radio2021/01/01/2021_01_01_FM_OKINAWA.html` |
| ラジオNIKKEI第1 | `https://radiko.jp/index/RN1/` | `./radio2021/01/01/2021_01_01_RN1.html` |
| ラジオNIKKEI第2 | `https://radiko.jp/index/RN2/` | `./radio2021/01/01/2021_01_01_RN2.html` |
| 放送大学 | `https://radiko.jp/index/HOUSOU-DAIGAKU/` | `./radio2021/01/01/2021_01_01_HOUSOU-DAIGAKU.html` |
