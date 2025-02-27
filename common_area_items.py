import logging
from env import *
from env import TYPE 
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
# print = logging.info  # Redirect print to info-level logging



# israel_support_comments = [
#     "Israel has the right to defend itself.",
#     "Stand with Israel!",
#     "Israel is a beacon of democracy in the Middle East.",
#     "Israel's innovation is inspiring.",
#     "Support Israel and its quest for peace.",
#     "Israel is a land of hope and resilience.",
#     "I stand with the people of Israel.",
#     "Israel is a vital ally.",
#     "The strength of Israel is admirable.",
#     "Israel's culture is rich and vibrant.",
#     "Israel is a symbol of survival.",
#     "Together for Israel!",
#     "Israel's achievements in technology are remarkable.",
#     "Support Israel's right to exist.",
#     "Israel represents freedom and democracy.",
#     "The history of Israel is a testament to perseverance.",
#     "Israel's contributions to science benefit us all.",
#     "Proud to support Israel!",
#     "Israel is a land of diverse cultures.",
#     "The spirit of Israel is unbreakable.",
#     "Israel's military is one of the best in the world.",
#     "We must defend Israel's right to self-determination.",
#     "Israel's landscapes are breathtaking.",
#     "Israel is a sanctuary for many.",
#     "The resilience of Israel is inspiring.",
#     "Israel's commitment to peace is commendable.",
#     "Stand with our friends in Israel!",
#     "Israel is a land of opportunity.",
#     "The people of Israel deserve peace.",
#     "Support Israel's democratic values.",
#     "Israel's diversity is its strength.",
#     "We will never forget Israel's sacrifices.",
#     "Israel is an example of coexistence.",
#     "Proud of Israel's cultural contributions.",
#     "Israel stands strong against adversity.",
#     "Support Israel's innovation and creativity.",
#     "Israel is a light unto the nations.",
#     "The bond with Israel is unbreakable.",
#     "Israel's history is a story of resilience.",
#     "The future of Israel is bright.",
#     "Support Israel's right to security.",
#     "Israel is a hub of knowledge and learning.",
#     "Together we can ensure Israel's safety.",
#     "Israel's farmers feed the world.",
#     "The spirit of Israel lives on.",
#     "Support for Israel is support for peace.",
#     "Israel's artistic community is vibrant.",
#     "Israel's unity is its strength.",
#     "We stand with Israel in times of need.",
#     "The Israeli people are strong and resilient.",
#     "Israel is a land of progress.",
#     "The achievements of Israel are commendable.",
#     "We cannot ignore Israel's challenges.",
#     "Support Israel's quest for lasting peace.",
#     "The history of Israel is a testament to hope.",
#     "Israel is a model for democracy.",
#     "Together, we stand with Israel.",
#     "Israel is a haven for many seeking refuge.",
#     "Support Israel's right to thrive.",
#     "Israel's advancements in medicine save lives.",
#     "Proud of Israel's technological leadership.",
#     "Israel's spirit of innovation is unmatched.",
#     "Stand strong with Israel.",
#     "The diversity of Israel enriches us all.",
#     "Israel's achievements inspire generations.",
#     "We cannot forget Israel's sacrifices for peace.",
#     "Support for Israel is support for democracy.",
#     "Israel's military innovation is impressive.",
#     "Israel is a champion of human rights.",
#     "The future of Israel is in our hands.",
#     "Israel's agricultural innovations are groundbreaking.",
#     "We support Israel's quest for stability.",
#     "The culture of Israel is a treasure.",
#     "Israel is a land of dreams and possibilities.",
#     "The spirit of the Israeli people is incredible.",
#     "Support Israel's commitment to peace and security.",
#     "Israel is a land of opportunity for all.",
#     "Together, we stand with the people of Israel.",
#     "Israel's technological advancements benefit humanity.",
#     "Proud of Israel's rich history.",
#     "Israel's youth are its future.",
#     "Support for Israel is support for progress.",
#     "Israel is a land where hope thrives.",
#     "The achievements of Israel's scientists are remarkable.",
#     "Israel is a symbol of strength and courage.",
#     "We celebrate Israel's vibrant culture.",
#     "Support Israel's democratic processes.",
#     "The resilience of Israel is an inspiration.",
#     "Together, we can support Israel's growth.",
#     "Israel's commitment to peace is unwavering.",
#     "Stand with Israel for a better tomorrow.",
#     "Israel is a nation of pioneers.",
#     "The beauty of Israel is unmatched.",
#     "We must advocate for Israel's rights.",
#     "Support for Israel is a call for unity.",
#     "Israel's heritage is a source of pride.",
#     "Together, we celebrate Israel's successes.",
#     "The strength of Israel is its people.",
#     "Support Israel's efforts for peace and understanding.",
#     "Israel is a land of innovation and creativity.",
#     "We stand with Israel in solidarity.",
#     "The future is bright for Israel.",
#     "I stand with Israel!",
#     "Solidarity with Israel 🇮🇱",
#     "Peace for Israel always.",
#     "Israel has my support!",
#     "Forever pro-Israel",
#     "Standing strong with Israel.",
#     "Israels right to defend!",
#     "Supporting Israels future.",
#     "Am Yisrael Chai!",
#     "Peace for Israel",
#     "Supporting Israels security.",
#     "Defending Israels sovereignty!",
#     "Israel deserves peace.",
#     "Proudly pro-Israel!",
#     "Strength for Israel.",
#     "Backing Israel always!",
#     "Unity with Israel",
#     "Israel forever",
#     "Israel deserves justice!",
#     "Always with Israel."
# ]
israel_support_comments = [
    "wow, this really made me stop and think. thank you for sharing",
    "such a great post, really apprciate you putting this out there",
    "this is so intrasting, i always enjoy seeing posts like this",
    "this is really something special. thanks for sharing",
    "so much thought went into this well done!",
    "i didnt expect to come across this, but im so glad i did",
    "this is so well done. really makes you reflect",
    "such a great reminder of the things that matter most",
    "thanks for sharing this, its so important",
    "this is truely fascinating, appriciate you posting it",
    "what a thoughtful post, really resonates with me",
    "this made my day. thanks for putting it out there",
    "such an insightful take, really makes you think",
    "this is such an intrasting perspective. thank you for this",
    "such a simple yet powerful post. well done!",
    "i always enjoy seeing posts like this—thoughtful and meaningful",
    "this really stayed with me. great post",
    "such an important thing to share. thank you!",
    "this really made me smile, so uplifting",
    "wow, such a great reminder. thanks for posting this",
    "this is the kind of content that really connects with people",
    "such a meaningful post, really apprciate this perspective",
    "this is so thoughtful and well done",
    "i love seeing posts like this. so much to think about",
    "this is so intrasting, thank you for sharing",
    "this really moved me, so important to share",
    "thank you for this, it really stays with you",
    "this is so powerful in its simplicity",
    "such a great example of what makes content meaningful",
    "this is really something everyone should see. thank you",
    "wow, what a beautifully put-together post. so well done",
    "i cant get this post out of my head, its so impactful",
    "this is really uplifting. thank you for sharing it",
    "such a thought-provoking and reflective post",
    "this post has such a positive energy. love it!",
    "this really makes you stop and think. great job!",
    "such a unique take, really appriciate you sharing it",
    "this is so simple yet so meaningful. well done!",
    "really enjoyed this post. it has such a great message",
    "this is the kind of content that brings people together",
    "what a strong and important post. thank you for this",
    "this is so heartfelt and meaningful. thanks for sharing",
    "this really highlights something important. appriciate it",
    "such a well-done post, really made me reflect",
    "this is so versatile and thoughtful. love it!",
    "this really brings a fresh perspective. thank you for posting",
    "what a strong and powerful message. thank you!",
    "this is truely one of the most thoughtful posts ive seen",
    "thank you for sharing this, its really inspiring"
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
    "Its time to help the people of Iran free themselves from Ali Khameneis dictatorship.",
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
    # "israeltodaymag", TODO fix username
    "jewishagency", 
    "honestreporting", 
    "beyondtheheadlines",
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
("https://www.instagram.com/p/DDXanKiNmPa/?igsh=MTVkeWhqcW82MGxtaA==",8),
("https://www.instagram.com/reel/DCRFvJrqTHO/?igsh=YzljYTk1ODg3Zg==",8),
("https://www.instagram.com/reel/DDSlLsPOn62/?igsh=YzljYTk1ODg3Zg==",8),
]


