"""Authored translation triples. Technical literals intentionally retain spelling."""
UI=[]
UI.append((' · evidence saved',' · شواهد ذخیره شد',' · شواهد وساتل شول'))
def rows(text):
    for line in text.strip().splitlines():
        parts=line.split('|')
        assert len(parts)==3, line
        UI.append(tuple(s.replace('\\n','\n') for s in parts))

rows(r'''
 · evidence saved| · شواهد ذخیره شد| · شواهد وساتل شول
Absent|وجود ندارد|نشته
Partial|ناقص|نیمګړی
Meets requirements|نیازها را برآورده می‌کند|اړتیاوې پوره کوي
Improvements|بهبودها|اصلاحات
Backup exceeds 1 MB.|پشتیبان بیش از ۱ مگابایت است.|بیک‌اپ له ۱ مېګابایټه لوی دی.
Code exceeds 12,000 characters.|کد بیش از ۱۲٬۰۰۰ نویسه است.|کوډ له ۱۲٬۰۰۰ تورو زیات دی.
Bloom: {0} · {1} minutes|بلوم: {0} · {1} دقیقه|بلوم: {0} · {1} دقیقې
Lesson {0} · {1} min|درس {0} · {1} دقیقه|درس {0} · {1} دقیقې
Move line {0} down|سطر {0} را پایین ببرید|کرښه {0} ښکته کړئ
Move line {0} up|سطر {0} را بالا ببرید|کرښه {0} پورته کړئ
No prior programming; basic device and file use.|برنامه‌نویسی قبلی لازم نیست؛ کار ابتدایی با دستگاه و فایل.|مخکینی پروګرام لیکل نه غواړي؛ د آلې او فایل بنسټیزه کارونه.
Open prerequisite: {0}|بازکردن پیش‌نیاز: {0}|مخکینی کورس پرانیستل: {0}
Prerequisites: {0}|پیش‌نیازها: {0}|مخکینۍ اړتیاوې: {0}
Project brief · {0} hours|شرح پروژه · {0} ساعت|د پروژې لنډیز · {0} ساعتونه
Step {0}|گام {0}|ګام {0}
{0} hours · {1}/5 milestones self-reported\n{2}|{0} ساعت · {1}/5 مرحله به گزارش خود شاگرد\n{2}|{0} ساعتونه · {1}/5 پړاوونه په خپله راپور شوي\n{2}
{0} min  ·  {1}/{2} completed|{0} دقیقه  ·  {1}/{2} تکمیل|{0} دقیقې  ·  {1}/{2} بشپړ
{0} modules · {1} plans · {2} projects\n{3}|{0} بخش · {1} طرح · {2} پروژه\n{3}|{0} برخې · {1} پلانونه · {2} پروژې\n{3}
{0} of {1} exercises complete|{0} از {1} تمرین تکمیل|له {1} تمرینونو {0} بشپړ
{0} of {1} exercises completed. You can retry any exercise.|{0} از {1} تمرین تکمیل شده. هر تمرین را دوباره انجام داده می‌توانید.|له {1} تمرینونو {0} بشپړ دي. هر تمرین بیا کولی شئ.
{0} percent|{0} درصد|{0} سلنه
{0} total submissions · No streaks to lose. Learn at your own pace.|{0} پاسخ ثبت‌شده · زنجیرهٔ روزانه‌ای از دست نمی‌رود. با سرعت خود بیاموزید.|{0} ثبت شوي ځوابونه · ورځنۍ لړۍ نه بایلئ. په خپل سرعت زده کړئ.
{0} · 150 min|{0} · ۱۵۰ دقیقه|{0} · ۱۵۰ دقیقې
{0} · {1} minutes{2}|{0} · {1} دقیقه{2}|{0} · {1} دقیقې{2}
{0}.  {1}|{0}.  {1}|{0}.  {1}
{0} — {1}|{0} — {1}|{0} — {1}
{0} saved evidence entries across 15 curricula. Project milestones and rubric scores are self-assessed; they do not change your automatically graded Python exercise results. Open Courses to continue a plan or project.|{0} مدخل شواهد در ۱۵ برنامهٔ درسی ذخیره شده. مرحله و معیار پروژه خودارزیابی‌اند و نتیجهٔ خودکار تمرین پایتون را تغییر نمی‌دهند. برای ادامه دوره‌ها را باز کنید.|{0} شواهد په ۱۵ نصابونو کې ساتل شوي. د پروژې پړاوونه او نمرې خپله ارزونه ده او د پایتون اتومات پایلې نه بدلوي. د دوام لپاره کورسونه پرانیزئ.
This backup contains {0} completed exercises, {1} drafts, and {2} portfolio entries. It will replace the progress, saved drafts, and preferences on this device. Export your current data first if you want to keep it.|این پشتیبان {0} تمرین تکمیل، {1} پیش‌نویس و {2} مدخل دوسیه دارد. پیشرفت، پیش‌نویس و تنظیم این دستگاه را عوض می‌کند. برای حفظ دادهٔ فعلی نخست آن را صادر کنید.|دا بیک‌اپ {0} بشپړ تمرینونه، {1} مسودې او {2} دوسیې ثبتونه لري. د دې آلې پرمختګ، مسودې او تنظیمات بدلوي. د اوسنیو معلوماتو ساتلو لپاره لومړی یې صادر کړئ.
This is not a supported Learn By Marifat Team backup (version 1 or 2).|این پشتیبان پشتیبانی‌شدهٔ Learn By Marifat Team (نسخهٔ ۱ یا ۲) نیست.|دا د Learn By Marifat Team ملاتړ شوی بیک‌اپ (نسخه ۱ یا ۲) نه دی.
Invalid attempts in backup.|تلاش‌های پشتیبان نامعتبر است.|په بیک‌اپ کې هڅې نامعتبرې دي.
Invalid code drafts in backup.|پیش‌نویس کد پشتیبان نامعتبر است.|د بیک‌اپ کوډ مسودې نامعتبرې دي.
Invalid portfolio evidence or rubric.|شواهد یا معیار دوسیه نامعتبر است.|د دوسیې شواهد یا معیار نامعتبر دی.
Invalid portfolio identifiers in backup.|شناسهٔ دوسیه در پشتیبان نامعتبر است.|په بیک‌اپ کې د دوسیې پېژندنې نامعتبرې دي.
Invalid preferences in backup.|تنظیم پشتیبان نامعتبر است.|د بیک‌اپ تنظیمات نامعتبر دي.
Invalid {0} in backup.|بخش {0} پشتیبان نامعتبر است.|د بیک‌اپ {0} برخه نامعتبره ده.
Execution timed out. Simplify the program and try again.|مهلت اجرا تمام شد. برنامه را ساده و دوباره اجرا کنید.|د اجرا وخت ختم شو. پروګرام ساده او بیا یې وچلوئ.
The practice runner could not start. Try again.|اجراکنندهٔ تمرین آغاز نشد. دوباره بکوشید.|د تمرین چلوونکی پیل نشو. بیا هڅه وکړئ.
Unsupported operation. Check the language guide.|عملیات پشتیبانی نمی‌شود. راهنمای زبان را ببینید.|عملیات ملاتړ نه لري. د ژبې لارښود وګورئ.
return must be inside a function.|return باید داخل تابع باشد.|return باید د دندې دننه وي.
Line {0}: {1}|سطر {0}: {1}|کرښه {0}: {1}
Programs are limited to 12,000 characters.|برنامه به ۱۲٬۰۰۰ نویسه محدود است.|پروګرام تر ۱۲٬۰۰۰ تورو محدود دی.
Use four spaces instead of tabs.|به‌جای تب چهار فاصله بدهید.|د ټب پر ځای څلور تش ځایونه وکاروئ.
Indentation must use groups of four spaces.|تورفتگی باید گروه‌های چهار فاصله باشد.|دننه‌کول باید د څلورو تشو ځایونو ډلې وي.
Unexpected indentation.|تورفتگی غیرمنتظره.|ناڅاپي دننه‌کول.
Execution limit reached. Check your loop condition.|حد اجرا رسید. شرط حلقه را بررسی کنید.|د اجرا حد پوره شو. د کړۍ شرط وګورئ.
Output limit reached (16,000 characters).|حد خروجی (۱۶٬۰۰۰ نویسه) رسید.|د وتۍ حد (۱۶٬۰۰۰ توري) پوره شو.
This operation needs a number.|این عملیات عدد می‌خواهد.|دا عملیات عدد غواړي.
Nested value exceeds the practice limit.|مقدار تودرتو از حد تمرین بیشتر است.|دننه ارزښت د تمرین له حده زیات دی.
Value is too large for the practice runner.|مقدار برای اجراکنندهٔ تمرین بسیار بزرگ است.|ارزښت د تمرین چلوونکي لپاره ډېر لوی دی.
Number exceeds the practice limit.|عدد از حد تمرین بیشتر است.|عدد د تمرین له حده زیات دی.
Nesting limit reached.|حد تودرتویی رسید.|د دننه‌والي حد پوره شو.
Expected an indented block.|بلوک تورفته لازم است.|دننه شوی بلوک اړین دی.
Add a colon after the condition.|پس از شرط دونقطه اضافه کنید.|له شرط وروسته دوه‌ټکي زیات کړئ.
Use unique, simple parameter names.|نام ساده و یکتای پارامتر به‌کار برید.|ساده او یکتا پارامېټر نومونه وکاروئ.
A for loop needs a list, string, or range.|حلقهٔ for فهرست، رشته یا range می‌خواهد.|for کړۍ لېست، متن‌لړۍ یا range غواړي.
Nested functions are outside this runner.|تابع تودرتو در این اجراکننده پشتیبانی نمی‌شود.|دننه دندې په دې چلوونکي کې ملاتړ نه لري.
Name "{0}" is not defined.|نام "{0}" تعریف نشده است.|نوم "{0}" نه دی تعریف شوی.
Index a list or string with an integer.|اندیس فهرست یا رشته باید عدد صحیح باشد.|د لېست یا متن اندېکس باید صحیح عدد وي.
Index is outside the sequence.|اندیس بیرون دنباله است.|اندېکس له لړۍ بهر دی.
String repetition exceeds the limit.|تکرار رشته بیش از حد است.|د متن تکرار له حده زیات دی.
Cannot divide by zero.|تقسیم بر صفر ممکن نیست.|پر صفر تقسیم نشي کېدای.
Unsupported operator {0}.|عملگر {0} پشتیبانی نمی‌شود.|عملګر {0} ملاتړ نه لري.
{0} needs {1} argument(s).|{0} به {1} آرگومان نیاز دارد.|{0} ته {1} آرګومېنټونه اړین دي.
len needs a list or string.|len فهرست یا رشته می‌خواهد.|len لېست یا متن‌لړۍ غواړي.
Cannot convert this value to an integer.|این مقدار به عدد صحیح تبدیل نمی‌شود.|دا ارزښت صحیح عدد ته نه بدلېږي.
range needs 1 to 3 integers.|range یک تا سه عدد صحیح می‌خواهد.|range له یوه تر دریو صحیح عددونو غواړي.
range step cannot be zero.|گام range صفر شده نمی‌تواند.|د range ګام صفر نشي کېدای.
range is limited to 1,000 items.|range به ۱٬۰۰۰ عضو محدود است.|range تر ۱٬۰۰۰ غړو محدود دی.
Function "{0}" is unavailable. See the language guide.|تابع "{0}" موجود نیست. راهنمای زبان را ببینید.|دنده "{0}" نشته. د ژبې لارښود وګورئ.
Function call depth limit reached.|حد عمق فراخوانی تابع رسید.|د دندې د بللو ژوروالي حد پوره شو.
Unfinished string escape.|نویسهٔ گریز رشته ناتمام است.|د متن escape نیمګړی دی.
Unsupported string escape.|نویسهٔ گریز رشته پشتیبانی نمی‌شود.|د متن escape ملاتړ نه لري.
Close the string with a matching quote.|رشته را با نقل قول مطابق ببندید.|متن‌لړۍ په ورته نقل قول وتړئ.
Unsupported character "{0}". See the language guide.|نویسهٔ "{0}" پشتیبانی نمی‌شود. راهنمای زبان را ببینید.|توری "{0}" ملاتړ نه لري. د ژبې لارښود وګورئ.
Unexpected "{0}".|"{0}" غیرمنتظره است.|"{0}" ناڅاپي دی.
Expected "{0}".|"{0}" لازم است.|"{0}" اړین دی.
Expression nesting limit reached.|حد تودرتویی عبارت رسید.|د عبارت دننه‌والي حد پوره شو.
Use and between comparisons in this runner.|در این اجراکننده میان مقایسه‌ها and بنویسید.|په دې چلوونکي کې د پرتلو ترمنځ and ولیکئ.
Expected a value, found "{0}".|مقدار لازم بود؛ "{0}" یافت شد.|ارزښت اړین و؛ "{0}" وموندل شو.
Save Learn By Marifat Team backup|ذخیرهٔ پشتیبان Learn By Marifat Team|د Learn By Marifat Team بیک‌اپ ساتل
Open Learn By Marifat Team backup|بازکردن پشتیبان Learn By Marifat Team|د Learn By Marifat Team بیک‌اپ پرانیستل
''')

