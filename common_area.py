import random
import threading
from time import sleep
import cv2
import numpy as np
import requests
from PIL import Image
from io import BytesIO


israel_support_comments = [
    "Israel has the right to defend itself.",
    "Stand with Israel!",
    "Israel is a beacon of democracy in the Middle East.",
    "Israel's innovation is inspiring.",
    "Support Israel and its quest for peace.",
    "Israel is a land of hope and resilience.",
    "I stand with the people of Israel.",
    "Israel is a vital ally.",
    "The strength of Israel is admirable.",
    "Israel's culture is rich and vibrant.",
    "Israel is a symbol of survival.",
    "Together for Israel!",
    "Israel's achievements in technology are remarkable.",
    "Support Israel's right to exist.",
    "Israel represents freedom and democracy.",
    "The history of Israel is a testament to perseverance.",
    "Israel's contributions to science benefit us all.",
    "Proud to support Israel!",
    "Israel is a land of diverse cultures.",
    "The spirit of Israel is unbreakable.",
    "Israel's military is one of the best in the world.",
    "We must defend Israel's right to self-determination.",
    "Israel's landscapes are breathtaking.",
    "Israel is a sanctuary for many.",
    "The resilience of Israel is inspiring.",
    "Israel's commitment to peace is commendable.",
    "Stand with our friends in Israel!",
    "Israel is a land of opportunity.",
    "The people of Israel deserve peace.",
    "Support Israel's democratic values.",
    "Israel's diversity is its strength.",
    "We will never forget Israel's sacrifices.",
    "Israel is an example of coexistence.",
    "Proud of Israel's cultural contributions.",
    "Israel stands strong against adversity.",
    "Support Israel's innovation and creativity.",
    "Israel is a light unto the nations.",
    "The bond with Israel is unbreakable.",
    "Israel's history is a story of resilience.",
    "The future of Israel is bright.",
    "Support Israel's right to security.",
    "Israel is a hub of knowledge and learning.",
    "Together we can ensure Israel's safety.",
    "Israel's farmers feed the world.",
    "The spirit of Israel lives on.",
    "Support for Israel is support for peace.",
    "Israel's artistic community is vibrant.",
    "Israel's unity is its strength.",
    "We stand with Israel in times of need.",
    "The Israeli people are strong and resilient.",
    "Israel is a land of progress.",
    "The achievements of Israel are commendable.",
    "We cannot ignore Israel's challenges.",
    "Support Israel's quest for lasting peace.",
    "The history of Israel is a testament to hope.",
    "Israel is a model for democracy.",
    "Together, we stand with Israel.",
    "Israel is a haven for many seeking refuge.",
    "Support Israel's right to thrive.",
    "Israel's advancements in medicine save lives.",
    "Proud of Israel's technological leadership.",
    "Israel's spirit of innovation is unmatched.",
    "Stand strong with Israel.",
    "The diversity of Israel enriches us all.",
    "Israel's achievements inspire generations.",
    "We cannot forget Israel's sacrifices for peace.",
    "Support for Israel is support for democracy.",
    "Israel's military innovation is impressive.",
    "Israel is a champion of human rights.",
    "The future of Israel is in our hands.",
    "Israel's agricultural innovations are groundbreaking.",
    "We support Israel's quest for stability.",
    "The culture of Israel is a treasure.",
    "Israel is a land of dreams and possibilities.",
    "The spirit of the Israeli people is incredible.",
    "Support Israel's commitment to peace and security.",
    "Israel is a land of opportunity for all.",
    "Together, we stand with the people of Israel.",
    "Israel's technological advancements benefit humanity.",
    "Proud of Israel's rich history.",
    "Israel's youth are its future.",
    "Support for Israel is support for progress.",
    "Israel is a land where hope thrives.",
    "The achievements of Israel's scientists are remarkable.",
    "Israel is a symbol of strength and courage.",
    "We celebrate Israel's vibrant culture.",
    "Support Israel's democratic processes.",
    "The resilience of Israel is an inspiration.",
    "Together, we can support Israel's growth.",
    "Israel's commitment to peace is unwavering.",
    "Stand with Israel for a better tomorrow.",
    "Israel is a nation of pioneers.",
    "The beauty of Israel is unmatched.",
    "We must advocate for Israel's rights.",
    "Support for Israel is a call for unity.",
    "Israel's heritage is a source of pride.",
    "Together, we celebrate Israel's successes.",
    "The strength of Israel is its people.",
    "Support Israel's efforts for peace and understanding.",
    "Israel is a land of innovation and creativity.",
    "We stand with Israel in solidarity.",
    "The future is bright for Israel.",
    "I stand with Israel!",
    "Solidarity with Israel 🇮🇱",
    "Peace for Israel always.",
    "Israel has my support!",
    "Forever pro-Israel 🇮🇱",
    "Standing strong with Israel.",
    "Israel’s right to defend!",
    "Supporting Israel’s future.",
    "Am Yisrael Chai!",
    "Peace for Israel 🙏",
    "Supporting Israel’s security.",
    "Defending Israel’s sovereignty!",
    "Israel deserves peace.",
    "Proudly pro-Israel!",
    "Strength for Israel.",
    "Backing Israel always!",
    "Unity with Israel 🇮🇱",
    "Israel forever 💙",
    "Israel deserves justice!",
    "Always with Israel."
]