report_instagram_post_clicks = {
    "bullying or harassment":"d.click(370,1010):d.click(370,1255):d.click(370,1165):d.click(370,1336)",
    "Credible threat to safty":"d.click(370,1181):d.click(370,835)",
    "Seems like terrorism or organized crime":"d.click(370,1181):d.click(370,915)",
    "Calling for violence":"d.click(370,1181):d.click(370,1168)",
    "Hate speech or symbols":"d.click(370,1181):d.click(370,1090)",
    "Showing violence, death or severe injury":"d.click(370,1181):d.click(370,1256)",
    "False information-Health":"d.click(370,1518):d.click(370,1085)",
    "False information-Politics":"d.click(370,1518):d.click(370,1165)",
    "False information-Social issues":"d.click(370,1518):d.click(370,1252)",
    "False information-Digitally created or altered":"d.click(370,1518):d.click(370,1341)",
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
    "bullying or harassment":"d.click(370,1223):d.click(370,1304):d.click(370,1489)",
    "Terrorism":"d.click(370,1135):d.click(370,1000):d.click(370,1481)",
    "Violent threat":"d.click(370,1135):d.click(370,585):d.click(370,1481)",
    "Dangerous organizations or individuals":"d.click(370,1135):d.click(370,837):d.click(370,1481)",
    "Credible threat to safty":"d.click(370,1135):d.click(370,1085):d.click(370,1481)",
    "Hate speech or symbols":"d.click(370,1054):d.click(370,1500)",
    "False information":"d.click(370,1476)",
}
instagram_accounts_to_report =[
    ("https://www.instagram.com/free.palestine.1967?igsh=YzljYTk1ODg3Zg==",7)
]
report_instagram_account_keys = [
    "bullying or harassment",                     # 1
    "Terrorism",                                  # 2
    "Violent threat",                             # 3
    "Dangerous organizations or individuals",     # 4
    "Credible threat to safty",                   # 5
    "Hate speech or symbols",                     # 6
    "False information"                           # 7
]