rows(r'''
(no output)|(خروجی ندارد)|(وتۍ نشته)
+ 4 spaces|+ ۴ فاصله|+ ۴ تش ځایونه
100% offline|کاملا آفلاین|بشپړ آفلاین
15 guided hours + 42 project hours|۱۵ ساعت راهنمایی + ۴۲ ساعت پروژه|۱۵ لارښود ساعتونه + ۴۲ د پروژې ساعتونه
15 offline curricula · 180 lesson plans · 45 practical projects|۱۵ برنامهٔ درسی آفلاین · ۱۸۰ طرح درس · ۴۵ پروژهٔ عملی|۱۵ آفلاین نصابونه · ۱۸۰ درسي پلانونه · ۴۵ عملي پروژې
A backup you can carry.|پشتیبان قابل انتقال.|لېږدېدونکی بیک‌اپ.
A foundation you can build on.|بنیادی برای ساختن.|د جوړولو لپاره بنسټ.
A learning interpreter, not full CPython|مفسر آموزشی؛ نه CPython کامل|ښوونیز مفسر؛ بشپړ CPython نه دی
A little practice.\nA world of possibility.|اندکی تمرین.\nدنیایی از امکان.|لږ تمرین.\nد امکاناتو نړۍ.
A small challenge.|یک چالش کوچک.|یوه کوچنۍ ننګونه.
A softer workspace in low light|محیط ملایم‌تر در نور کم|په کمه رڼا کې نرم کاري چاپېریال
Acceptance conditions|شرط‌های پذیرش|د منلو شرطونه
All 15 courses|همهٔ ۱۵ دوره|ټول ۱۵ کورسونه
Appearance|ظاهر|بڼه
Arrange the code|کد را مرتب کنید|کوډ برابر کړئ
Assessment evidence|شواهد ارزیابی|د ارزونې شواهد
Assignments with acceptance conditions. Build them using the listed tools; the app stores your reflection and self-assessment, not external project files.|تمرین‌ها شرط پذیرش دارند. با ابزار فهرست‌شده بسازید؛ برنامه بازاندیشی و خودارزیابی را ذخیره می‌کند، نه فایل بیرونی پروژه را.|تمرینونه د منلو شرطونه لري. په یادو وسایلو یې جوړ کړئ؛ اپ ستاسې بیاکتنه او خپله ارزونه ساتي، نه بهرني پروژوي فایلونه.
Back to lesson|بازگشت به درس|درس ته ستنېدل
Backup exported. Keep a copy outside this device.|پشتیبان صادر شد. یک نسخه بیرون دستگاه نگه دارید.|بیک‌اپ صادر شو. یوه کاپي له دې آلې بهر وساتئ.
Backup restored, including saved code drafts.|پشتیبان همراه پیش‌نویس کد بازیابی شد.|بیک‌اپ له ساتلو کوډ مسودو سره بېرته راوړل شو.
Before moving on|پیش از ادامه|له وړاندې تلو مخکې
Before you begin|پیش از آغاز|له پیل مخکې
Bloom alignment|هم‌سویی با بلوم|له بلوم سره سمون
Bookmark lesson|نشانی‌کردن درس|درس نښه کول
Bookmarked lessons|درس‌های نشانی‌شده|نښه شوي درسونه
Built for independent practice. All lessons are available from the first launch.|برای تمرین مستقل ساخته شده؛ همهٔ درس‌ها از نخستین آغاز در دسترس‌اند.|د خپلواک تمرین لپاره جوړ شوی؛ ټول درسونه له لومړي پیل شته.
By Marifat Team|از تیم معرفت|د معرفت ټیم له خوا
Cancel|لغو|لغوه
Check answer|بررسی پاسخ|ځواب کتل
Check readiness|بررسی آمادگی|چمتووالی کتل
Check your understanding|فهم خود را بررسی کنید|خپله پوهه وګورئ
Choose your course.|دورهٔ خود را انتخاب کنید.|خپل کورس وټاکئ.
Code lab|لابراتوار کد|د کوډ لابراتوار
Continue learning|ادامهٔ یادگیری|زده‌کړې ته دوام
Correctness|درستی|سموالی
Could not save or read your data. Please try again.|ذخیره یا خواندن داده نشد. دوباره تلاش کنید.|معلومات ونه ساتل یا ونه لوستل شول. بیا هڅه وکړئ.
Course completion|تکمیل دوره|د کورس بشپړېدل
Courses|دوره‌ها|کورسونه
Dark appearance|ظاهر تیره|تیاره بڼه
Deliverables|موارد تحویل|سپارل کېدونکي توکي
Design|طراحی|ډیزاین
Discard changes|صرف‌نظر از تغییرها|بدلونونه پرېښودل
Draft saved on this device.|پیش‌نویس در دستگاه ذخیره شد.|مسوده پر دې آله وساتل شوه.
English|English|English
Every attempt is a step forward.|هر تلاش یک گام پیش است.|هره هڅه یو ګام وړاندې ده.
Evidence and reflection|شواهد و بازاندیشی|شواهد او بیاکتنه
Evidence and self-assessment saved on this device.|شواهد و خودارزیابی در دستگاه ذخیره شد.|شواهد او خپله ارزونه پر دې آله وساتل شول.
Expected output|خروجی مورد انتظار|تمه شوې وتۍ
Expected result|نتیجهٔ مورد انتظار|تمه شوې پایله
Experiment, make mistakes, and try again. Everything runs on this device.|تجربه کنید، اشتباه کنید و دوباره بکوشید. همه‌چیز روی همین دستگاه اجرا می‌شود.|تجربه، تېروتنه او بیا هڅه وکړئ. هر څه پر همدې آله چلېږي.
Explore the next lesson|درس بعدی را ببینید|بل درس وګورئ
Export backup|صدور پشتیبان|بیک‌اپ صادرول
First steps|گام‌های نخست|لومړي ګامونه
Guided practice|تمرین راهنمایی‌شده|لارښود تمرین
Hint|راهنما|لارښوونه
Ideas become code.|فکر به کد تبدیل می‌شود.|فکر په کوډ بدلېږي.
If something goes wrong|اگر مشکلی پیش آمد|که ستونزه پېښه شي
If you need another attempt|اگر تلاش دوباره لازم است|که بلې هڅې ته اړتیا وي
Interactive Python foundations|مبانی تعاملی پایتون|د پایتون متقابل بنسټونه
Keep editing|ادامهٔ ویرایش|سمون ته دوام
Keep your progress|پیشرفت را حفظ کنید|پرمختګ وساتئ
Learn|Learn|Learn
Learn By Marifat Team|Learn By Marifat Team|Learn By Marifat Team
Learn by doing|با انجام‌دادن بیاموزید|په کولو زده کړئ
Learn programming, one small step at a time. No connection needed.|برنامه‌نویسی را گام‌به‌گام بیاموزید. اتصال لازم نیست.|پروګرام لیکل ګام‌پر‌ګام زده کړئ. اړیکه نه غواړي.
Learning activity|فعالیت یادگیری|د زده‌کړې فعالیت
Learning language|زبان یادگیری|د زده‌کړې ژبه
Learning portfolio|دوسیهٔ یادگیری|د زده‌کړې دوسیه
Leave without saving?|بدون ذخیره خارج شوید؟|له ساتلو پرته وځئ؟
Local draft|پیش‌نویس محلی|محلي مسوده
Made for curious minds|برای ذهن‌های کنجکاو|د پلټونکو ذهنونو لپاره
Make it yours|مطابق میل خود سازید|خپل یې کړئ
Modules and lesson plans|بخش‌ها و طرح درس‌ها|برخې او درسي پلانونه
Move each line up or down. Keep the indentation shown.|هر سطر را بالا یا پایین ببرید. تورفتگی را حفظ کنید.|هره کرښه پورته یا ښکته کړئ. دننه‌کول وساتئ.
Need a hint?|راهنما می‌خواهید؟|لارښوونه غواړئ؟
No account, no subscription, and no connection required.|حساب، اشتراک و اتصال لازم نیست.|حساب، ګډون او اړیکه نه غواړي.
No lessons found. Try another search or turn off the bookmark filter.|درسی یافت نشد. جست‌وجوی دیگر یا خاموش‌کردن فیلتر نشانی را امتحان کنید.|درس ونه موندل شو. بل لټون وکړئ یا د نښو چاڼ بند کړئ.
No matching courses. Try another topic.|دورهٔ مطابق یافت نشد. موضوع دیگر بنویسید.|سم کورس ونه موندل شو. بله موضوع ولیکئ.
OUTPUT|خروجی|وتۍ
Offline Python subset · language guide|زیرمجموعهٔ آفلاین پایتون · راهنمای زبان|آفلاین پایتون فرعي برخه · د ژبې لارښود
Offline development tools|ابزار توسعهٔ آفلاین|د آفلاین پراختیا وسایل
Open seven interactive foundation lessons|هفت درس تعاملی مقدماتی را باز کنید|اووه متقابل بنسټیز درسونه پرانیزئ
Open-source licenses|جوازهای متن‌باز|د خلاصې سرچینې جوازونه
Overview|نمای کلی|عمومي کتنه
PYTHON FUNDAMENTALS|مبانی پایتون|د پایتون بنسټونه
Practice|تمرین|تمرین
Practice Python foundations|تمرین مبانی پایتون|د پایتون بنسټونه تمرین کړئ
Progress|پیشرفت|پرمختګ
Project milestones|مرحله‌های پروژه|د پروژې پړاوونه
Put it into practice|در عمل استفاده کنید|په عمل کې یې وکاروئ
Python foundation exercise results and your wider learning portfolio are saved on this device.|نتیجهٔ تمرین پایتون و دوسیهٔ یادگیری در این دستگاه ذخیره می‌شود.|د پایتون تمرین پایلې او د زده‌کړې دوسیه پر دې آله ساتل کېږي.
Python fundamentals|مبانی پایتون|د پایتون بنسټونه
Python practice code|کد تمرین پایتون|د پایتون تمرین کوډ
Read the code|کد را بخوانید|کوډ ولولئ
Read. Predict. Practice.\nBuild the confidence to write your own code.|بخوانید. پیش‌بینی کنید. تمرین کنید.\nاعتماد نوشتن کد خود را بسازید.|ولولئ. اټکل وکړئ. تمرین وکړئ.\nد خپل کوډ لیکلو باور جوړ کړئ.
Ready for guided practice|آمادهٔ تمرین راهنمایی‌شده|لارښود تمرین ته چمتو
Real-world projects|پروژه‌های کاربردی|عملي پروژې
Reference solution — open after trying|راه‌حل نمونه — پس از تلاش باز کنید|نمونوي حل — له هڅې وروسته یې پرانیزئ
Replace & restore|جایگزینی و بازیابی|بدلول او بېرته راوړل
Reproducibility|تکرارپذیری|بیا ترسره کېدنه
Restore backup|بازیابی پشتیبان|بیک‌اپ بېرته راوړل
Restore this backup?|این پشتیبان بازیابی شود؟|دا بیک‌اپ بېرته راوړل شي؟
Retrieval 10 min → design 15 → implementation 35 → testing and review 20 → reflection 10.|یادآوری ۱۰ دقیقه ← طراحی ۱۵ ← پیاده‌سازی ۳۵ ← آزمون و بازبینی ۲۰ ← بازاندیشی ۱۰.|یادونه ۱۰ دقیقې ← ډیزاین ۱۵ ← پلي کول ۳۵ ← ازموینه او کتنه ۲۰ ← بیا فکر ۱۰.
Retrieval 5 min → worked explanation 15 → guided practice 20 → assessment 15 → reflection 5.|یادآوری ۵ دقیقه ← توضیح نمونه ۱۵ ← تمرین راهنمایی‌شده ۲۰ ← ارزیابی ۱۵ ← بازاندیشی ۵.|یادونه ۵ دقیقې ← د نمونې تشریح ۱۵ ← لارښود تمرین ۲۰ ← ارزونه ۱۵ ← بیا فکر ۵.
Review and try again|بازبینی و تلاش دوباره|بیاکتنه او بیا هڅه
Review the course|مرور دوره|کورس بیا کتل
Review the example, adjust your answer, and retry.|نمونه را مرور، پاسخ را اصلاح و دوباره تلاش کنید.|نمونه وګورئ، ځواب سم او بیا هڅه وکړئ.
Run & check|اجرا و بررسی|چلول او کتل
Run code|اجرای کد|کوډ چلول
Running…|در حال اجرا…|د چلولو په حال کې…
Save draft|ذخیرهٔ پیش‌نویس|مسوده ساتل
Save evidence|ذخیرهٔ شواهد|شواهد ساتل
Save evidence • unsaved changes|ذخیرهٔ شواهد • تغییر ذخیره‌نشده|شواهد ساتل • نه‌ساتل شوي بدلونونه
Saving…|در حال ذخیره…|د ساتلو په حال کې…
Search courses, topics, or projects|جست‌وجوی دوره، موضوع یا پروژه|کورس، موضوع یا پروژه ولټوئ
Search lessons and concepts|جست‌وجوی درس و مفهوم|درسونه او مفاهیم ولټوئ
See how far you have come|پیشرفت خود را ببینید|خپل پرمختګ وګورئ
Self-assessment rubric|معیار خودارزیابی|د خپلې ارزونې معیارونه
Session plan|طرح جلسه|د ناستې پلان
Settings|تنظیمات|تنظیمات
Seven guided lessons. Learn in order, or revisit a concept whenever you need it.|هفت درس راهنمایی‌شده. به ترتیب بیاموزید یا هر زمان مفهوم را مرور کنید.|اووه لارښود درسونه. په ترتیب زده کړئ یا هر وخت مفهوم بیا وګورئ.
Small steps.\nReal understanding.|گام‌های کوچک.\nفهم واقعی.|کوچني ګامونه.\nرښتینې پوهه.
Start here — no guessing|از این‌جا آغاز کنید — بدون حدس|له دې ځایه پیل — له اټکل پرته
Start learning|آغاز یادگیری|زده‌کړه پیل کړئ
Take one step at a time. Read, predict, try, and explain.|هر بار یک گام. بخوانید، پیش‌بینی، تمرین و توضیح دهید.|هر ځل یو ګام. ولولئ، اټکل، تمرین او تشریح وکړئ.
The complete course|دورهٔ کامل|بشپړ کورس
Try again — you are learning.|دوباره بکوشید — در حال یادگیری هستید.|بیا هڅه وکړئ — زده‌کړه کوئ.
Unsaved changes|تغییرهای ذخیره‌نشده|نه‌ساتل شوي بدلونونه
Usability / accessibility|کاربردپذیری / دسترس‌پذیری|کارېدنه / لاسرسی
Use fictional data. Save before leaving this page. External files are not attached to the app backup.|دادهٔ فرضی به‌کار برید. پیش از خروج ذخیره کنید. فایل بیرونی ضمیمهٔ پشتیبان نیست.|فرضي معلومات وکاروئ. له پاڼې وتلو مخکې وساتئ. بهرني فایلونه د اپ بیک‌اپ برخه نه دي.
Use four spaces for indentation. Save or run to keep your draft.|برای تورفتگی چهار فاصله بدهید. برای حفظ پیش‌نویس ذخیره یا اجرا کنید.|د دننه کولو لپاره څلور تش ځایونه وکاروئ. د مسودې ساتلو لپاره یې وساتئ یا وچلوئ.
Verification|بررسی|تایید
Vocabulary, setup, a worked example, guided practice, and a readiness check|واژگان، آماده‌سازی، نمونه، تمرین راهنمایی‌شده و بررسی آمادگی|لغتونه، چمتووالی، حل شوې نمونه، لارښود تمرین او د چمتووالي کتنه
What did you build? Which tests passed or failed? Record file names, decisions, feedback, and your next improvement.|چه ساختید؟ کدام آزمون موفق یا ناموفق شد؟ نام فایل، تصمیم، بازخورد و بهبود بعدی را ثبت کنید.|څه مو جوړ کړل؟ کومې ازموینې بریالۍ یا ناکامې شوې؟ د فایل نومونه، پرېکړې، غبرګون او بل اصلاح ثبت کړئ.
Words you will use|واژه‌های لازم|کارېدونکي لغتونه
Worked example|نمونهٔ توضیح‌شده|تشریح شوې نمونه
Worked example / design fragment — use the course toolchain|نمونه / قطعهٔ طراحی — از ابزار دوره استفاده کنید|نمونه / ډیزاین ټوټه — د کورس وسایل وکاروئ
Write a program|برنامه بنویسید|پروګرام ولیکئ
You completed Python fundamentals! Try rewriting the examples without looking, then test your understanding on a full Python environment.|مبانی پایتون را تکمیل کردید! نمونه را بدون دیدن بازنویسی و سپس در محیط کامل پایتون فهم خود را بیازمایید.|د پایتون بنسټونه مو بشپړ کړل! نمونې له کتلو پرته بیا ولیکئ او بیا خپله پوهه په بشپړ پایتون چاپېریال وازمویئ.
You identified the result. Now explain why it happens, then try the task below.|نتیجه را شناختید. اکنون علت را توضیح و کار زیر را انجام دهید.|پایله مو وپېژندله. اوس یې علت ووایئ او لاندې کار وکړئ.
Your latest evidence and self-assessment changes have not been saved.|آخرین تغییر شواهد و خودارزیابی ذخیره نشده است.|ستاسې وروستي شواهد او د خپلې ارزونې بدلونونه نه دي ساتل شوي.
Your learning path|مسیر یادگیری شما|ستاسې د زده‌کړې لاره
Your learning. Your device.|یادگیری شما. دستگاه شما.|ستاسې زده‌کړه. ستاسې آله.
Your next chapter starts here.|فصل بعدی شما از این‌جا آغاز می‌شود.|ستاسې بل فصل له دې ځایه پیلېږي.
Your offline workspace|محیط کار آفلاین شما|ستاسې آفلاین کاري ځای
Your output will appear here.|خروجی شما این‌جا نمایش می‌یابد.|ستاسې وتۍ به دلته ښکاره شي.
Your turn to code.|نوبت کدنویسی شماست.|د کوډ لیکلو وار مو دی.
course progress|پیشرفت دوره|د کورس پرمختګ
exercises completed|تمرین تکمیل‌شده|بشپړ شوي تمرینونه
guided lessons|درس راهنمایی‌شده|لارښود درسونه
main.py|main.py|main.py
✓ Nicely done. Progress saved.|✓ خوب انجام شد. پیشرفت ذخیره شد.|✓ ښه ترسره شو. پرمختګ وساتل شو.
''')
rows(r'''
0 = absent; 1 = partial with major gaps; 2 = meets requirements with evidence; 3 = meets requirements plus justified edge-case improvements. Aim for every dimension at least 2 and every acceptance condition demonstrated. A teacher or peer should review the evidence; this is not automatic certification.|۰ = وجود ندارد؛ ۱ = ناقص با کمبود جدی؛ ۲ = نیازها با شواهد برآورده شده؛ ۳ = نیازها همراه بهبود مستدل حالت مرزی. هر بُعد دست‌کم ۲ و هر شرط پذیرش نشان داده شود. معلم یا هم‌صنفی شواهد را بررسی کند؛ این تصدیق خودکار نیست.|۰ = نشته؛ ۱ = نیمګړی له لویو تشو؛ ۲ = اړتیاوې له شواهدو پوره؛ ۳ = اړتیاوې او مستدل سرحدي اصلاحات. هر بُعد لږ تر لږه ۲ او هر منلو شرط ثابت کړئ. ښوونکی یا همزولی دې شواهد وګوري؛ دا اتومات سند نه دی.
Check the file name, capital letters, quotes, brackets, and indentation against the example. Make one change at a time. Save before running. A missing compiler or package is a setup issue: use the listed provisioned tools or ask your teacher; repeated code edits will not install it.|نام فایل، حروف بزرگ، نقل قول، قوس و تورفتگی را با نمونه مقایسه کنید. هر بار یک تغییر بدهید. پیش از اجرا ذخیره کنید. کامپایلر یا بستهٔ گم‌شده مشکل آماده‌سازی است: از ابزار آماده استفاده یا از معلم کمک بخواهید؛ ویرایش مکرر کد آن را نصب نمی‌کند.|د فایل نوم، لوی توري، نقل قول، قوسونه او دننه‌کول له نمونې سره وګورئ. هر ځل یو بدلون وکړئ. له چلولو مخکې وساتئ. ورک کمپایلر یا بسته د چمتووالي ستونزه ده: چمتو وسایل وکاروئ یا له ښوونکي مرسته وغواړئ؛ تکراري کوډ سمون یې نه نصبوي.
Choose English, Dari, or Pashto for the interface and learning content. Code and program output keep their original spelling. Translations still require native-speaker review.|برای رابط و محتوا انگلیسی، دری یا پشتو انتخاب کنید. نوشتار کد و خروجی اصلی می‌ماند. ترجمه هنوز بررسی گویندهٔ بومی می‌خواهد.|د مخپاڼې او محتوا لپاره انګلیسي، دري یا پښتو وټاکئ. کوډ او وتۍ خپل اصلي لیکدود ساتي. ژباړې لا د بومي ویونکي کتنې ته اړتیا لري.
Estimates exclude additional practice. Plans progress from foundations to an independent capstone. Completion requires evidence, not simply reading.|زمان تخمینی تمرین اضافی را شامل نمی‌شود. طرح‌ها از مبانی به پروژهٔ مستقل می‌روند. تکمیل شواهد می‌خواهد، نه تنها خواندن.|اټکل شوی وخت اضافي تمرین نه رانغاړي. پلانونه له بنسټونو خپلواکې پروژې ته ځي. بشپړېدل شواهد غواړي، نه یوازې لوستل.
Export progress and saved code to a JSON file. Transfer it using local storage or USB. Uninstalling the app can erase local data. Backups are readable files; store them where you trust.|پیشرفت و کد ذخیره‌شده را به JSON صادر و با ذخیرهٔ محلی یا USB منتقل کنید. حذف برنامه ممکن است دادهٔ محلی را پاک کند. پشتیبان خواندنی است؛ در جای مطمئن نگه دارید.|پرمختګ او ساتلی کوډ JSON ته صادر او په محلي ساتنه یا USB ولېږدوئ. د اپ لرې کول محلي معلومات پاکولی شي. بیک‌اپ لوستل کېدونکی دی؛ په باوري ځای یې وساتئ.
Keep source files, a README with local build/run instructions, fictional fixtures, test results, a component diagram, one architecture decision, and a demonstration in your external project folder. Record their names and your findings below. Back up those files separately.|منبع، README با راهنمای ساخت و اجرای محلی، دادهٔ فرضی، نتیجهٔ آزمون، نمودار اجزا، یک تصمیم معماری و نمایش را در پوشهٔ بیرونی پروژه نگه دارید. نام و یافته را پایین ثبت و فایل‌ها را جدا پشتیبان بگیرید.|سرچینه، README له محلي جوړولو او چلولو لارښوونو، فرضي نمونې، د ازموینې پایلې، د اجزاوو انځور، یوه معماري پرېکړه او ننداره په بهرني پروژوي پوښۍ کې وساتئ. نومونه او موندنې لاندې ثبت او فایلونه جلا بیک‌اپ کړئ.
Learn By Marifat Team 1.1 · 15 offline curricula\nOriginal course content. A local-first learning application for Afghan CS students. No analytics, remote services, or online activation. Practice scores are learning aids, not formal credentials.|Learn By Marifat Team 1.1 · ۱۵ برنامهٔ درسی آفلاین\nمحتوای تألیفی برای شاگردان کمپیوترساینس افغانستان. بدون تحلیل‌گر، خدمت دور یا فعال‌سازی آنلاین. نمرهٔ تمرین کمک یادگیری است، نه سند رسمی.|Learn By Marifat Team 1.1 · ۱۵ آفلاین نصابونه\nد افغانستان د کمپیوټرساینس زده‌کوونکو لپاره تألیفي محتوا. تحلیل، لیرې خدمت یا آنلاین فعالول نشته. تمرین نمرې د زده‌کړې مرسته ده، نه رسمي سند.
Reduce the example to one record. Trace each state change on paper, explain the failure, then try again with a different input. For an extension, add one justified requirement and regression tests.|نمونه را به یک رکورد کم کنید. تغییر حالت را روی کاغذ دنبال، شکست را توضیح و با ورودی دیگر دوباره امتحان کنید. برای گسترش یک نیاز مستدل و آزمون بازگشت خطا بیفزایید.|نمونه یوه ریکارډ ته کمه کړئ. د حالت بدلون پر کاغذ تعقیب، ناکامي تشریح او په بل ننوت بیا هڅه وکړئ. د غځولو لپاره یوه مستدله اړتیا او د تېروتنې د بیا راتګ ازموینې ورزیاتې کړئ.
Remember the relevant concepts; explain the data flow; apply techniques to implement requirements; analyze failing cases; evaluate alternatives against tests and usability; create an original working solution and demonstrate it.|مفهوم را به‌یاد آورید؛ جریان داده را توضیح دهید؛ فن را برای نیاز به‌کار برید؛ شکست را تحلیل کنید؛ گزینه‌ها را با آزمون و کاربردپذیری بسنجید؛ راه‌حل تازهٔ فعال بسازید و نشان دهید.|مفاهیم یاد کړئ؛ د معلوماتو بهیر تشریح کړئ؛ تخنیکونه د اړتیاوو لپاره وکاروئ؛ ناکامي وشنئ؛ بدیلونه په ازموینو او کارېدنه وسنجوئ؛ نوی فعال حل جوړ او وښیئ.
Return to the numbered explanation. Trace each line in order and distinguish code from displayed output. You can retry without losing progress.|به توضیح شماره‌دار برگردید. هر سطر را به ترتیب دنبال و کد را از خروجی جدا کنید. تلاش دوباره پیشرفت را حذف نمی‌کند.|شمېره‌لرونکې تشریح ته ستانه شئ. هره کرښه په ترتیب تعقیب او کوډ له وتۍ جلا کړئ. له پرمختګ بایللو پرته بیا هڅه کولی شئ.
Run or trace your solution, compare the result, and explain each line in your own words. Change one value and predict the new result. If you cannot yet explain it, repeat this lesson before the next module.|راه‌حل را اجرا یا دنبال کنید، نتیجه را مقایسه و هر سطر را به زبان خود توضیح دهید. یک مقدار را عوض و نتیجه را پیش‌بینی کنید. اگر توضیح داده نمی‌توانید، پیش از بخش بعد درس را تکرار کنید.|خپل حل وچلوئ یا تعقیب، پایله پرتله او هره کرښه په خپلو کلمو تشریح کړئ. یو ارزښت بدل او نوې پایله اټکل کړئ. که یې لا نشئ تشریح کولی، له بلې برخې مخکې درس تکرار کړئ.
Study every plan here and save your evidence locally. The Code lab runs a limited Python subset. Other programming work uses a separately provisioned local toolchain.|هر طرح را این‌جا بخوانید و شواهد را محلی ذخیره کنید. لابراتوار کد زیرمجموعهٔ محدود پایتون را اجرا می‌کند. کارهای دیگر ابزار محلی جداگانهٔ آماده می‌خواهند.|هر پلان دلته ولولئ او شواهد محلي وساتئ. د کوډ لابراتوار د پایتون محدوده برخه چلوي. نور پروګرامي کارونه جلا چمتو محلي وسایل غواړي.
Supported: numbers, strings, booleans, lists, variables, arithmetic, comparisons, and/or/not, if/else, for, while, simple top-level functions and return. Built-ins: print, range, len, str, int. List and string indexing are supported. Use four-space indentation.\n\nNot supported: imports, packages, input(), files, networking, classes, exceptions, f-strings, list methods, keyword/default arguments, closures, chained comparisons, break/continue, or full Python semantics. Names use Latin letters. String indexing uses UTF-16 units in this version.\n\nLimits: 12,000 code characters, 20,000 execution steps, 1,000 list/range items, 16,000 output characters, 32 function calls deep, and a 3-second worker timeout. Each run starts with fresh variables.\n\nCoding exercises compare displayed output. They do not prove that a particular algorithm was used. Use these for practice, not secure examinations.|پشتیبانی: عدد، رشته، مقدار منطقی، فهرست، متغیر، حساب، مقایسه، and/or/not، if/else، for، while، تابع سادهٔ سطح بالا و return. توابع آماده: print، range، len، str و int. اندیس رشته و فهرست پشتیبانی می‌شود. چهار فاصله تورفتگی بدهید.\n\nبدون پشتیبانی: import، بسته، input()، فایل، شبکه، کلاس، استثنا، f-string، روش فهرست، آرگومان نام‌دار یا پیش‌فرض، closure، مقایسهٔ زنجیره‌ای، break/continue و معنای کامل پایتون. نام‌ها با حروف لاتین‌اند. اندیس رشته در این نسخه واحد UTF-16 دارد.\n\nحدود: ۱۲٬۰۰۰ نویسهٔ کد، ۲۰٬۰۰۰ گام اجرا، ۱٬۰۰۰ عضو فهرست یا range، ۱۶٬۰۰۰ نویسهٔ خروجی، عمق ۳۲ فراخوانی تابع و مهلت ۳ ثانیهٔ کارگر. هر اجرا متغیر تازه دارد.\n\nتمرین کد خروجی نمایش‌داده‌شده را مقایسه می‌کند و الگوریتم خاص را ثابت نمی‌کند. برای تمرین استفاده کنید، نه امتحان امن.|ملاتړ: عددونه، متن‌لړۍ، منطقي ارزښتونه، لېستونه، متغیرونه، حساب، پرتله، and/or/not، if/else، for، while، ساده لوړې دندې او return. چمتو دندې: print، range، len، str او int. د لېست او متن اندېکس ملاتړ شته. څلور تش ځایه دننه کړئ.\n\nبې‌ملاتړه: import، بسته، input()، فایل، شبکه، کلاس، استثنا، f-string، د لېست مېتود، نوم‌لرونکی یا اصلي آرګومېنټ، closure، ځنځیري پرتله، break/continue او بشپړه پایتون معنا. نومونه لاتین توري لري. د متن اندېکس په دې نسخه کې UTF-16 واحدونه کاروي.\n\nحدونه: ۱۲٬۰۰۰ د کوډ توري، ۲۰٬۰۰۰ د اجرا ګامونه، ۱٬۰۰۰ د لېست یا range غړي، ۱۶٬۰۰۰ د وتۍ توري، ۳۲ د دندو ژوروالی او د کارګر ۳ ثانیې مهلت. هر چلول نوي متغیرونه لري.\n\nکوډ تمرین ښودل شوې وتۍ پرتله کوي او ځانګړی الگوریتم نه ثابتوي. د تمرین لپاره یې وکاروئ، نه د خوندي امتحان لپاره.
''')

