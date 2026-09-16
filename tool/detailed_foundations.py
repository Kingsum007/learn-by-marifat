"""Parallel, authored teaching text. Language coverage is not native review."""
import json
from pathlib import Path

# Each lesson has: a grounded explanation, a trace of the existing example,
# and help transferring the idea to the existing assessed exercises.
GUIDES = {
'hello': {
'en': [
'''A computer does not understand an intention such as “greet my class” on its own. A program gives it exact instructions. Code is the text in which we write those instructions; Python is one language for writing them. You do not need to install anything to do these introductory exercises in this app.

Think of the editor as the place where you write instructions and the output area as the place where you see their result. Writing code alone does not display its result: the Run button asks the app to execute it. print() is an instruction that displays a value. The parentheses contain what to display. Text must be enclosed in a matching pair of straight quotes, such as "Salam". These marks tell Python where the text starts and ends; they are not displayed.

Python reads these instructions from top to bottom. A line starting with # is a note for the reader. You may write a comment to explain your intention, but the comment itself does not display a greeting.''',
'''Line 1 is a comment, so it produces no output. Line 2 passes the text Hello, Afghanistan! to print(). That text appears on the first output line. Line 3 passes I can learn to code. to another print() call; it appears on the next output line. The quotation marks and parentheses belong to the code, not to the result.

Before continuing, say which message would appear first if you swapped the two print lines. It would be I can learn to code. The computer follows the new order; it does not decide which greeting sounds better.''',
'''For the first question, choose what a reader would see in the output, not the punctuation used to write the instruction. For the ordering exercise, place the instruction for First before the instruction for Second. For the writing exercise, write two separate print() calls: one for Salam and one for Kabul. Run your code and compare both the words and their order with the requested result.

If your code does not run, check that every opening quote has a closing quote and every opening parenthesis has a closing parenthesis. Use straight keyboard quotes, not decorative quotation marks. Python names are case-sensitive: Print is different from print. An error is information about what to correct; change one thing and run again.'''],
'fa': [
'''کمپیوتر خواست شما را خودبه‌خود نمی‌فهمد. اگر بخواهید «به صنف سلام بده»، باید دستور دقیق بنویسید. مجموعهٔ این دستورها یک پروگرام است. متنی را که برای نوشتن دستورها استفاده می‌کنیم، کود می‌گوییم. پایتون یکی از زبان‌های نوشتن کود است. برای انجام تمرین‌های ابتدایی این بخش، به نصب ابزار دیگر ضرورت ندارید.

محل نوشتن کود جایی است که دستور خود را می‌نویسید؛ بخش نتیجه نشان می‌دهد پس از اجرا چه اتفاق افتاده است. تنها نوشتن کود کافی نیست: دکمهٔ اجرا را بزنید تا برنامه دستورها را اجرا کند. دستور print() یک مقدار را در بخش نتیجه نشان می‌دهد. داخل قوس‌ها مشخص می‌کنیم چه چیزی نمایش داده شود. متن را میان دو علامت نقل قول مستقیم، مانند "Salam"، می‌نویسیم. این علامت‌ها آغاز و پایان متن را مشخص می‌کنند و در نتیجه دیده نمی‌شوند.

پایتون این دستورها را از بالا به پایین اجرا می‌کند. خطی که با # شروع شود، یادداشت برای خواننده است. یادداشت می‌تواند هدف کود را توضیح بدهد، اما خودش پیامی را نمایش نمی‌دهد.''',
'''خط اول یادداشت است؛ بنابراین چیزی در بخش نتیجه نشان نمی‌دهد. در خط دوم، متن Hello, Afghanistan! به print() داده می‌شود و در سطر اول نتیجه ظاهر می‌شود. در خط سوم، متن I can learn to code. به دستور دیگر print() داده می‌شود و در سطر بعدی ظاهر می‌شود. علامت‌های نقل قول و قوس‌ها جزو نوشتار کود اند، نه جزو نتیجه.

پیش از ادامه فکر کنید: اگر جای دو خط print را عوض کنیم، کدام پیام اول دیده می‌شود؟ پیام I can learn to code. اول می‌آید. کمپیوتر ترتیب تازهٔ دستورها را دنبال می‌کند؛ خودش تصمیم نمی‌گیرد کدام سلام مناسب‌تر است.''',
'''در پرسش اول، چیزی را انتخاب کنید که در بخش نتیجه دیده می‌شود؛ نه علامت‌هایی را که برای نوشتن دستور استفاده شده‌اند. در تمرین ترتیب، دستور نمایش First را پیش از دستور نمایش Second قرار بدهید. در تمرین نوشتن، دو دستور جداگانهٔ print() بنویسید: یکی برای Salam و دیگری برای Kabul. کود را اجرا کنید و واژه‌ها و ترتیب سطرها را با نتیجهٔ خواسته‌شده مقایسه کنید.

اگر کود اجرا نشد، ببینید هر نقل قول باز، نقل قول بسته دارد و هر قوس باز، قوس بسته دارد. از نقل قول مستقیم صفحه‌کلید استفاده کنید. نام‌ها به حروف کلان و کوچک حساس اند: Print با print فرق دارد. پیام خطا کمک می‌کند بفهمید کجا را اصلاح کنید؛ یک مورد را تغییر بدهید و دوباره اجرا کنید.'''],
'ps': [
'''کمپیوټر ستاسو موخه په خپله نه پوهېږي. که غواړئ «زما ټولګي ته سلام ووایه»، باید ورته څرګندې لارښوونې ولیکئ. د دغو لارښوونو ټولګې ته پروګرام وایو. هغه متن چې لارښوونې پکې لیکو، کوډ دی. پایتون د کوډ لیکلو یوه ژبه ده. د دې برخې د لومړنیو تمرینونو لپاره بل پروګرام نصبول اړین نه دي.

د کوډ لیکلو ځای هغه برخه ده چې لارښوونې پکې لیکئ؛ د پایلې برخه ښيي چې له چلولو وروسته څه وشول. یوازې لیکل پایله نه ښيي: د چلولو تڼۍ کېکاږئ چې لارښوونې اجرا شي. print() یو ورکړل شوی ارزښت د پایلې په برخه کې ښيي. د قوسونو دننه لیکو چې څه باید ښکاره شي. متن د نقل قول د دوو نېغو نښو ترمنځ لیکو، لکه "Salam". دا نښې د متن پیل او پای ټاکي؛ په پایله کې نه ښکاري.

پایتون دا لارښوونې له پاسه ښکته اجرا کوي. هغه کرښه چې په # پیل کېږي، د لوستونکي لپاره یادونه ده. یادونه د کوډ موخه تشریح کولای شي، خو په خپله سلام نه ښکاره کوي.''',
'''لومړۍ کرښه یادونه ده؛ نو په پایله کې هېڅ نه ښيي. دویمه کرښه Hello, Afghanistan! متن print() ته ورکوي او دا متن د پایلې په لومړۍ کرښه کې ښکاري. درېیمه کرښه I can learn to code. متن بل print() ته ورکوي او هغه په بله کرښه کې ښکاري. د نقل قول نښې او قوسونه د کوډ د لیکلو برخه دي، د پایلې برخه نه دي.

له مخکې تلو وړاندې فکر وکړئ: که د دواړو print کرښو ځایونه بدل کړو، کوم پیغام به لومړی ښکاره شي؟ I can learn to code. به لومړی وي. کمپیوټر نوی ترتیب تعقیبوي؛ په خپله نه ټاکي چې کوم سلام غوره دی.''',
'''په لومړۍ پوښتنه کې هغه څه وټاکئ چې د پایلې په برخه کې ښکاري، نه د کوډ د لیکلو نښې. د ترتیب په تمرین کې د First د ښودلو لارښوونه د Second له لارښوونې مخکې کېږدئ. د لیکلو په تمرین کې دوه جلا print() لارښوونې ولیکئ: یوه د Salam او بله د Kabul لپاره. کوډ وچلوئ او ټکي او د کرښو ترتیب له غوښتل شوې پایلې سره پرتله کړئ.

که کوډ نه چلېږي، وګورئ چې هره پرانیستې د نقل قول نښه تړونکې نښه لري او هر پرانیستی قوس تړل شوی دی. د کیبورډ نېغې نښې وکاروئ. لوی او واړه توري توپیر لري: Print له print سره یو شان نه دی. د تېروتنې پیغام د سمولو ځای درښيي؛ یو شی سم کړئ او بیا یې وچلوئ.''']},
'variables': {
'en': ['''Suppose a class has 24 students and one more joins. We need to keep the old count and replace it with a new count. A variable is a name referring to a value, such as students referring to 24. Assignment uses =. First Python works out the right-hand side; then it makes the name on the left refer to that result.

Text and numbers have different roles. "Herat" is text and needs quotes. 24 is a number and can take part in arithmetic. students without quotes asks for the stored value; "students" means the literal word students. A meaningful name makes your program easier to read.''',
'''Line 1 assigns the text Herat to city. Line 2 assigns 24 to students. Line 3 first reads the old students value, calculates 24 + 1, and assigns 25 back to students. This is why students = students + 1 is a valid update: it is not a mathematical equality. Line 4 displays Herat. Line 5 displays 25. Assignment alone has not displayed anything.

If another students = students + 1 line came before the print, the displayed count would be 26. If print(students) came before the update instead, it would display 24.''',
'''In the writing activity, books already has the value 12. Add 3 to that stored value and assign the result back to books; then display books. Reading from a variable before assigning it a value is an error. Check spelling and letter case if the app says a name is unknown.

Do not put the variable name in quotes when you want its value. print("books") shows the word books, whereas print(books) shows its current value. After your solution works, explain why placing print before the update changes the result.'''],
'fa': ['''فرض کنید در یک صنف ۲۴ شاگرد است و یک شاگرد دیگر شامل می‌شود. باید تعداد قبلی را نگه داریم و بعد با تعداد تازه عوض کنیم. متغیر نامی است که به یک مقدار اشاره می‌کند؛ مثلاً students به مقدار 24 اشاره می‌کند. برای دادن مقدار از = استفاده می‌کنیم. پایتون اول طرف راست را حساب می‌کند، سپس نتیجه را به نام طرف چپ می‌دهد.

متن و عدد یک کار را انجام نمی‌دهند. "Herat" متن است و به نقل قول ضرورت دارد. 24 عدد است و می‌توانیم با آن حساب کنیم. students بدون نقل قول یعنی مقدار ذخیره‌شده را بخوان؛ "students" یعنی خودِ واژهٔ students. نام روشن کمک می‌کند هدف کود را بفهمید.''',
'''خط اول متن Herat را به city می‌دهد. خط دوم مقدار 24 را به students می‌دهد. خط سوم نخست مقدار قبلی students را می‌خواند، 24 + 1 را حساب می‌کند و مقدار 25 را دوباره در students نگه می‌دارد. پس students = students + 1 یک دستور تغییر مقدار است، نه تساوی ریاضی. خط چهارم Herat و خط پنجم 25 را نمایش می‌دهد. دستورهای مقداردهی به‌تنهایی چیزی نمایش نداده‌اند.

اگر پیش از نمایش یک بار دیگر students = students + 1 اجرا شود، تعداد 26 دیده می‌شود. اگر print(students) پیش از تغییر مقدار باشد، تعداد 24 دیده می‌شود.''',
'''در تمرین نوشتن، books از قبل مقدار 12 دارد. به همان مقدار 3 اضافه کنید، نتیجه را دوباره به books بدهید و سپس مقدار books را نمایش بدهید. خواندن متغیر پیش از مقداردهی خطا است. اگر برنامه می‌گوید نام شناخته نشده، املای نام و حروف کلان و کوچک آن را بررسی کنید.

وقتی مقدار متغیر را می‌خواهید، نامش را داخل نقل قول نگذارید. print("books") خودِ واژهٔ books را نشان می‌دهد؛ print(books) مقدار فعلی آن را نشان می‌دهد. پس از درست شدن کود، توضیح بدهید چرا انتقال print به پیش از تغییر مقدار، نتیجه را عوض می‌کند.'''],
'ps': ['''فرض کړئ په یوه ټولګي کې ۲۴ زده کوونکي دي او یو بل ورسره یوځای کېږي. پخوانی شمېر ساتو او بیا یې په نوي شمېر بدلوو. متغیر هغه نوم دی چې یوه ارزښت ته اشاره کوي؛ لکه students چې 24 ته اشاره کوي. د ارزښت ورکولو لپاره = کاروو. پایتون لومړی ښی اړخ حسابوي، بیا پایله د کیڼ اړخ نوم ته ورکوي.

متن او شمېر بېل کارونه لري. "Herat" متن دی او د نقل قول نښو ته اړتیا لري. 24 شمېر دی او حساب پرې کولای شو. students له نښو پرته د ساتل شوي ارزښت لوستل غواړي؛ "students" خپله د students کلمه ده. څرګند نوم د کوډ په پوهېدو کې مرسته کوي.''',
'''لومړۍ کرښه Herat متن city ته ورکوي. دویمه کرښه 24 ارزښت students ته ورکوي. درېیمه کرښه لومړی د students پخوانی ارزښت لولي، 24 + 1 حسابوي او 25 بېرته students ته ورکوي. له همدې امله students = students + 1 د ارزښت بدلولو لارښوونه ده، ریاضيکي مساوات نه دی. څلورمه کرښه Herat او پنځمه 25 ښيي. یوازې ارزښت ورکولو هېڅ نه دي ښکاره کړي.

که له ښودلو مخکې students = students + 1 یو ځل بیا وچلېږي، 26 به ښکاره شي. که print(students) له بدلون مخکې وي، 24 به ښکاره شي.''',
'''د لیکلو په تمرین کې books له مخکې 12 ارزښت لري. 3 ورزیات کړئ، پایله بېرته books ته ورکړئ او بیا یې ارزښت ښکاره کړئ. متغیر ته له ارزښت ورکولو مخکې د هغه لوستل تېروتنه ده. که پروګرام نوم نه پېژني، املا او لوی او واړه توري یې وګورئ.

کله چې د متغیر ارزښت غواړئ، نوم یې د نقل قول په نښو کې مه لیکئ. print("books") د books کلمه ښيي، خو print(books) یې اوسنی ارزښت ښيي. له سمېدو وروسته ووایئ چې ولې د بدلون مخکې د print لیکل پایله بدلوي.''']},
'numbers': {
'en': ['''Imagine sharing 17 books equally among 5 students without cutting a book. Each student gets 3 books; 2 are left. Python uses // for floor division and % for the remainder. With these positive whole numbers, these operations answer “how many whole books each?” and “how many remain?”. Ordinary / division instead gives 3.4.

Use + to add, - to subtract, and * to multiply. Multiplication and division are evaluated before addition and subtraction: 2 + 3 * 4 is 14. Parentheses change the grouping: (2 + 3) * 4 is 20. Floor division rounds down, not towards zero: -7 // 3 is -3. First practise the positive book example before trying negative values.''',
'''Lines 1 and 2 store 17 and 5. Line 3 calculates 17 // 5 and displays 3. Line 4 calculates 17 % 5 and displays 2. Check the sharing: 5 * 3 + 2 equals the original 17 books. Line 5 calculates the parentheses first, so 2 + 3 becomes 5, then 5 * 4 becomes 20. The output therefore has three lines: 3, 2, and 20.

If there were 20 books instead, each student would get 4 and the remainder would be 0. A remainder of zero means the books divide evenly.''',
'''Before entering a calculation, work out a small example by hand. Use parentheses if you mean to add before multiplying. Do not use the letter x as a multiplication sign; Python uses *. A divisor cannot be zero: dividing books among zero students has no valid result here.

When an answer differs from your prediction, inspect the order of operations before changing the numbers. Explain separately the whole share and the remainder; they answer different questions.'''],
'fa': ['''تصور کنید ۱۷ کتاب را میان ۵ شاگرد مساوی تقسیم می‌کنیم و هیچ کتابی را تکه نمی‌کنیم. به هر شاگرد ۳ کتاب می‌رسد و ۲ کتاب باقی می‌ماند. در پایتون // تقسیم با گرد کردن به پایین و % باقی‌مانده را حساب می‌کند. برای این عددهای صحیح مثبت، اولی سهم کامل هر نفر و دومی تعداد باقی‌مانده را می‌دهد. تقسیم عادی با / نتیجهٔ 3.4 می‌دهد.

برای جمع +، برای تفریق - و برای ضرب * بنویسید. ضرب و تقسیم پیش از جمع و تفریق حساب می‌شوند؛ پس 2 + 3 * 4 برابر 14 است. قوس ترتیب را تغییر می‌دهد: (2 + 3) * 4 برابر 20 است. تقسیم // به پایین گرد می‌کند، نه به طرف صفر؛ بنابراین -7 // 3 برابر -3 است. نخست مثال کتاب‌ها با عددهای مثبت را تمرین کنید.''',
'''خط‌های اول و دوم 17 و 5 را ذخیره می‌کنند. خط سوم 17 // 5 را حساب می‌کند و 3 را نمایش می‌دهد. خط چهارم 17 % 5 را حساب می‌کند و 2 را نشان می‌دهد. برای بررسی: 5 * 3 + 2 همان 17 کتاب اولیه است. خط پنجم اول داخل قوس را حساب می‌کند؛ 2 + 3 می‌شود 5 و سپس 5 * 4 می‌شود 20. نتیجه سه سطر دارد: 3، سپس 2 و بعد 20.

اگر به‌جای 17، تعداد کتاب‌ها 20 باشد، سهم هر شاگرد 4 و باقی‌مانده 0 می‌شود. باقی‌ماندهٔ صفر یعنی تقسیم بدون باقی‌مانده انجام شده است.''',
'''پیش از نوشتن محاسبه، یک نمونهٔ کوچک را خودتان حساب کنید. اگر می‌خواهید جمع پیش از ضرب انجام شود، از قوس استفاده کنید. حرف x علامت ضرب در پایتون نیست؛ باید * بنویسید. عددی که بر آن تقسیم می‌کنید نباید صفر باشد؛ تقسیم کتاب‌ها میان صفر شاگرد در این محاسبه نتیجهٔ معتبر ندارد.

اگر جواب با پیش‌بینی شما فرق داشت، پیش از تغییر عددها ترتیب عملیات را بررسی کنید. سهم کامل و باقی‌مانده را جدا توضیح بدهید؛ هر کدام به پرسش متفاوت جواب می‌دهد.'''],
'ps': ['''فکر وکړئ ۱۷ کتابونه پر ۵ زده کوونکو مساوي وېشو او هېڅ کتاب نه ټوټه کوو. هر زده کوونکي ته ۳ کتابونه رسېږي او ۲ پاتې کېږي. په پایتون کې // د وېش پایله ښکته بشپړ عدد ته راګرځوي او % پاتې شونی حسابوي. د دغو مثبتو بشپړو عددونو لپاره لومړی عمل د هر کس بشپړه برخه او دویم پاتې کتابونه راکوي. عادي وېش په / سره 3.4 ورکوي.

د جمع لپاره +، د تفریق لپاره - او د ضرب لپاره * ولیکئ. ضرب او وېش له جمع او تفریق مخکې حسابېږي؛ نو 2 + 3 * 4 برابر له 14 سره دی. قوسونه ترتیب بدلوي: (2 + 3) * 4 برابر له 20 سره دی. // پایله ښکته راګرځوي، نه د صفر پر لور؛ نو -7 // 3 برابر له -3 سره دی. لومړی د کتابونو مثبت مثال تمرین کړئ.''',
'''لومړۍ او دویمه کرښه 17 او 5 ساتي. درېیمه کرښه 17 // 5 حسابوي او 3 ښيي. څلورمه 17 % 5 حسابوي او 2 ښيي. د کتنې لپاره: 5 * 3 + 2 هماغه لومړني 17 کتابونه کېږي. پنځمه کرښه لومړی د قوسونو دننه حساب کوي؛ 2 + 3 کېږي 5، بیا 5 * 4 کېږي 20. پایله درې کرښې لري: 3، بیا 2 او بیا 20.

که 20 کتابونه وای، د هر زده کوونکي برخه 4 او پاتې شونی 0 کېده. صفر پاتې شونی یعنې کتابونه پوره مساوي وېشل شوي دي.''',
'''د محاسبې له لیکلو مخکې یو کوچنی مثال په خپله حساب کړئ. که جمع له ضرب مخکې غواړئ، قوسونه وکاروئ. x د پایتون د ضرب نښه نه ده؛ * ولیکئ. هغه عدد چې وېش پرې کوئ صفر کېدای نه شي؛ پر صفر زده کوونکو د کتابونو وېشل دلته معتبره پایله نه لري.

که ځواب له اټکل سره توپیر لري، د عددونو له بدلولو مخکې د عملیاتو ترتیب وګورئ. بشپړه برخه او پاتې شونی جلا تشریح کړئ؛ هر یو بېلې پوښتنې ته ځواب ورکوي.''']},
'decisions': {
'en': ['''A program sometimes needs to choose an action. In this example, a score of 50 or more means Pass; a lower score means Keep practicing. A condition is a question with a True or False answer. score >= 50 asks whether the score is at least 50. The = sign assigns a value, whereas == asks whether two values are equal.

Write if, the condition, and a colon. Indent the instruction belonging to that branch by four spaces. else introduces the alternative when the condition is false. Indentation is part of Python grammar: it tells the program which instructions belong together.''',
'''Line 1 sets score to 72. Line 2 asks whether 72 is greater than or equal to 50. It is True, so line 3 displays Pass. The else branch is skipped, so Keep practicing is not displayed. Only one branch runs in this example.

Try the boundary mentally: 50 also passes because >= includes equality. 49 follows else. If you wrote > instead, a score of exactly 50 would no longer pass. This small symbol changes the rule.''',
'''For the coding exercise, the score is already 65. Write the condition that checks the pass rule, end the condition line with a colon, and indent the print instruction underneath it. Do not write = when comparing equality; = changes a stored value, while == compares.

If both messages appear, check whether a print has accidentally been placed outside the branches. If the app reports an indentation error, align the branch bodies consistently. Once your example works, reason through scores 49, 50, and 51 to test the edge of the rule.'''],
'fa': ['''گاهی پروگرام باید یک کار را انتخاب کند. در این مثال، نمرهٔ 50 یا بالاتر یعنی کامیابی و نمرهٔ پایین‌تر یعنی ضرورت به تمرین بیشتر. شرط پرسشی است که جواب آن True یعنی درست یا False یعنی نادرست می‌شود. score >= 50 می‌پرسد آیا نمره حداقل 50 است؟ علامت = مقدار می‌دهد؛ اما == می‌پرسد آیا دو مقدار برابر اند؟

کلمهٔ if، شرط و سپس دونقطه را بنویسید. دستور مربوط به آن حالت را در خط بعد، با چهار فاصله از آغاز خط بنویسید. else حالت دیگر را مشخص می‌کند که وقتی شرط نادرست باشد اجرا می‌شود. فاصلهٔ آغاز خط در پایتون تنها برای زیبایی نیست؛ مشخص می‌کند کدام دستورها مربوط به یک بخش اند.''',
'''خط اول score را 72 می‌سازد. خط دوم بررسی می‌کند آیا 72 بزرگ‌تر یا مساوی 50 است. جواب True است؛ پس خط سوم Pass را نمایش می‌دهد. بخش else اجرا نمی‌شود و Keep practicing دیده نمی‌شود. در این مثال فقط یکی از دو حالت اجرا می‌شود.

حالت مرزی را بررسی کنید: نمرهٔ 50 هم کامیاب است، چون >= برابری را شامل می‌شود. نمرهٔ 49 به else می‌رود. اگر به‌جای >= تنها > بنویسید، نمرهٔ دقیقاً 50 دیگر کامیاب نمی‌شود. همین علامت کوچک قاعده را تغییر می‌دهد.''',
'''در تمرین کودنویسی، نمره از قبل 65 است. شرط کامیابی را بنویسید، آخر خط شرط دونقطه بگذارید و دستور print را زیر آن با فاصلهٔ آغاز خط بنویسید. برای مقایسهٔ برابری = ننویسید؛ = مقدار را تغییر می‌دهد، اما == مقایسه می‌کند.

اگر هر دو پیام دیده شدند، ببینید آیا یک print اشتباهاً بیرون از بخش‌های شرط نوشته شده است. اگر خطای فاصله‌گذاری آمد، فاصلهٔ آغاز خط‌های مربوط به هر بخش را یکسان کنید. پس از درست شدن مثال، نمره‌های 49، 50 و 51 را قدم‌به‌قدم بررسی کنید.'''],
'ps': ['''کله ناکله پروګرام باید یو کار وټاکي. په دې مثال کې 50 یا تر هغې لوړه نمره بریا ده او ټیټه نمره د نور تمرین اړتیا ښيي. شرط هغه پوښتنه ده چې ځواب یې True یعنې رښتیا یا False یعنې ناسم وي. score >= 50 پوښتي چې نمره لږ تر لږه 50 ده که نه. = ارزښت ورکوي، خو == پوښتي چې دوه ارزښتونه برابر دي که نه.

if، شرط او ورپسې دوه ټکي ولیکئ. د هغه حالت لارښوونه په بله کرښه کې د پیل له ځایه څلور تشې دننه ولیکئ. else هغه بل حالت ټاکي چې د شرط د ناسمېدو پر مهال اجرا کېږي. د کرښې د پیل تشې په پایتون کې یوازې ښکلا نه ده؛ ښيي چې کومې لارښوونې د یوې برخې دي.''',
'''لومړۍ کرښه score ته 72 ورکوي. دویمه ګوري چې 72 له 50 لوی یا ورسره برابر دی که نه. ځواب True دی، نو درېیمه کرښه Pass ښيي. د else برخه نه اجرا کېږي او Keep practicing نه ښکاري. په دې مثال کې یوازې یو حالت اجرا کېږي.

د پولې ارزښت وګورئ: 50 هم بریالی دی، ځکه >= برابري هم رانغاړي. 49 د else برخې ته ځي. که یوازې > ولیکئ، پوره 50 نمره به بریالۍ نه وي. همدا کوچنۍ نښه قاعده بدلوي.''',
'''د کوډ په تمرین کې نمره له مخکې 65 ده. د بریا شرط ولیکئ، د شرط کرښه په دوو ټکو پای ته ورسوئ او لاندې print د پیل له ځایه دننه ولیکئ. د برابرۍ د پرتله کولو لپاره = مه لیکئ؛ = ارزښت بدلوي، خو == پرتله کوي.

که دواړه پیغامونه ښکاره شي، وګورئ چې کوم print مو په تېروتنه له شرطونو بهر نه دی لیکلی. که د تشو تېروتنه راغله، د هرې برخې د کرښو د پیل تشې برابرې کړئ. بیا 49، 50 او 51 نمرې ګام په ګام وڅېړئ.''']},
'loops': {
'en': ['''A loop repeats a group of instructions so that you do not have to copy the same line many times. for takes one value at a time from a sequence. range(1, 5) supplies 1, 2, 3, and 4: the starting value is included and the stopping value is excluded.

To keep a running sum, create total before the loop and start it at zero. Each repetition adds the current number to the previous total. The indented line is the repeated work. A line aligned with for is outside the loop and runs after all its repetitions finish.''',
'''Line 1 starts total at 0. On the first repetition, number is 1 and total becomes 1. On the second, number is 2 and total becomes 3. On the third, number is 3 and total becomes 6. On the fourth, number is 4 and total becomes 10. There is no repetition with number equal to 5.

The last print is outside the loop, so it displays only 10. If you moved it into the loop, it would display the intermediate totals 1, 3, 6, and 10 on separate lines. If you moved total = 0 into the loop, you would erase the previous total on every repetition.''',
'''The writing activity wants each number, not a sum. Use a range that supplies 1, 2, and 3 and put print inside the loop. Ask yourself both “what repeats?” and “how many times?”. Keep the colon at the end of the for line and indent the repeated instruction.

If the last required number is missing, inspect the excluded stopping value. A while loop is another kind of loop: it keeps running while its condition is true. Its controlling value must change so that it can stop; this app stops excessive execution rather than letting it run forever.'''],
'fa': ['''حلقه یک گروه از دستورها را تکرار می‌کند تا مجبور نباشید همان خط را چندین بار کاپی کنید. for در هر نوبت یک مقدار را از یک ترتیب می‌گیرد. range(1, 5) مقدارهای 1، 2، 3 و 4 را می‌دهد؛ مقدار آغاز شامل است و مقدار پایان شامل نیست.

برای نگه‌داشتن مجموع، total را پیش از حلقه بسازید و از صفر آغاز کنید. در هر نوبت، عدد فعلی به مجموع قبلی اضافه می‌شود. خطی که با فاصلهٔ آغاز خط زیر حلقه نوشته شده، کار تکراری است. خطی که هم‌ردیف for باشد بیرون از حلقه است و پس از پایان همهٔ نوبت‌ها اجرا می‌شود.''',
'''خط اول total را 0 می‌سازد. در نوبت اول number برابر 1 است و total به 1 می‌رسد. در نوبت دوم number برابر 2 است و total به 3 می‌رسد. در نوبت سوم number برابر 3 است و total به 6 می‌رسد. در نوبت چهارم number برابر 4 است و total به 10 می‌رسد. نوبتی با مقدار 5 وجود ندارد.

آخرین print بیرون از حلقه است؛ پس تنها 10 را نمایش می‌دهد. اگر آن را داخل حلقه ببرید، مجموع‌های میانی 1، 3، 6 و 10 در سطرهای جدا دیده می‌شوند. اگر total = 0 را داخل حلقه ببرید، در هر نوبت مجموع قبلی را پاک می‌کنید.''',
'''تمرین نوشتن نمایش هر عدد را می‌خواهد، نه مجموع را. از range استفاده کنید که 1، 2 و 3 بدهد و print را داخل حلقه بگذارید. دو پرسش را جواب بدهید: «چه کاری تکرار می‌شود؟» و «چند بار؟». دونقطهٔ آخر خط for و فاصلهٔ آغاز خط دستور تکراری را فراموش نکنید.

اگر آخرین عدد لازم دیده نشد، مقدار پایان range را بررسی کنید، چون شامل نمی‌شود. while نوع دیگر حلقه است که تا درست بودن شرط ادامه می‌یابد. مقدار کنترول‌کنندهٔ آن باید تغییر کند تا حلقه پایان یابد؛ این برنامه اجرای بیش از حد را متوقف می‌کند.'''],
'ps': ['''کړۍ د لارښوونو یوه ډله تکراروي، څو یوه کرښه بیا بیا کاپي نه کړئ. for په هر وار له یوه ترتیب څخه یو ارزښت اخلي. range(1, 5) د 1، 2، 3 او 4 ارزښتونه ورکوي؛ د پیل ارزښت پکې شامل دی، خو د پای ارزښت نه دی.

د مجموعې ساتلو لپاره total له کړۍ مخکې جوړ او په صفر یې پیل کړئ. په هر وار اوسنی عدد له پخوانۍ مجموعې سره جمع کېږي. هغه کرښه چې د کړۍ لاندې دننه لیکل شوې، تکرارېدونکی کار دی. د for سره برابره کرښه له کړۍ بهر ده او د ټولو وارونو له پای ته رسېدو وروسته اجرا کېږي.''',
'''لومړۍ کرښه total په 0 پیلوي. په لومړي وار number برابر له 1 سره دی او total کېږي 1. په دویم وار number برابر له 2 سره دی او total کېږي 3. په درېیم وار number برابر له 3 سره دی او total کېږي 6. په څلورم وار number برابر له 4 سره دی او total کېږي 10. د 5 ارزښت لپاره وار نشته.

وروستی print له کړۍ بهر دی، نو یوازې 10 ښيي. که دننه یې یوسئ، منځنۍ مجموعې 1، 3، 6 او 10 په جلا کرښو کې ښيي. که total = 0 دننه یوسئ، په هر وار پخوانۍ مجموعه له منځه وړئ.''',
'''د لیکلو تمرین د هر عدد ښودل غواړي، نه مجموعه. داسې range وکاروئ چې 1، 2 او 3 ورکړي او print د کړۍ دننه ولیکئ. دواړه پوښتنې ځواب کړئ: «څه تکرارېږي؟» او «څو ځله؟». د for د کرښې دوه ټکي او د تکرارېدونکې کرښې د پیل تشې مه هېروئ.

که وروستی اړین عدد نه ښکاري، د range د پای ارزښت وګورئ، ځکه هغه نه شاملېږي. while بله کړۍ ده چې تر هغه روانه وي چې شرط یې رښتیا وي. کنټرولوونکی ارزښت یې باید بدل شي څو پای ته ورسېږي؛ دا اپ ډېر اوږد اجرا کېدل دروي.''']},
'lists': {
'en': ['''When several values belong together, a list keeps them in a defined order under one name. Write square brackets around the values and separate them with commas. In the example, cities contains three text values. Each text value still needs its own quotes.

An index is the position used to retrieve an item. Python counts positions from zero: position 0 is Kabul, position 1 is Bamyan, and position 2 is Herat. len(cities) counts items and returns 3; it does not return the last valid position. In this app you can create lists, read items, count them, and loop over them. Changing an item by index or using list methods requires a fuller Python environment.''',
'''Line 1 creates the three-item list. Line 2 reads the item at position 0 and displays Kabul. Line 3 displays the item count, 3. The for loop then takes each city value in order. Its print runs three times, displaying Kabul, then Bamyan, then Herat.

Kabul appears twice in the whole output: once from the direct index lookup and once from the loop. cities[3] would be an error because there is no fourth item. An empty list has length zero and a for loop over it has no repetitions.''',
'''In the writing exercise, marks contains 10, 20, and 30. Keep total = 0 outside the loop. Add each mark to total inside the loop. Display total after the loop. The running total should change from 0 to 10, then 30, then 60.

Do not display only marks[0]: that gives the first mark, not the sum. Do not confuse an item value with its position. To check understanding, explain why marks[1] is 20 even though it is the second item.'''],
'fa': ['''وقتی چند مقدار مربوط به هم باشند، فهرست آن‌ها را با ترتیب مشخص زیر یک نام نگه می‌دارد. مقدارها را داخل قوس‌های مربع بنویسید و با کامه جدا کنید. در مثال، cities سه مقدار متنی دارد. هر متن هنوز به نقل قول جداگانه ضرورت دارد.

اندیس شمارهٔ جای یک عضو است که برای خواندن آن استفاده می‌شود. پایتون جایگاه‌ها را از صفر می‌شمارد: جای 0 مربوط Kabul، جای 1 مربوط Bamyan و جای 2 مربوط Herat است. len(cities) تعداد عضوها را می‌شمارد و 3 می‌دهد؛ این عدد آخرین اندیس معتبر نیست. در این برنامه می‌توانید فهرست بسازید، عضوها را بخوانید، بشمارید و با حلقه مرور کنید. تغییر عضو با اندیس یا استفاده از روش‌های فهرست به محیط کامل‌تر پایتون ضرورت دارد.''',
'''خط اول فهرست سه‌عضوی را می‌سازد. خط دوم عضو جای 0 را می‌خواند و Kabul را نشان می‌دهد. خط سوم تعداد عضوها، یعنی 3 را نشان می‌دهد. سپس حلقهٔ for هر شهر را به ترتیب می‌گیرد. دستور print داخل آن سه بار اجرا می‌شود: Kabul، سپس Bamyan و بعد Herat.

در تمام نتیجه Kabul دو بار دیده می‌شود: یک بار از خواندن مستقیم با اندیس و یک بار از حلقه. cities[3] خطا می‌دهد، چون عضو چهارمی وجود ندارد. فهرست خالی طول صفر دارد و حلقهٔ for روی آن هیچ نوبتی اجرا نمی‌کند.''',
'''در تمرین نوشتن، marks مقدارهای 10، 20 و 30 دارد. total = 0 را بیرون از حلقه نگه دارید. داخل حلقه هر نمره را به total اضافه کنید. پس از حلقه total را نمایش بدهید. مجموع باید از 0 به 10، سپس 30 و بعد 60 برسد.

تنها marks[0] را نمایش ندهید؛ این اولین نمره است، نه مجموع. مقدار عضو را با شمارهٔ جای آن اشتباه نگیرید. برای بررسی فهم خود توضیح بدهید چرا marks[1] برابر 20 است، با آن‌که عضو دوم فهرست است.'''],
'ps': ['''کله چې څو ارزښتونه سره تړاو لري، لېست یې په ټاکلي ترتیب تر یوه نوم لاندې ساتي. ارزښتونه په مربع قوسونو کې ولیکئ او په کامو یې جلا کړئ. په مثال کې cities درې متني ارزښتونه لري. هر متن بیا هم د نقل قول خپلو نښو ته اړتیا لري.

اندیس د غړي د ځای شمېره ده چې په وسیله یې غړی لولو. پایتون ځایونه له صفره شمېري: 0 د Kabul، 1 د Bamyan او 2 د Herat ځای دی. len(cities) غړي شمېري او 3 ورکوي؛ دا وروستی معتبر اندیس نه دی. په دې اپ کې لېست جوړول، غړي لوستل، شمېرل او په کړۍ کې تېرولای شئ. په اندیس د غړي بدلول او د لېست مېتودونه بشپړ پایتون چاپېریال ته اړتیا لري.''',
'''لومړۍ کرښه درې غړي لرونکی لېست جوړوي. دویمه د 0 ځای غړی لولي او Kabul ښيي. درېیمه د غړو شمېر، یعنې 3 ښيي. بیا for هر ښار په ترتیب اخلي. دننه print درې ځله اجرا کېږي: Kabul، بیا Bamyan او بیا Herat.

په ټوله پایله کې Kabul دوه ځله ښکاري: یو ځل د اندیس له مستقیم لوستلو او بل ځل له کړۍ څخه. cities[3] تېروتنه ده، ځکه څلورم غړی نشته. تش لېست صفر اوږدوالی لري او for پرې هېڅ وار نه اجرا کېږي.''',
'''د لیکلو په تمرین کې marks د 10، 20 او 30 ارزښتونه لري. total = 0 له کړۍ بهر وساتئ. دننه هره نمره له total سره جمع کړئ. له کړۍ وروسته total ښکاره کړئ. مجموعه باید له 0 څخه 10، بیا 30 او بیا 60 ته ورسېږي.

یوازې marks[0] مه ښکاره کوئ؛ دا لومړۍ نمره ده، نه مجموعه. د غړي ارزښت د هغه له ځای سره مه ګډوئ. د خپلې پوهې د کتلو لپاره ووایئ چې ولې marks[1] برابر له 20 سره دی، که څه هم دا دویم غړی دی.''']},
'functions': {
'en': ['''Suppose you must square several numbers. Instead of copying the multiplication for every use, define a function: a named group of instructions that you can call again. def square(number): defines a function named square. number is a parameter, a local name for the value supplied in a call.

Defining the function does not run its body. Calling square(4) runs it with number equal to 4. return sends the calculated value back to the caller and ends that call. Returning a result is different from displaying it: print is used when you want the result on screen.''',
'''The first two lines define square; they display nothing. In print(square(4)), Python first calls square with 4. Inside that call, number * number becomes 4 * 4, or 16. return sends 16 back; the outer print displays it. The last line makes a fresh call with 7, calculates 49, and displays 49.

Each call uses its own parameter value. The 4 from the first call does not remain as the parameter in the second call. The blank line makes the code easier to read but performs no calculation.''',
'''For the writing activity, define add with two parameters, a and b. Inside it, return their sum. Outside the function, call add(4, 6) and display its returned value. The arguments 4 and 6 become the local values of a and b during that call.

Indent return beneath def, but keep the final print outside the function. Define the function before calling it. If you only define it, nothing is displayed. If you calculate a + b without returning it, you have not sent the result back to the caller. Explain this difference before moving to a project.'''],
'fa': ['''فرض کنید باید مربع چند عدد را حساب کنید. به‌جای کاپی کردن ضرب در هر جای کود، تابع می‌سازیم: گروهی از دستورها با یک نام که می‌توانیم دوباره از آن استفاده کنیم. def square(number): تابعی به نام square تعریف می‌کند. number پارامتر است؛ یعنی نام محلی برای مقداری که هنگام فراخوانی به تابع می‌دهیم.

تعریف تابع، دستورهای داخل آن را اجرا نمی‌کند. فراخوانی square(4) آن‌ها را با مقدار 4 برای number اجرا می‌کند. return نتیجه را به محل فراخوانی برمی‌گرداند و همان اجرای تابع را پایان می‌دهد. برگرداندن نتیجه با نمایش آن فرق دارد؛ برای دیدن نتیجه در صفحه از print استفاده می‌کنیم.''',
'''دو خط اول square را تعریف می‌کنند و چیزی نمایش نمی‌دهند. در print(square(4))، پایتون نخست square را با 4 فراخوانی می‌کند. داخل این اجرا، number * number می‌شود 4 * 4، یعنی 16. دستور return مقدار 16 را برمی‌گرداند و print بیرونی آن را نمایش می‌دهد. خط آخر یک فراخوانی تازه با 7 می‌سازد، 49 را حساب می‌کند و 49 را نمایش می‌دهد.

هر فراخوانی مقدار پارامتر خودش را دارد. مقدار 4 از اجرای اول به‌عنوان پارامتر اجرای دوم باقی نمی‌ماند. خط خالی خواندن کود را آسان می‌کند، اما هیچ محاسبه‌ای انجام نمی‌دهد.''',
'''در تمرین نوشتن، add را با دو پارامتر a و b تعریف کنید. داخل تابع مجموع آن‌ها را با return برگردانید. بیرون تابع add(4, 6) را فراخوانی کنید و مقدار برگشتی را نمایش بدهید. هنگام همین فراخوانی، عددهای 4 و 6 مقدارهای محلی a و b می‌شوند.

خط return را با فاصلهٔ آغاز خط زیر def بنویسید، اما print آخر را بیرون تابع نگه دارید. تابع را پیش از فراخوانی تعریف کنید. اگر تنها تعریف کنید، چیزی نمایش داده نمی‌شود. اگر a + b را حساب کنید ولی return نکنید، نتیجه را به محل فراخوانی نفرستاده‌اید. پیش از رفتن به پروژه این تفاوت را توضیح بدهید.'''],
'ps': ['''فرض کړئ د څو عددونو مربع حسابوئ. د هر ځل ضرب د کاپي کولو پر ځای تابع جوړوو: د لارښوونو یوه نوم لرونکې ډله چې بیا یې کارولای شو. def square(number): د square په نوم تابع تعریفوي. number پارامتر دی؛ یعنې د هغه ارزښت محلي نوم چې د تابع د رابللو پر مهال یې ورکوو.

د تابع تعریف دننه لارښوونې نه اجرا کوي. square(4) یې له 4 سره اجرا کوي چې د number ارزښت ګرځي. return پایله د رابللو ځای ته بېرته ورکوي او هماغه اجرا پای ته رسوي. د پایلې بېرته ورکول او ښودل توپیر لري؛ په پرده د ښودلو لپاره print کاروو.''',
'''لومړۍ دوه کرښې square تعریفوي او هېڅ نه ښيي. په print(square(4)) کې پایتون لومړی square له 4 سره رابولي. دننه number * number کېږي 4 * 4، یعنې 16. return د 16 ارزښت بېرته ورکوي او بهرنی print یې ښيي. وروستۍ کرښه له 7 سره نوې اجرا پیلوي، 49 حسابوي او 49 ښيي.

هر ځل رابلل د پارامتر خپل ارزښت لري. د لومړي ځل 4 د دویم ځل د پارامتر په توګه نه پاتې کېږي. تشه کرښه د کوډ لوستل اسانه کوي، خو حساب نه کوي.''',
'''د لیکلو په تمرین کې add له دوو پارامترونو a او b سره تعریف کړئ. دننه یې مجموعه په return بېرته ورکړئ. له تابع بهر add(4, 6) راوبولئ او بېرته ورکړل شوی ارزښت ښکاره کړئ. په همدې اجرا کې 4 او 6 د a او b محلي ارزښتونه کېږي.

return د def لاندې دننه ولیکئ، خو وروستی print له تابع بهر وساتئ. تابع له رابللو مخکې تعریف کړئ. که یوازې یې تعریف کړئ، هېڅ نه ښکاري. که a + b حساب کړئ خو return یې نه کړئ، پایله مو د رابللو ځای ته نه ده ورکړې. پروژې ته له تلو مخکې دا توپیر تشریح کړئ.''']}
}

OUTPUTS = {'hello':'Hello, Afghanistan!\nI can learn to code.', 'variables':'Herat\n25', 'numbers':'3\n2\n20', 'decisions':'Pass', 'loops':'10', 'lists':'Kabul\n3\nKabul\nBamyan\nHerat', 'functions':'16\n49'}

def build():
    root = Path(__file__).resolve().parents[1]
    for guide in GUIDES.values():
        assert set(guide) == {'en','fa','ps'}
        assert all(len(parts) == 3 and all(len(p)>300 for p in parts) for parts in guide.values())
    payload = json.dumps(GUIDES, ensure_ascii=False)
    outputs = json.dumps(OUTPUTS)
    (root/'lib/data/detailed_foundations.dart').write_text(
        "// Generated by tool/detailed_foundations.py.\nimport 'dart:convert';\n\n"
        + "final Map<String, dynamic> detailedFoundations = jsonDecode(r'''"+payload+"''') as Map<String, dynamic>;\n"
        + "final Map<String, dynamic> foundationOutputs = jsonDecode(r'''"+outputs+"''') as Map<String, dynamic>;\n", encoding='utf-8')

if __name__ == '__main__':
    build()