anti_iran_comments =  [
    "Free Iran from repression.", 
    "Iran is supporting terror.",
    "Qatar is supporting terror.",
    "Iran will be free when the Iranian people stand up and have a revolution to end their current slavery.",
    "Freedom and peace are universal rights. Iran might have forgot about them.",
    "Iran and Qatar are supporting terror.",
    "Iran stole Lebanon to make it a terror base for a war on Israel.",
    "Free Iran From Radical Islamists.",
    "Only a matter of time before Iranians are free from this evil Islamic Regime in Iran.",
    "Remember when Arabia was the center of knowledge, and then Islam happened destroying it all?",
    "It would be amazing to visit Iran someday once it is free.",
    "Help free Iran from Islamic slavery.",
    "Qatar are collaborating with Iranian oppressive regime.",
    "All the pressure should be applied in Iran, Qatar and Hamas to end the war.",
    "It’s time to help the people of Iran free themselves from Ali Khamenei’s dictatorship.",
    "A free Iran will free the Middle East from terror.",
    "A FreeIran means no money for terrorists, no funding of militias in Lebanon, Yemen, Syria, Iraq, which means no refugee crisis, no nuclear threat. Most important it means 85 million people will be freed from terrorists taking them hostage for 43 yrs.",
]


twitter_handles = [
    "YishaiFleisher",
    "DavidMFriedman",
    "Ostrov_A",
    "LahavHarkov",
    "havivrettiggur",
    "Gil_Hoffman",
    "AIPAC",
    "sfrantzman",
    "EylonALevy",
    "FleurHassanN",
    "khaledAbuToameh",
    "rich_goldberg",
    "EVKontorovich",
    "imshin",
    "BarakRavid",
    "MaxAbrahms",
    "mickyrosenfeld",
    "RaphaelAhren",
    "YaakovLappin",
    "ynetnews",
    "HananyaNaftali",
    "AmbDermer",
    "BoothWilliam",
    "AnshelPfeffer",
    "ElhananMiller",
    "GershonBaskin",
    "HonestReporting",
    "issacharoff",
    "CarolineGlick",
    "dansenor",
    "JeffreyGoldberg",
    "KhaledAbuToameh",
    "LahavHarkov",
    "DannyNis",
    "TuckerAndrew_",
    "EC4Israel"
]

tiktok_accounts = [
    "israel",
    "powerisrael",
    "israel_hayom",
    "tbn_official",
    "tbn_fr",
    "tbnua",
    "cbnnewsofficial",
    "cbcnews",
    "newsmaxtv",
    "hananyanaftali",
    "Shaidavidai",
    "noybeyleyb",
    "EylonALevy",
    "yoavdavis",
    "millennialmoor",
    "Jews_of_Ny",
    "noatishby",
    "jewishhistory",
    "houseoflev",
    "melissaschapman",
    "Jewisnews",
    "EndJewHatred",
    "jew_ishcontent",
    "alizalicht",
    "ec4israel"
    ]