rows(r'''
Your first program|نخستین برنامهٔ شما|ستاسې لومړی پروګرام
Turn an idea into an instruction.|فکر را به دستور تبدیل کنید.|فکر په لارښوونه بدل کړئ.
A program is a sequence of instructions. Python runs statements from top to bottom. The print() function displays a value. Put text inside matching quotes. A line beginning with # is a comment: it explains the code to a person and is not executed.\n\nTry predicting the output before running each example. This habit builds your ability to trace a program rather than guess what it does.|برنامه دنبالهٔ دستورهاست. پایتون دستور را از بالا به پایین اجرا می‌کند. print() مقدار را نشان می‌دهد. متن را میان نقل قول‌های هماهنگ بگذارید. سطر آغازشده با # توضیح است: کد را برای انسان شرح می‌دهد و اجرا نمی‌شود.\n\nپیش از اجرای هر نمونه خروجی را پیش‌بینی کنید. این عادت توانایی دنبال‌کردن برنامه را به‌جای حدس‌زدن تقویت می‌کند.|پروګرام د لارښوونو لړۍ ده. پایتون امرونه له پاسه ښکته چلوي. print() ارزښت ښيي. متن د یو شان نقل قول نښو ترمنځ کېږدئ. له # پیل شوې کرښه تبصره ده: انسان ته کوډ تشریح کوي او نه اجرا کېږي.\n\nله هرې نمونې چلولو مخکې وتۍ اټکل کړئ. دا عادت د اټکل پر ځای د پروګرام د تعقیب وړتیا پیاوړې کوي.
Programs run in order. Quotes turn words into string values.|برنامه به ترتیب اجرا می‌شود. نقل قول واژه را به رشته تبدیل می‌کند.|پروګرام په ترتیب چلېږي. نقل قول کلمې متن‌لړۍ ګرځوي.
What does print("Salam") display?|print("Salam") چه نشان می‌دهد؟|print("Salam") څه ښيي؟
Quotes mark the beginning and end of a string. They are not part of the displayed text.|نقل قول آغاز و پایان رشته را مشخص می‌کند و جزء متن نمایش‌داده‌شده نیست.|نقل قول د متن‌لړۍ پیل او پای ښيي او د ښکاره متن برخه نه ده.
"Salam" including the quotes|"Salam" همراه نقل قول‌ها|"Salam" له نقل قول نښو سره
Arrange the lines to display First, then Second.|سطرها را طوری مرتب کنید که نخست First و سپس Second نشان داده شود.|کرښې داسې برابرې کړئ چې لومړی First او بیا Second ښکاره شي.
The first statement runs before the second statement.|دستور اول پیش از دستور دوم اجرا می‌شود.|لومړی امر له دویم مخکې اجرا کېږي.
Display Salam on one line and Kabul on the next.|Salam را در یک سطر و Kabul را در سطر بعد نشان دهید.|Salam په یوه او Kabul په بله کرښه وښیئ.
Each print() call finishes its output with a new line.|هر فراخوانی print() خروجی را با سطر تازه پایان می‌دهد.|هر print() خپل وتۍ په نوې کرښه ختموي.
Use print("Salam") and then another print statement.|print("Salam") و سپس یک دستور print دیگر به‌کار برید.|print("Salam") او بیا بل print امر وکاروئ.
Names that remember|نام‌هایی که نگه می‌دارند|نومونه چې یاد ساتي
Store and update information.|معلومات را ذخیره و به‌روز کنید.|معلومات وساتئ او تازه کړئ.
A variable gives a name to a value. The assignment operator = evaluates the expression on its right and stores the result under the name on its left.\n\nIn students = students + 1, Python reads the old value first, adds one, and then replaces it. This is an update, not a mathematical equation. Use descriptive names such as student_count. Names are case-sensitive: score and Score are different.|متغیر به مقدار نام می‌دهد. عملگر = عبارت سمت راست را حساب و نتیجه را زیر نام سمت چپ ذخیره می‌کند.\n\nدر students = students + 1، پایتون ابتدا مقدار قبلی را می‌خواند، یک می‌افزاید و سپس جایگزین می‌کند. این به‌روزرسانی است، نه معادلهٔ ریاضی. نام روشن مانند student_count به‌کار برید. حروف بزرگ و کوچک فرق دارند: score و Score متفاوت‌اند.|متغیر ارزښت ته نوم ورکوي. د = عملګر ښي اړخ عبارت محاسبه او پایله د چپ اړخ په نوم ساتي.\n\nپه students = students + 1 کې پایتون لومړی پخوانی ارزښت لولي، یو ورزیاتوي او بیا یې بدلوي. دا تازه کول دي، نه ریاضي معادله. روښانه نومونه لکه student_count وکاروئ. لوی او کوچني توري توپیر لري: score او Score جلا دي.
Assignment stores a value; later assignments can replace it.|مقداردهی مقدار را نگه می‌دارد؛ مقداردهی بعدی می‌تواند آن را عوض کند.|ټاکنه ارزښت ساتي؛ راتلونکې ټاکنه یې بدلولی شي.
After x = 4 and x = x + 3, what is x?|پس از x = 4 و x = x + 3، مقدار x چیست؟|له x = 4 او x = x + 3 وروسته x څو دی؟
The old value 4 is read, 3 is added, and 7 is stored in x.|مقدار قبلی 4 خوانده، 3 افزوده و 7 در x ذخیره می‌شود.|پخوانی 4 لوستل کېږي، 3 ورزیاتېږي او 7 په x کې ساتل کېږي.
Create a score, increase it, then display it.|نمره بسازید، افزایش دهید و سپس نشان دهید.|نمره جوړه، زیاته او بیا یې وښیئ.
Define a variable before reading it. Print after the update to see the new value.|پیش از خواندن متغیر را تعریف کنید. برای دیدن مقدار تازه پس از تغییر چاپ کنید.|متغیر له لوستلو مخکې تعریف کړئ. د نوي ارزښت لیدلو لپاره له بدلون وروسته چاپ وکړئ.
Create books with value 12, add 3, and print the result.|books را با مقدار 12 بسازید، 3 بیفزایید و نتیجه را چاپ کنید.|books په 12 جوړ، 3 ورزیات او پایله چاپ کړئ.
The updated value is 15.|مقدار تازه 15 است.|نوی ارزښت 15 دی.
Assign books = books + 3 before print(books).|پیش از print(books)، دستور books = books + 3 را بنویسید.|له print(books) مخکې books = books + 3 ولیکئ.
Work with numbers|کار با عددها|له عددونو سره کار
Calculate, compare, and predict.|حساب، مقایسه و پیش‌بینی کنید.|محاسبه، پرتله او وړاندوینه وکړئ.
Use +, -, *, and / for addition, subtraction, multiplication, and division. Multiplication and division happen before addition and subtraction. Parentheses make the order explicit. // is floor division and % gives the remainder.\n\nFor 17 books shared among 5 students, 17 // 5 is 3 and 17 % 5 is 2. Each student gets three books and two remain. Division by zero is an error; check your inputs before dividing.|برای جمع، تفریق، ضرب و تقسیم از +، -، * و / استفاده کنید. ضرب و تقسیم پیش از جمع و تفریق انجام می‌شوند. قوس ترتیب را روشن می‌کند. // تقسیم کف و % باقی‌مانده را می‌دهد.\n\nبرای 17 کتاب بین 5 شاگرد، 17 // 5 برابر 3 و 17 % 5 برابر 2 است. هر شاگرد سه کتاب می‌گیرد و دو می‌ماند. تقسیم بر صفر خطاست؛ پیش از تقسیم ورودی را بررسی کنید.|د جمع، تفریق، ضرب او تقسیم لپاره +، -، * او / وکاروئ. ضرب او تقسیم له جمع او تفریق مخکې کېږي. قوسونه ترتیب څرګندوي. // ښکته صحیح تقسیم او % پاتې شونی ورکوي.\n\nد 17 کتابونو او 5 زده‌کوونکو لپاره 17 // 5 مساوي 3 او 17 % 5 مساوي 2 دی. هر زده‌کوونکی درې کتابونه اخلي او دوه پاتې کېږي. پر صفر تقسیم خطا ده؛ له تقسیم مخکې ننوت وګورئ.
Use parentheses for clarity and remainder for what is left over.|برای وضاحت از قوس و برای مقدار باقی از باقی‌مانده استفاده کنید.|د وضاحت لپاره قوس او د پاتې مقدار لپاره پاتې شونی وکاروئ.
What is 2 + 3 * 4?|مقدار 2 + 3 * 4 چیست؟|2 + 3 * 4 څو کېږي؟
Multiply 3 by 4 first, then add 2: the answer is 14.|نخست 3 را در 4 ضرب و سپس 2 جمع کنید: پاسخ 14 است.|لومړی 3 په 4 ضرب او بیا 2 جمع کړئ: ځواب 14 دی.
Calculate the total cost of five notebooks at 20 each.|قیمت مجموع پنج کتابچه، هرکدام 20، را حساب کنید.|د پنځو کتابچو مجموعي بیه حساب کړئ چې هره یوه 20 ده.
The unit price must be defined before calculating the total.|قیمت واحد باید پیش از مجموع تعریف شود.|د واحد بیه باید له مجموعې مخکې تعریف شي.
Print the remainder when 23 is divided by 4.|باقی‌ماندهٔ تقسیم 23 بر 4 را چاپ کنید.|د 23 پر 4 د تقسیم پاتې شونی چاپ کړئ.
4 fits into 23 five times, leaving 3.|4 پنج بار در 23 جا می‌شود و 3 می‌ماند.|4 په 23 کې پنځه ځله ځایېږي او 3 پاتې کېږي.
The % operator computes a remainder.|عملگر % باقی‌مانده را حساب می‌کند.|د % عملګر پاتې شونی حسابوي.
Make a decision|تصمیم بگیرید|پرېکړه وکړئ
Let conditions choose the next step.|شرط گام بعد را انتخاب کند.|شرطونه دې بل ګام وټاکي.
An if statement runs an indented block only when its condition is true. An optional else block handles the other case. End each if or else header with a colon and indent the block by four spaces.\n\nUse == to compare equality, != for inequality, and <, <=, >, >= for ordering. The operator = assigns; == compares. Boolean values are True and False. Use and, or, and not to combine or invert conditions.|if بلوک تورفته را فقط وقتی شرط درست باشد اجرا می‌کند. else اختیاری حالت دیگر را مدیریت می‌کند. سرآغاز if یا else را با دونقطه تمام و بلوک را چهار فاصله داخل کنید.\n\nبرای برابری ==، نابرابری != و ترتیب <، <=، > و >= به‌کار برید. = مقدار می‌دهد و == مقایسه می‌کند. مقدار منطقی True و False است. and، or و not شرط‌ها را ترکیب یا معکوس می‌کنند.|if دننه شوی بلوک یوازې د شرط د سموالي پر مهال چلوي. اختیاري else بل حالت اداره کوي. د if یا else سر په دوه‌ټکو ختم او بلوک څلور تش ځایه دننه کړئ.\n\nد برابرۍ لپاره ==، نابرابرۍ لپاره != او ترتیب لپاره <، <=، > او >= وکاروئ. = ارزښت ټاکي او == پرتله کوي. منطقي ارزښتونه True او False دي. and، or او not شرطونه یوځای یا معکوسوي.
A condition chooses a branch; indentation defines the branch body.|شرط شاخه را انتخاب و تورفتگی بدنهٔ آن را مشخص می‌کند.|شرط څانګه ټاکي؛ دننه‌کول یې بدنه تعریفوي.
Which expression checks whether score equals 50?|کدام عبارت برابری score با 50 را بررسی می‌کند؟|کوم عبارت ګوري چې score له 50 سره برابر دی؟
== compares two values. A single = is an assignment.|== دو مقدار را مقایسه می‌کند. یک = مقداردهی است.|== دوه ارزښتونه پرتله کوي. یو = ټاکنه ده.
Set a temperature and print Cold when it is below 10.|دما را تعیین و اگر زیر 10 بود Cold چاپ کنید.|تودوخه وټاکئ او که له 10 کمه وه Cold چاپ کړئ.
Define the value, test it, and indent the action under the condition.|مقدار را تعریف، بررسی و عمل را زیر شرط تورفته کنید.|ارزښت تعریف او وګورئ؛ عمل د شرط لاندې دننه کړئ.
Complete this condition so the program displays Pass.|شرط را تکمیل کنید تا برنامه Pass نشان دهد.|شرط بشپړ کړئ څو پروګرام Pass وښيي.
65 meets the condition score >= 50, so the indented print runs.|65 شرط score >= 50 را برآورده می‌کند، پس print تورفته اجرا می‌شود.|65 د score >= 50 شرط پوره کوي، نو دننه print اجرا کېږي.
Use if score >= 50: followed by an indented print("Pass").|if score >= 50: و سپس print("Pass") تورفته بنویسید.|if score >= 50: او ورپسې دننه print("Pass") ولیکئ.
Repeat with purpose|تکرار هدفمند|هدف‌لرونکی تکرار
Use loops to do the repetitive work.|کار تکراری را به حلقه بسپارید.|تکراري کار کړیو ته وسپارئ.
A for loop visits each value in a sequence. range(1, 4) produces 1, 2, and 3: the end is excluded. range(4) starts at zero.\n\nAn accumulator starts with an initial value and is updated on each iteration. For a sum, start at zero. Put the final print outside the loop when you want just the total.\n\nA while loop repeats while a condition is true. Update the controlling variable so the loop can finish. The practice runner stops excessive execution.|حلقهٔ for هر مقدار دنباله را می‌بیند. range(1, 4) مقدارهای 1، 2 و 3 می‌دهد؛ پایان شامل نیست. range(4) از صفر آغاز می‌شود.\n\nجمع‌کننده با مقدار آغازین شروع و در هر دور به‌روز می‌شود. برای مجموع از صفر آغاز کنید. اگر تنها مجموع را می‌خواهید، print نهایی را بیرون حلقه بگذارید.\n\nwhile تا وقتی شرط درست است تکرار می‌کند. متغیر کنترول را تغییر دهید تا حلقه تمام شود. اجراکنندهٔ تمرین اجرای بیش از حد را متوقف می‌کند.|for کړۍ د لړۍ هر ارزښت ګوري. range(1, 4) ارزښتونه 1، 2 او 3 ورکوي؛ پای پکې نشته. range(4) له صفره پیلېږي.\n\nراټولوونکی له لومړني ارزښته پیل او په هر پړاو کې تازه کېږي. د مجموعې لپاره له صفره پیل کړئ. که یوازې مجموعه غواړئ، وروستی print له کړۍ بهر کېږدئ.\n\nwhile تر هغه تکرارېږي چې شرط سم وي. کنټرولوونکی متغیر بدل کړئ څو کړۍ ختمه شي. د تمرین چلوونکی زیات اجرا دروي.
range excludes its stop value. Indentation controls what repeats.|range مقدار پایان را شامل نمی‌کند. تورفتگی تعیین می‌کند چه تکرار شود.|range خپل پای ارزښت نه رانغاړي. دننه‌کول ټاکي چې څه تکرار شي.
Which values does range(1, 4) produce?|range(1, 4) کدام مقدارها را تولید می‌کند؟|range(1, 4) کوم ارزښتونه تولیدوي؟
The start is included and the stop is excluded.|آغاز شامل است و پایان شامل نیست.|پیل شامل دی او پای شامل نه دی.
Accumulate 1 + 2 + 3 and display the final sum.|1 + 2 + 3 را جمع و مجموع نهایی را نشان دهید.|1 + 2 + 3 راټول او وروستۍ مجموعه وښیئ.
Initialize once, update inside the loop, then print outside it.|یک‌بار آغاز، داخل حلقه به‌روز و بیرون آن چاپ کنید.|یو ځل پیل، د کړۍ دننه تازه او بهر چاپ کړئ.
Use a loop to print 1, 2, and 3 on separate lines.|با حلقه 1، 2 و 3 را در سطرهای جدا چاپ کنید.|په کړۍ 1، 2 او 3 په جلا کرښو چاپ کړئ.
The three iterations bind n to 1, 2, and then 3.|سه دور n را به 1، 2 و سپس 3 پیوند می‌دهند.|درې پړاوونه n له 1، 2 او بیا 3 سره تړي.
Use for n in range(1, 4): and indent print(n).|for n in range(1, 4): بنویسید و print(n) را تورفته کنید.|for n in range(1, 4): ولیکئ او print(n) دننه کړئ.
Keep things together|چیزها را یک‌جا نگه دارید|شیان یوځای وساتئ
Organize a collection of values.|مجموعهٔ مقدارها را تنظیم کنید.|د ارزښتونو ټولګه تنظیم کړئ.
A list stores a sequence of values between square brackets. Indexing starts at zero, so cities[0] retrieves the first item. len(cities) gives the number of items. An index outside the list raises an error.\n\nA for loop can visit list values directly: for city in cities. This is useful when you need each value without its position. The practice runner supports list literals, reading indexes, len(), and iteration; list methods and index assignment are outside this version.|فهرست دنبالهٔ مقدارها را میان قوس مربع نگه می‌دارد. اندیس از صفر آغاز می‌شود، پس cities[0] عضو اول را می‌گیرد. len(cities) شمار اعضا را می‌دهد. اندیس بیرون فهرست خطا می‌دهد.\n\nfor می‌تواند مستقیم مقدارها را ببیند: for city in cities. وقتی مقدار را بدون جایگاه می‌خواهید مفید است. اجراکنندهٔ تمرین ساخت فهرست، خواندن اندیس، len() و پیمایش را پشتیبانی می‌کند؛ روش فهرست و مقداردهی اندیس در این نسخه نیست.|لېست د ارزښتونو لړۍ د مربع قوسونو ترمنځ ساتي. اندېکس له صفره پیلېږي، نو cities[0] لومړی غړی اخلي. len(cities) د غړو شمېر ورکوي. له لېسته بهر اندېکس خطا کوي.\n\nfor ارزښتونه مستقیم لیدلی شي: for city in cities. دا هغه وخت ګټور دی چې ارزښت بې له ځایه غواړئ. د تمرین چلوونکی د لېست جوړول، د اندېکس لوستل، len() او تکرار ملاتړ کوي؛ د لېست مېتودونه او اندېکس ټاکنه په دې نسخه کې نشته.
Lists group values. The first item has index zero.|فهرست مقدارها را گروه می‌کند. عضو اول اندیس صفر دارد.|لېست ارزښتونه راټولوي. د لومړي غړي اندېکس صفر دی.
For marks = [70, 80, 90], what is marks[1]?|برای marks = [70, 80, 90]، مقدار marks[1] چیست؟|په marks = [70, 80, 90] کې marks[1] څو دی؟
Index 0 is 70, index 1 is 80, and index 2 is 90.|اندیس 0 مقدار 70، اندیس 1 مقدار 80 و اندیس 2 مقدار 90 دارد.|اندېکس 0 ارزښت 70، اندېکس 1 ارزښت 80 او اندېکس 2 ارزښت 90 لري.
Store names, loop over them, and display each name.|نام‌ها را نگه دارید، روی آن‌ها حلقه بزنید و هر نام را نشان دهید.|نومونه وساتئ، پر هغوی کړۍ ووهئ او هر نوم وښیئ.
The loop visits each name and the indented print displays it.|حلقه هر نام را می‌بیند و print تورفته آن را نشان می‌دهد.|کړۍ هر نوم ګوري او دننه print یې ښيي.
Print the sum of all three marks using an accumulator.|مجموع هر سه نمره را با جمع‌کننده چاپ کنید.|د درېواړو نمرو مجموعه په راټولوونکي چاپ کړئ.
Starting at zero, the running total becomes 10, 30, then 60.|با آغاز از صفر، مجموع جاری 10، 30 و سپس 60 می‌شود.|له صفره پیل سره روانه مجموعه 10، 30 او بیا 60 کېږي.
Add each mark to total inside a for loop. Print total after the loop.|هر نمره را داخل for به total بیفزایید. total را پس از حلقه چاپ کنید.|هره نمره د for دننه total ته زیاته کړئ. total له کړۍ وروسته چاپ کړئ.
Build reusable ideas|فکر قابل استفادهٔ دوباره بسازید|بیاکارېدونکي فکرونه جوړ کړئ
Name a process and use it again.|به روند نام دهید و دوباره استفاده کنید.|بهیر ته نوم ورکړئ او بیا یې وکاروئ.
A function packages instructions under a name. Define it with def, a name, parentheses, and a colon. Parameters are names for values supplied by the caller. return sends a result back and ends the function.\n\nA returned value is not automatically displayed: use print() to display it. Variables assigned inside these simple functions belong to that function call. Start with small functions that each do one clear thing.|تابع دستورها را زیر یک نام بسته می‌کند. با def، نام، قوس و دونقطه تعریفش کنید. پارامتر نام مقدار داده‌شده توسط فراخواننده است. return نتیجه را برمی‌گرداند و تابع را تمام می‌کند.\n\nمقدار برگشتی خودکار نمایش نمی‌یابد؛ print() به‌کار برید. متغیر تعریف‌شده در این تابع ساده متعلق به همان فراخوانی است. با تابع کوچک آغاز کنید که هرکدام یک کار روشن انجام دهد.|دنده لارښوونې تر یوه نوم لاندې راټولوي. په def، نوم، قوسونو او دوه‌ټکو یې تعریف کړئ. پارامېټر د بلونکي ورکړي ارزښت نوم دی. return پایله بېرته لېږي او دنده ختموي.\n\nبېرته ورکړل شوی ارزښت پخپله نه ښکاري؛ print() وکاروئ. د دې ساده دندو دننه ټاکل شوی متغیر د همدې زنګ دی. له کوچنیو دندو پیل کړئ چې هره یوه یو څرګند کار کوي.
Parameters carry values in; return carries a result out.|پارامتر مقدار را داخل و return نتیجه را بیرون می‌برد.|پارامېټر ارزښت دننه او return پایله بهر وړي.
What does return do inside a function?|return داخل تابع چه می‌کند؟|return د دندې دننه څه کوي؟
return exits the function with a value. print() is a separate operation.|return با مقدار از تابع خارج می‌شود. print() عملیات جدا است.|return له ارزښت سره له دندې وځي. print() جلا کار دی.
Always prints text|همیشه متن چاپ می‌کند|تل متن چاپوي
Sends a value to the caller and exits|مقدار را به فراخواننده می‌فرستد و خارج می‌شود|ارزښت بلونکي ته لېږي او وځي
Repeats the function|تابع را تکرار می‌کند|دنده تکراروي
Define a function that doubles a number, then use it.|تابع دوبرابرکنندهٔ عدد تعریف و سپس استفاده کنید.|د عدد دوه‌برابروونکې دنده تعریف او بیا یې وکاروئ.
Define the function before calling it. Its return statement is indented.|تابع را پیش از فراخوانی تعریف کنید. return آن تورفته است.|دنده له بللو مخکې تعریف کړئ. return یې دننه دی.
Define add(a, b) and print add(4, 6).|add(a, b) را تعریف و add(4, 6) را چاپ کنید.|add(a, b) تعریف او add(4, 6) چاپ کړئ.
The arguments 4 and 6 become a and b; the function returns 10.|آرگومان‌های 4 و 6 به a و b تبدیل می‌شوند؛ تابع 10 برمی‌گرداند.|آرګومېنټونه 4 او 6 د a او b ارزښتونه کېږي؛ دنده 10 ورکوي.
Use def add(a, b): with an indented return a + b.|def add(a, b): را با return a + b تورفته به‌کار برید.|def add(a, b): له دننه return a + b سره وکاروئ.
''')

