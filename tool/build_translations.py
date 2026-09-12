"""Build local translation dictionaries and a completeness report; no network."""
import json
import re
from pathlib import Path
from translation_content import MODULES, PROJECTS, TOOLS, BEGINNERS
from translation_ui import UI
from project_translations import STEPS
ROOT=Path(__file__).resolve().parents[1]
catalog=json.loads((ROOT/'assets/curriculum/catalog.json').read_text(encoding='utf-8'))
translations={'fa':{},'ps':{}}
def put(en, fa, ps):
    translations['fa'][en]=fa; translations['ps'][en]=ps
for row in UI: put(*row)
levels={'fa':['به‌یادآوردن','فهمیدن','به‌کاربردن','تحلیل','ارزیابی','آفرینش'], 'ps':['یادول','پوهېدل','کارول','شننه','ارزونه','پنځول']}
for lang in translations:
    for en,local in zip(['remember','understand','apply','analyze','evaluate','create'],levels[lang]): translations[lang][en]=local; translations[lang][en.upper()]=local
for c in catalog:
    for lang in translations:
        out=translations[lang]
        assert len(MODULES[c['id']][lang])==6
        assert len(PROJECTS[c['id']][lang])==3
        for m,row in zip(c['modules'],MODULES[c['id']][lang]):
            title,explanation,challenge=row
            out[m['title']]=title; out[m['explanation']]=explanation
            for index,p in enumerate(m['plans']):
                out[p['title']]=title+(': بررسی راهنمایی‌شده' if lang=='fa' and index==0 else ': تمرین مستقل' if lang=='fa' else ': لارښود څېړنه' if index==0 else ': خپلواک تمرین')
                if lang=='fa':
                    objectives={'remember':f'اصطلاح و نوشتار مهم «{title}» را بدون دیدن نمونه بشناسید.', 'understand':f'با دنبال‌کردن نمونه توضیح دهید «{title}» چگونه رفتار برنامه را تغییر می‌دهد.', 'apply':challenge, 'analyze':f'فرض نادرست در «{title}» را پیدا و با کوچک‌ترین نمونه جدا کنید.', 'evaluate':f'دو روش «{title}» را با معیار درستی، نگه‌داری و کار آفلاین بسنجید.', 'create':f'با «{title}» گسترش تازه طراحی و با آزمون پذیرش روشن تحویل دهید.'}
                    activity=(f'توضیح را بخوانید. نمونه را روی کاغذ دنبال و هر تغییر حالت را ثبت کنید؛ سپس با ابزار دوره اجرا کنید. {challenge} نتیجهٔ واقعی را با پیش‌بینی مقایسه کنید.' if index==0 else f'{challenge} یک نیاز را تغییر دهید، راه‌حل خود را بسازید و عمدا یک شکست مرزی ایجاد کنید. بدون کپی نمونه، علت را پیدا و اصلاح کنید.')
                else:
                    objectives={'remember':f'د «{title}» مهم اصطلاحات او لیکدود له نمونې کتلو پرته وپېژنئ.', 'understand':f'د نمونې په تعقیب ووایئ چې «{title}» د پروګرام چلند څنګه بدلوي.', 'apply':challenge, 'analyze':f'په «{title}» کې ناسمه انګېرنه ومومئ او په تر ټولو کوچنۍ نمونه یې جلا کړئ.', 'evaluate':f'د «{title}» دوه لارې د سموالي، ساتنې او آفلاین کار له مخې وسنجوئ.', 'create':f'په «{title}» نوی غځول طرحه او له څرګندو منلو ازموینو سره وسپارئ.'}
                    activity=(f'تشریح ولولئ. نمونه پر کاغذ تعقیب، هر حالت بدلون ثبت او بیا یې د کورس په وسایلو وچلوئ. {challenge} واقعي پایله له وړاندوینې پرتله کړئ.' if index==0 else f'{challenge} یوه اړتیا بدله، خپل حل جوړ او قصداً سرحدي ناکامي رامنځته کړئ. د نمونې له کاپي کولو پرته علت پیدا او اصلاح کړئ.')
                out[p['objective']]=objectives[p['level']]; out[p['activity']]=activity
        for p,row in zip(c['projects'],PROJECTS[c['id']][lang]):
            assert len(row)==5
            out[p['title']]=row[0];out[p['brief']]=row[1]
            for en,target in zip(p['requirements'],row[2:]):out[en]=target
        g=c['beginner']; originals=[*g['terms'],g['before'],*g['trace'],g['question'],g['task'],g['hint'],g['result']]
        assert len(originals)==len(BEGINNERS[c['id']][lang]),(c['id'],lang,len(BEGINNERS[c['id']][lang]))
        for en,target in zip(originals,BEGINNERS[c['id']][lang]):out[en]=target
        if c['id'] in TOOLS:out[c['tools']]=TOOLS[c['id']][lang]

