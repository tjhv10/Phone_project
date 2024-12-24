
import logging

# Configure logging
log_file = "logs.log"  # Log file to capture output
logging.basicConfig(
    level=logging.INFO,  # Log all messages of level DEBUG and above
    format="%(asctime)s - %(levelname)s - %(message)s",  # Include timestamp, level, and message
    handlers=[
        logging.FileHandler(log_file, mode='w'),  # Write logs to a file
        logging.StreamHandler()  # Also print logs to the console
    ]
)

# Replace all `print` statements with `logging.info` or appropriate log levels
print = logging.info  # Redirect print to info-level logging



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
    "Forever pro-Israel",
    "Standing strong with Israel.",
    "Israel’s right to defend!",
    "Supporting Israel’s future.",
    "Am Yisrael Chai!",
    "Peace for Israel",
    "Supporting Israel’s security.",
    "Defending Israel’s sovereignty!",
    "Israel deserves peace.",
    "Proudly pro-Israel!",
    "Strength for Israel.",
    "Backing Israel always!",
    "Unity with Israel",
    "Israel forever",
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
    "EC4Israel",
    "JewsFightBack",
    "VividProwess",
    "RosieE2017",
    "rachelhalinasor",
    "heart_israeli",
    "Amiran_Zizovi",
    "tanamakomakoto",
    "AviKaner",
    "NiohBerg",
    "kyg_best",
    "veguigui",
    "israelifihther",
    "Seeingidoc",
    "EYakoby",
    "AzatAlsalim",
    "eylonalevy",
    "IsraelAllies",
    "Israellycool",
    "bandlersbanter",
    "HilzFuld",
    "ZionistFed",
    "all_israel_news",
    "JewsFightBack",
    "VividProwess",
    "RosieE2017",
    "rachelhalinasor",
    "heart_israeli",
    "Amiran_Zizovi",
    "tanamakomakoto",
    "AviKaner",
    "NiohBerg",
    "kyg_best",
    "veguigui",
    # "israelifihther", #check this account
    "Seeingidoc",
    "EYakoby",
    "AzatAlsalim",
    "eylonalevy",
    "IsraelAllies",
    "Israellycool",
    "bandlersbanter",
    "HilzFuld",
    "ZionistFed",
    "THEREALJEW613",
    "JakeWSimons",
    "AvivaKlompas",
]
#Todo fix some of issue in bad names and add new names
tiktok_accounts = [
    "berelsolomon",
    "danielryanspaulding",
    "theamyalbertson",
    "thatopinionatedgirl",
    "alexandramoulavi",
    "hananyanaftali",
    "zionqueens",
    "eylonalevy",
    "that.zionist",
    "israelintheph",
    "israel.restoratio",
    "we.jewish",
    "zachmargs",
    "joiceglobal",
    "livinglchaim",
    "emilyintelaviv",
    "israelwithcindy",
    "hen.mazzig",
    "am.israel_chai",
    "israel",
    "israel_news_il",
    "hillelintl",
    "all_israel_news",
    "Israelkicksass",
    "heatherduttonmart",
    "myholystyle",
    "israel12344567789",
    "bring.evyatar.home",
    "imyerushalayimkaplam",
    "zahavaschwartz",
    "birthrightisrael",
    "adar.hatufim.7.10.2023",
    "therealmelindastrauss",
    "miatalias",
    "danielle.myriam",
    "lfparodies",
    "clevergirl2023",
    "israelforever667",
    "standuptojewishhate",
    "yosephhaddad",
    "beaaza1",
    "naorzion9",
    "semiongrafman",
    "shirazshukrun",
    "stand_with_us",
    "idfofficial",
    "michalgspan",
    "idf",
    "Perorationer",
    "End_Wahhabism",
    "NourNaim88"
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
    "ariseforisrael",
    "israel"
]


tiktok_handles_specials = [
    "ariseforisrael",
    "women.of.the.midd",
    "unapologetic.israeli",
]