rows(r'''
Python Course Zero to Hero|دورهٔ پایتون از صفر تا مهارت|د پایتون کورس له صفره تر مهارت
Web Design|طراحی وب|د ویب ډیزاین
Web Development|توسعهٔ وب|د ویب پراختیا
Java|Java|Java
Kotlin|Kotlin|Kotlin
Android|Android|Android
iOS|iOS|iOS
Swift|Swift|Swift
C++|C++|C++
JavaScript|JavaScript|JavaScript
ReactJs|ReactJs|ReactJs
ReactNative|ReactNative|ReactNative
NodeJs|NodeJs|NodeJs
ExpressJs|ExpressJs|ExpressJs
Flutter and Dart|Flutter و Dart|Flutter او Dart
Submit five correctly defined terms and label their occurrences in the example; correct at least four before continuing.|پنج اصطلاح را درست تعریف و جای آن‌ها را در نمونه مشخص کنید؛ پیش از ادامه دست‌کم چهار مورد را درست کنید.|پنځه اصطلاحات سم تعریف او په نمونه کې یې ځایونه وښیئ؛ له دوام مخکې لږ تر لږه څلور سم کړئ.
Submit a state trace and a causal explanation of two outputs. Explain a changed input without running it first.|رد حالت و توضیح علت دو خروجی را ارائه کنید. نتیجهٔ ورودی تغییرکرده را پیش از اجرا توضیح دهید.|د حالت تعقیب او د دوو وتیو علت ورکړئ. بدل ننوت له چلولو مخکې تشریح کړئ.
Submit source and normal, empty, and invalid input results. Each stated acceptance condition must pass.|منبع و نتیجهٔ ورودی عادی، خالی و نامعتبر را بدهید. هر شرط پذیرش باید موفق شود.|سرچینه او د عادي، تش او نامعتبر ننوت پایلې ورکړئ. د منلو هر شرط باید بریالی وي.
Submit the failing case, root cause, minimal fix, and a regression test that fails before the fix and passes after.|حالت شکست، علت اصلی، اصلاح کوچک و آزمونی بدهید که پیش از اصلاح شکست و پس از آن موفق شود.|ناکام حالت، اصلي علت، لږ اصلاح او داسې ازموینه ورکړئ چې مخکې ناکامه او وروسته بریالۍ شي.
Submit a comparison of two designs, evidence from tests, one limitation of the chosen design, and a reasoned decision.|مقایسهٔ دو طراحی، شواهد آزمون، یک محدودیت طرح انتخابی و تصمیم مستدل ارائه کنید.|د دوو ډیزاینونو پرتله، د ازموینو شواهد، د ټاکلي ډیزاین یو حد او مستدله پرېکړه ورکړئ.
Submit your own requirements, design, source, test evidence, and a short demonstration. Explain how your extension differs from the example.|نیاز، طرح، منبع، شواهد آزمون و نمایش کوتاه خود را ارائه کنید. تفاوت گسترش خود با نمونه را توضیح دهید.|خپلې اړتیاوې، ډیزاین، سرچینه، ازموینې شواهد او لنډه ننداره ورکړئ. له نمونې سره د خپل غځولو توپیر بیان کړئ.
Discover: write three user stories, scope exclusions, and acceptance examples using fictional data.|شناخت: با دادهٔ فرضی سه داستان کاربر، موارد بیرون محدوده و نمونهٔ پذیرش بنویسید.|پېژندنه: په فرضي معلوماتو درې کارن کیسې، له ساحې بهر موارد او د منلو بېلګې ولیکئ.
Design: sketch components and data flow; justify one tradeoff in an architecture decision record.|طراحی: اجزا و جریان داده را رسم و یک انتخاب میان مزیت‌ها را در سند تصمیم معماری توجیه کنید.|ډیزاین: اجزا او د معلوماتو بهیر رسم او یو انتخاب په معماري پرېکړه کې توجیه کړئ.
Build: implement the required behaviors in small reviewable changes; record how to reproduce the build offline.|ساخت: رفتار لازم را در تغییرهای کوچک قابل بررسی پیاده و روش بازساخت آفلاین را ثبت کنید.|جوړول: اړین چلند په کوچنیو کتل کېدونکو بدلونونو پلي او د آفلاین بیا جوړولو لاره ثبت کړئ.
Verify: test every acceptance condition, empty/invalid data, and restart behavior; retain results.|بررسی: هر شرط پذیرش، دادهٔ خالی یا نامعتبر و رفتار آغاز دوباره را بیازمایید؛ نتیجه را نگه دارید.|کتنه: هر منلو شرط، تش یا نامعتبر معلومات او بیا پیل وازمویئ؛ پایلې وساتئ.
Review: demonstrate to a peer or conduct a recorded self-review; document feedback, improvements, and limitations.|بازبینی: به هم‌صنفی نشان دهید یا خودبازبینی ثبت‌شده کنید؛ بازخورد، بهبود و محدودیت را مستند کنید.|بیاکتنه: همزولي ته وښیئ یا ثبت شوې خپله کتنه وکړئ؛ غبرګون، اصلاحات او حدود مستند کړئ.
Salam|Salam|Salam
Kabul|Kabul|Kabul
name|name|name
Nothing|هیچ‌چیز|هېڅ
p|p|p
h1|h1|h1
html|html|html
The server|سرور|سرور
The CSS file|فایل CSS|د CSS فایل
The keyboard|صفحه‌کلید|کیبورډ
Main.java|Main.java|Main.java
String[]|String[]|String[]
println|println|println
main|main|main
A database table|جدول پایگاه داده|د ډیټابېس جدول
Visible text|متن قابل دیدن|ښکاره متن
A network download|دریافت از شبکه|له شبکې ښکته کول
ContentView.swift|ContentView.swift|ContentView.swift
import SwiftUI|import SwiftUI|import SwiftUI
print|print|print
let|let|let
city|city|city
std::cout|std::cout|std::cout
#include|#include|#include
return 0|return 0|return 0
20|20|20
5|5|5
25|25|25
40|40|40
A heading description|توصیف عنوان|د سرلیک تشریح
A database connection|اتصال پایگاه داده|د ډیټابېس اړیکه
A Python function|تابع پایتون|د پایتون دنده
View|View|View
Text|Text|Text
The terminal|ترمینال|ټرمنل
A browser heading|عنوان مرورگر|د مرورګر سرلیک
A phone notification|اعلان تلفن|د موبایل خبرتیا
The source file|فایل منبع|سرچینه فایل
The console|کنسول|کنسول
A Text widget automatically|ویجت Text به‌صورت خودکار|په اتومات ډول Text ویجټ
A database|پایگاه داده|ډیټابېس
''')