instagram_accounts = [
    "rudy_israel",
    "Shaidavidai",
    "adelacojab",
    "EylonALevy",
    "yoavdavis",
    "millennialmoor",
    "Jews_of_Ny",
    "noatishby",
    "jewishhistory",
    "melissaschapman",
    "EndJewHatred",
    "wearetov",
    "idf",
    "fleurhassann",
    "standwithus",
    "israel", 
    "israeltodaymag", 
    "jewishagency", 
    "honestreporting", 
    "beyondtheheadline", 
    "simonwiesenthalcenter", 
    "maccabiusa", 
    "aipac", 
    "Birthrightisraelbeyond", 
    "ariseforisrael",
    "houseoflev",
]

twitter_handles_specials = [
    "YosephHaddad",
    "ariseforisrael"
]


tiktok_handles_specials = [
    "ariseforisrael",
    "yosephhaddad"
]


instagram_handles_special = [
    "theisraelstory",
    "womenofmiddleeast",
    "unapologetic_israeli",
    "wildbranchmedia",
    "ariseforisrael",
]


anti_israel_twitter = [
    "PressTV",
    "Tasnimnews_E",
    "EnglishFars",
    "MehrnewsCom",
    "AlalamChannel",
    "khamenei_ir",
    "HassanRouhani",
    "JZarif",
    "IranFrontPage",
    "IranDaily",
    "AJEnglish",
    "AJArabic",
    "QNAEnglish",
    "dohanews",
    "GulfTimes_QATAR",
    "PeninsulaQatar",
    "Qatar_Tribune",
    "QF",
    "qatarairways",
    "qatar_olympic",
    "khamenei_ir",
    "raisi_com",
    "TamimBinHamad",
    "MBA_AlThani",
]

anti_israel_tiktok = [
    "AlalamChannel",
    "aljazeeraenglish",
    "qatarliving",
    "qatarlivingmagazine",
    "qatarsports",
    "peninsulanewsdaily",
    "qatarday",
    "qatarlifestyle",
    "visitqatar",
    "irigcnews",
    "iranianvoice",
    "tehrantimesdaily",
    "realirannews",
    "ajplus",
    "iranintltv1",
]



keyboard_dic = {
    "q": (40, 1200),
    "w": (110, 1200),
    "e": (180, 1200),
    "r": (250, 1200),
    "t": (320, 1200),
    "y": (390, 1200),
    "u": (460, 1200),
    "i": (530, 1200),
    "o": (600, 1200),
    "p": (670, 1200),
    "a": (70, 1285),
    "s": (140, 1285),
    "d": (210, 1285),
    "f": (280, 1285),
    "g": (350, 1285),
    "h": (420, 1285),
    "j": (490, 1285),
    "k": (560, 1285),
    "l": (630, 1285),
    "z": (150, 1400),
    "x": (220, 1400),
    "c": (290, 1400),
    "v": (360, 1400),
    "b": (430, 1400),
    "n": (500, 1400),
    "m": (570, 1400),
    ".": (570,1500),
    ",": (150,1500),
    " ": (400,1500)
}