instagram_handles_special = [
    "theisraelstory",
    "womenofmiddleeast",
    "unapologetic_israeli",
    "wildbranchmedia",
    "ariseforisrael",
]


anti_israel_twitter = [
    # -----proIran
    "PressTV",
    "Tasnimnews_EN",
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
    "Slogging.infoerFamily",
    "DravenNoctis",
    # -----antiIsrael
    "umyaznemo",
    "_NicoleNonya",
    "Naila_Ayad",
    "RehamMeri",
    "RimabestRima12",
    "brendancbrowne",
    "AcaforPalestine",
    "sahouraxo",
    "omarsuleiman",
    "EyeonPalestine",
    "OnlinePalEng",
    "Palestine_UN",
    "nocurvature",
    "MouinRabbani",
    "HaShem_GAZA_",
    "Lucas_Gage_",
    "nick_rose96",
    "OmarShargawi",
    "HackneySwp",
    "Yusufafsar",
    "Crazycaptaincat",
    "TorahJudaism",
    "drhusseinabd",
    "Muizzfail",
    "Africa4Pal",
    "Ian63506160",
    "KerryBurgess",
    "Mr_RimoniTMD",
    "nuzlyazhar",
    "fedoration",
    "BeautyMrked",
    "mohamadfakih8",
    "CNDuk",
    "realflanbinflan",
    "avoidingtrolls",
    "b_salem1",
    "ithaitmelloul",
    "MannieMighty1",
    "Adli02030892",
    "Michael35081695",
    "ClaireD3041358",
    "Anna_AnninaEl",
    "MissRinaIdrus",
    "poordad00",
    "GotPropaganda",
    "Humanityclouded",
    "AssalRad"
]

anti_israel_tiktok = [
    "AlalamChannel",
    "aj_plus",
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
    "love__iran",
    "antiisrael_action",
    "antizionistjewguy",
    "oxact4pal",
    "ameenahisma00",
    "nyxnyc",
    "amna.naji",
    "hakamsoufan",
    "fromthe.river.to_the.sea",
    "imrankan937",
    "palestine3030",
    "palestine1thefirstone",
    "west.bank.girl",
    "sarrbiran",
    "bunkercat36",
    "palestine_for_ever_2024",
    "yourfavoriteguy",
    "healwithtati",
    "aygofiz",
    "david.beazley70",
    "_NicoleNonya",
    "amnestyuk",
    "javiersorianony",
    "outlawz.co.uk",
    "hagoora_14._",
    "palestine967"
]

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