rows(r"""
Open workspace|بازکردن فضای کار|کاري ځای پرانیستل
In-app workspace|فضای کار درون برنامه|د اپ دننه کاري ځای
Write, save, and revise.|بنویسید، ذخیره و اصلاح کنید.|ولیکئ، خوندي او سم یې کړئ.
Your files are stored locally and included in your exported backup.|فایل‌های شما روی دستگاه ذخیره و در نسخهٔ پشتیبان صادرشده شامل می‌شوند.|ستاسو فایلونه په وسیله کې ساتل کېږي او په صادر شوي شاتړ کې شاملېږي.
The initial code is a small teaching example, not a completed project. Extend it to meet the requirements below.|کد آغازین یک نمونهٔ آموزشی کوچک است، نه پروژهٔ تکمیل‌شده. آن را برای برآوردن نیازهای زیر گسترش دهید.|لومړنی کوډ یوه کوچنۍ ښوونیزه نمونه ده، بشپړه پروژه نه ده. د لاندې اړتیاوو لپاره یې پراخ کړئ.
Source or project notes|کد یا یادداشت‌های پروژه|کوډ یا د پروژې یادښتونه
Each file supports up to 12,000 characters. Save before leaving.|هر فایل تا ۱۲٬۰۰۰ نویسه می‌پذیرد. پیش از خروج ذخیره کنید.|هر فایل تر ۱۲٬۰۰۰ تورو مني. له وتلو مخکې یې خوندي کړئ.
Save files|ذخیرهٔ فایل‌ها|فایلونه خوندي کول
Save files • unsaved changes|ذخیرهٔ فایل‌ها • تغییرات ذخیره نشده|فایلونه خوندي کول • بدلونونه نه دي خوندي شوي
Run with teaching Python|اجرا با پایتون آموزشی|په ښوونیز پایتون چلول
Execution uses the documented Python subset. Imports, files, classes, and full CPython are not supported. Output is not an automatic project grade.|اجرا از زیرمجموعهٔ مستند پایتون استفاده می‌کند. واردکردن کتابخانه، فایل، کلاس و CPython کامل پشتیبانی نمی‌شود. خروجی نمره‌دهی خودکار پروژه نیست.|اجرا د پایتون مستندې برخې کاروي. کتابتون واردول، فایلونه، کلاسونه او بشپړ CPython نه ملاتړ کېږي. پایله د پروژې اتومات نمره نه ده.
Source editing and storage work here. This language has no embedded compiler in this release; these files are not being executed or automatically graded.|ویرایش و ذخیرهٔ کد اینجا کار می‌کند. این زبان در این نسخه کامپایلر داخلی ندارد؛ فایل‌ها اجرا یا خودکار نمره‌دهی نمی‌شوند.|دلته کوډ سمول او ساتل کار کوي. دا ژبه په دې نسخه کې دنننی کمپایلر نه لري؛ فایلونه نه چلېږي او اتومات نمرې نه ورکول کېږي.
Use README.md to explain your design and usage. Use TESTS.md for inputs, expected results, actual results, and failures. Keep questions and reflections in NOTES.md.|طرح و روش استفاده را در README.md شرح دهید. ورودی‌ها، نتایج مورد انتظار و واقعی و شکست‌ها را در TESTS.md بنویسید. پرسش‌ها و بازاندیشی را در NOTES.md نگه دارید.|طرح او کارونه په README.md کې تشریح کړئ. ننوتنې، تمه شوې او واقعي پایلې او ناکامۍ په TESTS.md کې ولیکئ. پوښتنې او فکرونه په NOTES.md کې وساتئ.
Workspace files saved on this device.|فایل‌های فضای کار روی این دستگاه ذخیره شد.|د کاري ځای فایلونه په دې وسیله خوندي شول.
Your source changes have not been saved.|تغییرات کد شما ذخیره نشده است.|ستاسو د کوډ بدلونونه نه دي خوندي شوي.
Backup exceeds 16 MB.|نسخهٔ پشتیبان بیش از ۱۶ مگابایت است.|شاتړ له ۱۶ مېګابایټو لوی دی.
Backup is not valid JSON.|نسخهٔ پشتیبان JSON معتبر نیست.|شاتړ سم JSON نه دی.
Invalid workspace files. Use at most four files of 12,000 characters each.|فایل‌های فضای کار نامعتبر است. حداکثر چهار فایل، هرکدام تا ۱۲٬۰۰۰ نویسه، استفاده کنید.|د کاري ځای فایلونه ناسم دي. تر څلورو فایلونو، هر یو تر ۱۲٬۰۰۰ تورو، وکاروئ.
This is not a supported Learn By Marifat Team backup (version 1, 2, or 3).|این نسخهٔ پشتیبان پشتیبانی‌شدهٔ Learn By Marifat Team نیست (نسخهٔ ۱، ۲ یا ۳).|دا د Learn By Marifat Team منل شوی شاتړ نه دی (نسخه ۱، ۲ یا ۳).
""")

rows(r"""
Each assignment includes acceptance conditions and an in-app workspace for four small source or note files. Full builds require the listed development tools.|هر تمرین شرایط پذیرش و فضای کار درون برنامه برای چهار فایل کوچک کد یا یادداشت دارد. ساخت کامل به ابزارهای توسعهٔ ذکرشده نیاز دارد.|هره دنده د منلو شرطونه او د څلورو کوچنیو کوډ یا یادښت فایلونو لپاره دنننی کاري ځای لري. بشپړ جوړول یادو پرمختیايي وسایلو ته اړتیا لري.
Save small source files and design, usage, and test notes in the workspace. Include fictional fixtures, a component diagram, and one architecture decision. Larger external build folders need a separate backup.|فایل‌های کوچک کد و یادداشت‌های طرح، استفاده و آزمون را در فضای کار ذخیره کنید. دادهٔ آزمایشی خیالی، نمودار اجزا و یک تصمیم معماری را شامل سازید. پوشه‌های بزرگ ساخت بیرونی به پشتیبان جدا نیاز دارند.|کوچني کوډ فایلونه او د طرحې، کارونې او ازموینې یادښتونه په کاري ځای کې وساتئ. خیالي ازمایښتي معلومات، د برخو انځور او یوه معماري پرېکړه ورسره کړئ. لوی بهرني جوړښتي فولډرونه جلا شاتړ غواړي.
Your saved data could not be opened. No data has been erased. Check available storage and try again.|اطلاعات ذخیره‌شده باز نشد. هیچ داده‌ای پاک نشده است. فضای خالی را بررسی و دوباره کوشش کنید.|ستاسو خوندي معلومات پرانیستل نه شول. هېڅ معلومات نه دي ړنګ شوي. خالي ځای وګورئ او بیا هڅه وکړئ.
Try again|کوشش دوباره|بیا هڅه
Backup is not valid UTF-8.|نسخهٔ پشتیبان UTF-8 معتبر نیست.|شاتړ سم UTF-8 نه دی.
""")

