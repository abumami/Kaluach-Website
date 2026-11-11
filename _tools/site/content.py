# Content of kaluach.com's app sections (one dict per app, English and Hebrew).
# Each app: about page, privacy statement, support page with the contact form.

ACCESS_KEY = "b6964e45-f32f-49a7-a12c-6f3900c1c99e"   # the site's existing Web3Forms key (public by design)

APPS = {}

# Kaluach for Windows: zmanim alarms (and the matching privacy wording) are shown only once
# the update that has them (4.0.52 or later) is live in the Microsoft Store. Set to True then.
WIN_ALARMS_LIVE = True     # 4.0.52 live in the Microsoft Store, 3 Nov 2026

# ---------------------------------------------------------------- Kaluach for the Mac
APPS["mac"] = dict(
    icon="kaluach-mac-icon.png",
    en=dict(
        name="Kaluach™ for the Mac", plain="Kaluach for the Mac", topic="Kaluach for the Mac",
        status="Coming soon to the Mac App Store",
        lead="The Hebrew and civil calendars side by side, with holidays, the weekly parsha, zmanim for your location, and personal events such as yahrzeits, birthdays and anniversaries. Print or export a whole year.",
        features=[
            "Civil Month and Hebrew Month views, Today and Go to Year — back to 3760 BCE, with the Julian calendar before the Gregorian reform.",
            "Open on today, or on the day you last selected.",
            "Move through the calendar with the arrow keys: ← → a day, ↑ ↓ a week.",
            "Jewish, Israeli and civil holidays, the weekly parsha and special Shabbatot, for Israel or the diaspora.",
            "Zmanim for any location, by the built-in shitot (GRA, Magen Avraham, Chabad, Harav Ovadiah Yosef, Harav Mordechai Eliyahu, Kisei Rachamim, Maaseh Nissim) or your own, with Rabbeinu Tam if you wish.",
            "Places in Judea and Samaria use Israel’s clock, including daylight saving.",
            "Personal events — azkarot, birthdays, anniversaries, one-time dates — with reminders, Bar and Bat Mitzvah dates, and an optional civil date.",
            "Set or change an event’s date by its civil or Hebrew date.",
            "Share events with your family or your shul: choose which events to export to a Kaluach events file, and which to import from one.",
            "Zmanim alarms, never on Shabbat or Yom Tov.",
            "Print a year of Shabbatot and holidays with their times, or export every day to a spreadsheet.",
            "English and Hebrew. Your events and locations stay the same on your Macs and in iKaluach through iCloud.",
        ],
        requirements="macOS 14 Sonoma or later.",
        help=[("../help/mac/index.html", "Kaluach for the Mac Help", "English"), ("../help/mac/he/index.html", "עזרה לקלוח למק", "עברית")],
        helpnote="The same help is built into the app: Help › Kaluach Help.",
        privacy=[
            ("lead", "Kaluach™ for the Mac collects no personal data. There are no accounts, no ads, no analytics and no tracking."),
            ("Where your data is kept", "Your events, saved locations, custom zmanim shitot, alarm settings and preferences are stored on your Mac (and in your Mac’s own backups). The developer never receives them."),
            ("iCloud", "When you are signed into iCloud, your events, saved locations and custom zmanim shitot are also kept in your own iCloud account, so that they are the same on your other Macs and in iKaluach on your iPhone. They are stored and transferred by Apple under <a href=\"https://www.apple.com/legal/privacy/\">Apple’s privacy policy</a>; the developer has no access to them. Alarm settings and preferences stay on each device. If iCloud is off for the app, nothing leaves your Mac."),
            ("Location", "Location is optional. If you choose <strong>Use My Location</strong>, your position is used on the Mac to calculate zmanim. To show the place’s name and time zone, the app asks Apple’s map service, as Apple’s own apps do. When you search for a city, the text you type is sent to Apple’s map service to find matching places. These requests are handled by Apple under <a href=\"https://www.apple.com/legal/privacy/\">Apple’s privacy policy</a>; the developer does not receive them."),
            ("Alarms and reminders", "Zmanim alarms and event reminders are scheduled on the Mac itself. Nothing is sent to a server."),
        ],
    ),
    he=dict(
        name="קלוח™ למק", plain="קלוח למק", topic="קלוח למק",
        status="בקרוב ב־Mac App Store",
        lead="הלוח העברי והלוח הלועזי זה לצד זה, עם חגים, פרשת השבוע, זמני היום למיקום שלך ואירועים אישיים — אזכרות, ימי הולדת וימי נישואין. הדפסה וייצוא של שנה שלמה.",
        features=[
            "תצוגת חודש אזרחי וחודש עברי, היום ומעבר לשנה — עד שנת 3760 לפנה״ס, עם הלוח היוליאני שלפני המעבר ללוח הגרגוריאני.",
            "פתיחה ביום הנוכחי, או ביום האחרון שבחרתם.",
            "מעבר בלוח במקשי החיצים: ← → יום, ↑ ↓ שבוע.",
            "חגים ומועדים יהודיים, ישראליים ואזרחיים, פרשת השבוע ושבתות מיוחדות, לארץ ישראל או לחוץ לארץ.",
            "זמני היום לכל מיקום, לפי השיטות המובנות (גר״א, מגן אברהם, חב״ד, הרב עובדיה יוסף, הרב מרדכי אליהו, כסא רחמים, מעשה ניסים) או לפי שיטה משלך, ואם רוצים — גם רבינו תם.",
            "מקומות ביהודה ושומרון משתמשים בשעון ישראל, כולל שעון הקיץ.",
            "אירועים אישיים — אזכרות, ימי הולדת, ימי נישואין ותאריכים חד־פעמיים — עם תזכורות, תאריך בר ובת מצווה ותאריך לועזי לפי הצורך.",
            "קביעה ושינוי של תאריך אירוע לפי התאריך הלועזי או העברי.",
            "שיתוף אירועים עם המשפחה או עם בית הכנסת: בוחרים אילו אירועים לייצא לקובץ האירועים של קלוח, ואילו לייבא ממנו.",
            "התראות זמנים, לעולם לא בשבת וביום טוב.",
            "הדפסת שנה של שבתות וחגים עם זמניהם, או ייצוא של כל ימי השנה לגיליון.",
            "עברית ואנגלית. האירועים והמיקומים שלך זהים במקים האחרים שלך ובאיי־קלוח, דרך iCloud.",
        ],
        requirements="macOS 14 Sonoma ומעלה.",
        help=[("../../help/mac/he/index.html", "עזרה לקלוח למק", "עברית"), ("../../help/mac/index.html", "Kaluach for the Mac Help", "English")],
        helpnote="אותה עזרה כלולה באפליקציה: בתפריט Help › עזרה לקלוח.",
        privacy=[
            ("lead", "קלוח™ למק אינו אוסף מידע אישי. אין חשבונות משתמש, אין פרסומות, אין ניתוח שימוש ואין מעקב."),
            ("היכן נשמר המידע שלך", "האירועים, המיקומים השמורים, שיטות הזמנים המותאמות, הגדרות ההתראות וההעדפות נשמרים במק שלך (ובגיבויים של המק עצמו). המפתח אינו מקבל אותם לעולם."),
            ("iCloud", "כשאתה מחובר ל־iCloud, האירועים, המיקומים השמורים ושיטות הזמנים המותאמות נשמרים גם בחשבון iCloud שלך, כדי שיהיו זהים במקים האחרים שלך ובאיי־קלוח באייפון. הם נשמרים ומועברים על ידי Apple לפי <a href=\"https://www.apple.com/legal/privacy/\">מדיניות הפרטיות של Apple</a>; למפתח אין גישה אליהם. הגדרות ההתראות וההעדפות נשארות בכל מכשיר. אם iCloud כבוי עבור האפליקציה, שום דבר אינו יוצא מהמק שלך."),
            ("מיקום", "המיקום הוא רשות. אם בוחרים <strong>השתמש במיקום שלי</strong>, המיקום משמש במק לחישוב הזמנים. כדי להציג את שם המקום ואת אזור הזמן שלו, האפליקציה פונה לשירות המפות של Apple, כפי שעושות האפליקציות של Apple עצמה. בחיפוש עיר, הטקסט שמקלידים נשלח לשירות המפות של Apple כדי למצוא מקומות מתאימים. בקשות אלה מטופלות על ידי Apple לפי <a href=\"https://www.apple.com/legal/privacy/\">מדיניות הפרטיות של Apple</a>; המפתח אינו מקבל אותן."),
            ("התראות ותזכורות", "התראות הזמנים והתזכורות לאירועים מתוזמנות במק עצמו. דבר אינו נשלח לשרת."),
        ],
    ),
)