report_tiktok_clicks = {
    'Exploitation and abuse of people under 18': 'd.click(350,390):d.click(350,390):d.click(350,1500):d.click(350,1380)',
    'Physical violence and violent threats': 'd.click(350,390):d.click(350,460):d.click(350,1500):d.click(350,1380)',
    'Sexual exploitation and abuse': 'd.click(350,390):d.click(350,616):d.click(350,1500):d.click(350,1380)',
    'Human exploitation': 'd.click(350,390):d.click(350,710):d.click(350,1500):d.click(350,1380)', 
    'Other criminal activities': 'd.click(350,390):d.click(350,922):d.click(350,1500):d.click(350,1380)',
    'Dangerous activities and challenges': 'd.click(350,849):d.click(350,1500):d.click(350,1380)',
    'Shocking and graphic content': 'd.click(350,1058):d.click(350,1500):d.click(350,1380)',
    'Hate speech and hateful behaviors':'d.click(350,460):d.click(350,390):d.click(350,1500):d.click(350,1380)',
    'Harassment and bullying':'d.click(350,460):d.click(350,460):d.click(350,390):d.click(350,1500):d.click(350,1380)',
    'Harmful misinformation':'d.click(350,1149):d.click(350,460):d.click(350,1500):d.click(350,1380)',
    'Deepfakes, synthetic media, and manipulated media':'d.click(350,1149):d.click(350,590):d.click(350,1500):d.click(350,1380)',
    'Child sexual exploitation':'d.swipe(500, 1200, 500, 300, duration=0.05):d.click(350,1213):d.swipe(500, 300, 500, 1200, duration=0.05):d.click(350,390):d.click(350,1500):d.click(350,1380)', 
    'Illegal hate speech':'d.swipe(500, 1200, 500, 300:duration=0.05):d.click(350,1213):d.swipe(500, 300, 500, 1200, duration=0.05):d.click(350,560):d.click(350,1500):d.click(350,1380)', 
    'Content relating to violent or organized crime':'d.swipe(500, 1200, 500, 300, duration=0.05):d.click(350,1213):d.click(350,420):d.click(350,1500):d.click(350,1380)', 
    'Harrassment or threats':'d.swipe(500, 1200, 500, 300, duration=0.05):d.click(350,1213):d.click(350,870):d.click(350,1500):d.click(350,1380)', 
    'Defamation':'d.swipe(500, 1200, 500, 300, duration=0.05):d.click(350,1213):d.click(350,970):d.click(350,1500):d.click(350,1380)',
    'Other': 'd.swipe(500, 1200, 500, 300, duration=0.05):d.click(350,1500):d.click(350,1500):d.click(350,1380)'
}


report_tiktok_keys = [
    'Exploitation and abuse of people under 18',               # 1
    'Physical violence and violent threats',                   # 2
    'Sexual exploitation and abuse',                           # 3
    'Human exploitation',                                      # 4
    'Other criminal activities',                               # 5
    'Dangerous activities and challenges',                     # 6
    'Shocking and graphic content',                            # 7
    'Hate speech and hateful behaviors',                       # 8
    'Harassment and bullying',                                 # 9
    'Harmful misinformation',                                  # 10
    'Deepfakes, synthetic media, and manipulated media',       # 11
    'Child sexual exploitation',                               # 12
    'Illegal hate speech',                                     # 13
    'Content relating to violent or organized crime',          # 14
    'Harassment or threats',                                   # 15
    'Defamation',                                              # 16
    'Other'                                                    # 17
]