rows(r"""
Guided project walkthrough|راهنمای گام‌به‌گام پروژه|د پروژې ګام په ګام لارښود
In-app practice scope|محدودهٔ تمرین درون برنامه|د دننني تمرین حدود
The practice workspace runs the calculation and validation core. The full reference program below needs CPython on a computer; its file and database operations cannot run in the teaching interpreter.|فضای تمرین هستهٔ محاسبه و اعتبارسنجی را اجرا می‌کند. برنامهٔ مرجع کامل زیر به CPython روی کمپیوتر نیاز دارد؛ عملیات فایل و پایگاه دادهٔ آن در مفسر آموزشی اجرا نمی‌شود.|کاري ځای د محاسبې او ارزونې بنسټیزه برخه چلوي. لاندې بشپړ مرجع په کمپیوټر کې CPython غواړي؛ د فایل او ډیټابیس عملیات یې په ښوونیز مفسر کې نه چلېږي.
Complete reference program|برنامهٔ مرجع کامل|بشپړ مرجع پروګرام
Save this source using the filename shown, then use the local commands below.|این کد را با نام فایل نشان‌داده‌شده ذخیره و دستورهای محلی زیر را استفاده کنید.|دا کوډ په ښودل شوي فایل نوم وساتئ او لاندې محلي قوماندې وکاروئ.
Replace current source?|کد فعلی جایگزین شود؟|اوسنی کوډ بدل شي؟
This replaces the current source with the practice solution. Your previous saved version stays unchanged until you press Save files.|این کار کد فعلی را با راه‌حل تمرین جایگزین می‌کند. نسخهٔ ذخیره‌شدهٔ قبلی تا فشردن ذخیرهٔ فایل‌ها تغییر نمی‌کند.|دا اوسنی کوډ د تمرین په حل بدلوي. پخوانۍ خوندي نسخه د فایلونو خوندي کولو تر کېکاږلو نه بدلېږي.
Load practice solution|آوردن راه‌حل تمرین|د تمرین حل راوړل
Complete the practice function, run the supplied examples, and compare with the expected output. These examples check the core rules, not the full project requirements.|تابع تمرین را تکمیل، نمونه‌ها را اجرا و با خروجی مورد انتظار مقایسه کنید. نمونه‌ها قوانین اصلی را می‌سنجند، نه همهٔ نیازهای پروژه را.|د تمرین تابع بشپړه، بېلګې وچلوئ او له تمه شوې پایلې سره یې پرتله کړئ. دا بېلګې بنسټیز قوانین ګوري، د پروژې ټولې اړتیاوې نه.
Expected practice output|خروجی مورد انتظار تمرین|د تمرین تمه شوې پایله
Explain each result before viewing the solution. Matching output is practice feedback, not certification of a complete project.|پیش از دیدن راه‌حل هر نتیجه را توضیح دهید. برابرشدن خروجی بازخورد تمرین است، نه تأیید پروژهٔ کامل.|د حل له کتلو مخکې هره پایله تشریح کړئ. د پایلې برابرېدل د تمرین نظر دی، د بشپړې پروژې تصدیق نه دی.
""")

rows(r"""
Save all three reference programs and test_projects.py in the same folder. Run the command below with CPython; no packages or network are required.|هر سه برنامهٔ مرجع و test_projects.py را در یک پوشه ذخیره کنید. دستور زیر را با CPython اجرا کنید؛ بسته یا شبکه لازم نیست.|درې واړه مرجع پروګرامونه او test_projects.py په یوه فولډر کې وساتئ. لاندې قومانده په CPython وچلوئ؛ کڅوړې یا شبکه نه غواړي.
Reference regression tests|آزمون‌های پس‌رفت مرجع|د مرجع د بیا خرابېدو ازموینې
""")

rows(r"""
Home|خانه|کور
Practice|تمرین|تمرین
Your space|فضای شما|ستاسو ځای
Practice at your pace.|به وقت و توان خود تمرین کنید.|په خپل وخت تمرین وکړئ.
Start with a lesson. Use these tools when you want to explore.|با یک درس شروع کنید. هر وقت خواستید بیشتر امتحان کنید، از این ابزارها استفاده کنید.|له یوه درس پیل وکړئ. د نورو ازموینو لپاره دا وسایل وکاروئ.
Try small Python programs and see their output.|برنامه‌های کوچک پایتون را امتحان و نتیجه را ببینید.|کوچني پایتون پروګرامونه وازمویئ او پایله وګورئ.
See what you have practiced.|تمرین‌های انجام‌شدهٔ خود را ببینید.|خپل ترسره شوي تمرینونه وګورئ.
Marifat|معرفت|معرفت
Marifat Software Team|تیم نرم‌افزاری معرفت|د معرفت سافټویر ټیم
Learn by doing|با تمرین یاد بگیر|په تمرین یې زده کړه
Welcome to Marifat|به معرفت خوش آمدید|معرفت ته ښه راغلاست
Your first step starts here.|اولین قدم، همین‌جاست.|لومړی ګام مو همدلته دی.
Welcome back. Let’s continue.|خوش آمدید. ادامه بدهیم.|ښه راغلاست. دوام ورکړو.
No programming experience needed. We will take it one step at a time.|تجربهٔ برنامه‌نویسی لازم نیست. با هم قدم‌به‌قدم پیش می‌رویم.|د پروګرام لیکلو تجربه نه غواړي. ګام په ګام به مخکې ځو.
Start with Python|شروع با پایتون|له پایتون پیل
Read a short example, try one small task, and see what happens.|یک مثال کوتاه بخوانید، یک تمرین کوچک انجام دهید و نتیجه را ببینید.|لنډه بېلګه ولولئ، کوچنی تمرین وکړئ او پایله وګورئ.
How learning works|چگونه یاد می‌گیریم؟|څنګه زده کوو؟
1. See an example|۱. یک مثال ببینید|۱. بېلګه وګورئ
We explain the code before asking you to write it.|پیش از نوشتن کد، آن را برای شما توضیح می‌دهیم.|له کوډ لیکلو مخکې یې درته تشریح کوو.
2. Try it yourself|۲. خودتان امتحان کنید|۲. خپله یې وازمویئ
Choose an answer, arrange lines, or change a small program.|پاسخ را انتخاب کنید، خط‌ها را مرتب کنید یا یک برنامهٔ کوچک را تغییر دهید.|ځواب وټاکئ، کرښې سمې کړئ یا کوچنی پروګرام بدل کړئ.
3. Learn from the result|۳. از نتیجه یاد بگیرید|۳. له پایلې زده کړئ
Mistakes are welcome. Use a hint and try again.|اشتباه بخشی از یادگیری است. راهنمایی بگیرید و دوباره امتحان کنید.|تېروتنه د زده کړې برخه ده. لارښوونه واخلئ او بیا هڅه وکړئ.
Explore other courses|دیدن دوره‌های دیگر|نور کورسونه وګورئ
Two guided activities|دو تمرین همراه با راهنما|دوه لارښود تمرینونه
{0} minutes|{0} دقیقه|{0} دقیقې
What you will learn|چه یاد می‌گیرید؟|څه زده کوئ؟
Lessons and activities|درس‌ها و تمرین‌ها|درسونه او تمرینونه
Review your work|کار خود را بررسی کنید|خپل کار وګورئ
Start here — no experience needed|شروع از صفر؛ بدون نیاز به تجربه|له صفر پیل؛ تجربه نه غواړي
Build on what you already know|برای ادامهٔ آموخته‌های قبلی شما|د پخوانیو زده کړو دوام
Try the next activity|تمرین بعدی را امتحان کنید|راتلونکی تمرین وازمویئ
Choose something you would like to build.|چه چیزی دوست دارید بسازید؟|څه جوړول غواړئ؟
New to programming? Start with Python. Some advanced courses need additional tools; each course explains what is needed.|تازه شروع می‌کنید؟ از پایتون آغاز کنید. بعضی دوره‌های پیشرفته ابزارهای بیشتری می‌خواهند؛ در هر دوره توضیح داده شده است.|نوي یاست؟ له پایتون پیل وکړئ. ځینې پرمختللي کورسونه نور وسایل غواړي؛ هر کورس یې اړتیاوې تشریح کوي.
{0}/{1} exercises completed|{0} از {1} تمرین انجام شده|له {1} تمرینونو {0} بشپړ شوي
""")

rows(r"""
Understand the idea|مفهوم را بشناسید|مفهوم وپېژنئ
See it in action|مثال را ببینید|بېلګه وګورئ
Try it yourself|خودتان امتحان کنید|خپله یې وازمویئ
You finished this lesson. Well done.|این درس را تمام کردید. آفرین!|دا درس مو بشپړ کړ. آفرین!
Try one activity at a time. You can always use a hint.|هر بار یک تمرین انجام دهید. هر وقت خواستید از راهنما کمک بگیرید.|هر ځل یو تمرین وکړئ. هر وخت له لارښوونې مرسته اخیستلای شئ.
See an example|دیدن یک مثال|بېلګه کتل
Back to home|برگشت به خانه|کور ته ستنېدل
Next lesson|درس بعدی|راتلونکی درس
""")

rows(r"""
The problem|موضوع پروژه|د پروژې موضوع
Follow an example|یک مثال را دنبال کنید|بېلګه تعقیب کړئ
Your turn|حالا نوبت شماست|اوس ستاسو وار دی
Find and fix a mistake|یک اشتباه را پیدا و اصلاح کنید|تېروتنه ومومئ او سمه یې کړئ
Make a choice|روش مناسب را انتخاب کنید|مناسبه لاره وټاکئ
Build something of your own|چیزی از خودتان بسازید|خپل یو څه جوړ کړئ
""")

rows(r"""
Before you start: time and tools|پیش از شروع: زمان و ابزارها|له پیل مخکې: وخت او وسایل
Start the first lesson|شروع اولین درس|لومړی درس پیل کړئ
Meet the basics with a short example and a guided task.|با یک مثال کوتاه و تمرین راهنمایی‌شده با مفاهیم اولیه آشنا شوید.|په لنډه بېلګه او لارښود تمرین بنسټونه وپېژنئ.
""")

rows(r"""
Save your changes?|تغییرات ذخیره شود؟|بدلونونه خوندي شي؟
Your code has changes that are not saved yet.|تغییرات کد شما هنوز ذخیره نشده است.|ستاسو د کوډ بدلونونه لا نه دي خوندي شوي.
Save and leave|ذخیره و برگشت|خوندي کول او ستنېدل
""")

rows(r"""
+{0} XP earned|{0}+ امتیاز گرفتید|{0}+ امتیاز مو واخیست
Back to course|برگشت به دوره|کورس ته ستنېدل
Build your first real project|اولین پروژهٔ واقعی خود را بسازید|خپله لومړۍ واقعي پروژه جوړه کړئ
Challenge completed. Keep your adventure going!|چالش را حل کردید. به مسیرتان ادامه دهید!|ننګونه مو حل کړه. خپل سفر ته دوام ورکړئ!
Choose a stop. You can revisit any lesson without losing points.|یک مرحله انتخاب کنید. مرور درس‌ها امتیاز شما را کم نمی‌کند.|پړاو وټاکئ. د درسونو بیاکتنه مو امتیاز نه کموي.
Continue|ادامه|دوام
Earn 10 XP for each new correct answer and 20 XP for a completed Python lesson. Replays are always free.|هر پاسخ درست تازه ۱۰ امتیاز و تکمیل هر درس پایتون ۲۰ امتیاز دارد. تمرین دوباره همیشه آزاد است.|هر نوی سم ځواب ۱۰ امتیاز او د پایتون د هر درس بشپړول ۲۰ امتیاز لري. بیا تمرین تل ازاد دی.
Explore each stop with a short explanation, an example, and a task.|در هر مرحله یک توضیح کوتاه، یک مثال و یک تمرین دارید.|په هر پړاو کې لنډه تشریح، بېلګه او تمرین لرئ.
First spark|اولین جرقه|لومړۍ ځلا
Follow the path. Solve a challenge. Collect your next badge.|مسیر را دنبال کنید، چالش را حل کنید و نشان بعدی را بگیرید.|لاره تعقیب، ننګونه حل او راتلونکې نښه ترلاسه کړئ.
Guided workshop|کارگاه همراه با راهنما|لارښود کارځای
Lesson champion|قهرمان درس|د درس اتل
Level {0}|سطح {0}|کچه {0}
Next challenge|چالش بعدی|راتلونکې ننګونه
Problem solver|حل‌کنندهٔ مسئله|د مسئلې حلوونکی
Project challenge|چالش پروژه|د پروژې ننګونه
Python explorer|کاوشگر پایتون|د پایتون سپړونکی
Reference library and advanced tools|کتابخانهٔ مرجع و ابزارهای پیشرفته|مرجع کتابتون او پرمختللي وسایل
These workshops use the course tools. They do not award automatic XP.|این کارگاه‌ها از ابزارهای دوره استفاده می‌کنند و امتیاز خودکار ندارند.|دا کارځایونه د کورس وسایل کاروي او اتومات امتیاز نه لري.
Your badges|نشان‌های شما|ستاسو نښې
Your coding adventure|ماجراجویی برنامه‌نویسی شما|ستاسو د کوډ لیکلو سفر
Your mission map|نقشهٔ چالش‌های شما|ستاسو د ننګونو نقشه
{0} XP|{0} امتیاز|{0} امتیاز
{0} XP to the next level|{0} امتیاز تا سطح بعدی|راتلونکې کچې ته {0} امتیاز
{0}/{1} challenges|{0} از {1} چالش|له {1} ننګونو {0}
""")

rows(r"""
Badges: solve 1 challenge, solve 5 challenges, finish 1 lesson, then finish all 7 foundation lessons.|نشان‌ها: حل ۱ چالش، حل ۵ چالش، تکمیل ۱ درس و سپس تکمیل هر ۷ درس مقدماتی.|نښې: ۱ ننګونه حل کړئ، ۵ ننګونې حل کړئ، ۱ درس او بیا ټول ۷ بنسټیز درسونه بشپړ کړئ.
""")

