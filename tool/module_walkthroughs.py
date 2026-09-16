"""Authored module explanations in English, Dari and Pashto. Native review pending."""
import json
WALKTHROUGHS = json.loads(r'''{
  "web-design": [
    {
      "en": "Read this as a document, not a calculation. main contains the important content. h1 names the page. The link points to the section whose id is hours; selecting it moves to that section. Tags describe meaning and are not printed. A missing matching id breaks this navigation.",
      "fa": "این نمونه سند است، نه محاسبه. main محتوای اصلی را در بر می‌گیرد و h1 نام صفحه را مشخص می‌کند. پیوند به بخشی می‌رود که id آن hours است. تگ‌ها معنی بخش‌ها را مشخص می‌کنند و نمایش داده نمی‌شوند. اگر id مطابق نباشد، پیوند به محل درست نمی‌رود.",
      "ps": "دا نمونه سند دی، محاسبه نه ده. main اصلي منځپانګه رانغاړي او h1 د پاڼې نوم ټاکي. تړونی هغې برخې ته ځي چې id یې hours دی. ټګونه د برخو مانا ټاکي او نه ښکاري. که id برابر نه وي، تړونی سم ځای ته نه ځي."
    },
    {
      "en": "The body rule chooses the font, line spacing, and outer margin. main limits reading width and centres the content with automatic inline margins. The focus rule draws an outline when a link has visible focus. Tab through links to check it; do not remove the outline just for appearance.",
      "fa": "دستور body نوع خط، فاصلهٔ سطرها و حاشیه را تعیین می‌کند. main عرض متن را محدود و با حاشیهٔ خودکار محتوا را در وسط قرار می‌دهد. دستور focus دور پیوند فعال خط می‌کشد. با کلید Tab پیوندها را بررسی کنید؛ این نشانه را تنها برای زیبایی حذف نکنید.",
      "ps": "د body قاعده لیکبڼه، د کرښو واټن او بهرنۍ څنډه ټاکي. main د متن پلنوالی محدودوي او په اتومات څنډو یې منځ ته راولي. د focus قاعده د فعال تړوني شاوخوا کرښه رسموي. په Tab تړوني وګورئ؛ یوازې د ښکلا لپاره دا نښه مه لرې کوئ."
    },
    {
      "en": "This is a CSS rule for an existing cards container, not a complete HTML page. Grid creates columns and gap separates cards. Each column aims for at least 16rem but can shrink to the container width. Narrow the window: cards should move to new rows instead of forcing horizontal scrolling.",
      "fa": "این قاعدهٔ CSS برای ظرف موجود cards است، نه یک صفحهٔ کامل. Grid ستون می‌سازد و gap میان کارت‌ها فاصله می‌گذارد. هر ستون تا حد امکان حداقل 16rem عرض می‌گیرد، اما از عرض ظرف بزرگ‌تر نمی‌شود. پنجره را باریک کنید؛ کارت‌ها باید به سطر بعد بروند.",
      "ps": "دا د موجود cards لوښي لپاره د CSS قاعده ده، بشپړه HTML پاڼه نه ده. Grid ستنې جوړوي او gap کارتونه بېلوي. هره ستنه تر شونې بریده لږ تر لږه 16rem پلنوالی اخلي، خو د لوښي تر پلنوالي نه اوړي. کړکۍ تنګه کړئ؛ کارتونه باید نوو کتارونو ته لاړ شي."
    },
    {
      "en": "The label's for value matches the input's id, so selecting the label focuses the field. required participates in browser form validation. aria-describedby connects the help paragraph to the field. These rules improve interaction; they do not save a student's name or replace server validation.",
      "fa": "مقدار for در label با id ورودی مطابق است؛ انتخاب نام فیلد، ورودی را فعال می‌کند. required در بررسی فورم توسط مرورگر سهم دارد. aria-describedby متن رهنما را به فیلد وصل می‌کند. این‌ها نام شاگرد را ذخیره نمی‌کنند و جای بررسی معلومات در سرور را نمی‌گیرند.",
      "ps": "د label د for ارزښت د input له id سره برابر دی؛ د نوم ټاکل خانه فعاله کوي. required د براوزر د فورم په کتنه کې کارېږي. aria-describedby د مرستې متن له خانې سره تړي. دا قواعد د زده کوونکي نوم نه ساتي او د سرور د معلوماتو کتنه نه بدلوي."
    },
    {
      "en": "lang identifies the language; dir sets the reading direction. The article reads right to left, while the code block explicitly stays left to right. Direction is not translation: English text will remain English. Check punctuation, numbers, and keyboard focus using real Dari and Pashto sentences.",
      "fa": "lang زبان و dir جهت خواندن را مشخص می‌کند. متن article از راست به چپ است، اما بخش کود صریحاً چپ به راست می‌ماند. جهت دادن ترجمه نیست؛ متن انگلیسی خودبه‌خود دری نمی‌شود. علامت‌ها، عددها و حرکت صفحه‌کلید را با جمله‌های واقعی دری و پشتو بررسی کنید.",
      "ps": "lang ژبه او dir د لوستلو لوری ټاکي. article له ښي چپ ته لوستل کېږي، خو کوډ په څرګنده له کیڼ ښي ته پاتې کېږي. لوری ټاکل ژباړه نه ده؛ انګلیسي متن په خپله نه ژباړل کېږي. نښې، شمېرې او د کیبورډ حرکت په واقعي دري او پښتو جملو وازمویئ."
    },
    {
      "en": "The root declarations name reusable design values. A card reads those values with var(), so changing --space updates its padding without editing every card. This does not prove usability. Ask someone to find opening hours and observe whether the layout helps them complete that task.",
      "fa": "تعریف‌های root مقدارهای قابل استفادهٔ دوباره را نام‌گذاری می‌کنند. کارت با var() آن‌ها را می‌خواند؛ تغییر --space فاصلهٔ داخلی را بدون ویرایش همهٔ کارت‌ها عوض می‌کند. این کار به‌تنهایی کاربردپذیری را ثابت نمی‌کند. از یک نفر بخواهید ساعت کار را پیدا کند و مسیرش را مشاهده کنید.",
      "ps": "د root تعریفونه بیا کارېدونکو ارزښتونو ته نومونه ورکوي. کارت یې په var() لولي؛ د --space بدلول د ټولو کارتونو له سمولو پرته دنننی واټن بدلوي. دا په خپله د کارولو اسانتیا نه ثابتوي. له چا وغواړئ د کار وخت پیدا کړي او لاره یې وګورئ."
    }
  ],
  "web-development": [
    {
      "en": "The first block is a request from a client to a local server; the second is its response. GET asks to read books. Status 200 indicates success and Content-Type describes the body as JSON. The array contains one book. This transcript does not start a server or draw a page.",
      "fa": "بخش اول درخواست مشتری به سرور محلی و بخش دوم جواب آن است. GET خواندن کتاب‌ها را می‌خواهد. وضعیت 200 موفقیت را نشان می‌دهد و Content-Type نوع بدنه را JSON معرفی می‌کند. آرایه یک کتاب دارد. این متن نمونه، سرور را راه‌اندازی نمی‌کند و صفحه نمی‌سازد.",
      "ps": "لومړۍ برخه د مشتری غوښتنه محلي سرور ته او دویمه یې ځواب دی. GET د کتابونو لوستل غواړي. 200 بریا ښيي او Content-Type د بدن ډول JSON ټاکي. لړۍ یو کتاب لري. دا لیکل شوې نمونه سرور نه پیلوي او پاڼه نه رسموي."
    },
    {
      "en": "fetch requests the local API, then await waits for its response without blocking the whole browser. A failed HTTP status triggers the explicit error. Only a successful response is parsed as JSON. Network failure can reject fetch itself, so the surrounding screen must also handle that failure and keep a retry action.",
      "fa": "fetch محلي API را صدا می‌زند و await منتظر جواب می‌ماند، بدون آن‌که تمام مرورگر را بند کند. وضعیت ناموفق خطای مشخص را ایجاد می‌کند. فقط جواب موفق به JSON تبدیل می‌شود. خود fetch هم ممکن است ناکام شود؛ صفحه باید این خطا و امکان تلاش دوباره را مدیریت کند.",
      "ps": "fetch محلي API رابولي او await ځواب ته انتظار کوي، خو ټول براوزر نه بندوي. ناکام HTTP حالت څرګنده تېروتنه جوړوي. یوازې بریالی ځواب په JSON لوستل کېږي. خپله fetch هم ناکامېدای شي؛ پاڼه باید دا تېروتنه او بیا هڅه اداره کړي."
    },
    {
      "en": "books owns each book's identity and title. loans stores a reference to that identity instead of copying the title. One book can appear in several historical loans. The foreign key alone does not prevent two active loans; that business rule needs an additional constraint or transactional service check.",
      "fa": "جدول books شناسه و عنوان هر کتاب را نگه می‌دارد. loans به‌جای کاپی عنوان، به همان شناسه اشاره می‌کند. یک کتاب می‌تواند چند سابقهٔ امانت داشته باشد. کلید خارجی به‌تنهایی دو امانت فعال را منع نمی‌کند؛ این قاعده به محدودیت اضافی یا بررسی در معامله ضرورت دارد.",
      "ps": "books د هر کتاب پېژند او نوم ساتي. loans د نوم د کاپي پر ځای هماغه پېژند ته اشاره ساتي. یو کتاب په څو پخوانیو پورونو کې راتلای شي. بهرنی کلی یوازې دوه فعال پورونه نه منع کوي؛ دې قاعدې ته اضافي محدودیت یا معاملاتي کتنه پکار ده."
    },
    {
      "en": "createElement creates an empty span. Assigning textContent inserts a title as text, so angle brackets in a user's title are not interpreted as HTML. No element is visible until it is attached to the page. This protects this insertion point; other inputs and authorization still require their own checks.",
      "fa": "createElement یک span خالی می‌سازد. textContent عنوان را به صورت متن وارد می‌کند؛ علامت‌های HTML در عنوان کاربر به کود صفحه تبدیل نمی‌شوند. عنصر تا به صفحه وصل نشود دیده نمی‌شود. این روش فقط همین محل درج را محافظت می‌کند؛ ورودی‌ها و صلاحیت‌ها بررسی جدا می‌خواهند.",
      "ps": "createElement تش span جوړوي. textContent نوم د متن په توګه ورزیاتوي؛ د کارن د نوم HTML نښې د پاڼې کوډ نه ګرځي. عنصر تر پاڼې سره له نښلېدو مخکې نه ښکاري. دا یوازې همدا د ورزیاتولو ځای ساتي؛ نورې داخلې او صلاحیتونه جلا کتنه غواړي."
    },
    {
      "en": "The operation object names one intended loan. Its id stays the same during a retry. Store that id and the loan together, so a second request returns the earlier result rather than lending twice. The comment states a requirement, not an implementation; test the transaction failing between the two writes.",
      "fa": "شیء operation یک امانت مورد نظر را مشخص می‌کند. id آن هنگام تلاش دوباره ثابت می‌ماند. شناسه و امانت را یک‌جا ذخیره کنید تا درخواست دوم نتیجهٔ قبلی را بگیرد و ثبت تکراری نشود. یادداشت نمونه تنها نیاز را بیان می‌کند؛ ناکامی میان دو ذخیره را آزمایش کنید.",
      "ps": "operation یو غوښتل شوی پور ټاکي. id یې د بیا هڅې پر مهال هماغه وي. پېژند او پور یوځای وساتئ، څو دویمه غوښتنه پخوانۍ پایله واخلي او پور تکرار نه شي. د نمونې یادونه یوازې اړتیا بیانوي؛ د دوو لیکنو ترمنځ ناکامي وازمویئ."
    },
    {
      "en": "This tree is a suggested separation of responsibilities. domain decides loan rules, HTTP translates requests, storage persists records, and public contains the screen. It is not executable code. Start with one loan rule and test it without HTTP, then connect adapters; folder names alone do not create clean architecture.",
      "fa": "این ساختار پوشه‌ها مسئولیت‌ها را جدا می‌کند: domain قواعد امانت، HTTP تبدیل درخواست، storage ذخیره و public صفحه را نگه می‌دارد. این متن قابل اجرا نیست. نخست یک قاعده را بدون HTTP آزمایش کنید و بعد بخش‌ها را وصل کنید؛ نام پوشه به‌تنهایی معماری درست نمی‌سازد.",
      "ps": "دا د پوښیو جوړښت دندې بېلوي: domain د پور قواعد، HTTP غوښتنې، storage ساتنه او public پاڼه لري. دا اجرا کېدونکی کوډ نه دی. لومړی یوه قاعده له HTTP پرته وازمویئ، بیا برخې ونښلوئ؛ د پوښۍ نوم په خپله سمه معماري نه جوړوي."
    }
  ],
  "java": [
    {
      "en": "Save this complete program as Main.java. main is the starting method. total begins at zero; the loop reads 10, 20, then 30 and changes total to 10, 30, then 60. println displays 60 once, after the loop. A mismatched public class and filename prevents compilation.",
      "fa": "این پروگرام کامل را در Main.java ذخیره کنید. main محل آغاز است. total از صفر شروع می‌شود؛ حلقه 10، 20 و 30 را می‌خواند و مجموع به 10، 30 و 60 می‌رسد. println پس از حلقه یک بار 60 را نشان می‌دهد. نام صنف عمومی و فایل باید مطابق باشند.",
      "ps": "دا بشپړ پروګرام په Main.java کې وساتئ. main د پیل مېتود دی. total له صفره پیلېږي؛ کړۍ 10، 20 او 30 لولي او مجموعه 10، 30 او 60 کېږي. println له کړۍ وروسته یو ځل 60 ښيي. د عام ټولګي او فایل نومونه باید برابر وي."
    },
    {
      "en": "The constructor checks the proposed quantity before storing it. A negative value throws an exception, so an invalid Stock is not created. private prevents ordinary outside code from directly changing quantity. The method reads it without exposing a setter. This class fragment needs a caller to create and inspect an object.",
      "fa": "سازنده پیش از ذخیره، تعداد را بررسی می‌کند. مقدار منفی خطا می‌دهد و Stock نامعتبر ساخته نمی‌شود. private تغییر مستقیم quantity را از بیرون منع می‌کند. متود مقدار را بدون راه تغییر مستقیم می‌خواند. این بخش صنف به کود دیگری برای ساختن و بررسی شیء ضرورت دارد.",
      "ps": "جوړوونکی د ساتلو مخکې شمېر ګوري. منفي ارزښت استثنا جوړوي او ناسم Stock نه جوړېږي. private له بهر څخه د quantity مستقیم بدلون منع کوي. مېتود یې ارزښت لولي، خو د بدلولو لاره نه ورکوي. دا برخه د شي د جوړولو او کتلو لپاره بل کوډ غواړي."
    },
    {
      "en": "The map connects text keys with integer quantities. put creates Notebook with 5. merge finds that key and adds 2 using Integer::sum, leaving 7. It does not add a second Notebook entry. This fragment prints nothing; inspect stock.get(\"Notebook\") in a method to check the stored result.",
      "fa": "نقشه کلید متنی را به تعداد صحیح وصل می‌کند. put برای Notebook مقدار 5 می‌گذارد. merge همان کلید را پیدا و با Integer::sum مقدار 2 اضافه می‌کند؛ نتیجه 7 است، نه یک ثبت دوم. این بخش چیزی نمایش نمی‌دهد؛ در یک متود stock.get(\"Notebook\") را بررسی کنید.",
      "ps": "نقشه متني کلي له صحیح شمېر سره تړي. put د Notebook لپاره 5 ږدي. merge هماغه کلی مومي او په Integer::sum دوه ورزیاتوي؛ پایله 7 ده، دویم ثبت نه دی. دا برخه هېڅ نه ښيي؛ په مېتود کې stock.get(\"Notebook\") وګورئ."
    },
    {
      "en": "Files.lines opens a stream from items.txt. filter removes blank lines and forEach prints those remaining. The try-with-resources block closes the stream even on failure. A missing file still needs error handling. Create a fixture with an empty line between two names and expect only the names to print.",
      "fa": "Files.lines جریان خط‌ها را از items.txt باز می‌کند. filter خط‌های خالی را حذف و forEach باقی را نمایش می‌دهد. try-with-resources حتی هنگام ناکامی جریان را می‌بندد. فایل گم‌شده هنوز مدیریت خطا می‌خواهد. میان دو نام یک خط خالی بگذارید؛ فقط نام‌ها باید نمایش داده شوند.",
      "ps": "Files.lines له items.txt څخه د کرښو بهیر پرانیزي. filter تشې کرښې لرې کوي او forEach پاتې کرښې ښيي. try-with-resources بهیر حتی د ناکامۍ پر مهال تړي. ورک فایل بیا هم د تېروتنې اداره غواړي. د دوو نومونو ترمنځ تشه کرښه کېږدئ؛ یوازې نومونه باید ښکاره شي."
    },
    {
      "en": "stream creates a processing pipeline; sorted orders the three names and toList collects a new result. The original list is unchanged. The assertion checks the count, not alphabetical correctness, and Java assertions require enabling. Add an explicit check of the expected order rather than treating a size check as a complete test.",
      "fa": "stream مسیر پردازش می‌سازد؛ sorted سه نام را مرتب و toList نتیجهٔ تازه جمع می‌کند. فهرست اولیه تغییر نمی‌کند. assertion فقط تعداد را بررسی می‌کند و در جاوا به فعال‌سازی ضرورت دارد. ترتیب مورد انتظار را هم بررسی کنید؛ درست بودن تعداد، درستی ترتیب را ثابت نمی‌کند.",
      "ps": "stream د پروسس لړۍ جوړوي؛ sorted درې نومونه مرتبوي او toList نوې پایله راټولوي. لومړنی لېست نه بدلېږي. assertion یوازې شمېر ګوري او په جاوا کې فعالول غواړي. تمه شوی ترتیب هم وګورئ؛ سم شمېر د ترتیب سموالی نه ثابتوي."
    },
    {
      "en": "Report receives its repository through the constructor. count asks for names and returns their number; it does not know whether they came from memory or a file. Test with a repository returning two names and expect 2. Replacing storage should not require rewriting the counting rule.",
      "fa": "Report مخزن را از سازنده می‌گیرد. count نام‌ها را می‌خواهد و تعدادشان را برمی‌گرداند؛ نمی‌داند از حافظه آمده‌اند یا فایل. با مخزنی که دو نام می‌دهد آزمایش کنید و 2 انتظار داشته باشید. تغییر ذخیره‌گاه نباید بازنویسی قاعدهٔ شمارش را لازم سازد.",
      "ps": "Report خپل زېرمتون له جوړوونکي اخلي. count نومونه غواړي او شمېر یې ورکوي؛ نه پوهېږي چې له حافظې راغلي که له فایل. له داسې زېرمتون سره یې وازمویئ چې دوه نومونه ورکوي؛ 2 تمه وکړئ. د ساتنې بدلول باید د شمېرلو قاعده بدله نه کړي."
    }
  ],
  "kotlin": [
    {
      "en": "String? allows name to be absent. Because it is null, the safe call does not run uppercase. The Elvis operator supplies Guest, which println displays. With \"Amina\" instead, AMINA is displayed. Do not replace the safe call with !! merely to silence the compiler; that would fail for null.",
      "fa": "String? اجازه می‌دهد name موجود نباشد. چون null است، فراخوانی امن uppercase اجرا نمی‌شود. عملگر Elvis مقدار Guest می‌دهد و println آن را نشان می‌دهد. با \"Amina\" نتیجه AMINA است. برای خاموش کردن خطای مترجم، !! نگذارید؛ برای null ناکام می‌شود.",
      "ps": "String? اجازه ورکوي چې name نه وي. ځکه null دی، خوندي uppercase نه اجرا کېږي. Elvis د Guest ارزښت ورکوي او println یې ښيي. له \"Amina\" سره AMINA ښکاري. یوازې د کمپایلر د چوپولو لپاره !! مه کاروئ؛ له null سره ناکامېږي."
    },
    {
      "en": "filter keeps values strictly greater than 10, so the intermediate list contains 20 and 30. fold starts at 0, adds 20, then 30, giving 50. total stores 50 but is not printed. Changing > to >= includes 10 and changes the result to 60.",
      "fa": "filter مقدارهای بزرگ‌تر از 10 را نگه می‌دارد؛ فهرست میانی 20 و 30 دارد. fold از صفر شروع، 20 و بعد 30 را جمع می‌کند؛ نتیجه 50 است. total آن را ذخیره می‌کند ولی نمایش نمی‌دهد. تغییر > به >= مقدار 10 را شامل می‌کند و نتیجه 60 می‌شود.",
      "ps": "filter یوازې له 10 لوی مقدارونه ساتي؛ منځنی لېست 20 او 30 لري. fold له صفره پیل، 20 او بیا 30 جمع کوي؛ نتیجه 50 ده. total یې ساتي خو نه یې ښيي. د > پر ځای >= لیکل 10 هم شاملوي او نتیجه 60 کوي."
    },
    {
      "en": "SaveResult names the allowed outcomes of saving. Saved carries an id; Rejected carries a reason. Declaring them does not save anything. A caller should handle both outcomes explicitly with when. This prevents a failure reason from being confused with a successful record identifier.",
      "fa": "SaveResult حالت‌های ممکن ذخیره را نام می‌دهد. Saved شناسه و Rejected دلیل رد را نگه می‌دارد. تعریف آن‌ها چیزی ذخیره نمی‌کند. فراخواننده باید با when هر دو حالت را جدا مدیریت کند تا دلیل ناکامی با شناسهٔ ثبت موفق اشتباه نشود.",
      "ps": "SaveResult د ساتلو ممکنې پایلې نوموي. Saved پېژند او Rejected د رد دلیل لري. تعریفول یې څه نه ساتي. رابلونکی باید په when دواړه حالتونه جلا اداره کړي، څو د ناکامۍ دلیل له بریالي پېژند سره ګډ نه شي."
    },
    {
      "en": "Repository<T> can return a list of a chosen type without hard-coding one record type. The extension trims outside spaces and lowercases text: \" Kabul \" becomes \"kabul\". It returns a new string; it does not edit the original. Decide whether lowercasing is appropriate before using it for personal names.",
      "fa": "Repository<T> فهرستی از نوع انتخاب‌شده را می‌دهد. تابع افزوده فاصله‌های بیرونی را حذف و حروف را کوچک می‌کند؛ \" Kabul \" به \"kabul\" تبدیل می‌شود. رشتهٔ تازه برمی‌گرداند و اصل را تغییر نمی‌دهد. پیش از کاربرد برای نام اشخاص، مناسب بودن تغییر حروف را بررسی کنید.",
      "ps": "Repository<T> د ټاکلي ډول لېست ورکوي. غځېدلې دنده بهرنۍ تشې لرې کوي او توري کوچني کوي؛ \" Kabul \" په \"kabul\" بدلېږي. نوی متن ورکوي او اصل نه بدلوي. د اشخاصو د نومونو لپاره لومړی د تورو د بدلولو مناسبت وڅېړئ."
    },
    {
      "en": "suspend permits a function to suspend within a coroutine. loadNames delegates to the repository and returns its list. This declaration neither launches a coroutine nor chooses a background thread. A caller must own the coroutine's lifetime, handle failure, and cancel work when its result is no longer needed.",
      "fa": "suspend اجازه می‌دهد تابع در coroutine معلق شود. loadNames کار را به مخزن می‌دهد و فهرستش را برمی‌گرداند. این تعریف نه coroutine آغاز می‌کند و نه رشتهٔ پس‌زمینه انتخاب می‌کند. فراخواننده باید عمر کار، ناکامی و لغو نتیجهٔ دیگر لازم‌نبوده را مدیریت کند.",
      "ps": "suspend تابع ته په coroutine کې د تم کېدو اجازه ورکوي. loadNames کار زېرمتون ته سپاري او لېست یې ورکوي. دا تعریف نه coroutine پیلوي او نه شالید تار ټاکي. رابلونکی باید د کار عمر، ناکامي او د نالازمې پایلې لغوه کول اداره کړي."
    },
    {
      "en": "validStock returns true for zero and positive values, false for negatives. The two checks cover the boundary zero and the invalid value -1. They display nothing when successful. A failing check throws. Add a positive case and explain why zero is valid for an item that is temporarily sold out.",
      "fa": "validStock صفر و عدد مثبت را درست و منفی را نادرست می‌داند. دو بررسی، مرز صفر و مقدار نامعتبر -1 را پوشش می‌دهند. هنگام موفقیت چیزی نمایش نمی‌دهند؛ بررسی ناکام خطا می‌دهد. یک مقدار مثبت اضافه کنید و توضیح بدهید چرا موجودی صفر معتبر است.",
      "ps": "validStock صفر او مثبت عدد سم او منفي ناسم ګڼي. دوه کتنې د صفر پوله او ناسم -1 پوښي. د بریا پر مهال هېڅ نه ښيي؛ ناکامه کتنه استثنا جوړوي. مثبت حالت ورزیات کړئ او ووایئ چې ولې صفر موجودي معتبره ده."
    }
  ],
  "android": [
    {
      "en": "Android calls onCreate when creating this activity. super performs the parent's setup; setContent supplies a Compose interface containing Salam. This is a project fragment, not a whole installable app. It needs the indicated import and a configured Compose project. Recreating an activity is not the same as reinstalling the app.",
      "fa": "اندروید هنگام ساخت activity، onCreate را صدا می‌زند. super آماده‌سازی والد را انجام می‌دهد و setContent رابط Compose با Salam می‌سازد. این بخش پروژه است، نه برنامهٔ کامل قابل نصب. import ذکرشده و پروژهٔ آمادهٔ Compose لازم است. ساخت دوبارهٔ activity با نصب دوباره فرق دارد.",
      "ps": "اندروید د activity د جوړولو پر مهال onCreate رابولي. super د مورني ټولګي چمتووالی کوي او setContent د Salam لرونکی Compose مخ جوړوي. دا د پروژې برخه ده، بشپړ نصبېدونکی اپ نه دی. یاد import او چمتو Compose پروژه غواړي. د activity بیا جوړول بیا نصبول نه دي."
    },
    {
      "en": "count starts at zero. A button press increases it, and Compose redraws the label using the changed state. rememberSaveable can restore supported small UI state across recreation; it is not a database. After two presses expect Count: 2. Test recreation separately from a normal redraw.",
      "fa": "count از صفر شروع می‌شود. فشار دکمه آن را زیاد می‌کند و Compose نوشته را با حالت تازه نمایش می‌دهد. rememberSaveable حالت کوچک پشتیبانی‌شده را پس از بازسازی برمی‌گرداند؛ دیتابیس نیست. پس از دو فشار Count: 2 انتظار داشته باشید. بازسازی را جدا آزمایش کنید.",
      "ps": "count له صفره پیلېږي. د تڼۍ وهل یې زیاتوي او Compose نوم له نوي حالت سره بیا رسموي. rememberSaveable د بیا جوړېدو پر مهال وړوکی ملاتړ شوی حالت راګرځولای شي؛ ډیټابېس نه دی. له دوو وهلو وروسته Count: 2 تمه وکړئ. بیا جوړېدل جلا وازمویئ."
    },
    {
      "en": "UiState describes what a screen can show: a list and an optional error. Empty names and no error do not automatically mean loading; add an explicit loading field if needed. A ViewModel owns changes and the screen observes them. The comment does not implement navigation or StateFlow collection.",
      "fa": "UiState وضعیت قابل نمایش را توضیح می‌دهد: فهرست و خطای اختیاری. فهرست خالی بدون خطا خودبه‌خود به معنی بارگذاری نیست؛ اگر لازم است حالت بارگذاری جدا اضافه کنید. ViewModel تغییرها را مالک است و صفحه مشاهده می‌کند. یادداشت، مسیریابی و مشاهدهٔ StateFlow را پیاده نکرده است.",
      "ps": "UiState د پردې حالت بیانوي: لېست او اختیاري تېروتنه. تش لېست بې تېروتنې په خپله د لوډ کېدو مانا نه لري؛ اړتیا وي جلا loading حالت ورزیات کړئ. ViewModel بدلونونه اداره کوي او پرده یې څاري. یادونه navigation او د StateFlow څارنه نه پلي کوي."
    },
    {
      "en": "Entity marks Note as stored data and PrimaryKey identifies each row. The DAO query orders notes by id and exposes updates through Flow. An empty table yields an empty list. The fragment lacks a RoomDatabase and write methods; connect those before claiming persistence across restart.",
      "fa": "Entity، Note را معلومات ذخیره‌شدنی معرفی و PrimaryKey هر سطر را مشخص می‌کند. پرس‌وجوی DAO یادداشت‌ها را با id مرتب و تغییرها را از Flow می‌دهد. جدول خالی فهرست خالی می‌دهد. RoomDatabase و متودهای نوشتن هنوز لازم اند؛ پیش از آن دوام ذخیره را ادعا نکنید.",
      "ps": "Entity د Note ساتل کېدونکي معلومات ټاکي او PrimaryKey هر کتار پېژني. د DAO پوښتنه یادښتونه په id مرتبوي او بدلونونه په Flow ورکوي. تش جدول تش لېست ورکوي. RoomDatabase او لیکلو مېتودونه لا پکار دي؛ تر هغې د بیا پرانیستلو ساتنه مه بشپړه ګڼئ."
    },
    {
      "en": "These comments describe an export state machine. queued becomes running, then either succeeded or failed. Repeating the same operation id must not create another ledger entry. Build the transitions and store their results; the arrows alone do not schedule work or request permission. Ask only for permissions the chosen export actually needs.",
      "fa": "این یادداشت‌ها حالت‌های خروجی‌گیری را نشان می‌دهند: انتظار، اجرا و سپس موفقیت یا ناکامی. تکرار همان شناسه نباید ثبت مالی دوم بسازد. تغییر حالت و نتیجه را ذخیره کنید؛ فلش‌ها کار را زمان‌بندی نمی‌کنند. فقط صلاحیتی را بخواهید که روش خروجی‌گیری واقعاً لازم دارد.",
      "ps": "دا یادونې د صادرولو حالتونه ښيي: انتظار، اجرا او بیا بریا یا ناکامي. د هماغه پېژند تکرار باید دویم مالي ثبت جوړ نه کړي. د حالت بدلون او پایلې وساتئ؛ غشي کار نه مهالویشوي. یوازې هغه اجازه وغواړئ چې ټاکلی صادرول ورته اړتیا لري."
    },
    {
      "en": "The validator rejects empty and whitespace-only names. The test passes an empty string and expects false. It does not test the whole screen or packaging. Add a whitespace case, a real name, and an interaction test verifying that an invalid form keeps its input and shows a useful message.",
      "fa": "بررسی‌کننده نام خالی یا فقط فاصله را رد می‌کند. آزمون رشتهٔ خالی می‌دهد و false انتظار دارد. این آزمون تمام صفحه یا بستهٔ نصب را بررسی نمی‌کند. فاصله، نام معتبر و آزمونی اضافه کنید که فورم نامعتبر ورودی را نگه دارد و پیام مفید نشان بدهد.",
      "ps": "کتونکی تش او یوازې تشې لرونکی نوم ردوي. ازموینه تش متن ورکوي او false غواړي. دا ټوله پرده یا نصب نه ازمويي. تشې، سم نوم او د فورم داسې ازموینه ورزیاته کړئ چې ناسمې داخلې وساتي او ګټور پیغام وښيي."
    }
  ],
  "ios": [
    {
      "en": "SwiftUI supplies the interface types. @main identifies the app entry point, WindowGroup creates its scene, and Text displays Salam. Put this in an appropriately configured Xcode app target. It is not a Python program and cannot run in the Python editor. The first screen should work without a network request.",
      "fa": "SwiftUI نوع‌های رابط را فراهم می‌کند. @main نقطهٔ آغاز، WindowGroup صحنه و Text متن Salam را می‌سازد. این کود را در هدف آمادهٔ برنامهٔ Xcode بگذارید. کود پایتون نیست و در ویرایشگر پایتون اجرا نمی‌شود. صفحهٔ اول باید بدون درخواست اینترنت کار کند.",
      "ps": "SwiftUI د مخ ډولونه برابروي. @main د پیل ځای، WindowGroup صحنه او Text د Salam متن جوړوي. دا په چمتو Xcode app target کې کېږدئ. پایتون نه دی او د پایتون په سمونګر کې نه چلېږي. لومړۍ پرده باید بې انټرنېټه کار وکړي."
    },
    {
      "en": "@State stores the counter for this view's identity. The button reads count for its label and increments it on each press, causing the view to update. Two presses show Count: 2. State is not durable storage; closing and relaunching needs a separate persistence design if the count must survive.",
      "fa": "@State شمارنده را برای هویت این نما نگه می‌دارد. دکمه count را در نوشته می‌خواند و با هر فشار زیاد می‌کند؛ نما تازه می‌شود. دو فشار Count: 2 می‌دهد. این ذخیرهٔ دایمی نیست؛ برای باقی ماندن پس از بازشدن دوباره، ذخیره‌سازی جدا لازم است.",
      "ps": "@State د دې لید د هویت لپاره شمېرونکی ساتي. تڼۍ count په نوم کې لولي او هر وهل یې زیاتوي؛ لید تازه کېږي. دوه وهل Count: 2 ورکوي. دا دایمي ساتنه نه ده؛ له بیا پرانیستلو وروسته پاتې کېدل جلا ساتنه غواړي."
    },
    {
      "en": "The stack owns navigation. List makes two rows; each NavigationLink opens a Text detail for that row's name. Using the name as identity works here only because the names are unique. Real editable records should use stable IDs, so renaming an item does not change which record a route means.",
      "fa": "stack مسیریابی را مدیریت می‌کند. List دو سطر می‌سازد و هر NavigationLink جزئیات همان نام را باز می‌کند. استفاده از نام به‌عنوان شناسه این‌جا فقط به دلیل یکتا بودن نام‌ها درست است. ثبت قابل ویرایش شناسهٔ ثابت می‌خواهد تا تغییر نام مسیر را عوض نکند.",
      "ps": "stack د تګ راتګ اداره کوي. List دوه کتارونه جوړوي او هر NavigationLink د هماغه نوم جزییات پرانیزي. نوم دلته ځکه پېژند کېدای شي چې یکتا دی. د سمون وړ ثبت ثابت پېژند غواړي، څو د نوم بدلون د لارې مانا بدله نه کړي."
    },
    {
      "en": "Codable allows Note to be encoded and decoded. JSONEncoder turns the one-note array into bytes; this alone has not written a file. Save those bytes atomically and decode them on restart. Keep an old valid copy if writing fails, and validate a decoded note before accepting it into the model.",
      "fa": "Codable تبدیل Note به معلومات و برعکس را ممکن می‌سازد. JSONEncoder آرایهٔ یک یادداشت را به بایت تبدیل می‌کند؛ هنوز فایلی نوشته نشده است. بایت‌ها را یک‌پارچه ذخیره و پس از بازشدن بخوانید. هنگام ناکامی نسخهٔ معتبر قبلی را نگه دارید و معلومات خوانده‌شده را بررسی کنید.",
      "ps": "Codable د Note کوډول او بېرته لوستل ممکنوي. JSONEncoder د یوه یادښت لړۍ په بایټونو بدلوي؛ لا فایل نه دی لیکل شوی. بایټونه په اټومي ډول وساتئ او د بیا پرانیستلو پر مهال یې ولولئ. ناکامي کې پخوانۍ سمه کاپي وساتئ او لوستل شوي معلومات وګورئ."
    },
    {
      "en": "NoteStore promises an asynchronous load that may throw. refresh awaits it before replacing notes. MainActor isolates this model's access; it does not make slow work free. A thrown load leaves the assignment unfinished. The screen must show the error and retain useful old content instead of pretending an empty list was loaded.",
      "fa": "NoteStore بارگذاری غیرهم‌زمانی را تعریف می‌کند که ممکن است خطا بدهد. refresh پیش از جایگزینی notes منتظر می‌ماند. MainActor دسترسی به مدل را جدا می‌کند؛ کار کند را رایگان نمی‌سازد. خطا مقداردهی را ناتمام می‌گذارد. صفحه باید خطا و محتوای مفید قبلی را نگه دارد.",
      "ps": "NoteStore ناهماهنګ لوستل تعریفوي چې استثنا ورکولای شي. refresh د notes تر بدلولو مخکې انتظار کوي. MainActor د ماډل لاسرسی جلا کوي؛ ورو کار وړیا نه کوي. استثنا ارزښت ورکول نیمګړي پرېږدي. پرده باید تېروتنه وښيي او ګټور پخوانی متن وساتي."
    },
    {
      "en": "The test trims the single space, producing an empty string, and asserts that it is empty. It checks a string rule, not an installed application. Add tests of the actual save action with blank and valid titles. Device installation and distribution are separate steps requiring the appropriate Apple development environment.",
      "fa": "آزمون یک فاصله را حذف می‌کند، رشتهٔ خالی می‌سازد و خالی بودنش را بررسی می‌کند. این قاعدهٔ متن است، نه آزمون برنامهٔ نصب‌شده. عمل ذخیره را با عنوان خالی و معتبر آزمایش کنید. نصب و توزیع مرحله‌های جدا با محیط توسعهٔ مناسب اپل اند.",
      "ps": "ازموینه یوه تشه لرې کوي، تش متن جوړوي او تشوالی یې ګوري. دا د متن قاعده ده، د نصب شوي اپ ازموینه نه ده. د ساتلو عمل له تش او سم نوم سره وازمویئ. نصب او وېش د اپل مناسب پراختیايي چاپېریال سره جلا ګامونه دي."
    }
  ],
  "swift": [
    {
      "en": "Int tries to convert the text \"42\" into a number. if let unwraps the successful optional value, so adding 1 displays 43. Replacing the text with \"hello\" follows the error branch. Optional handling forces you to consider failed conversion instead of assuming every input is numeric.",
      "fa": "Int تلاش می‌کند متن \"42\" را به عدد تبدیل کند. if let مقدار اختیاری موفق را باز می‌کند؛ افزودن یک، 43 را نمایش می‌دهد. متن \"hello\" به حالت خطا می‌رود. مقدار اختیاری مجبور می‌سازد ناکامی تبدیل را هم در نظر بگیرید.",
      "ps": "Int هڅه کوي \"42\" متن په عدد بدل کړي. if let بریالی اختیاري ارزښت راباسي؛ یو ورزیاتول 43 ښيي. که متن \"hello\" شي، د خطا برخه اجرا کېږي. اختیاري ارزښت مو اړ باسي ناکامه بدلون هم په پام کې ونیسئ."
    },
    {
      "en": "reduce starts at zero and adds every element. An empty list performs no additions, so total([]) returns zero. The assertion checks that boundary and prints nothing. With [10, 20], the running sum becomes 10 and then 30. Keeping the function pure makes this rule easy to test.",
      "fa": "reduce از صفر شروع و هر عضو را جمع می‌کند. فهرست خالی هیچ جمعی ندارد؛ پس total([]) صفر می‌دهد. assertion همین مرز را بررسی می‌کند و چیزی نمایش نمی‌دهد. با [10, 20] مجموع به 10 و 30 می‌رسد. تابع مستقل از ذخیره و صفحه آسان‌تر آزمایش می‌شود.",
      "ps": "reduce له صفره پیلېږي او هر غړی جمع کوي. تش لېست جمع نه لري؛ total([]) صفر ورکوي. assertion همدا پوله ګوري او څه نه ښيي. له [10, 20] سره مجموعه 10 او بیا 30 کېږي. له ساتنې او پردې خپلواکه تابع اسانه ازمویل کېږي."
    },
    {
      "en": "Validation models either an accepted integer or a rejection reason. Item separates an immutable id from a changeable quantity. These declarations do not reject negative stock by themselves; add a validated construction or update path. A data type's shape and its business rules are related but different responsibilities.",
      "fa": "Validation یا عدد پذیرفته‌شده دارد یا دلیل رد. Item شناسهٔ ثابت را از تعداد قابل تغییر جدا می‌کند. این تعریف‌ها به‌تنهایی موجودی منفی را رد نمی‌کنند؛ مسیر ساخت یا تغییر بررسی‌شده اضافه کنید. شکل معلومات و قواعد کاری دو مسئولیت مرتبط ولی جدا اند.",
      "ps": "Validation یا منل شوی عدد لري یا د رد دلیل. Item ثابت پېژند له بدلېدونکي شمېر څخه بېلوي. دا تعریفونه په خپله منفي موجودي نه ردوي؛ کتل شوی جوړول یا بدلول ورزیات کړئ. د معلوماتو بڼه او کاري قواعد جلا خو تړلې دندې دي."
    },
    {
      "en": "The encoder turns Expense(amount: 20) into JSON bytes. The decoder rebuilds an Expense from those bytes, and print displays 20. A successful decode shows compatible structure, not that every amount is allowed. Reject negative amounts explicitly if the expense rules forbid them.",
      "fa": "رمزگذار Expense(amount: 20) را به بایت‌های JSON تبدیل می‌کند. رمزگشا از آن Expense می‌سازد و print مقدار 20 را نشان می‌دهد. خواندن موفق ساختار سازگار را ثابت می‌کند، نه مجاز بودن هر مبلغ. اگر قاعده مصرف منفی را منع می‌کند، آن را صریحاً رد کنید.",
      "ps": "کوډوونکی Expense(amount: 20) په JSON بایټونو بدلوي. لوستونکی ترې بېرته Expense جوړوي او print د 20 ارزښت ښيي. بریالی لوستل برابر جوړښت ثابتوي، نه د هر مقدار منل. که د مصرف قاعده منفي منع کوي، په څرګنده یې رد کړئ."
    },
    {
      "en": "The actor owns value and serializes access to its isolated state. increment changes it; read returns it. This declaration makes no calls and displays nothing. From outside the actor, use the required asynchronous access. Actor isolation protects this state but does not automatically make several separate calls one atomic business operation.",
      "fa": "actor مالک value است و دسترسی به حالت خود را نوبتی می‌کند. increment تغییر می‌دهد و read می‌خواند. تعریف چیزی را فراخوانی یا نمایش نمی‌دهد. از بیرون دسترسی غیرهم‌زمان لازم را استفاده کنید. حفاظت actor چند فراخوانی جدا را خودبه‌خود یک عملیات یک‌پارچه نمی‌سازد.",
      "ps": "actor د value مالک دی او خپل حالت ته لاسرسی په نوبت کوي. increment یې بدلوي او read یې ورکوي. تعریف څه نه رابولي او نه ښيي. له بهر اړین ناهماهنګ لاسرسی وکاروئ. د actor ساتنه څو جلا غوښتنې په خپله یو اټومي کاري عمل نه ګرځوي."
    },
    {
      "en": "balance receives any store obeying LedgerStore. It loads amounts and adds them from zero. If loading throws, balance propagates the failure instead of reporting a false zero balance. Test an empty store, two amounts, and a throwing store to distinguish valid emptiness from unavailable data.",
      "fa": "balance هر ذخیره‌گاه مطابق LedgerStore را می‌گیرد، مبلغ‌ها را می‌خواند و از صفر جمع می‌کند. اگر خواندن خطا بدهد، خطا منتقل می‌شود؛ موجودی دروغین صفر گزارش نمی‌شود. ذخیره‌گاه خالی، دو مبلغ و ناکامی را جدا آزمایش کنید تا خالی بودن معتبر با نبود معلومات اشتباه نشود.",
      "ps": "balance هر LedgerStore اخلي، مبلغونه لولي او له صفره یې جمع کوي. که لوستل استثنا ورکړي، خطا لېږدوي؛ دروغجن صفر نه ښيي. تش زېرمتون، دوه مبلغونه او ناکامي جلا وازمویئ، څو معتبر تشوالی له نه شته معلوماتو سره ګډ نه شي."
    }
  ],
  "cpp": [
    {
      "en": "iostream provides stream output. main starts the program, total starts at zero, and the loop adds 10, 20, then 30. cout writes 60 followed by a newline. Compile this as a C++ source file with the provisioned compiler; include lines and semicolons are part of the program, not displayed output.",
      "fa": "iostream ابزار نمایش را فراهم می‌کند. main آغاز می‌شود، total صفر است و حلقه 10، 20 و 30 را اضافه می‌کند. cout مقدار 60 و سپس سطر نو می‌نویسد. فایل را با مترجم آمادهٔ C++ بسازید؛ include و نقطه‌ویرگول جزو کود اند، نه نتیجه.",
      "ps": "iostream د ښودلو وسایل برابروي. main پیل دی، total صفر دی او کړۍ 10، 20 او 30 زیاتوي. cout د 60 ارزښت او نوې کرښه لیکي. فایل په چمتو C++ کمپایلر جوړ کړئ؛ include او سیمیکولن د کوډ برخه دي، د پایلې نه."
    },
    {
      "en": "The reference avoids copying the vector and const prevents this function from changing its elements. result starts at zero, accumulates each value, and is returned. The fragment has no main and prints nothing. Call sum with an empty vector to verify that it returns zero without reading a nonexistent element.",
      "fa": "ارجاع از کاپی بردار جلوگیری و const تغییر عضوها را در این تابع منع می‌کند. result از صفر شروع، مقدارها را جمع و برمی‌گرداند. این بخش main ندارد و چیزی نمایش نمی‌دهد. با بردار خالی فراخوانی کنید؛ باید بدون خواندن عضو ناموجود صفر بدهد.",
      "ps": "ارجاع د ویکتور کاپي نه جوړوي او const په دې تابع کې د غړو بدلون منع کوي. result له صفره پیل، مقدارونه جمع او بېرته ورکوي. دا برخه main نه لري او څه نه ښيي. له تش ویکتور سره یې راوبولئ؛ باید بې ناموجود غړي لوستلو صفر ورکړي."
    },
    {
      "en": "make_unique creates an Item and returns its sole owning pointer. stock begins at zero. When the owner leaves scope, its object is released automatically. This is ownership, not merely a convenient spelling of new. Do not create another owning pointer from the same raw address or free the object manually.",
      "fa": "make_unique یک Item می‌سازد و اشاره‌گر مالک یگانه را می‌دهد. stock صفر آغاز می‌شود. با پایان محدودهٔ مالک، شیء خودکار آزاد می‌شود. این قاعدهٔ مالکیت است، نه تنها شکل کوتاه new. از همان آدرس مالک دوم نسازید و شیء را دستی آزاد نکنید.",
      "ps": "make_unique یو Item جوړوي او یوازینی مالک اشاره ورکوونکی ورکوي. stock له صفره پیلېږي. د مالک د ساحې په پای کې شی په خپله خوشې کېږي. دا مالکیت دی، یوازې د new لنډه بڼه نه ده. له هماغه پتې دویم مالک مه جوړوئ او شی په لاس مه خوشې کوئ."
    },
    {
      "en": "values starts as 3, 1, 2. The sort call is currently a comment and does nothing. Place and uncomment it inside a function to obtain 1, 2, 3. Sorting changes this vector in place. Keep a copy if the original order matters, and test duplicates as well as distinct values.",
      "fa": "values با 3، 1 و 2 آغاز می‌شود. فراخوانی sort فعلاً یادداشت است و اجرا نمی‌شود. داخل تابع آن را از یادداشت بیرون کنید تا 1، 2 و 3 شود. مرتب‌سازی همین بردار را تغییر می‌دهد. اگر ترتیب اولیه مهم است کاپی نگه دارید و تکرارها را هم آزمایش کنید.",
      "ps": "values د 3، 1 او 2 په ترتیب پیلېږي. sort اوس یادونه ده او کار نه کوي. د تابع دننه یې له یادونې وباسئ؛ 1، 2 او 3 به شي. ترتیب همدا ویکتور بدلوي. که پخوانی ترتیب مهم وي کاپي وساتئ او تکراري مقدارونه هم وازمویئ."
    },
    {
      "en": "The parser first attempts to read an integer, then consumes trailing whitespace, then requires the input to end. \"12 \" is accepted; \"12abc\" is rejected instead of silently becoming 12. Failed conversion throws. The caller must handle that failure and must not overwrite a valid record with an unvalidated value.",
      "fa": "تجزیه‌کننده نخست عدد صحیح، بعد فاصلهٔ پایانی را می‌خواند و پایان متن را لازم می‌داند. \"12 \" پذیرفته و \"12abc\" رد می‌شود؛ بی‌صدا 12 نمی‌شود. تبدیل ناکام خطا می‌دهد. فراخواننده باید خطا را مدیریت کند و ثبت معتبر را با مقدار بررسی‌نشده عوض نکند.",
      "ps": "لوستونکی لومړی صحیح عدد او بیا وروستۍ تشې لولي او د متن پای غواړي. \"12 \" مني خو \"12abc\" ردوي؛ په پټه 12 نه ګرځي. ناکام بدلون استثنا ورکوي. رابلونکی باید خطا اداره کړي او معتبر ثبت په نه کتل شوي ارزښت بدل نه کړي."
    },
    {
      "en": "The template creates a comparison function for a type supporting <. larger(3, 7) returns 7; equal values return the first argument. This fragment does not measure performance. Establish correct boundary behavior first, then measure realistic inputs before deciding that a template or another abstraction is too expensive.",
      "fa": "قالب برای نوعی که < را پشتیبانی کند تابع مقایسه می‌سازد. larger(3, 7) مقدار 7 می‌دهد؛ مقدارهای برابر آرگومان اول را می‌دهند. این بخش سرعت را اندازه نمی‌گیرد. نخست مرزها را درست بسازید، سپس با ورودی واقعی هزینهٔ روش را اندازه بگیرید.",
      "ps": "قالب د داسې ډول لپاره پرتله جوړوي چې < مني. larger(3, 7) د 7 ارزښت ورکوي؛ برابر ارزښتونه لومړی آرګومان ورکوي. دا برخه سرعت نه اندازه کوي. لومړی پولې سمې کړئ، بیا په واقعي داخلو د طریقې لګښت اندازه کړئ."
    }
  ],
  "javascript": [
    {
      "en": "prices is the list to read; total is changeable because it uses let. The for-of loop reads values, not indexes. total becomes 10, 30, then 60, and console.log displays 60. const prevents rebinding prices; it does not make every object inside a collection immutable.",
      "fa": "prices فهرست خواندنی است و total با let قابل تغییر است. حلقهٔ for-of مقدارها را می‌خواند، نه اندیس‌ها را. مجموع 10، 30 و 60 می‌شود و console.log مقدار 60 را نشان می‌دهد. const تعویض خود prices را منع می‌کند؛ همهٔ عضوها را تغییرناپذیر نمی‌سازد.",
      "ps": "prices لوستل کېدونکی لېست دی او total په let بدلېدونکی دی. for-of ارزښتونه لولي، اندیسونه نه. مجموعه 10، 30 او 60 کېږي او console.log د 60 ارزښت ښيي. const د prices بیا تړل منع کوي؛ ټول غړي نه بدلېدونکي نه ګرځوي."
    },
    {
      "en": "Each object holds a category and amount. reduce begins with 0, adds the first amount 20 and the second 10, and stores 30. An empty array would return 0 because an initial value was supplied. The code does not validate amount types; add validation before accepting imported records.",
      "fa": "هر شیء کتگوری و مبلغ دارد. reduce از صفر شروع، اول 20 و بعد 10 را جمع می‌کند و 30 ذخیره می‌شود. آرایهٔ خالی با مقدار آغازین صفر، صفر می‌دهد. کود نوع مبلغ را بررسی نمی‌کند؛ پیش از پذیرش ثبت واردشده، بررسی اضافه کنید.",
      "ps": "هر شی کتګوري او مبلغ لري. reduce له صفره پیل، لومړی 20 او بیا 10 جمع کوي او 30 ساتي. تشه لړۍ د ورکړل شوي صفر له امله صفر ورکوي. کوډ د مبلغ ډول نه ګوري؛ د واردو شوو ثبتونو له منلو مخکې کتنه ورزیاته کړئ."
    },
    {
      "en": "querySelector finds existing page elements. The click handler changes output text only when the button is pressed. The message says Saved locally, but no save occurs in this snippet. Connect real persistence before showing that success message, and check missing elements rather than calling methods on null.",
      "fa": "querySelector عنصرهای موجود صفحه را پیدا می‌کند. رویداد کلیک فقط با فشار دکمه متن output را تغییر می‌دهد. پیام می‌گوید محلی ذخیره شد، اما این نمونه چیزی ذخیره نکرده است. پیش از پیام موفقیت ذخیرهٔ واقعی وصل کنید و عنصر ناموجود را بررسی کنید.",
      "ps": "querySelector د پاڼې موجود عناصر مومي. د کلیک اداره یوازې د تڼۍ په وهلو output بدلوي. پیغام وايي محلي وساتل شو، خو نمونه څه نه ساتي. د بریا له پیغام مخکې واقعي ساتنه ونښلوئ او ناموجود عناصر وګورئ."
    },
    {
      "en": "load awaits the supplied read function. The resolved array reaches then and is logged. If read rejects, catch returns an empty array instead. That policy hides the difference between no books and failed loading; for a real screen, return an explicit error state when the distinction matters.",
      "fa": "load منتظر تابع read می‌ماند. آرایهٔ موفق به then می‌رسد و نمایش داده می‌شود. اگر read ناکام شود، catch آرایهٔ خالی می‌دهد. این روش تفاوت «کتاب نیست» و «خواندن ناکام شد» را پنهان می‌کند؛ در صفحهٔ واقعی خطای جدا برگردانید.",
      "ps": "load د read تابع ته انتظار کوي. بریالۍ لړۍ then ته رسېږي او ښودل کېږي. که read ناکام شي، catch تشه لړۍ ورکوي. دا «کتاب نشته» او «لوستل ناکام شول» ګډوي؛ په واقعي پرده کې جلا خطا حالت ورکړئ."
    },
    {
      "en": "JSON.stringify converts the snapshot to text before localStorage stores it under tasks. Saving can fail, and browser storage can be cleared. On load, parse the text and validate version and fields. A saved string is not proof of a usable backup; test restoring it into a fresh profile.",
      "fa": "JSON.stringify عکس معلومات را به متن تبدیل می‌کند و localStorage زیر tasks نگه می‌دارد. ذخیره ممکن است ناکام یا توسط مرورگر پاک شود. هنگام خواندن، متن، نسخه و فیلدها را بررسی کنید. متن ذخیره‌شده به‌تنهایی پشتیبان معتبر نیست؛ بازگردانی در محیط تازه را آزمایش کنید.",
      "ps": "JSON.stringify د معلوماتو بڼه متن کوي او localStorage یې تر tasks لاندې ساتي. ساتنه ناکامېدای او براوزر یې پاکولای شي. د لوستلو پر مهال متن، نسخه او خانې وګورئ. ساتل شوی متن په خپله معتبره بیک اپ نه ده؛ په نوي چاپېریال کې راګرځول وازمویئ."
    },
    {
      "en": "Number.isFinite rejects non-number and infinite inputs before addition. add(2,3) returns 5 and the assertion passes. JavaScript's + can concatenate strings, which is why validation matters. Test a string, NaN, and an ordinary negative number; the last is finite even if your particular business rule later forbids it.",
      "fa": "Number.isFinite ورودی غیرعددی و بی‌نهایت را پیش از جمع رد می‌کند. add(2,3) مقدار 5 می‌دهد. + می‌تواند متن‌ها را وصل کند؛ پس بررسی مهم است. متن، NaN و عدد منفی عادی را آزمایش کنید؛ منفی محدود است، هرچند قاعدهٔ کاری ممکن است آن را منع کند.",
      "ps": "Number.isFinite غیرعددي او بې پای داخله له جمع مخکې ردوي. add(2,3) پنځه ورکوي. + متنونه هم نښلولای شي؛ نو کتنه مهمه ده. متن، NaN او عادي منفي عدد وازمویئ؛ منفي محدود دی، که څه هم کاري قاعده یې منع کولای شي."
    }
  ],
  "reactjs": [
    {
      "en": "CourseCard receives title through props and places it inside a heading. Calling the component with title=\"Python\" produces a card headed Python. JSX describes UI and needs a prepared React build environment. This function alone neither mounts the application nor saves a selected course.",
      "fa": "CourseCard عنوان را از props می‌گیرد و در سرعنوان می‌گذارد. با title=\"Python\" کارت عنوان Python می‌گیرد. JSX رابط را توضیح می‌دهد و محیط آمادهٔ React می‌خواهد. این تابع به‌تنهایی نه برنامه را روی صفحه نصب می‌کند و نه انتخاب کورس را ذخیره می‌کند.",
      "ps": "CourseCard نوم له props اخلي او په سرلیک کې یې ږدي. له title=\"Python\" سره کارت د Python نوم لري. JSX مخ تشریح کوي او چمتو React چاپېریال غواړي. یوازې دا تابع نه اپ پاڼې ته نښلوي او نه ټاکل شوی کورس ساتي."
    },
    {
      "en": "useState returns the current count and a setter. The updater receives the previous count and returns one more, so two clicks eventually display 2. Directly changing a local variable would not request this render. The component's state is temporary; saving across reloads requires a separate storage step.",
      "fa": "useState مقدار فعلی و تابع تغییر را می‌دهد. تغییر‌دهنده مقدار قبلی را می‌گیرد و یک اضافه می‌کند؛ دو کلیک 2 نشان می‌دهد. تغییر متغیر محلی خودبه‌خود این نمایش را تازه نمی‌کند. حالت موقتی است؛ دوام پس از بازخوانی ذخیرهٔ جدا می‌خواهد.",
      "ps": "useState اوسنی شمېر او بدلوونکې تابع ورکوي. بدلوونکی پخوانی شمېر اخلي او یو ورزیاتوي؛ دوه کلیکونه 2 ښيي. د محلي متغیر بدلون په خپله دا رسمول نه غواړي. حالت لنډمهالی دی؛ له بیا لوډ وروسته پاتې کېدل جلا ساتنه غواړي."
    },
    {
      "en": "The reducer handles add by creating a new array containing the old items and action.item. Other actions return the old state unchanged. It does not reject duplicate IDs or blank titles. Add those domain rules separately and test that rejected actions leave the prior state intact.",
      "fa": "reducer در حالت add آرایهٔ تازه از عضوهای قبلی و action.item می‌سازد. عمل‌های دیگر حالت قبلی را نگه می‌دارند. شناسهٔ تکراری و عنوان خالی هنوز رد نمی‌شوند. قواعد را اضافه و آزمایش کنید که عمل ردشده حالت معتبر قبلی را تغییر ندهد.",
      "ps": "reducer د add لپاره له پخوانیو غړو او action.item نوې لړۍ جوړوي. نور عملونه پخوانی حالت پرېږدي. تکراري پېژند او تش نوم لا نه ردوي. قواعد ورزیات او وازمویئ چې رد شوی عمل پخوانی سم حالت بدل نه کړي."
    },
    {
      "en": "The effect subscribes to the browser's online event and cleanup removes the same handler. It does not listen for offline events or verify that a particular service is reachable. Treat this as a subscription example, not a complete connectivity detector. Always pair external subscriptions with cleanup.",
      "fa": "effect رویداد online مرورگر را مشاهده و cleanup همان handler را حذف می‌کند. offline را نمی‌شنود و دسترسی به خدمت مشخص را ثابت نمی‌کند. این مثال اشتراک رویداد است، نه تشخیص کامل اتصال. مشاهدهٔ بیرونی را همیشه با پاک‌سازی همراه سازید.",
      "ps": "effect د براوزر online پېښې ته غوږ نیسي او cleanup هماغه handler لرې کوي. offline نه څاري او د ځانګړي خدمت رسېدل نه ثابتوي. دا د ګډون مثال دی، بشپړ اتصال معلوموونکی نه دی. بهرنی ګډون تل له پاکولو سره یوځای کړئ."
    },
    {
      "en": "Field renders a label and the supplied children. htmlFor should match the id on the actual input child. The wrapper does not create that input or validate it. Test selecting the label and using the keyboard, and make sure the caller passes a unique id for each field.",
      "fa": "Field برچسب و children را نمایش می‌دهد. htmlFor باید با id ورودی واقعی مطابق باشد. این ظرف خود ورودی نمی‌سازد و بررسی نمی‌کند. انتخاب برچسب و صفحه‌کلید را آزمایش کنید و برای هر فیلد شناسهٔ یکتا بدهید.",
      "ps": "Field نوم او ورکړل شوي children ښيي. htmlFor باید د واقعي input له id سره برابر وي. دا لوښی په خپله input نه جوړوي او نه یې ګوري. د نوم ټاکل او کیبورډ وازمویئ او هرې خانې ته یکتا پېژند ورکړئ."
    },
    {
      "en": "The tree separates task behavior, local storage, and reusable fields. It is a design sketch, not a runnable project. A reducer should be testable without rendering React. Bundle scripts, styles, and fonts locally; a successful development server does not prove the exported build works without internet.",
      "fa": "ساختار، رفتار وظیفه، ذخیرهٔ محلی و فیلد مشترک را جدا می‌کند. طرح است، نه پروژهٔ قابل اجرا. reducer باید بدون نمایش React آزمایش شود. کود، سبک و خط را محلی بسته‌بندی کنید؛ کار سرور توسعه ثابت نمی‌کند بستهٔ نهایی بدون اینترنت کار می‌کند.",
      "ps": "جوړښت د دندې چلند، محلي ساتنه او ګډې خانې بېلوي. طرحه ده، اجرا کېدونکې پروژه نه ده. reducer باید له React رسمولو پرته وازمویل شي. سکریپټ، بڼه او لیکبڼه محلي بسته کړئ؛ پراختیايي سرور د وروستي بې انټرنېټه کار ثبوت نه دی."
    }
  ],
  "reactnative": [
    {
      "en": "View is a native layout container and Text displays Salam inside it. padding creates space inside the container. These are not HTML div and p elements. The component must be registered in a provisioned native project; a browser-only React setup cannot produce the Android or iOS installation by itself.",
      "fa": "View ظرف چیدمان بومی و Text نمایش‌دهندهٔ Salam است. padding داخل ظرف فاصله می‌سازد. این‌ها div و p در HTML نیستند. جزء باید در پروژهٔ بومی آماده ثبت شود؛ محیط React مرورگر به‌تنهایی نصب اندروید یا iOS تولید نمی‌کند.",
      "ps": "View اصلي ترتیب لوښی او Text د Salam ښودونکی دی. padding دننه واټن جوړوي. دا د HTML د div او p عناصر نه دي. برخه باید په چمتو اصلي پروژه کې ثبت شي؛ یوازې د براوزر React د اندروید یا iOS نصب نه جوړوي."
    },
    {
      "en": "FlatList receives records and renders each title. keyExtractor uses a stable string id so the list can identify rows across changes. Empty data needs a helpful empty-state component. Do not use position as identity when items can move or be deleted; the wrong row can otherwise retain another item's state.",
      "fa": "FlatList ثبت‌ها را می‌گیرد و عنوان هر کدام را نشان می‌دهد. keyExtractor شناسهٔ متنی ثابت را برای شناسایی سطرها استفاده می‌کند. معلومات خالی پیام رهنما می‌خواهد. برای عضو قابل جابه‌جایی یا حذف از شمارهٔ جایگاه استفاده نکنید؛ حالت سطرها ممکن است اشتباه حفظ شود.",
      "ps": "FlatList ثبتونه اخلي او هر نوم ښيي. keyExtractor ثابت متني پېژند کاروي، څو کتارونه وپېژني. تش معلومات ګټور تش حالت غواړي. د خوځېدونکو یا ړنګېدونکو غړو لپاره ځای پېژند مه ګرځوئ؛ د کتار حالت له بل سره ګډېدای شي."
    },
    {
      "en": "This is a route contract: open a catalog, select an itemId, then edit that same id. Fetch the current record from the repository on the destination screen. Passing a whole old object can show stale information. Handle a missing record explicitly when it was removed before the route opened.",
      "fa": "این قرارداد مسیر است: فهرست، انتخاب itemId و ویرایش همان شناسه. در صفحهٔ مقصد ثبت فعلی را از مخزن بگیرید. فرستادن شیء قدیمی کامل می‌تواند معلومات کهنه نشان بدهد. اگر ثبت پیش از بازشدن حذف شده، حالت ناموجود را صریح مدیریت کنید.",
      "ps": "دا د لارې تړون دی: فهرست، itemId ټاکل او هماغه پېژند سمول. په وروستۍ پرده کې اوسنی ثبت له زېرمتونه واخلئ. د بشپړ زاړه شي لېږل زاړه معلومات ښودلای شي. که ثبت مخکې ړنګ شوی وي، ناموجود حالت په څرګنده اداره کړئ."
    },
    {
      "en": "saveItem checks for a blank trimmed title before calling storage. await means success is not returned before storage completes. The snippet does not ensure that item.title is a string, so validate incoming record structure first. On rejection or storage failure, keep the draft and let the user correct or retry.",
      "fa": "saveItem پیش از ذخیره، خالی نبودن عنوان را بررسی می‌کند. await موفقیت را تا پایان ذخیره برنمی‌گرداند. نمونه متنی بودن item.title را تضمین نمی‌کند؛ نخست ساختار معلومات را بررسی کنید. هنگام رد یا ناکامی، پیش‌نویس را نگه دارید تا کاربر اصلاح یا دوباره تلاش کند.",
      "ps": "saveItem د ساتلو مخکې تش نوم ګوري. await د ساتنې تر پای بریا نه ورکوي. نمونه د item.title متني والی نه تضمینوي؛ لومړی جوړښت وګورئ. د رد یا ناکامۍ پر مهال مسوده وساتئ، څو کارن سمون یا بیا هڅه وکړي."
    },
    {
      "en": "Pressable calls save when activated. The role tells assistive technology that it is a button and the label explains the action. The code does not implement save. Verify screen-reader speech, a sufficient touch target, disabled behavior during saving, and an actual persisted record before showing success.",
      "fa": "Pressable هنگام فعال شدن save را صدا می‌زند. role به ابزار کمکی می‌گوید دکمه است و label کار را توضیح می‌دهد. save هنوز پیاده نشده است. خوانش صوتی، اندازهٔ لمس، غیرفعال بودن هنگام ذخیره و ثبت واقعی را پیش از پیام موفقیت بررسی کنید.",
      "ps": "Pressable د فعالېدو پر مهال save رابولي. role مرستندویه وسیلې ته تڼۍ ښيي او label کار تشریح کوي. save لا نه دی پلي شوی. غږیز لوستل، د لمس اندازه، د ساتنې پر مهال غیرفعال حالت او واقعي ثبت د بریا له پیغام مخکې وګورئ."
    },
    {
      "en": "The matrix names conditions to test; comments do not execute tests. Start with a save-and-relaunch journey on each target platform. Repeat with a failed save and large text. Record observed behavior rather than marking an entire platform passed because one component rendered in a JavaScript test.",
      "fa": "جدول حالت‌های لازم آزمایش را نام می‌دهد؛ یادداشت آزمون اجرا نمی‌کند. در هر پلتفرم مسیر ذخیره و بازشدن دوباره را آغاز کنید. با ناکامی ذخیره و خط کلان تکرار کنید. رفتار مشاهده‌شده را ثبت کنید؛ نمایش یک جزء در آزمون JavaScript تأیید تمام پلتفرم نیست.",
      "ps": "جدول د ازموینې حالتونه نوموي؛ یادونې ازموینې نه چلوي. په هر پلېټفارم کې ساتل او بیا پرانیستل وازمویئ. له ناکامې ساتنې او لوی متن سره یې تکرار کړئ. لیدل شوی چلند ثبت کړئ؛ د JavaScript د یوې برخې رسمېدل د ټول پلېټفارم بریا نه ده."
    }
  ],
  "nodejs": [
    {
      "en": "The node: prefix loads a built-in module, not a downloaded package. parseArgs separates command-line arguments, and positionals contains ordinary unnamed values. Run a .mjs file with a sample word to see it in the array. This runs in Node, not in a browser page with a DOM.",
      "fa": "پیشوند node: ماژول داخلی را می‌خواند، نه بستهٔ دانلودشده. parseArgs آرگومان‌های خط فرمان را جدا می‌کند و positionals مقدارهای بدون نام را می‌گیرد. فایل .mjs را با یک واژه اجرا کنید تا آن را در آرایه ببینید. این محیط Node است، نه صفحهٔ مرورگر با DOM.",
      "ps": "د node: مخکښ داخلي ماډیول لولي، ډاونلوډ شوې بسته نه. parseArgs د قوماندې آرګومانونه بېلوي او positionals بې نومه ارزښتونه اخلي. .mjs فایل له یوې کلمې سره وچلوئ چې په لړۍ کې یې ووینئ. دا Node دی، د DOM براوزر پاڼه نه ده."
    },
    {
      "en": "readFile reads the local file as UTF-8 text, then JSON.parse converts valid JSON into a value. A missing file and malformed JSON are different failures. Neither step validates business fields. Keep those checks separate so the learner or user receives the right recovery instruction.",
      "fa": "readFile فایل محلی را به متن UTF-8 می‌خواند و JSON.parse متن معتبر را به مقدار تبدیل می‌کند. فایل ناموجود و JSON خراب دو ناکامی متفاوت اند. هیچ‌کدام فیلدهای کاری را بررسی نمی‌کنند. بررسی‌ها را جدا نگه دارید تا پیام اصلاح مناسب داده شود.",
      "ps": "readFile محلي فایل د UTF-8 متن په توګه لولي او JSON.parse معتبر متن په ارزښت بدلوي. ورک فایل او خراب JSON دوه بېلې ناکامۍ دي. هېڅ یو کاري خانې نه ګوري. کتنې جلا وساتئ څو د سمون سمه لارښوونه ورکړل شي."
    },
    {
      "en": "pipeline connects a readable stream to a writable one and manages backpressure, so a slow destination does not require the whole file in memory. It rejects on failure. This example writes copy.txt and can replace its contents; use disposable fixture files and never select the same source and destination path.",
      "fa": "pipeline جریان خواندن را به نوشتن وصل و سرعت انتقال را هماهنگ می‌کند تا مقصد کند تمام فایل را در حافظه جمع نکند. ناکامی خطا می‌دهد. این مثال copy.txt را می‌نویسد و می‌تواند محتوایش را عوض کند؛ فایل تمرینی و مسیرهای جدا استفاده کنید.",
      "ps": "pipeline لوستونکی بهیر له لیکونکي سره نښلوي او فشار اداره کوي، څو ورو منزل ټول فایل حافظې ته وانه چوي. ناکامي خطا ورکوي. نمونه copy.txt لیکي او محتوا یې بدلولای شي؛ تمریني فایلونه او بېلې سرچینې او منزل لارې وکاروئ."
    },
    {
      "en": "createServer installs a handler, then listen binds to this computer's loopback address. Each request receives status 200 and JSON with status ok. This example has no routing or authentication. A local address avoids needing internet, but it does not turn a demonstration endpoint into a complete application service.",
      "fa": "createServer اداره‌کننده می‌سازد و listen به آدرس همین کمپیوتر وصل می‌شود. هر درخواست وضعیت 200 و JSON با status ok می‌گیرد. نمونه مسیرهای جدا یا تصدیق هویت ندارد. آدرس محلی اینترنت نمی‌خواهد، اما خدمت نمایشی را کامل نمی‌سازد.",
      "ps": "createServer اداره کوونکی جوړوي او listen د همدې کمپیوټر loopback ته تړي. هره غوښتنه 200 او د status ok لرونکی JSON اخلي. نمونه جلا لارې او هویت کتنه نه لري. محلي پته انټرنېټ نه غواړي، خو نمایشي خدمت بشپړ نه ګرځوي."
    },
    {
      "en": "The built-in test runner registers one test. reduce on an empty array returns its supplied initial zero, and strict equality checks that result. Run with node --test. This covers one calculation boundary, not file failure or worker cancellation; add those tests when those behaviors enter your design.",
      "fa": "اجراکنندهٔ داخلی یک آزمون ثبت می‌کند. reduce روی آرایهٔ خالی صفر آغازین را می‌دهد و برابری دقیق آن را بررسی می‌کند. با node --test اجرا کنید. این فقط یک مرز محاسبه است؛ ناکامی فایل و لغو worker هنگام افزودن آن رفتارها آزمون جدا می‌خواهند.",
      "ps": "داخلي چلوونکی یوه ازموینه ثبتوي. reduce په تشه لړۍ ورکړل شوی صفر ورکوي او دقیق برابروالی یې ګوري. په node --test یې وچلوئ. دا یوازې د حساب یوه پوله ده؛ د فایل ناکامي او د worker لغوه کول جلا ازموینې غواړي."
    },
    {
      "en": "cli interprets command-line input, domain/report calculates, and adapters/files reads or writes data. This tree is an architectural sketch. Test the report with in-memory values before involving disk. A recovery guide should say what happens to the old file when a write fails, not only how to start the program.",
      "fa": "cli ورودی فرمان را می‌خواند، domain/report حساب می‌کند و adapters/files معلومات را می‌خواند یا می‌نویسد. این ساختار طرح معماری است. پیش از دیسک، گزارش را با مقدارهای حافظه آزمایش کنید. رهنمای بازیابی باید وضعیت فایل قبلی هنگام ناکامی ذخیره را هم توضیح بدهد.",
      "ps": "cli د قوماندې داخله لولي، domain/report حساب کوي او adapters/files معلومات لولي یا لیکي. دا جوړښت معماري طرحه ده. له ډیسک مخکې راپور په حافظوي ارزښتونو وازمویئ. د راګرځولو لارښود باید د ناکامې لیکنې پر مهال د زاړه فایل حالت هم بیان کړي."
    }
  ],
  "expressjs": [
    {
      "en": "express creates the app. The JSON middleware is registered before routes, with a bounded body size. GET /health responds with JSON, and listen starts a loopback server. Only that route is defined. Prepare the Express dependency locally before disconnected use; this import is not a built-in Node module.",
      "fa": "express برنامه را می‌سازد. میان‌افزار JSON با اندازهٔ محدود پیش از مسیرها ثبت می‌شود. GET /health جواب JSON می‌دهد و listen سرور محلی را آغاز می‌کند. فقط همین مسیر تعریف شده است. وابستگی Express را از قبل آماده کنید؛ ماژول داخلی Node نیست.",
      "ps": "express اپ جوړوي. د محدود بدن JSON منځګړی له لارو مخکې ثبتېږي. GET /health د JSON ځواب ورکوي او listen محلي سرور پیلوي. یوازې همدا لاره تعریف شوې ده. Express تړاو له مخکې برابر کړئ؛ د Node داخلي ماډیول نه دی."
    },
    {
      "en": "The route rejects a missing, non-string, or blank name with 400, then returns a trimmed name with 201. It does not actually persist an item; 201 should represent real creation in the finished service. Add repository saving and return success only after that write completes.",
      "fa": "مسیر نام ناموجود، غیرمتنی یا خالی را با 400 رد و نام پاک‌شده را با 201 برمی‌گرداند. هنوز چیزی ذخیره نمی‌کند؛ در خدمت نهایی 201 باید ایجاد واقعی باشد. ذخیره در مخزن را اضافه و موفقیت را فقط پس از پایان آن گزارش کنید.",
      "ps": "لاره ورک، غیرمتني یا تش نوم په 400 ردوي او پاک شوی نوم په 201 ورکوي. لا څه نه ساتي؛ په وروستي خدمت کې 201 باید واقعي جوړول وي. زېرمتون ته ساتل ورزیات او یوازې له بشپړېدو وروسته بریا ورکړئ."
    },
    {
      "en": "The factory receives a repository and returns a service exposing list. Calling list delegates to that repository. No HTTP object is needed to test it. This thin example has no business validation yet; place loan or capacity rules here when they must be shared by several routes.",
      "fa": "کارخانه مخزن را می‌گیرد و خدمت list می‌دهد. فراخوانی list کار را به همان مخزن می‌سپارد و آزمونش شیء HTTP لازم ندارد. این مثال هنوز بررسی کاری ندارد؛ قاعدهٔ امانت یا ظرفیت مشترک میان چند مسیر را در همین لایه بگذارید.",
      "ps": "کارخانه زېرمتون اخلي او د list خدمت ورکوي. list کار هماغه زېرمتون ته سپاري او ازموینه یې HTTP شی نه غواړي. دا نمونه لا کاري کتنه نه لري؛ د څو لارو ګډ د پور یا ظرفیت قواعد همدې پوړ ته ورکړئ."
    },
    {
      "en": "The four-argument function is error middleware and belongs after routes. If headers have already been sent, it forwards the error instead of sending a second response. Otherwise it sends a generic 500. Validation and authorization failures should have intentional responses rather than all becoming internal errors.",
      "fa": "تابع چهارآرگومانی میان‌افزار خطا است و پس از مسیرها می‌آید. اگر سرآیند فرستاده شده باشد، خطا را منتقل می‌کند تا جواب دوم نفرستد؛ در غیر آن 500 عمومی می‌دهد. ناکامی بررسی و صلاحیت باید جواب مناسب خود را داشته باشند.",
      "ps": "څلور آرګومانه تابع د خطا منځګړی دی او له لارو وروسته راځي. که سرلیکونه لېږل شوي وي، خطا لېږدوي څو دویم ځواب ورنه کړي؛ که نه عمومي 500 ورکوي. د معلوماتو او صلاحیت ناکامي باید خپل مناسب ځواب ولري."
    },
    {
      "en": "These are acceptance scenarios, not test code. First create a loan, then retry the same operation id and verify no duplicate record. Try a conflicting loan and a forced storage failure. Check the database after each response; a correct status code alone does not prove transaction safety.",
      "fa": "این‌ها حالت‌های پذیرش اند، نه کود آزمون. نخست امانت بسازید، همان شناسهٔ عملیات را تکرار و نبود ثبت دوم را بررسی کنید. امانت متضاد و ناکامی اجباری ذخیره را آزمایش کنید. پس از هر جواب دیتابیس را ببینید؛ وضعیت درست به‌تنهایی امنیت معامله را ثابت نمی‌کند.",
      "ps": "دا د منلو حالتونه دي، د ازموینې کوډ نه. لومړی پور جوړ، بیا هماغه عملیات پېژند تکرار او د دویم ثبت نشتوالی وګورئ. متضاد پور او جبري ذخیره ناکامي وازمویئ. له هر ځواب وروسته ډیټابېس وګورئ؛ سم حالت د معاملې خوندیتوب نه ثابتوي."
    },
    {
      "en": "createApp installs a route and returns the app without opening a port. A test can supply a fake service and own startup and cleanup. The handler awaits list and forwards errors to middleware. Add error middleware in the completed composition; this factory alone does not define your complete failure response policy.",
      "fa": "createApp مسیر را ثبت و برنامه را بدون باز کردن پورت برمی‌گرداند. آزمون خدمت فرضی می‌دهد و آغاز و پایان را مالک می‌شود. اداره‌کننده منتظر list می‌ماند و خطا را به میان‌افزار می‌دهد. میان‌افزار خطا را در ترکیب نهایی اضافه کنید؛ این کارخانه سیاست کامل ناکامی نیست.",
      "ps": "createApp لاره ثبتوي او اپ بې پورټ پرانیستلو ورکوي. ازموینه فرضي خدمت ورکوي او پیل او پاکول اداره کوي. اداره کوونکی list ته انتظار او خطا منځګړي ته ورکوي. په وروستي ترکیب کې د خطا منځګړی ورزیات کړئ؛ دا کارخانه بشپړه خطا تګلاره نه ده."
    }
  ],
  "flutter-dart": [
    {
      "en": "total accepts a list of integers. fold starts with zero and adds each value. The empty-list assertion passes, and the example prints 30 for [10,20]. This is a complete small Dart program; it does not need Flutter widgets. A Future or stream is not involved in this particular synchronous calculation.",
      "fa": "total فهرست عددهای صحیح را می‌گیرد. fold از صفر آغاز و هر مقدار را جمع می‌کند. بررسی فهرست خالی موفق و نتیجهٔ [10,20] برابر 30 نمایش داده می‌شود. این پروگرام کوچک کامل Dart است و ویجت نمی‌خواهد. در این محاسبه Future یا جریان دخیل نیست.",
      "ps": "total د صحیح عددونو لېست اخلي. fold له صفره پیل او هر ارزښت جمع کوي. د تش لېست کتنه بریالۍ او د [10,20] پایله 30 ښودل کېږي. دا کوچنی بشپړ Dart پروګرام دی او ویجټ نه غواړي. په دې حساب کې Future یا بهیر نشته."
    },
    {
      "en": "Greeting describes a Padding widget containing Text. The parent supplies size constraints; the widget does not choose an arbitrary screen width. This fragment needs the material import and an app that places Greeting in its tree. Increase text size and narrow the window to check that the greeting remains readable.",
      "fa": "Greeting یک Padding با Text توضیح می‌دهد. والد محدودیت اندازه را می‌دهد؛ ویجت عرض دلخواه صفحه انتخاب نمی‌کند. این بخش import مربوط و برنامه‌ای می‌خواهد که Greeting را در درخت بگذارد. خط را کلان و پنجره را باریک کنید؛ سلام باید خوانا بماند.",
      "ps": "Greeting د Text لرونکی Padding تشریح کوي. مورنی ویجټ د اندازې حدود ورکوي؛ دا ویجټ د پردې هر پلنوالی نه ټاکي. نمونه material import او داسې اپ غواړي چې Greeting پکې کېږدي. متن لوی او کړکۍ تنګه کړئ؛ سلام باید لوستل کېدونکی پاتې شي."
    },
    {
      "en": "formKey identifies a Form so its validation can be requested. The commented field rejects null or blank text and otherwise returns null to mean valid. Merely creating the key does not build the form or save anything. Keep the key in the appropriate state owner rather than recreating it during every build.",
      "fa": "formKey فورم را برای درخواست بررسی مشخص می‌کند. فیلد یادداشت‌شده متن null یا خالی را رد و برای معتبر null برمی‌گرداند. ساخت کلید به‌تنهایی فورم یا ذخیره نمی‌سازد. کلید را در مالک مناسب حالت نگه دارید، نه آن‌که در هر build دوباره بسازید.",
      "ps": "formKey د کتنې غوښتلو لپاره Form پېژني. یادونه شوی field تش یا null متن ردوي او د معتبر لپاره null ورکوي. یوازې کلی جوړول فورم یا ساتنه نه جوړوي. کلی د حالت په مناسب مالک کې وساتئ، هر build کې یې بیا مه جوړوئ."
    },
    {
      "en": "NoteRepository defines load and save contracts. LoadNotes receives an implementation and delegates loading without knowing its storage technology. Inject an in-memory adapter for tests and a persistent adapter for real use. A contract alone does not guarantee atomic writes; verify that behavior in the storage adapter.",
      "fa": "NoteRepository قرارداد خواندن و ذخیره را تعریف می‌کند. LoadNotes پیاده‌سازی را می‌گیرد و بدون دانستن نوع ذخیره، خواندن را می‌سپارد. در آزمون حافظه و در استفادهٔ واقعی ذخیرهٔ دایمی بدهید. قرارداد به‌تنهایی نوشتن یک‌پارچه را تضمین نمی‌کند؛ رفتار adapter را آزمایش کنید.",
      "ps": "NoteRepository د لوستلو او ساتلو تړون ټاکي. LoadNotes پلي شوې برخه اخلي او د ساتنې له ډول پوهېدو پرته لوستل سپاري. ازموینې ته حافظوي او واقعي کار ته دایمي adapter ورکړئ. تړون په خپله اټومي لیکنه نه تضمینوي؛ adapter وازمویئ."
    },
    {
      "en": "Isolate.run performs the closure in another isolate and returns its result asynchronously. The sum becomes 6, but this fragment does not display it. Separate memory prevents direct shared-variable mutation. A short sum does not justify a worker by itself; use isolates for measured heavy work and plan error handling and cancellation.",
      "fa": "Isolate.run کار را در isolate دیگر انجام و نتیجه را غیرهم‌زمان می‌دهد. مجموع 6 می‌شود، اما نمایش داده نمی‌شود. حافظهٔ جدا تغییر مستقیم متغیر مشترک را منع می‌کند. جمع کوتاه به‌تنهایی worker لازم ندارد؛ برای کار سنگین سنجیده‌شده، با مدیریت خطا و لغو استفاده کنید.",
      "ps": "Isolate.run کار په بل isolate کې کوي او نتیجه ناهماهنګه ورکوي. مجموعه 6 ده، خو نه ښودل کېږي. جلا حافظه مستقیم ګډ متغیر بدلون نه پرېږدي. لنډ حساب په خپله worker نه غواړي؛ د اندازه شوي درانه کار لپاره یې له خطا او لغوه کولو سره وکاروئ."
    },
    {
      "en": "The directories name boundaries: domain contains rules, application coordinates actions, data stores content, presentation builds screens, and runtime executes code. This is a design map, not a build script. Verify a packaged app on a disconnected device, including first launch, saving, restart, and bundled fonts, before claiming offline operation.",
      "fa": "پوشه‌ها مرزها را نام می‌دهند: domain قواعد، application هماهنگی، data معلومات، presentation صفحه و runtime اجرای کود. این نقشه است، نه دستور ساخت. بسته را در دستگاه بدون اینترنت با آغاز اول، ذخیره، بازشدن و خط‌های همراه بررسی کنید؛ بعد کار آفلاین را تأیید کنید.",
      "ps": "پوښۍ پولې نوموي: domain قواعد، application همغږي، data معلومات، presentation پردې او runtime کوډ اجرا کوي. دا نقشه ده، د جوړولو سکریپټ نه. بسته په بې انټرنېټه وسیله کې له لومړي پیل، ساتلو، بیا پرانیستلو او لیکبڼو سره وګورئ؛ بیا آفلاین کار تایید کړئ."
    }
  ]
}''' )