# Content inventory deliberately excludes code, IDs, file paths and durations.
required=set()
project_guides=json.loads((ROOT/'assets/curriculum/project_guides.json').read_text(encoding='utf-8'))
for id,guide in project_guides.items():
    required.update(guide['steps'])
    for lang in translations:
        assert len(guide['steps']) == len(STEPS[id][lang])
        translations[lang].update(zip(guide['steps'],STEPS[id][lang]))

for c in catalog:
    required.update([c['title'],c['tools']])
    for m in c['modules']:
        required.update([m['title'],m['explanation']])
        for p in m['plans']:required.update(p[k] for k in ['title','objective','activity','evidence'])
    for p in c['projects']:required.update([p['title'],p['brief'],*p['requirements'],*p['milestones']])
    g=c['beginner'];required.update([*g['terms'],g['before'],*g['trace'],g['question'],*g['options'],g['task'],g['hint'],g['result']])
report={lang:sorted(required-set(values)) for lang,values in translations.items()}
foundation=json.loads((ROOT/'assets/curriculum/python_foundations.json').read_text(encoding='utf-8'))
for lesson in foundation:
    required.update(lesson[k] for k in ['title','summary','concept','takeaway'])
    for exercise in lesson['exercises']:
        required.update(exercise[k] for k in ['prompt','explanation','hint'] if exercise[k])
        required.update(exercise['options'])
        for option in exercise['options']:
            if re.fullmatch(r'[\d, ]+|score (?:=|==|\+) 50',option):put(option,option,option)
ui_inventory=json.loads((ROOT/'assets/curriculum/ui_inventory.json').read_text(encoding='utf-8'))
required.update(ui_inventory)
required.update(['Your saved data could not be opened. No data has been erased. Check available storage and try again.','Try again','Backup is not valid UTF-8.'])
report={lang:sorted(required-set(values)) for lang,values in translations.items()}
(ROOT/'work').mkdir(exist_ok=True)
(ROOT/'work/translation_missing.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
# Case aliases serve section headings; exact case remains authoritative.
for values in translations.values():
    for key,value in list(values.items()):values.setdefault(key.lower(),value)
payload=json.dumps(translations,ensure_ascii=False,separators=(',',':'))
(ROOT/'lib/data/translation_catalog.dart').write_text("// Generated by tool/build_translations.py. Native-speaker review pending.\nimport 'dart:convert';\nfinal Map<String,Map<String,String>> translations = (jsonDecode(r'''"+payload+"''') as Map<String,dynamic>).map((key,value)=>MapEntry(key,(value as Map<String,dynamic>).cast<String,String>()));\n",encoding='utf-8')
(ROOT/'assets/curriculum/translation_inventory.json').write_text(json.dumps(sorted(required),ensure_ascii=False,indent=2),encoding='utf-8')
print({lang:len(missing) for lang,missing in report.items()}, 'missing curriculum keys')

if any(report.values()): raise SystemExit("Missing translations; see work/translation_missing.json")