rows(r"""
All foundation missions completed!|تمام چالش‌های مقدماتی را تمام کردید!|ټولې بنسټیزې ننګونې مو بشپړې کړې!
Output|نتیجهٔ مثال|د مثال پایله
Choose a language, write code, and keep a separate draft for each.|زبان را انتخاب کنید، کود بنویسید و برای هر زبان پیش‌نویس جدا نگه دارید.|ژبه وټاکئ، کوډ ولیکئ او د هرې ژبې لپاره جلا مسوده وساتئ.
Coding language|زبان کودنویسی|د کوډ لیکلو ژبه
Your code|کود شما|ستاسو کوډ
Copy code|کاپی کود|کوډ کاپي کړئ
Code copied.|کود کاپی شد.|کوډ کاپي شو.
Save before switching language?|پیش از تغییر زبان ذخیره شود؟|د ژبې له بدلولو مخکې یې وساتو؟
Each language has its own draft. Choose what to do with your current changes.|هر زبان پیش‌نویس جدا دارد. انتخاب کنید با تغییرهای فعلی چه شود.|هره ژبه جلا مسوده لري. وټاکئ چې له اوسنیو بدلونونو سره څه وشي.
Save and switch|ذخیره و تغییر زبان|ساتل او ژبه بدلول
Save your draft on this device. Code keeps its original writing direction.|پیش‌نویس را در همین دستگاه ذخیره کنید. جهت اصلی نوشتن کود حفظ می‌شود.|مسوده په همدې وسیله وساتئ. د کوډ اصلي لیکلو لوری ساتل کېږي.
Write, save, and run offline.|آفلاین بنویسید، ذخیره و اجرا کنید.|آفلاین ولیکئ، وساتئ او وچلوئ.
Write and save offline. Running this language requires the course tools on your computer.|آفلاین کود بنویسید و ذخیره کنید. اجرای این زبان ابزارهای کورس را در کمپیوتر شما لازم دارد.|آفلاین کوډ ولیکئ او وساتئ. د دې ژبې چلول ستاسو په کمپیوټر کې د کورس وسایل غواړي.
This SQL runner reads fictional tables only. Use SELECT queries up to 2000 characters.|این اجراکنندهٔ SQL فقط جدول‌های فرضی را می‌خواند. پرس‌وجوی SELECT تا 2000 حرف بنویسید.|دا SQL چلوونکی یوازې فرضي جدولونه لولي. تر 2000 تورو SELECT پوښتنې ولیکئ.
Check your work|کار خود را بررسی کنید|خپل کار وګورئ
Course tools|ابزارهای کورس|د کورس وسایل
Walk through the example|مثال را قدم‌به‌قدم بفهمیم|مثال ګام په ګام وپوهېږو
Offline SQL practice|تمرین آفلاین SQL|آفلاین SQL تمرین
Open offline SQL practice|باز کردن تمرین آفلاین SQL|آفلاین SQL تمرین پرانیزئ
Explore fictional tables and see real query results.|جدول فرضی را بررسی و نتیجهٔ واقعی پرس‌وجو را ببینید.|فرضي جدولونه وګورئ او د پوښتنې واقعي پایله ووینئ.
Practice tables|جدول‌های تمرین|تمریني جدولونه
Your SQL query|پرس‌وجوی SQL شما|ستاسو SQL پوښتنه
Run query|اجرای پرس‌وجو|پوښتنه وچلوئ
Running...|در حال اجرا…|د اجرا په حال کې…
Query result|نتیجهٔ پرس‌وجو|د پوښتنې پایله
Leave SQL practice?|از تمرین SQL بیرون می‌شوید؟|له SQL تمرینه وځئ؟
Discard and leave|بیرون شدن بدون نگه‌داشتن|له ساتلو پرته وتل
This query is temporary. Copy it before leaving if you want to keep it.|این پرس‌وجو موقتی است. برای نگه‌داشتن، پیش از بیرون شدن آن را کاپی کنید.|دا پوښتنه موقتي ده. که ساتئ یې، له وتلو مخکې یې کاپي کړئ.
No rows matched. Check your filter; an empty result is not an execution error.|سطر مطابق پیدا نشد. فلتر را بررسی کنید؛ نتیجهٔ خالی خطای اجرا نیست.|برابر کتار ونه موندل شو. چاڼ وګورئ؛ تشه پایله د اجرا خطا نه ده.
Try finding books priced at 100. Then count loans for each book, including books with no loans.|کتاب‌های با قیمت 100 را پیدا کنید. سپس امانت هر کتاب، حتی کتاب بی‌امانت را بشمارید.|د 100 بیې کتابونه ومومئ. بیا د هر کتاب پورونه وشمېرئ، بې پوره کتابونه هم شامل کړئ.
Read fictional tables with SELECT, filters, joins, grouping, and ordering. Each run uses fresh data and shows at most 100 rows. Queries here are temporary; copy any work you want to keep. Updates, subqueries, and server-specific commands are not supported in this practice.|جدول فرضی را با SELECT، فلتر، وصل، گروه‌بندی و ترتیب بخوانید. هر اجرا معلومات تازه و حداکثر 100 سطر نشان می‌دهد. پرس‌وجو موقتی است؛ کار لازم را کاپی کنید. تغییر معلومات، پرس‌وجوی تو‌در‌تو و دستور ویژهٔ سرور در این تمرین اجرا نمی‌شود.|فرضي جدولونه په SELECT، چاڼ، نښلونه، ډله کولو او ترتیب ولولئ. هر اجرا تازه معلومات او تر 100 کتارونو ښيي. پوښتنې موقتي دي؛ اړین کار کاپي کړئ. بدلون، دنننۍ پوښتنې او د سرور ځانګړې قوماندې دلته نه چلېږي.
SQL practice could not start. Your query is still here; try again.|تمرین SQL آغاز نشد. پرس‌وجوی شما باقی است؛ دوباره تلاش کنید.|SQL تمرین پیل نه شو. پوښتنه مو پاتې ده؛ بیا هڅه وکړئ.
Use one SELECT query on books, students, or loans. This practice does not change stored data.|یک پرس‌وجوی SELECT روی books، students یا loans بنویسید. این تمرین معلومات ذخیره‌شده را تغییر نمی‌دهد.|پر books، students یا loans یوه SELECT پوښتنه ولیکئ. دا تمرین ساتل شوي معلومات نه بدلوي.
Write a query of 1 to 2000 characters.|پرس‌وجو باید از 1 تا 2000 حرف داشته باشد.|پوښتنه باید له 1 تر 2000 تورو وي.
Use the displayed table and column names. Supported functions include COUNT, SUM, AVG, MIN, MAX, and COALESCE.|نام جدول و ستون نمایش‌داده‌شده را استفاده کنید. COUNT، SUM، AVG، MIN، MAX و COALESCE پشتیبانی می‌شوند.|ښودل شوي جدول او ستنې نومونه وکاروئ. COUNT، SUM، AVG، MIN، MAX او COALESCE ملاتړ کېږي.
The query could not run. Check column names, commas, quotes, and the order of SELECT, FROM, WHERE, GROUP BY, and ORDER BY.|پرس‌وجو اجرا نشد. نام ستون، کامه، نقل قول و ترتیب SELECT، FROM، WHERE، GROUP BY و ORDER BY را بررسی کنید.|پوښتنه ونه چلېده. د ستنې نوم، کامه، نقل قول او د SELECT، FROM، WHERE، GROUP BY او ORDER BY ترتیب وګورئ.
""")

rows(r"""
From foundations to advanced practice|از اساسات تا تمرین‌های پیشرفته|له بنسټونو تر پرمختللو تمرینونو
Start with the introduction. Study the workshops in order, then apply what you learned in a project. You can return to any earlier topic.|از معرفی آغاز کنید. کارگاه‌ها را به ترتیب بخوانید، سپس آموخته‌های خود را در یک پروژه عملی کنید. هر وقت خواستید به موضوع قبلی برگردید.|له پېژندنې پیل وکړئ. کارګاوې په ترتیب ولولئ، بیا زده کړي شیان په یوه پروژه کې عملي کړئ. هر پخواني مطلب ته بېرته تللی شئ.
Build your foundation|اساسات را یاد بگیرید|بنسټونه زده کړئ
Connect your skills|مهارت‌های خود را یکجا کنید|خپل مهارتونه سره وتړئ
Advanced practice|تمرین پیشرفته|پرمختللی تمرین
Your learning goal|هدف یادگیری شما|ستاسې د زده کړې موخه
Build on the previous lesson|از درس قبلی کمک بگیرید|له تېر درس څخه ګټه واخلئ
Before starting, explain the previous example in your own words and repeat its practice without copying. If you are unsure, revisit it first.|پیش از آغاز، مثال قبلی را به زبان خود توضیح دهید و تمرین آن را بدون کاپی تکرار کنید. اگر مطمئن نیستید، نخست آن را مرور کنید.|له پیل مخکې، پخوانی مثال په خپلو خبرو تشریح کړئ او تمرین یې له کاپي کولو پرته بیا وکړئ. که ډاډه نه یاست، لومړی یې بیا ولولئ.
Pause and predict|کمی مکث کنید و نتیجه را پیش‌بینی کنید|لږ تم شئ او پایله اټکل کړئ
Before reading the explanation, identify the input, follow each operation, and write the result you expect. Some examples are fragments: check the course tools before trying to run them.|پیش از خواندن توضیح، ورودی را مشخص کنید، هر عمل را دنبال کنید و نتیجهٔ مورد انتظار را بنویسید. بعضی مثال‌ها بخشی از برنامه هستند؛ پیش از اجرا، ابزارهای دوره را بررسی کنید.|د تشریح له لوستلو مخکې، ورودي معلومات وپېژنئ، هر عمل تعقیب کړئ او تمه شوې پایله ولیکئ. ځینې مثالونه د پروګرام برخې دي؛ له چلولو مخکې د کورس وسایل وګورئ.
Practice in small steps|قدم‌به‌قدم تمرین کنید|ګام په ګام تمرین وکړئ
First reproduce the example. Then change one value or rule and predict the difference. Finally complete the task without copying. Keep your work and explain why it works.|نخست مثال را دوباره بسازید. سپس یک مقدار یا قاعده را تغییر دهید و تفاوت را پیش‌بینی کنید. در پایان تمرین را بدون کاپی انجام دهید. کار خود را نگه دارید و توضیح دهید چرا درست کار می‌کند.|لومړی مثال بیا جوړ کړئ. بیا یو ارزښت یا قاعده بدله کړئ او توپیر اټکل کړئ. په پای کې تمرین له کاپي کولو پرته بشپړ کړئ. خپل کار وساتئ او تشریح کړئ چې ولې سم کار کوي.
When something goes wrong|وقتی نتیجه درست نیست|کله چې پایله سمه نه وي
Compare your result with your prediction. Find the first step where they differ. Check names, values, and punctuation; change one thing and try again. A mistake is a clue, not a reason to stop.|نتیجه را با پیش‌بینی خود مقایسه کنید. اولین قدمی را پیدا کنید که تفاوت ایجاد می‌شود. نام‌ها، مقدارها و نشانه‌ها را بررسی کنید؛ یک چیز را تغییر دهید و دوباره کوشش کنید. اشتباه برای یافتن مشکل کمک می‌کند، دلیل توقف نیست.|پایله له خپل اټکل سره پرتله کړئ. لومړی هغه ګام ومومئ چې توپیر پکې پیدا کېږي. نومونه، ارزښتونه او نښې وګورئ؛ یو شی بدل کړئ او بیا هڅه وکړئ. تېروتنه د ستونزې نښه ده، د درېدو دلیل نه دی.
Ready for the next lesson?|برای درس بعدی آماده هستید؟|راتلونکي درس ته چمتو یاست؟
You are ready when you can explain the idea, complete the task, and describe one mistake you corrected. This is a self-check, not an automatic grade. Use the practice activities below to save your evidence.|وقتی آماده هستید که بتوانید مفهوم را توضیح دهید، تمرین را انجام دهید و یک اشتباه اصلاح‌شده را شرح دهید. این بررسی شخصی است و نمرهٔ خودکار ندارد. برای ثبت کار خود از فعالیت‌های تمرینی پایین استفاده کنید.|هغه وخت چمتو یاست چې مفهوم تشریح، تمرین بشپړ او یوه سمه کړې تېروتنه بیان کړای شئ. دا خپله ارزونه ده او اتومات نمره نه لري. د خپل کار د ثبت لپاره لاندې تمرینونه وکاروئ.
""")