# ---------------------------------------------------------------- iKaluach
APPS["iKaluach"] = dict(
    icon="ikaluach-icon.png",
    # The App Store page (Apple ID 6819030251); live since 3 Nov 2026: every /iKaluach
    # page shows the "Download on the App Store" badge in place of the status line.
    store=dict(live=True, url="https://apps.apple.com/app/ikaluach-hebrew-calendar/id6819030251",
               en="Available on the App Store", he="זמין ב־App Store",
               badge="https://tools.applemediaservices.com/api/badges/download-on-the-app-store/black/en-us?size=250x83",
               alt_en="Download on the App Store", alt_he="הורדה מה־App Store", width=180),
    en=dict(
        name="iKaluach™", plain="iKaluach", topic="iKaluach (iPhone)",
        status="Coming later for iPhone",
        lead="The same calendars, zmanim and personal events as Kaluach for the Mac, on your iPhone.",
        features=[
            "Civil Month and Hebrew Month views, Today and Go to Year — back to 3760 BCE, with the Julian calendar before the Gregorian reform.",
            "Open on today, or on the day you last selected.",
            "Jewish, Israeli and civil holidays, the weekly parsha and special Shabbatot, for Israel or the diaspora.",
            "Zmanim for any location, by the built-in shitot or your own, with Rabbeinu Tam if you wish.",
            "Places in Judea and Samaria use Israel’s clock, including daylight saving.",
            "Personal events — azkarot, birthdays, anniversaries, one-time dates — with reminders, Bar and Bat Mitzvah dates, and an optional civil date.",
            "Set or change an event’s date by its civil or Hebrew date.",
            "Share events with your family or your shul: choose which events to export to a Kaluach events file, and which to import from one.",
            "Zmanim alarms, never on Shabbat or Yom Tov.",
            "English and Hebrew. Your events and locations stay the same as on your Mac, through iCloud.",
        ],
        requirements="An iPhone with iOS 17 or later. It also runs on an iPad with iPadOS 17 or later.",
        help=[("../help/iphone/index.html", "iKaluach Help", "English"), ("../help/iphone/he/index.html", "עזרה לאיי־קלוח", "עברית")],
        helpnote="The same help is built into the app: Settings › Help.",
        privacy=[
            ("lead", "iKaluach™ collects no personal data. There are no accounts, no ads, no analytics and no tracking."),
            ("Where your data is kept", "Your events, saved locations, custom zmanim shitot, alarm settings and preferences are stored on your iPhone (and in your iPhone’s own backups). The developer never receives them."),
            ("iCloud", "When you are signed into iCloud, your events, saved locations and custom zmanim shitot are also kept in your own iCloud account, so that they are the same in Kaluach for the Mac on your Mac. They are stored and transferred by Apple under <a href=\"https://www.apple.com/legal/privacy/\">Apple’s privacy policy</a>; the developer has no access to them. Alarm settings and preferences stay on each device. If iCloud is off for the app, nothing leaves your iPhone."),
            ("Location", "Location is optional. If you choose <strong>Use My Location</strong>, your position is used on the iPhone to calculate zmanim. To show the place’s name and time zone, the app asks Apple’s map service, as Apple’s own apps do. When you search for a city, the text you type is sent to Apple’s map service to find matching places. These requests are handled by Apple under <a href=\"https://www.apple.com/legal/privacy/\">Apple’s privacy policy</a>; the developer does not receive them."),
            ("Alarms and reminders", "Zmanim alarms and event reminders are scheduled on the iPhone itself. Nothing is sent to a server."),
        ],
    ),
    he=dict(
        name="איי־קלוח™", plain="איי־קלוח", topic="איי־קלוח (אייפון)",
        status="בהמשך, לאייפון",
        lead="אותו לוח, אותם זמני היום ואותם אירועים אישיים כמו בקלוח למק — באייפון.",
        features=[
            "תצוגת חודש אזרחי וחודש עברי, היום ומעבר לשנה — עד שנת 3760 לפנה״ס, עם הלוח היוליאני שלפני המעבר ללוח הגרגוריאני.",
            "פתיחה ביום הנוכחי, או ביום האחרון שבחרתם.",
            "חגים ומועדים יהודיים, ישראליים ואזרחיים, פרשת השבוע ושבתות מיוחדות, לארץ ישראל או לחוץ לארץ.",
            "זמני היום לכל מיקום, לפי השיטות המובנות או לפי שיטה משלך, ואם רוצים — גם רבינו תם.",
            "מקומות ביהודה ושומרון משתמשים בשעון ישראל, כולל שעון הקיץ.",
            "אירועים אישיים — אזכרות, ימי הולדת, ימי נישואין ותאריכים חד־פעמיים — עם תזכורות, תאריך בר ובת מצווה ותאריך לועזי לפי הצורך.",
            "קביעה ושינוי של תאריך אירוע לפי התאריך הלועזי או העברי.",
            "שיתוף אירועים עם המשפחה או עם בית הכנסת: בוחרים אילו אירועים לייצא לקובץ האירועים של קלוח, ואילו לייבא ממנו.",
            "התראות זמנים, לעולם לא בשבת וביום טוב.",
            "עברית ואנגלית. האירועים והמיקומים שלך זהים לאלה שבמק, דרך iCloud.",
        ],
        requirements="אייפון עם iOS 17 ומעלה. פועל גם באייפד עם iPadOS 17 ומעלה.",
        help=[("../../help/iphone/he/index.html", "עזרה לאיי־קלוח", "עברית"), ("../../help/iphone/index.html", "iKaluach Help", "English")],
        helpnote="אותה עזרה כלולה באפליקציה: בהגדרות › עזרה.",
        privacy=[
            ("lead", "איי־קלוח™ אינו אוסף מידע אישי. אין חשבונות משתמש, אין פרסומות, אין ניתוח שימוש ואין מעקב."),
            ("היכן נשמר המידע שלך", "האירועים, המיקומים השמורים, שיטות הזמנים המותאמות, הגדרות ההתראות וההעדפות נשמרים באייפון שלך (ובגיבויים של האייפון עצמו). המפתח אינו מקבל אותם לעולם."),
            ("iCloud", "כשאתה מחובר ל־iCloud, האירועים, המיקומים השמורים ושיטות הזמנים המותאמות נשמרים גם בחשבון iCloud שלך, כדי שיהיו זהים לאלה שבקלוח למק. הם נשמרים ומועברים על ידי Apple לפי <a href=\"https://www.apple.com/legal/privacy/\">מדיניות הפרטיות של Apple</a>; למפתח אין גישה אליהם. הגדרות ההתראות וההעדפות נשארות בכל מכשיר. אם iCloud כבוי עבור האפליקציה, שום דבר אינו יוצא מהאייפון שלך."),
            ("מיקום", "המיקום הוא רשות. אם בוחרים <strong>השתמש במיקום שלי</strong>, המיקום משמש באייפון לחישוב הזמנים. כדי להציג את שם המקום ואת אזור הזמן שלו, האפליקציה פונה לשירות המפות של Apple, כפי שעושות האפליקציות של Apple עצמה. בחיפוש עיר, הטקסט שמקלידים נשלח לשירות המפות של Apple כדי למצוא מקומות מתאימים. בקשות אלה מטופלות על ידי Apple לפי <a href=\"https://www.apple.com/legal/privacy/\">מדיניות הפרטיות של Apple</a>; המפתח אינו מקבל אותן."),
            ("התראות ותזכורות", "התראות הזמנים והתזכורות לאירועים מתוזמנות באייפון עצמו. דבר אינו נשלח לשרת."),
        ],
    ),
)