# TODO here:
# report_tiktok_account = {
#     'Physical violence and violent threats': 'd.click(350,390):d.click(350,460):d.click(350,1500):d.click(350,1380)',
#     'Sexual exploitation and abuse': 'd.click(350,390):d.click(350,616):d.click(350,1500):d.click(350,1380)',
#     'Human exploitation': 'd.click(350,390):d.click(350,710):d.click(350,1500):d.click(350,1380)', 
#     'Other criminal activities': 'd.click(350,390):d.click(350,922):d.click(350,1500):d.click(350,1380)',
#     'Dangerous activities and challenges': 'd.click(350,849):d.click(350,1500):d.click(350,1380)',
#     'Shocking and graphic content': 'd.click(350,1058):d.click(350,1500):d.click(350,1380)',
#     'Hate speech and hateful behaviors':'d.click(350,460):d.click(350,390):d.click(350,1500):d.click(350,1380)',
#     'Harassment and bullying':'d.click(350,460):d.click(350,460):d.click(350,390):d.click(350,1500):d.click(350,1380)',
#     'Harmful misinformation':'d.click(350,1149):d.click(350,460):d.click(350,1500):d.click(350,1380)',
#     'Deepfakes, synthetic media, and manipulated media':'d.click(350,1149):d.click(350,590):d.click(350,1500):d.click(350,1380)',
#     'Child sexual exploitation':'d.swipe(500, 1200, 500, 300, duration=0.05):d.click(350,1213):d.swipe(500, 300, 500, 1200, duration=0.05):d.click(350,390):d.click(350,1500):d.click(350,1380)', 
#     'Illegal hate speech':'d.swipe(500, 1200, 500, 300:duration=0.05):d.click(350,1213):d.swipe(500, 300, 500, 1200, duration=0.05):d.click(350,560):d.click(350,1500):d.click(350,1380)', 
#     'Content relating to violent or organized crime':'d.swipe(500, 1200, 500, 300, duration=0.05):d.click(350,1213):d.click(350,420):d.click(350,1500):d.click(350,1380)', 
#     'Harrassment or threats':'d.swipe(500, 1200, 500, 300, duration=0.05):d.click(350,1213):d.click(350,870):d.click(350,1500):d.click(350,1380)', 
#     'Defamation':'d.swipe(500, 1200, 500, 300, duration=0.05):d.click(350,1213):d.click(350,970):d.click(350,1500):d.click(350,1380)',
#     'Other': 'd.swipe(500, 1200, 500, 300, duration=0.05):d.click(350,1500):d.click(350,1500):d.click(350,1380)'
# }

report_twitter_clicks = {
    "Slurs & Tropes":"d.click(370,670):d.click(370,1450):d.click(370,670):d.click(370,1450):d.click(370,1450)",
    "Hateful References":"d.click(370,670):d.click(370,1450):d.click(370,950):d.click(370,1450):d.click(370,1450)",
    "Dehumanization":"d.click(370,670):d.click(370,1450):d.click(370,1250):d.click(370,1450):d.click(370,1450)",
    "Hateful Imagery":"d.click(370,670):d.click(370,1450):d.swipe(500, 1200, 500, 300, duration=0.05):d.click(370,860):d.click(370,1450):d.click(370,1450)",
    "Incitement":"d.click(370,670)::d.click(370,1450)d.swipe(500, 1200, 500, 300, duration=0.05):d.click(370,1214):d.click(370,1450):d.click(370,1450)",
    "Unwanted NSFW & Graphic Content":"d.click(370,965):d.click(370,1450):d.click(370,560):d.click(370,1450):d.click(370,1450)",
    "Targeted Harassment":"d.click(370,965):d.click(370,1450):d.click(370,770):d.click(370,1450):d.click(370,1450)",
    "Insults":"d.click(370,965):d.click(370,1450):d.click(370,986):d.click(370,1450):d.click(370,1450)",
    "Violent Event Denial":"d.click(370,965):d.swipe(500, 1200, 500, 300, duration=0.05):d.click(370,1450):d.click(370,895):d.click(370,1450):d.click(370,1450)",
    "Inciting Harassment":"d.click(370,965):d.swipe(500, 1200, 500, 300, duration=0.05):d.click(370,1450):d.click(370,1200):d.click(370,1450):d.click(370,1450)",
    "Violent Threats":"d.click(370,1180):d.click(370,1450):d.click(370,560):d.click(370,1450):d.click(370,1450)",
    "Glorification of Violence":"d.click(370,1180):d.click(370,1450):d.click(370,980):d.click(370,1450):d.click(370,1450)",
    "Incitement of Violence":"d.click(370,1180):d.click(370,1450):d.click(370,1280):d.click(370,1450):d.click(370,1450)",
    "Wish of Harm":"d.click(370,1180):d.swipe(500, 1200, 500, 300, duration=0.05):d.click(370,1450):d.click(370,925):d.click(370,1450):d.click(370,1450)",
    "Coded Incitement of Violence":"d.click(370,1180):d.swipe(500, 1200, 500, 300, duration=0.05):d.click(370,1450):d.click(370,1200):d.click(370,1450):d.click(370,1450)",
    "Spam":"d.swipe(500, 1200, 500, 300, duration=0.05):d.click(370,1450):d.click(370,363):d.click(370,1450):d.click(370,1450)",
    "Violent & hateful entities":"d.swipe(500, 1200, 500, 300, duration=0.05):d.click(370,1450):d.click(370,1240):d.click(370,1450):d.click(370,1450)"
}