rows(r"""
Topic locked|موضوع قفل است|مطلب تړلی دی
Complete each topic to unlock the next. Finished topics remain available for review.|هر موضوع را تکمیل کنید تا موضوع بعدی باز شود. موضوع‌های تکمیل‌شده برای مرور باز می‌مانند.|هر مطلب بشپړ کړئ چې راتلونکی خلاص شي. بشپړ شوي مطالب د بیاکتنې لپاره خلاص پاتې کېږي.
I completed this activity and checked my work.|این فعالیت را تکمیل کردم و کار خود را بررسی کردم.|ما دا فعالیت بشپړ کړ او خپل کار مې وکوت.
Finish the earlier topics first. For Python foundations, solve every challenge. For workshops, save evidence and confirm completion in both practice activities. Projects unlock after the workshops.|نخست موضوع‌های قبلی را تکمیل کنید. در اساسات پایتون، همهٔ چالش‌ها را حل کنید. در کارگاه‌ها، کار خود را ذخیره کنید و تکمیل هر دو فعالیت تمرینی را تأیید کنید. پروژه‌ها پس از کارگاه‌ها باز می‌شوند.|لومړی پخواني مطالب بشپړ کړئ. د پایتون په بنسټونو کې ټولې ننګونې حل کړئ. په کارګاوو کې خپل کار وساتئ او د دواړو تمرینونو بشپړېدل تایید کړئ. پروژې له کارګاوو وروسته خلاصېږي.
Ready to start|آمادهٔ آغاز|پیل ته چمتو
Finish first: {0}|نخست این را تکمیل کنید: {0}|لومړی دا بشپړ کړئ: {0}
Finish the required earlier course or topic first. For Python foundations, solve every challenge. For workshops, save evidence and confirm completion in both practice activities. Projects unlock after the workshops.|نخست دوره یا موضوع لازم قبلی را تکمیل کنید. در اساسات پایتون، همهٔ چالش‌ها را حل کنید. در کارگاه‌ها، کار خود را ذخیره کنید و تکمیل هر دو فعالیت تمرینی را تأیید کنید. پروژه‌ها پس از کارگاه‌ها باز می‌شوند.|لومړی اړین پخوانی کورس یا مطلب بشپړ کړئ. د پایتون په بنسټونو کې ټولې ننګونې حل کړئ. په کارګاوو کې خپل کار وساتئ او د دواړو تمرینونو بشپړېدل تایید کړئ. پروژې له کارګاوو وروسته خلاصېږي.
Complete introduction and unlock topic 1|معرفی را تکمیل و موضوع اول را باز کنید|پېژندنه بشپړه او لومړی مطلب خلاص کړئ
Topic 1 unlocked|موضوع اول باز شد|لومړی مطلب خلاص شو
Finish the previous topic to unlock this lesson.|برای باز کردن این درس، موضوع قبلی را تکمیل کنید.|د دې درس د خلاصولو لپاره پخوانی مطلب بشپړ کړئ.
About and support|درباره و پشتیبانی|زموږ په اړه او ملاتړ
About, contact, and support|درباره، ارتباط و پشتیبانی|زموږ په اړه، اړیکه او ملاتړ
Meet Marifat Team and find the HesabPay support number.|با تیم معرفت آشنا شوید و شمارهٔ حمایت حساب‌پی را پیدا کنید.|د معرفت ټیم وپېژنئ او د حساب‌پی د ملاتړ شمېره ومومئ.
Learn, build, and help others learn.|یاد بگیرید، بسازید و به یادگیری دیگران کمک کنید.|زده کړئ، جوړ یې کړئ او له نورو سره په زده کړه کې مرسته وکړئ.
Learn By Marifat Team is designed for Afghan students who need clear programming education that remains available without internet.|Learn By Marifat Team برای دانشجویان افغانستان ساخته شده که به آموزش روشن برنامه‌نویسی نیاز دارند و باید بدون اینترنت نیز در دسترس باشد.|Learn By Marifat Team د افغانستان هغو زده‌کوونکو لپاره جوړ شوی چې روښانه پروګرام‌لیکنې زده کړې ته اړتیا لري او باید له انټرنېټ پرته هم ورته لاسرسی ولري.
Support the project|از پروژه حمایت کنید|د پروژې ملاتړ وکړئ
Your voluntary contribution helps Marifat Team improve offline lessons, translations, testing, and learning resources. Learning content remains available without a donation.|کمک داوطلبانهٔ شما به تیم معرفت کمک می‌کند درس‌های آفلاین، ترجمه‌ها، آزمایش و منابع یادگیری را بهتر سازد. محتوای آموزشی بدون کمک مالی نیز در دسترس می‌ماند.|ستاسې خپله خوښه مرسته له معرفت ټیم سره د آفلاین درسونو، ژباړو، ازموینو او زده‌کړیزو سرچینو په ښه کولو کې مرسته کوي. زده‌کړیز مطالب له مرستې پرته هم د لاسرسي وړ پاتې کېږي.
HesabPay|حساب‌پی|حساب‌پی
Copy HesabPay number|کاپی شمارهٔ حساب‌پی|د حساب‌پی شمېره کاپي کړئ
HesabPay number copied|شمارهٔ حساب‌پی کاپی شد|د حساب‌پی شمېره کاپي شوه
About Marifat Team|دربارهٔ تیم معرفت|د معرفت ټیم په اړه
Marifat Software Team builds practical software and educational tools. This project focuses on understandable, project-based programming education for Afghanistan, with English, Dari, and Pashto content stored on the learner’s device.|تیم نرم‌افزاری معرفت نرم‌افزارهای کاربردی و ابزارهای آموزشی می‌سازد. این پروژه بر آموزش قابل‌فهم و پروژه‌محور برنامه‌نویسی برای افغانستان تمرکز دارد و محتوای انگلیسی، دری و پشتو را روی دستگاه یادگیرنده نگه می‌دارد.|د معرفت سافټویر ټیم عملي سافټویر او زده‌کړیز وسایل جوړوي. دا پروژه د افغانستان لپاره پر پوهېدونکې او پروژه‌محوره پروګرام‌لیکنې زده کړه تمرکز کوي او انګلیسي، دري او پښتو مطالب د زده‌کوونکي پر آله ساتي.
About the founder|دربارهٔ بنیان‌گذار|د بنسټګر په اړه
The founder’s verified name, biography, role, and public profile will be shown here after they are provided. The app does not invent or publish personal information.|نام تأییدشده، زندگی‌نامه، نقش و صفحهٔ عمومی بنیان‌گذار پس از دریافت در اینجا نشان داده می‌شود. برنامه اطلاعات شخصی را حدس نمی‌زند یا منتشر نمی‌کند.|د بنسټګر تایید شوی نوم، ژوندلیک، دنده او عامه پاڼه به له ترلاسه کېدو وروسته دلته ښکاره شي. اپ شخصي معلومات نه اټکلوي او نه یې خپروي.
Contact Marifat Team|ارتباط با تیم معرفت|له معرفت ټیم سره اړیکه
Verified public email, website, social pages, and messaging contacts will be listed here after they are provided.|ایمیل عمومی، وب‌سایت، صفحه‌های اجتماعی و راه‌های پیام‌رسانی تأییدشده پس از دریافت در اینجا فهرست می‌شوند.|تایید شوی عامه برېښنالیک، وېبپاڼه، ټولنیزې پاڼې او د پیغام اړیکې به له ترلاسه کېدو وروسته دلته ولیکل شي.
YouTube channel|کانال یوتیوب|یوټیوب چینل
The verified YouTube channel link will appear here after it is provided. Opening YouTube requires an internet connection; the courses themselves remain offline.|لینک تأییدشدهٔ کانال یوتیوب پس از دریافت در اینجا نشان داده می‌شود. باز کردن یوتیوب به اینترنت نیاز دارد؛ خود دوره‌ها آفلاین باقی می‌مانند.|د یوټیوب تایید شوی لینک به له ترلاسه کېدو وروسته دلته ښکاره شي. د یوټیوب پرانیستل انټرنېټ غواړي؛ خپله کورسونه آفلاین پاتې کېږي.
Learn By Marifat Team 2.9 · 20 offline courses\nOriginal course content. A local-first learning application for Afghan CS students. No analytics, remote services, or online activation. Practice scores are learning aids, not formal credentials.|Learn By Marifat Team 2.9 · ۲۰ دورهٔ آفلاین\nمحتوای اصلی دوره. یک برنامهٔ آموزشی با اولویت ذخیرهٔ محلی برای دانشجویان کمپیوترساینس افغانستان. بدون تحلیل رفتار، خدمات راه دور یا فعال‌سازی آنلاین. امتیاز تمرین ابزار یادگیری است، نه مدرک رسمی.|Learn By Marifat Team 2.9 · ۲۰ آفلاین کورسونه\nاصلي کورسي مطالب. د افغانستان د کمپیوټر ساینس زده‌کوونکو لپاره محلي لومړیتوب زده‌کړیز اپ. شننه، لیرې خدمتونه او آنلاین فعالول نه لري. د تمرین نمرې د زده کړې مرسته ده، رسمي سند نه دی.
Learn By Marifat Team 3.1 · 20 offline courses\nOriginal course content. A local-first learning application for Afghan CS students. No analytics, remote services, or online activation. Practice scores are learning aids, not formal credentials.|Learn By Marifat Team 3.1 · ۲۰ دورهٔ آفلاین\nمحتوای اصلی دوره. یک برنامهٔ آموزشی با اولویت ذخیرهٔ محلی برای دانشجویان کمپیوترساینس افغانستان. بدون تحلیل رفتار، خدمات راه دور یا فعال‌سازی آنلاین. امتیاز تمرین ابزار یادگیری است، نه مدرک رسمی.|Learn By Marifat Team 3.1 · ۲۰ آفلاین کورسونه\nاصلي کورسي مطالب. د افغانستان د کمپیوټر ساینس زده‌کوونکو لپاره محلي لومړیتوب زده‌کړیز اپ. شننه، لیرې خدمتونه او آنلاین فعالول نه لري. د تمرین نمرې د زده کړې مرسته ده، رسمي سند نه دی.
Learn By Marifat Team 3.0 · 20 offline courses\nOriginal course content. A local-first learning application for Afghan CS students. No analytics, remote services, or online activation. Practice scores are learning aids, not formal credentials.|Learn By Marifat Team 3.0 · ۲۰ دورهٔ آفلاین\nمحتوای اصلی دوره. یک برنامهٔ آموزشی با اولویت ذخیرهٔ محلی برای دانشجویان کمپیوترساینس افغانستان. بدون تحلیل رفتار، خدمات راه دور یا فعال‌سازی آنلاین. امتیاز تمرین ابزار یادگیری است، نه مدرک رسمی.|Learn By Marifat Team 3.0 · ۲۰ آفلاین کورسونه\nاصلي کورسي مطالب. د افغانستان د کمپیوټر ساینس زده‌کوونکو لپاره محلي لومړیتوب زده‌کړیز اپ. شننه، لیرې خدمتونه او آنلاین فعالول نه لري. د تمرین نمرې د زده کړې مرسته ده، رسمي سند نه دی.
STORE_BUILD|STORE_BUILD|STORE_BUILD
This is not a supported Learn By Marifat Team backup (version 1, 2, 3, or 4).|این فایل پشتیبان پشتیبانی نمی‌شود؛ نسخه باید 1، 2، 3 یا 4 برنامهٔ Learn By Marifat Team باشد.|دا شاتړ فایل نه ملاتړ کېږي؛ باید د Learn By Marifat Team د 1، 2، 3 یا 4 نسخې وي.
Safi Ullah Mirzai|صفی‌الله میرزایی|صفي‌الله میرزایي
Founder of Marifat Software Team, senior full-stack developer, and computer science lecturer in Kabul. He teaches databases, programming, mobile application development, software engineering, computer architecture, and software assurance. He holds a bachelor’s degree in Computer Science (Software Engineering) and is pursuing a master’s degree in Information Systems at Kabul University. His work includes educational tools, management information systems, web applications, mobile development, and database systems.|صفی‌الله میرزایی بنیان‌گذار تیم نرم‌افزاری معرفت، توسعه‌دهندهٔ ارشد فول‌استک و استاد کمپیوترساینس در کابل است. او دیتابیس، برنامه‌نویسی، توسعهٔ اپلیکیشن موبایل، مهندسی نرم‌افزار، معماری کمپیوتر و تضمین نرم‌افزار تدریس می‌کند. او مدرک لیسانس کمپیوترساینس در رشتهٔ مهندسی نرم‌افزار دارد و در دانشگاه کابل دورهٔ ماستری سیستم‌های اطلاعاتی را دنبال می‌کند. کارهای او شامل ابزارهای آموزشی، سیستم‌های معلوماتی مدیریتی، برنامه‌های وب، توسعهٔ موبایل و سیستم‌های دیتابیس است.|صفي‌الله میرزایي د معرفت سافټویر ټیم بنسټګر، د فول‌سټک لوړپوړی پراختیاکوونکی او په کابل کې د کمپیوټرساینس استاد دی. هغه ډیټابیسونه، پروګرام‌لیکنه، د موبایل اپلېکېشن پراختیا، سافټویر انجینري، د کمپیوټر معماري او د سافټویر تضمین تدریسوي. هغه د کمپیوټرساینس د سافټویر انجینرۍ لیسانس لري او په کابل پوهنتون کې د معلوماتي سیسټمونو ماستري تعقیبوي. د هغه په کارونو کې زده‌کړیز وسایل، مدیریتي معلوماتي سیسټمونه، وېب اپلېکېشنونه، د موبایل پراختیا او ډیټابیس سیسټمونه شامل دي.
Use the copy button to save a contact address. Opening websites and social pages requires internet access.|برای ذخیرهٔ یک راه ارتباطی از دکمهٔ کاپی استفاده کنید. باز کردن وب‌سایت‌ها و صفحه‌های اجتماعی به اینترنت نیاز دارد.|د اړیکې پته د ساتلو لپاره د کاپي تڼۍ وکاروئ. د وېبپاڼو او ټولنیزو پاڼو پرانیستل انټرنېټ غواړي.
Email|ایمیل|برېښنالیک
Website|وب‌سایت|وېبپاڼه
LinkedIn|لینکدین|لېنکډاېن
GitHub|گیت‌هاب|ګېټ‌هب
Phone and WhatsApp|تلفن و واتساپ|تلیفون او واټس‌اپ
Copy contact|کاپی راه ارتباطی|اړیکه کاپي کړئ
Contact copied|راه ارتباطی کاپی شد|اړیکه کاپي شوه
sumirzai@gmail.com|sumirzai@gmail.com|sumirzai@gmail.com
safimirzai.dev|safimirzai.dev|safimirzai.dev
linkedin.com/in/kingsum007|linkedin.com/in/kingsum007|linkedin.com/in/kingsum007
github.com/Kingsum007|github.com/Kingsum007|github.com/Kingsum007
A YouTube channel was not listed in the provided résumé. The verified channel link will appear here after it is provided. Opening YouTube requires an internet connection; the courses themselves remain offline.|در رزومهٔ ارائه‌شده کانال یوتیوب ذکر نشده است. لینک تأییدشدهٔ کانال پس از دریافت در اینجا نشان داده می‌شود. باز کردن یوتیوب به اینترنت نیاز دارد؛ خود دوره‌ها آفلاین باقی می‌مانند.|په ورکړل شوې ژوندلیک کې د یوټیوب چینل نه و یاد شوی. تایید شوی لینک به له ترلاسه کېدو وروسته دلته ښکاره شي. د یوټیوب پرانیستل انټرنېټ غواړي؛ خپله کورسونه آفلاین پاتې کېږي.
Code With Safi|کُد با صفی|له صفي سره کوډ
Watch programming lessons and practical tutorials on the official YouTube channel. Opening YouTube requires internet; the courses in this app remain offline.|درس‌های برنامه‌نویسی و آموزش‌های عملی را در کانال رسمی یوتیوب تماشا کنید. باز کردن یوتیوب به اینترنت نیاز دارد؛ دوره‌های داخل این برنامه آفلاین باقی می‌مانند.|د پروګرام‌لیکنې درسونه او عملي ښوونې په رسمي یوټیوب چینل کې وګورئ. د یوټیوب پرانیستل انټرنېټ غواړي؛ د دې اپ کورسونه آفلاین پاتې کېږي.
Open YouTube channel|بازکردن کانال یوتیوب|د یوټیوب چینل پرانیستل
Copy channel link|کاپی لینک کانال|د چینل لینک کاپي کړئ
YouTube link copied|لینک یوتیوب کاپی شد|د یوټیوب لینک کاپي شو
Could not open the YouTube channel|کانال یوتیوب باز نشد|د یوټیوب چینل خلاص نه شو
https://www.youtube.com/@codewithsafi-sum|https://www.youtube.com/@codewithsafi-sum|https://www.youtube.com/@codewithsafi-sum
START HERE|از این‌جا آغاز کنید|له دې ځایه پیل کړئ
Learn programming step by step|برنامه‌نویسی را گام‌به‌گام بیاموزید|پروګرام‌لیکنه ګام په ګام زده کړئ
Never coded before? Begin with Python. We explain every new idea, then help you practise it in a small project.|قبلاً کُد ننوشته‌اید؟ با پایتون آغاز کنید. هر مفهوم تازه را با توضیح روشن یاد می‌گیرید و سپس آن را در یک پروژهٔ کوچک تمرین می‌کنید.|مخکې مو کوډ نه دی لیکلی؟ له پایتون څخه پیل وکړئ. هر نوی مفهوم درته روښانه کوو، بیا یې په یوې کوچنۍ پروژې کې تمرینوئ.
Start with Python|آغاز با پایتون|له پایتون سره پیل
Learning paths|مسیرهای یادگیری|د زده‌کړې لارې
{0} courses|{0} دوره|{0} کورسونه
Begin with the first available path. New paths unlock as you complete their foundations.|از نخستین مسیر باز آغاز کنید. با تکمیل مبانی، مسیرهای تازه برایتان باز می‌شوند.|له لومړۍ پرانیستې لارې پیل وکړئ. د بنسټونو په بشپړولو سره نوې لارې درته پرانیستل کېږي.
Completed|تکمیل‌شده|بشپړ شوی
Locked|قفل|تړلی
Beginner friendly · no prior experience needed|مناسب مبتدی · بدون نیاز به تجربهٔ قبلی|د پیل کوونکي لپاره مناسب · پخوانۍ تجربه نه غواړي
Your next learning path is ready|مسیر بعدی یادگیری شما آماده است|ستاسې راتلونکې زده‌کړیزه لاره چمتو ده
Complete first: {0}|نخست تکمیل کنید: {0}|لومړی بشپړ کړئ: {0}
{0} modules|{0} بخش|{0} برخې
{0} projects|{0} پروژه|{0} پروژې
web-development|web-development|web-development
javascript|javascript|javascript
nodejs|nodejs|nodejs
expressjs|expressjs|expressjs
postgresql|postgresql|postgresql
mongodb|mongodb|mongodb
Quick checkpoint|بررسی کوتاه|لنډه کتنه
Reproduce the example, change one value, and predict the result. If it fails, find the first step that differs from your prediction and change one thing at a time. Continue when you can complete the task and explain one correction you made.|نمونه را دوباره بسازید، یک مقدار را تغییر دهید و نتیجه را پیش‌بینی کنید. اگر ناکام شد، نخستین گامی را پیدا کنید که با پیش‌بینی شما فرق دارد و هر بار فقط یک چیز را تغییر دهید. زمانی ادامه دهید که کار را تکمیل و یک اصلاح خود را توضیح داده بتوانید.|بېلګه بیا جوړه، یو ارزښت بدل او پایله اټکل کړئ. که ناکامه شوه، لومړی هغه ګام ومومئ چې له اټکل سره توپیر لري او هر ځل یوازې یو شی بدل کړئ. هغه وخت دوام ورکړئ چې کار بشپړ او خپل یو سمون تشریح کولی شئ.
Privacy and learner data|حریم خصوصی و داده‌های یادگیرنده|محرمیت او د زده‌کوونکي معلومات
The app has no account, advertising, analytics, or remote server. Lessons, progress, answers, drafts, and portfolio notes stay on this device. The app does not transmit learner data. You choose when and where to export a local backup. Opening the YouTube channel leaves the app and follows the privacy terms of the external service.|برنامه حساب کاربری، تبلیغات، تحلیل رفتار یا سرور دور ندارد. درس‌ها، پیشرفت، جواب‌ها، پیش‌نویس‌ها و یادداشت‌های دوسیه روی همین دستگاه می‌مانند. برنامه داده‌های یادگیرنده را انتقال نمی‌دهد. زمان و محل صدور پشتیبان محلی را خودتان انتخاب می‌کنید. بازکردن کانال یوتیوب شما را از برنامه بیرون می‌برد و تابع شرایط حریم خصوصی آن خدمت است.|اپ حساب، اعلانونه، شننه یا لیرې سرور نه لري. درسونه، پرمختګ، ځوابونه، مسودې او د کار دوسیې یادښتونه پر همدې آله پاتې کېږي. اپ د زده‌کوونکي معلومات نه لېږي. د محلي شاتړ د صادرولو وخت او ځای تاسې ټاکئ. د یوټیوب چینل پرانیستل له اپ څخه وځي او د بهرني خدمت د محرمیت شرطونه پلي کېږي.
""")