# ---------------------------------------------------------------- Kaluach for Windows (Kaluach 4; the Store name is "Kaluach")
APPS["win"] = dict(
    icon="kaluach-win-icon.png",
    # The Microsoft Store page (Store ID 9P9QW3JTB6NP); live since 15 Oct 2026: every /win
    # page shows the "Get it from Microsoft" badge in place of the status line.
    store=dict(live=True, url="https://apps.microsoft.com/detail/9P9QW3JTB6NP?mode=direct",
               en="Available in the Microsoft Store", he="זמין ב־Microsoft Store",
               badge="https://get.microsoft.com/images/en-us%20dark.svg"),
    en=dict(
        name="Kaluach™ for Windows", plain="Kaluach for Windows", topic="Kaluach for Windows (Windows)",
        status="Coming soon to the Microsoft Store",
        lead="Kaluach 4, the successor to Kaluach 3 for Windows: the Hebrew and civil calendars side by side, with holidays, the weekly parsha, zmanim for your location, and personal events such as yahrzeits, birthdays and anniversaries. Print or export a whole year.",
        features=[
            "Civil Month and Hebrew Month views, Today and Go to Year — back to 3760 BCE, with the Julian calendar before the Gregorian reform.",
            "Jewish, Israeli and civil holidays, the weekly parsha and special Shabbatot, for Israel or the diaspora.",
            "Zmanim for any location, by the built-in shitot (GRA, Magen Avraham, Chabad, Harav Ovadiah Yosef, Harav Mordechai Eliyahu, Kisei Rachamim, Maaseh Nissim) or your own, with Rabbeinu Tam if you wish.",
            "City search built in — about 170,000 places with their time zones, no internet connection needed.",
            "Personal events — azkarot, birthdays, anniversaries, one-time dates — with reminders as Windows notifications, never on Shabbat or Yom Tov.",
            *(["Zmanim alarms before (or after) the zmanim you choose, never on Shabbat or Yom Tov."] if WIN_ALARMS_LIVE else []),
            "Print a year of Shabbatot and holidays with their times, or export every day to a CSV spreadsheet.",
            "English and Hebrew, light and dark mode. Move your events to and from Kaluach on the Mac, iPhone and Android with the Kaluach events file, choosing which events to export or import.",
        ],
        requirements="Windows 10 (version 1809) or Windows 11, on an Intel/AMD (x64) or ARM64 PC.",
        help=[("../help/win/index.html", "Kaluach for Windows Help", "English"), ("../help/win/he/index.html", "עזרה לקלוח ל־Windows", "עברית")],
        helpnote="The same help is built into the app: the Help button in the toolbar, or F1.",
        extra=("Kaluach 3", "Looking for the legacy Kaluach 3? It is still available: <a href=\"https://download.kaluach.com/Kaluach-3.2.46.30.zip\">download Kaluach 3.2.46.30</a> · <a href=\"https://kaluach3help.kaluach.com\">Kaluach 3 Help</a>."),
        privacy=[
            ("lead", "Kaluach™ for Windows collects no personal data. There are no accounts, no ads, no analytics and no tracking, and the app sends nothing over the internet. (A link you click, such as to this website, opens in your browser.)"),
            ("Where your data is kept", "Your events, saved locations, custom zmanim shitot and settings are stored on your PC, in your Windows user folder. They are not synced anywhere, and the developer never receives them. A file you export (events, or a year’s CSV) goes only where you save it."),
            ("Location", "Kaluach for Windows doesn’t use your PC’s location. You choose a place by searching its built-in list of cities or by typing coordinates; the search happens on your PC and nothing is sent anywhere."),
            ("Alarms and reminders", "Zmanim alarms and event reminders are scheduled with Windows on your PC and shown as Windows notifications. Nothing is sent to a server.") if WIN_ALARMS_LIVE else
            ("Reminders", "Event reminders are scheduled with Windows on your PC and shown as Windows notifications. Nothing is sent to a server."),
            ("Installing and updates", "If you install Kaluach for Windows from the Microsoft Store, Microsoft handles the download, licence and updates under the <a href=\"https://privacy.microsoft.com/privacystatement\">Microsoft Privacy Statement</a>; the developer receives only the anonymous totals the Store reports to every developer (such as the number of installs), and, if you let Windows send diagnostic data, Microsoft’s reports of the app’s crashes."),
            ("Error log", "If the app stops unexpectedly, a short error log is written on your PC so that a problem can be diagnosed. It is never sent anywhere; you can choose to include it in a support message."),
        ],
    ),
    he=dict(
        name="קלוח™ ל־Windows", plain="קלוח ל־Windows", topic="קלוח ל־Windows",
        status="בקרוב ב־Microsoft Store",
        lead="קלוח 4, היורש של קלוח 3 ל־Windows: הלוח העברי והלוח הלועזי זה לצד זה, עם חגים, פרשת השבוע, זמני היום למיקום שלך ואירועים אישיים — אזכרות, ימי הולדת וימי נישואין. הדפסה וייצוא של שנה שלמה.",
        features=[
            "תצוגת חודש אזרחי וחודש עברי, היום ומעבר לשנה — עד שנת 3760 לפנה״ס, עם הלוח היוליאני שלפני המעבר ללוח הגרגוריאני.",
            "חגים ומועדים יהודיים, ישראליים ואזרחיים, פרשת השבוע ושבתות מיוחדות, לארץ ישראל או לחוץ לארץ.",
            "זמני היום לכל מיקום, לפי השיטות המובנות (גר״א, מגן אברהם, חב״ד, הרב עובדיה יוסף, הרב מרדכי אליהו, כסא רחמים, מעשה ניסים) או לפי שיטה משלך, ואם רוצים — גם רבינו תם.",
            "חיפוש ערים מובנה — כ־170,000 מקומות עם אזורי הזמן שלהם, בלי צורך בחיבור לאינטרנט.",
            "אירועים אישיים — אזכרות, ימי הולדת, ימי נישואין ותאריכים חד־פעמיים — עם תזכורות כהתראות של Windows, לעולם לא בשבת וביום טוב.",
            *(["התראות זמנים לפני הזמנים שבוחרים (או אחריהם), לעולם לא בשבת וביום טוב."] if WIN_ALARMS_LIVE else []),
            "הדפסת שנה של שבתות וחגים עם זמניהם, או ייצוא של כל ימי השנה לגיליון CSV.",
            "עברית ואנגלית, מצב בהיר ומצב כהה. העברת אירועים אל קלוח במק, באייפון ובאנדרואיד וממנו, בקובץ האירועים של קלוח, עם בחירה אילו אירועים לייצא או לייבא.",
        ],
        requirements="Windows 10 (גרסה 1809) או Windows 11, במחשב Intel/AMD (x64) או ARM64.",
        help=[("../../help/win/he/index.html", "עזרה לקלוח ל־Windows", "עברית"), ("../../help/win/index.html", "Kaluach for Windows Help", "English")],
        helpnote="אותה עזרה כלולה באפליקציה: לחצן העזרה בסרגל הכלים, או F1.",
        extra=("קלוח 3", "מחפשים את קלוח 3 הוותיק? הוא עדיין זמין: <a href=\"https://download.kaluach.com/Kaluach-3.2.46.30.zip\">הורדת קלוח 3.2.46.30</a> · <a href=\"https://kaluach3help.kaluach.com\">עזרה לקלוח 3</a>."),
        privacy=[
            ("lead", "קלוח™ ל־Windows אינו אוסף מידע אישי. אין חשבונות משתמש, אין פרסומות, אין ניתוח שימוש ואין מעקב, והאפליקציה אינה שולחת דבר באינטרנט. (קישור שלוחצים עליו, למשל לאתר זה, נפתח בדפדפן.)"),
            ("היכן נשמר המידע שלך", "האירועים, המיקומים השמורים, שיטות הזמנים המותאמות וההגדרות נשמרים במחשב שלך, בתיקיית המשתמש שלך ב־Windows. הם אינם מסונכרנים לשום מקום, והמפתח אינו מקבל אותם לעולם. קובץ שמייצאים (אירועים, או גיליון CSV של שנה) נשמר רק במקום שבוחרים."),
            ("מיקום", "קלוח ל־Windows אינו משתמש במיקום של המחשב. בוחרים מקום בחיפוש ברשימת הערים המובנית או בהקלדת קואורדינטות; החיפוש נעשה במחשב שלך ושום דבר אינו נשלח."),
            ("התראות ותזכורות", "התראות הזמנים והתזכורות לאירועים מתוזמנות ב־Windows במחשב שלך ומוצגות כהתראות של Windows. דבר אינו נשלח לשרת.") if WIN_ALARMS_LIVE else
            ("תזכורות", "התזכורות לאירועים מתוזמנות ב־Windows במחשב שלך ומוצגות כהתראות של Windows. דבר אינו נשלח לשרת."),
            ("התקנה ועדכונים", "בהתקנה של קלוח ל־Windows מ־Microsoft Store, Microsoft מטפלת בהורדה, ברישיון ובעדכונים לפי <a href=\"https://privacy.microsoft.com/privacystatement\">הצהרת הפרטיות של Microsoft</a>; המפתח מקבל רק את הנתונים הכוללים והאנונימיים שהחנות מדווחת לכל מפתח (כמו מספר ההתקנות), ואם מאפשרים ל־Windows לשלוח נתוני אבחון — את הדיווחים של Microsoft על קריסות של האפליקציה."),
            ("יומן שגיאות", "אם האפליקציה נסגרת באופן בלתי צפוי, נכתב במחשב שלך יומן שגיאות קצר כדי שאפשר יהיה לאבחן את הבעיה. הוא לעולם אינו נשלח; אפשר לבחור לצרף אותו לפנייה לתמיכה."),
        ],
    ),
)