twitter_report_keys = [
    "Slurs & Tropes",                            # 1
    "Hateful References",                        # 2
    "Dehumanization",                            # 3
    "Hateful Imagery",                           # 4
    "Incitement",                                # 5
    "Unwanted NSFW & Graphic Content",           # 6
    "Targeted Harassment",                       # 7
    "Insults",                                   # 8
    "Violent Event Denial",                      # 9
    "Inciting Harassment",                       # 10
    "Violent Threats",                           # 11
    "Glorification of Violence",                 # 12
    "Incitement of Violence",                    # 13
    "Wish of Harm",                              # 14
    "Coded Incitement of Violence",              # 15
    "Spam",                                      # 16
    "Violent & hateful entities"                 # 17
]

twitter_posts_to_report = [
    ("https://x.com/marwanbishara/status/1805202165054493148?t=zbQJshyDikFcHUFcMKC1yg&s=19",4)
    ("https://x.com/Lucas_Gage_/status/1720998157369192710",5)
    ("https://x.com/Mr_RimoniTMD/status/1854267057275306105",5)
    ("https://x.com/nuzlyazhar/status/1854454771358519722",5)
    ("https://x.com/fedoration/status/1852116998064607390",5)
    ("https://x.com/nick_rose96/status/1850365270302634042",5)
    ("https://x.com/OmarShargawi/status/1851868583057297697",5)
    ("https://x.com/HackneySwp/status/1852772248324633040",15)
    ("https://x.com/Yusufafsar/status/1852385840921456846",15)
    ("https://x.com/Yusufafsar/status/1852385492639035798",15)
    ("https://x.com/Du_con_Lajoie/status/1851356793328296326",15)
    ("https://x.com/komugi_twit/status/1852406478277357956",15)
    ("https://x.com/BeautyMrked/status/1853873503188984175",15)
    ("",5)
]

tiktok_report = [
    "https://vm.tiktok.com/ZGdNeymS6/",
    "https://vm.tiktok.com/ZGdNeFh4w/",
    "https://vm.tiktok.com/ZGdNe6WP9/",
    "https://vm.tiktok.com/ZGdNeBx2t/",
    "https://vm.tiktok.com/ZGdNefREq/",
    "https://vm.tiktok.com/ZGdNeMagN/",
    "https://www.tiktok.com/@nyxnyc/video/7351857780162284846?q=From%20the%20river%20to%20the%20sea&t=1730973145737",
    "https://www.tiktok.com/@kindakhatib22/video/7287249443303329031?q=palestine&t=1730973507062",
    "https://www.tiktok.com/@pascoliiii/video/7396072279362276641?q=From%20the%20river%20to%20&t=1730973687107",
    "https://www.tiktok.com/@amna.naji/video/7088113841766206726?q=freepalestine&t=1730973776643",
    "https://www.tiktok.com/@leyaaalyaa/video/7296362568703020290?q=freepalestine&t=1730973776643",
]

instagram_posts_to_report = [

]

tiktok_posts_to_report = [
    
]
report_instagram_post_clicks = {
    "bullying or harassment":"d.click(370,750):d.click(370,660):d.click(370,614):d.click(370,1481)",
    "Credible threat to safty":"d.click(370,930):d.click(370,571):d.click(370,1481)",
    "Seems like terrorism or organized crime":"d.click(370,930):d.click(370,658):d.click(370,1481)",
    "Calling for violence":"d.click(370,930):d.click(370,838):d.click(370,1481)",
    "Hate speech or symbols":"d.click(370,930):d.click(370,931):d.click(370,1481)",
    "Showing violence, death or severe injury":"d.click(370,930):d.click(370,1021):d.click(370,1481)",
    "False information-Health":"d.click(370,1286):d.click(370,520):d.click(370,1440)",
    "False information-Politics":"d.click(370,1286):d.click(370,613):d.click(370,1440)",
    "False information-Social issues":"d.click(370,1286):d.click(370,700):d.click(370,1440)",
    "False information-Digitally created or altered":"d.click(370,1286):d.click(370,800):d.click(370,1440)",
}
report_instagram_keys = [
    "bullying or harassment",                             # 1
    "Credible threat to safety",                          # 2
    "Seems like terrorism or organized crime",            # 3
    "Calling for violence",                               # 4
    "Hate speech or symbols",                             # 5
    "Showing violence, death or severe injury",           # 6
    "False information-Health",                           # 7
    "False information-Politics",                         # 8
    "False information-Social issues",                    # 9
    "False information-Digitally created or altered"     # 10
]