month_dict_month_to_number = {
    "jan": "1",
    "feb": "2",
    "mar": "3",
    "apr": "4",
    "may": "5",
    "jun": "6",
    "jul": "7",
    "aug": "8",
    "sep": "9",
    "oct": "10",
    "nov": "11",
    "dec": "12"
}
month_dict_month_to_number_capital = {
    "Jan": "1",
    "Feb": "2",
    "Mar": "3",
    "Apr": "4",
    "May": "5",
    "Jun": "6",
    "Jul": "7",
    "Aug": "8",
    "Sep": "9",
    "Oct": "10",
    "Nov": "11",
    "Dec": "12"
}
month_dict_number_to_month = {
    "1": "Jan",
    "2": "Feb",
    "3": "Mar",
    "4": "Apr",
    "5": "May",
    "6": "Jun",
    "7": "Jul",
    "8": "Aug",
    "9": "Sep",
    "10": "Oct",
    "11": "Nov",
    "12": "Dec"
}
y_start = 1304
y_end = 1382
YEAR_CROP_TWI = (447,y_start,568,y_end)
MONTH_CROP_TWI = (313,y_start,405,y_end)
DAY_CROP_TWI = (152,y_start,238,y_end)
y_start = 1056
y_end = 1412
YEAR_CROP_INST = (530,y_start,660,y_end)
MONTH_CROP_INST = (313,y_start,405,y_end)
DAY_CROP_INST = (37,y_start,186,y_end)
y_start = 1138
y_end = 1200
YEAR_CROP_TIK = (490,y_start,630,y_end)
MONTH_CROP_TIK = (102,y_start,200,y_end)
DAY_CROP_TIK = (300,y_start,400,y_end)
MAX_DURATION = 1800
swipe_function_param = ((400, 500), (1200, 1400), (-40, 40), (600, 700), 1, 0.05)