# ---------------------------------------------------------------- Android
APPS["android"] = dict(
    icon="kaluach-android-icon.png",
    en=dict(
        name="Kaluach for Android", plain="Kaluach for Android", topic="Kaluach for Android",
        status="In development · coming later to Google Play",
        # The about page links its status line to the tester section below.
        status_about="In development · <a href=\"#testers\">testers wanted</a> for Google Play",
        lead="The same calendars, zmanim and personal events as Kaluach for the Mac and iKaluach, on Android phones.",
        features=[
            "Civil Month and Hebrew Month views, Today and Go to Year.",
            "Jewish, Israeli and civil holidays, the weekly parsha and special Shabbatot, for Israel or the diaspora.",
            "Zmanim for any location, by the built-in shitot or your own.",
            "Personal events — azkarot, birthdays, anniversaries, one-time dates — with reminders.",
            "Zmanim alarms, never on Shabbat or Yom Tov.",
            "Print a year of Shabbatot and holidays, or export every day to a CSV spreadsheet.",
            "English and Hebrew. Move your events to and from Kaluach on the Mac, iPhone and Windows with the Kaluach events file.",
        ],
        requirements="Android 8.0 or later.",
        # The closed test on Google Play (12 testers for 14 days), after Requirements.
        testers='<h2 id="testers">Become a tester</h2>\n<p>Kaluach for Android is almost ready for Google Play. Before a new app can be published, Google requires a closed test: at least 12 people using it for 14 days in a row. You can help — and have Kaluach on your phone before anyone else.</p>\n<h3>What you need</h3>\n<ul>\n<li>An Android phone or tablet with Android 8.0 or later.</li>\n<li>A Google account — the one you use for Google Play on that phone.</li>\n</ul>\n<h3>What we ask</h3>\n<ul>\n<li>Keep Kaluach installed for at least two weeks.</li>\n<li>Open it now and then: check the zmanim, look up a date, add a yahrzeit or a birthday.</li>\n<li>Tell us what you find — anything wrong, confusing or missing.</li>\n</ul>\n<h3>How to join</h3>\n<ol>\n<li>Join the testers group: <a href="https://groups.google.com/g/kaluach-android-testers">Kaluach Android testers</a>. Sign in with the same Google account as on your phone.</li>\n<li>Open the <a href="https://play.google.com/apps/testing/com.abumami.kaluach">testing link</a>, on your phone or computer, and tap <strong>Become a tester</strong>. Use the same Google account.</li>\n<li>Install Kaluach from Google Play on your phone: <a href="https://play.google.com/store/apps/details?id=com.abumami.kaluach">Kaluach on Google Play</a>. This link works once you’ve done step 2; it may take a few minutes.</li>\n</ol>\n<p>Your email address is used only to give you access to the test, and members of the group can’t see each other. To stop testing, leave the group and uninstall Kaluach.</p>\n<p>Found something? Write to us through <a href="support/index.html">Support</a>.</p>\n\n',
        help=[],
        helpnote="Help is built into the app.",
        privacy=[
            ("lead", "Kaluach for Android collects no personal data. There are no accounts, no ads, no analytics and no tracking."),
            ("Where your data is kept", "Your events, saved locations, custom zmanim shitot, alarm settings and preferences are stored on your phone. The developer never receives them. A file you export (events, or a year’s CSV) goes only where you save or share it."),
            ("Android backup", "If backup is turned on for your phone, Android may include the app’s data in your own backup in your Google account, so that it can be restored on a new phone. That backup is handled by Google under the <a href=\"https://policies.google.com/privacy\">Google Privacy Policy</a>; the developer has no access to it."),
            ("Location", "Location is optional. If you choose <strong>Use My Location</strong>, the app asks for your approximate location and uses it on the phone to calculate zmanim. To show the place’s name, and when you search for a city, the app uses your phone’s place-search service (on most phones, provided by Google), which receives the text you type or the approximate position under its own privacy policy. The developer does not receive these requests."),
            ("Alarms and reminders", "Zmanim alarms and event reminders are scheduled on the phone itself. Nothing is sent to a server. The app asks permission to show notifications, and to set its alarms again after the phone restarts."),
        ],
    ),
    he=dict(
        name="קלוח לאנדרואיד", plain="קלוח לאנדרואיד", topic="קלוח לאנדרואיד",
        status="בפיתוח · בהמשך ב־Google Play",
        # The about page links its status line to the tester section below.
        status_about="בפיתוח · <a href=\"#testers\">דרושים בודקים</a> ל־Google Play",
        lead="אותו לוח, אותם זמני היום ואותם אירועים אישיים כמו בקלוח למק ובאיי־קלוח — בטלפונים עם אנדרואיד.",
        features=[
            "תצוגת חודש אזרחי וחודש עברי, היום ומעבר לשנה.",
            "חגים ומועדים יהודיים, ישראליים ואזרחיים, פרשת השבוע ושבתות מיוחדות, לארץ ישראל או לחוץ לארץ.",
            "זמני היום לכל מיקום, לפי השיטות המובנות או לפי שיטה משלך.",
            "אירועים אישיים — אזכרות, ימי הולדת, ימי נישואין ותאריכים חד־פעמיים — עם תזכורות.",
            "התראות זמנים, לעולם לא בשבת וביום טוב.",
            "הדפסת שנה של שבתות וחגים, או ייצוא של כל ימי השנה לגיליון CSV.",
            "עברית ואנגלית. העברת אירועים אל קלוח במק, באייפון וב־Windows וממנו, בקובץ האירועים של קלוח.",
        ],
        requirements="אנדרואיד 8.0 ומעלה.",
        testers='<h2 id="testers">הצטרפו לבודקים</h2>\n<p>קלוח לאנדרואיד כמעט מוכן ל־Google Play. לפני שאפליקציה חדשה מתפרסמת, Google דורשת בדיקה סגורה: לפחות 12 אנשים שמשתמשים בה 14 ימים ברציפות. אפשר לעזור — ולקבל את קלוח בטלפון לפני כולם.</p>\n<h3>מה צריך</h3>\n<ul>\n<li>טלפון או טאבלט עם אנדרואיד 8.0 ומעלה.</li>\n<li>חשבון Google — זה שמשמש ל־Google Play באותו טלפון.</li>\n</ul>\n<h3>מה מבקשים</h3>\n<ul>\n<li>להשאיר את קלוח מותקן לפחות שבועיים.</li>\n<li>לפתוח אותו מדי פעם: לבדוק זמנים, לחפש תאריך, להוסיף אזכרה או יום הולדת.</li>\n<li>לספר לנו מה מצאתם — כל דבר שגוי, מבלבל או חסר.</li>\n</ul>\n<h3>איך מצטרפים</h3>\n<ol>\n<li>מצטרפים לקבוצת הבודקים: <a href="https://groups.google.com/g/kaluach-android-testers">בודקי קלוח לאנדרואיד</a>. יש להתחבר עם אותו חשבון Google שבטלפון.</li>\n<li>פותחים את <a href="https://play.google.com/apps/testing/com.abumami.kaluach">קישור הבדיקה</a>, בטלפון או במחשב, ומאשרים את ההצטרפות לבדיקה. יש להשתמש באותו חשבון Google.</li>\n<li>מתקינים את קלוח מ־Google Play בטלפון: <a href="https://play.google.com/store/apps/details?id=com.abumami.kaluach">קלוח ב־Google Play</a>. הקישור עובד אחרי שלב 2; לפעמים זה לוקח כמה דקות.</li>\n</ol>\n<p>כתובת הדוא״ל שלכם משמשת רק כדי לתת לכם גישה לבדיקה, וחברי הקבוצה אינם רואים זה את זה. כדי להפסיק לבדוק, עוזבים את הקבוצה ומסירים את קלוח.</p>\n<p>מצאתם משהו? כתבו לנו דרך <a href="../support/he/index.html">התמיכה</a>.</p>\n\n',
        help=[],
        helpnote="העזרה כלולה באפליקציה.",
        privacy=[
            ("lead", "קלוח לאנדרואיד אינו אוסף מידע אישי. אין חשבונות משתמש, אין פרסומות, אין ניתוח שימוש ואין מעקב."),
            ("היכן נשמר המידע שלך", "האירועים, המיקומים השמורים, שיטות הזמנים המותאמות, הגדרות ההתראות וההעדפות נשמרים בטלפון שלך. המפתח אינו מקבל אותם לעולם. קובץ שמייצאים (אירועים, או גיליון CSV של שנה) נשמר או משותף רק לפי בחירתך."),
            ("גיבוי של אנדרואיד", "אם הגיבוי מופעל בטלפון שלך, אנדרואיד עשוי לכלול את נתוני האפליקציה בגיבוי שלך בחשבון Google שלך, כדי שאפשר יהיה לשחזר אותם בטלפון חדש. הגיבוי מטופל על ידי Google לפי <a href=\"https://policies.google.com/privacy\">מדיניות הפרטיות של Google</a>; למפתח אין גישה אליו."),
            ("מיקום", "המיקום הוא רשות. אם בוחרים <strong>השתמש במיקום שלי</strong>, האפליקציה מבקשת את המיקום המשוער שלך ומשתמשת בו בטלפון לחישוב הזמנים. כדי להציג את שם המקום, ובחיפוש עיר, האפליקציה משתמשת בשירות חיפוש המקומות של הטלפון (ברוב הטלפונים — של Google), שמקבל את הטקסט שמקלידים או את המיקום המשוער לפי מדיניות הפרטיות שלו. המפתח אינו מקבל בקשות אלה."),
            ("התראות ותזכורות", "התראות הזמנים והתזכורות לאירועים מתוזמנות בטלפון עצמו. דבר אינו נשלח לשרת. האפליקציה מבקשת הרשאה להציג התראות, ולקבוע מחדש את ההתראות שלה אחרי הפעלה מחדש של הטלפון."),
        ],
    ),
)

# Sections shared by every privacy statement (after the app's own).
COMMON_PRIVACY = dict(
    en=[
        ("Contact form", "If you write through the <a href=\"{support}\">support page</a>, the name, email address and message you enter are delivered to the developer by the form service Web3Forms and used only to answer you."),
        ("Children", "The app collects no data from anyone, including children."),
        ("Changes", "If this policy changes, the new version will be posted on this page."),
    ],
    he=[
        ("טופס יצירת קשר", "בפנייה דרך <a href=\"{support}\">דף התמיכה</a>, השם, כתובת הדוא״ל וההודעה שמזינים נמסרים למפתח באמצעות שירות הטפסים Web3Forms, ומשמשים רק למתן תשובה."),
        ("ילדים", "האפליקציה אינה אוספת מידע מאף אחד, כולל ילדים."),
        ("שינויים", "אם המדיניות תשתנה, הגרסה החדשה תפורסם בדף זה."),
    ],
)