report_instagram_account_clicks = {
    "bullying or harassment":"d.click(370,1334):d.click(370,790):d.click(370,1381)",
    "Terrorism":"d.click(370,1242):d.click(370,915):d.click(370,1481)",
    "Violent threat":"d.click(370,1242):d.click(370,450):d.click(370,1481)",
    "Dangerous organizations or individuals":"d.click(370,1242):d.click(370,723):d.click(370,1481)",
    "Credible threat to safty":"d.click(370,1242):d.click(370,1000):d.click(370,1481)",
    "Calling for violence":"d.click(370,930):d.click(370,838):d.click(370,1481)",
    "Hate speech or symbols":"d.click(370,1150):d.click(370,1381)",
    "False information":"d.swipe(500, 1200, 500, 300, duration=0.05):d.click(370,1533):d.click(370,1440)",
}

def tap_keyboard(d, text, keyboard = keyboard_dic):
    """
    Simulates tapping on the screen using the keyboard coordinates for each character in the text.
    """
    for char in text.lower():
        if char == "_":
            char = " "  
        if char in keyboard:
            x, y = keyboard[char]
            d.click(x, y)  # Simulate a tap on the screen at the corresponding coordinates
            sleep(random.uniform(0.04, 0.07))  # Add a small delay between taps
        else:
            print(f"{threading.current_thread().name}:{d.wlan_ip} Character '{char}' not found in keyboard dictionary!")


def take_screenshot(d, thread = threading.current_thread().name, app = "inst"):
    sleep(2)
    filename = f"Screenshots/{thread}-screenshot_{app}.png"
    print(f"{thread}:{d.wlan_ip} Taking screenshot...")
    d.screenshot(filename)
    print(f"Screenshot saved as {filename}.")
    return filename