report_tiktok_account = {
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
report_tiktok_account_keys = [
    "Physical violence and violent threats",
    "Sexual exploitation and abuse",
    "Human exploitation",
    "Other criminal activities",
    "Dangerous activities and challenges",
    "Shocking and graphic content",
    "Hate speech and hateful behaviors",
    "Harassment and bullying",
    "Harmful misinformation",
    "Deepfakes, synthetic media, and manipulated media",
    "Child sexual exploitation",
    "Illegal hate speech",
    "Content relating to violent or organized crime",
    "Harrassment or threats",
    "Defamation",
    "Other"
]


report_twitter_clicks = {
    "Slurs & Tropes":"d.click(370,670):d.click(370,1450):d.click(370,670):d.click(370,1450):d.click(370,1450)",
    "Hateful References":"d.click(370,670):d.click(370,1450):d.click(370,950):d.click(370,1450):d.click(370,1450)",
    "Dehumanization":"d.click(370,670):d.click(370,1450):d.click(370,1250):d.click(370,1450):d.click(370,1450)",
    "Hateful Imagery":"d.click(370,670):d.click(370,1450):d.swipe(500, 1200, 500, 300, duration=0.05):d.click(370,860):d.click(370,1450):d.click(370,1450)",
    "Incitement":"d.click(370,670):d.click(370,1450):d.swipe(500, 1200, 500, 300, duration=0.05):d.click(370,1214):d.click(370,1450):d.click(370,1450)",
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
    ("https://twitter.com/marwanbishara/status/1805202165054493148?t=zbQJshyDikFcHUFcMKC1yg&s=19",4),
    ("https://x.com/Lucas_Gage_/status/1720998157369192710",5),
    ("https://x.com/Mr_RimoniTMD/status/1854267057275306105",5),
    ("https://x.com/nuzlyazhar/status/1854454771358519722",5),
    ("https://x.com/fedoration/status/1852116998064607390",5),
    ("https://x.com/nick_rose96/status/1850365270302634042",5),
    ("https://x.com/OmarShargawi/status/1851868583057297697",5),
    ("https://x.com/HackneySwp/status/1852772248324633040",15),
    ("https://x.com/Yusufafsar/status/1852385840921456846",15),
    # ("https://x.com/Yusufafsar/status/1852385492639035798",15),       #The post has been deleted
    # ("https://x.com/Du_con_Lajoie/status/1851356793328296326",15),    #The post has been deleted
    ("https://x.com/komugi_twit/status/1852406478277357956",15),
    ("https://x.com/BeautyMrked/status/1853873503188984175",15),
    ("https://x.com/mohamadfakih8/status/1855306559800385623",5),
    ("https://x.com/TorahJudaism/status/1848359235400147297",2),
    ("https://x.com/bobbydilettante/status/1804188608015876209",4),
    ("https://x.com/realflanbinflan/status/1759489765152346571",5),
    ("https://x.com/avoidingtrolls/status/1808133225190916122",4),
    ("https://x.com/b_salem1/status/1803164191315870120",4),
    ("https://x.com/utalkntme/status/1786263653748256919",13),
    ("https://x.com/drhusseinabd/status/1803744396375941322",4),
    ("https://x.com/drhusseinabd/status/1783478189567697302",4),
    ("https://x.com/ithaitmelloul/status/1754229590380212582",5),
    ("https://x.com/paulinepark/status/1855762196145266894",5),
    ("https://x.com/muslimnogo/status/1853502864678699251",4),
    ("https://x.com/Bernadotte22/status/1763231563045818814",5),
    ("https://x.com/Africa4Pal/status/1600882395120799745",5),
    ("https://x.com/sabriaballand/status/1855738166935744936",5),
    ("https://x.com/Andre__Damon/status/1854055465778642973",5),
    ("https://x.com/sabriaballand/status/1855738166935744936",5),
    ("https://x.com/bkeithb/status/1856448330575884619",5),
    ("https://x.com/MannieMighty1/status/1853460648673300801",5),
    ("https://x.com/Adli02030892/status/1853467503722197266",5),
    ("https://x.com/TheGreatFausto1/status/1853767671625683077",4),
    ("https://x.com/Michael35081695/status/1853464937147892090",5),
    ("https://x.com/quadrafenians/status/1853558606131597576",5),
    ("https://x.com/quadrafenians/status/1853558606131597576",5),
    ("https://x.com/ClaireD3041358/status/1853759909105467748",5),
    ("https://x.com/ElHombreEHombre/status/1853465961749160318",10),
    ("https://x.com/I2funSmile/status/1853480884684701817",5),
    ("https://x.com/itariqshah1/status/1854701705738203484",12),
    ("https://x.com/Anna_AnninaEl/status/1855004248905257382",4),
    ("https://x.com/RyanRozbiani/status/1855422624207425626",5),
    ("https://x.com/GAZAWOOD1/status/1855703803158253968",13),
    ("https://x.com/Amieradjah/status/1837128137148350957",4),
]

tiktok_accounts_to_report = [
    "https://www.tiktok.com/@healwithtati"
]

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


tiktok_posts_to_report = [
    # ("https://vm.tiktok.com/ZGdNeymS6/" ,4),      #The post has been deleted
    ("https://vm.tiktok.com/ZGdNeFh4w/" ,4),
    ("https://vm.tiktok.com/ZGdNe6WP9/" ,4),
    ("https://vm.tiktok.com/ZGdNeBx2t/" ,4),
    ("https://vm.tiktok.com/ZGdNefREq/" ,4),
    ("https://vm.tiktok.com/ZGdNeMagN/" ,4),
    ("https://www.tiktok.com/@nyxnyc/video/7351857780162284846?q=From%20the%20river%20to%20the%20sea&t=1730973145737" ,4),
    ("https://www.tiktok.com/@kindakhatib22/video/7287249443303329031?q=palestine&t=1730973507062" ,4),
    ("https://www.tiktok.com/@pascoliiii/video/7396072279362276641?q=From%20the%20river%20to%20&t=1730973687107" ,4),
    ("https://www.tiktok.com/@amna.naji/video/7088113841766206726?q=freepalestine&t=1730973776643" ,4),
    ("https://www.tiktok.com/@leyaaalyaa/video/7296362568703020290?q=freepalestine&t=1730973776643" ,4),
    ("https://www.tiktok.com/@hakamsoufan/video/7303444764655881490?is_from_webapp=1&sender_device=pc&web_id=7435566416340747831" ,8),
    ("https://www.tiktok.com/@imrankan937/video/7435347634035985697?is_from_webapp=1&sender_device=pc&web_id=7435566416340747831" ,8),
    ("https://www.tiktok.com/@thaliaelansari/video/7368556524911873288?is_from_webapp=1&sender_device=pc&web_id=7435566416340747831" ,8),
    ("https://www.tiktok.com/@ajnabiyeh/video/7307300683462593824?is_from_webapp=1&sender_device=pc&web_id=7435566416340747831" ,8),
    ("https://www.tiktok.com/@fromthe.river.to_the.sea/video/7430161622431255841?is_from_webapp=1&sender_device=pc&web_id=7435566416340747831" ,8),
    ("https://www.tiktok.com/@sellapuspi20/video/7289741587385568517?is_from_webapp=1&sender_device=pc&web_id=7435566416340747831" ,10),
    ("https://www.tiktok.com/@palestine3030/video/7435474614223899912?is_from_webapp=1&sender_device=pc&web_id=7435566416340747831" ,8),
    ("https://www.tiktok.com/@sethwatkinsmusic/video/7321073871388462382?is_from_webapp=1&sender_device=pc&web_id=7435566416340747831" ,8),
    ("https://www.tiktok.com/@palestine1thefirstone/video/7292327559075843333?q=river%20to%20the%20sea&t=1731334335157" ,8),
    ("https://www.tiktok.com/@aygofiz/video/7398070083152661765?q=genocide&t=1731334563770" ,8),
    ("https://www.tiktok.com/@wisdom.tales.from/video/7300860659036622113?q=zionist&t=1731334722020" ,8),
    ("https://www.tiktok.com/@thatorthodoxguy/video/7435282676090801431", 15),
    ("https://www.tiktok.com/@warproject.xy/video/7087965041647029530" ,8),
    ("https://www.tiktok.com/@reksifyptiktok/video/7323219220668501254" ,8),
    ("https://www.tiktok.com/@umut_var61/video/7292493802332474630?q=israwl&t=1731336259759" ,8),
    ("https://www.tiktok.com/@sam84178/video/7435315683027684640?is_from_webapp=1&sender_device=pc&web_id=7435566416340747831" ,8),
    ("https://www.tiktok.com/@sarrbiran/video/7436524242327407894?q=genocide&t=1731481221680" ,8),
    ("https://www.tiktok.com/@mohamed.elhady/video/7289816386308771079?q=genocide&t=1731481221680" ,8),
    ("https://www.tiktok.com/@dearmoooooon/video/7292009641440054529?q=genocide&t=1731481221680" ,8),
    ("https://www.tiktok.com/@babah.ja/video/7296793814633614597" ,8),
    # ("" ,),
]

instagram_posts_to_report = [

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