def find_best_match(image_path, users_template_path, d):
    """
    Finds the best match of a user's button icon in the screenshot using template matching.
    """
    sleep(0.5)
    print(f"{threading.current_thread().name}:{d.wlan_ip} Starting find_best_match function")
    
    img = cv2.imread(image_path)
    template = cv2.imread(users_template_path)

    if img is None or template is None:
        print(f"{threading.current_thread().name}:{d.wlan_ip} Error loading images.")
        return None

    h, w = template.shape[:2]
    result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.85
    loc = np.where(result >= threshold)

    matches = []
    for pt in zip(*loc[::-1]):
        matches.append((pt, result[pt[1], pt[0]]))

    if matches:
        # Get the best match (highest confidence value)
        best_match = max(matches, key=lambda x: x[1])
        best_coordinates = (best_match[0][0] + w // 2, best_match[0][1] + h // 2)
        best_value = best_match[1]
        print(f"{threading.current_thread().name}:{d.wlan_ip} Best match found with value: {best_value} at {best_coordinates}")
    else:
        # If no matches found above threshold, find the closest match
        _, max_val, _, max_loc = cv2.minMaxLoc(result)
        best_coordinates = (max_loc[0] + w // 2, max_loc[1] + h // 2)
        best_value = max_val
        print(f"{threading.current_thread().name}:{d.wlan_ip} No matches above threshold, closest match found with value: {best_value} at {best_coordinates}")
        return None
    
    print(f"{threading.current_thread().name}:{d.wlan_ip} Finished find_best_match function")
    
    return best_coordinates

def handle_user_selection(d,report_dict):
    print("Select a report reason:")
    numbered_report_dict = show_tree(report_dict)

    # User input for selection
    user_choice = input("Enter the number of the report reason you want to select: ")

    if user_choice.isdigit() and int(user_choice) in numbered_report_dict:
        action = numbered_report_dict[int(user_choice)]
        if isinstance(action, dict):  # If the selection has subcategories
            handle_user_selection(action)  # Show subcategories
        else:
            execute_action(d,action,report_dict)  # Execute the action for the selected reason
    else:
        print("Invalid selection. Please enter a valid number.")

def show_tree(report_dict, level=0):
    numbered_dict = {}
    count = 1
    for key in report_dict.keys():
        print("  " * level + f"{count}. {key}")
        numbered_dict[count] = key  # Store the original key for action retrieval
        count += 1
        if isinstance(report_dict[key], dict):
            # Recursive call for subcategories
            sub_count = show_tree(report_dict[key], level + 1)
            numbered_dict.update(sub_count)
    return numbered_dict

def execute_action(d,reason,report_dict):
    # Execute the corresponding action for the selected reason
    if reason in report_dict:
        action = report_dict[reason]
        actions = action.split(':')
        print(f"Executing action for '{reason}': {actions}")
        sleep(1)
        for act in actions:
            exec(act)
            sleep(3)  
    else:
        print("No action found for this reason.")


file_lock = threading.Lock()

def update_results_file(action_type):
    """
    Updates the results file with the incremented count for the given action.
    
    Parameters:
    action_type (str): The action type to update ('Likes', 'Comments', 'Follows', 'Reports').
    """
    file_path = "results.txt"
    
    with file_lock:  # Ensure only one thread accesses the file at a time
        # Load current values
        with open(file_path, "r") as file:
            data = file.readlines()

        # Parse current counts from the file
        stats = {}
        for line in data:
            key, value = line.strip().split(" - ")
            stats[key] = int(value)
        
        # Increment the relevant action count
        if action_type in stats:
            stats[action_type] += 1

        # Write updated values back to the file
        with open(file_path, "w") as file:
            for key, value in stats.items():
                file.write(f"{key} - {value}\n")



# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time
# import requests

# # Set up the WebDriver to connect to the existing Chrome instance with remote debugging
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("debuggerAddress", "localhost:9222")  # Connect to the remote debugging port

# # Set up the Chrome WebDriver path
# chrome_driver_path = 'C:/Users/goldf/OneDrive/Documents/chromedriver_win32/chromedriver.exe'

# # Initialize the WebDriver with the specified options to connect to the existing browser
# driver = webdriver.Chrome(options=chrome_options)

# # Open ChatGPT in the existing Chrome window (this will use the existing session)
# driver.get("https://chat.openai.com/")

# # Wait for the page to load
# time.sleep(15)

# # Send a prompt
# prompt_text = "Generate an image of a futuristic city skyline at sunset with flying cars."
# chat_input = driver.find_element(By.XPATH, '//*[@id="prompt-textarea"]/p')  # Find the text input box
# chat_input.send_keys(prompt_text)
# time.sleep(1)
# chat_input.send_keys(Keys.ENTER)

# # Wait for the image to be generated (adjust timing as needed)
# time.sleep(30)

# # Locate the generated image and download it
# try:
#     image_element = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/main/div[1]/div[1]/div/div/div/div/article[2]/div/div/div[2]/div/div[1]/div[1]/div/div/div/div[2]/img')
#     image_url = image_element.get_attribute("src")

#     # Download the image using requests
#     image_response = requests.get(image_url)
    
#     # Save the image
#     if image_response.status_code == 200:
#         with open("generated_image.png", 'wb') as f:
#             f.write(image_response.content)
#         print("Image downloaded successfully.")
#     else:
#         print("Failed to download the image.")

# except Exception as e:
#     print(f"Error: {e}")

# # Close the browser if necessary
# # driver.quit()


    