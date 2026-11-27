import re, html, os
HERE = os.path.dirname(os.path.abspath(__file__))
XKB = os.environ.get('XKB_TR', '/usr/share/X11/xkb/symbols/tr')
src = open(XKB).read()
blk = re.search(r'xkb_symbols "f" \{(.*?)\n\};', src, re.S).group(1)

NAMES = {
 'plus':'+','asterisk':'*','notsign':'¬','plusminus':'±','exclam':'!','onesuperior':'¹',
 'exclamdown':'¡','quotedbl':'"','twosuperior':'²','asciicircum':'^','numbersign':'#',
 'threesuperior':'³','dollar':'$','onequarter':'¼','ampersand':'&','threequarters':'¾',
 'apostrophe':"'",'braceleft':'{','parenleft':'(','bracketleft':'[','parenright':')',
 'bracketright':']','braceright':'}','equal':'=','degree':'°','slash':'/','question':'?',
 'backslash':'\\','questiondown':'¿','minus':'-','underscore':'_','bar':'|','gbreve':'ğ',
 'Gbreve':'Ğ','idotless':'ı','paragraph':'¶','ocircumflex':'ô','Ocircumflex':'Ô','yen':'¥',
 'registered':'®','sterling':'£','dead_diaeresis':'¨','dead_abovering':'˚','asciitilde':'~',
 'dead_breve':'˘','ucircumflex':'û','Ucircumflex':'Û','Iabovedot':'İ','icircumflex':'î',
 'Icircumflex':'Î','EuroSign':'€','acircumflex':'â','Acircumflex':'Â','udiaeresis':'ü',
 'Udiaeresis':'Ü','U20BA':'₺','mu':'µ','acute':'´','dead_acute':'´','scedilla':'ş',
 'Scedilla':'Ş','dead_caron':'ˇ','grave':'`','dead_grave':'`','less':'<','greater':'>',
 'guillemotleft':'«','guillemotright':'»','leftdoublequotemark':'“','rightdoublequotemark':'”',
 'cent':'¢','copyright':'©','ccedilla':'ç','Ccedilla':'Ç','section':'§','multiply':'×',
 'nobreakspace':'⍽','period':'.','colon':':','division':'÷','dead_abovedot':'˙','comma':',',
 'semicolon':';','periodcentered':'·','odiaeresis':'ö','Odiaeresis':'Ö','brokenbar':'¦','at':'@',
 'none':'',
}
def sym(s):
    s = s.strip()
    if len(s) == 1: return s
    if s in NAMES: return NAMES[s]
    raise SystemExit('unknown keysym: ' + s)

keys = {}
for m in re.finditer(r'key <(\w+)>\s*\{(?:\s*type\[group1\]\s*=\s*"[^"]*",)?\s*\[([^\]]+)\]', blk, re.S):
    keys[m.group(1)] = [sym(x) for x in m.group(2).split(',')]  # [base, shift, altgr, altgr+shift]

rows = [
  ['TLDE','AE01','AE02','AE03','AE04','AE05','AE06','AE07','AE08','AE09','AE10','AE11','AE12'],
  ['AD01','AD02','AD03','AD04','AD05','AD06','AD07','AD08','AD09','AD10','AD11','AD12'],
  ['AC01','AC02','AC03','AC04','AC05','AC06','AC07','AC08','AC09','AC10','AC11','BKSL'],
  ['LSGT','AB01','AB02','AB03','AB04','AB05','AB06','AB07','AB08','AB09','AB10'],
]
P = 11.5   # pitch mm (sheet spacing)
S = 10.0   # sticker size mm (stickable keycap area)
keys.setdefault('AE05', ['5', '%', '½', '⅜'])  # not in tr(f) block; from xkb 'latin' default section
X0 = (210 - 13*P) / 2
Y0 = 30
out = []
for r, row in enumerate(rows):
    for i, k in enumerate(row):
        lv = (keys.get(k, []) + ['','','',''])[:4]
        base, sh, ag, agsh = lv
        x = X0 + i*P; y = Y0 + r*P
        out.append(f'''<div class="k" style="left:{x:.2f}mm;top:{y:.2f}mm">
  <span class="sh">{html.escape(sh)}</span><span class="ag2">{html.escape(agsh)}</span>
  <span class="base">{html.escape(base)}</span>
  <span class="ag">{html.escape(ag)}</span></div>''')

doc = f'''<!doctype html><html><head><meta charset="utf-8"><title>Turkish F keycap stickers</title>
<style>
@page {{ size: A4; margin: 0; }}
html,body {{ margin:0; padding:0; background:#fff; }}
.sheet {{ position:relative; width:210mm; height:297mm; }}
.k {{ position:absolute; width:{S}mm; height:{S}mm; box-sizing:border-box;
     border-radius:1.5mm; outline:0.12mm dashed #9a9a9a; background:#fff;
     font-family:"DejaVu Sans","Liberation Sans",Arial,sans-serif; color:#000; }}
.k span {{ position:absolute; line-height:1; white-space:nowrap; }}
.base {{ left:0; right:0; bottom:0.6mm; text-align:center; font-size:5.0mm; }}
.sh   {{ left:0.9mm; top:0.8mm; font-size:2.6mm; }}
.ag2  {{ right:0.9mm; top:0.8mm; font-size:2.6mm; }}
.ag   {{ right:0.9mm; bottom:0.8mm; font-size:2.6mm; }}
.title {{ position:absolute; left:0; right:0; top:12mm; text-align:center; font:9pt sans-serif; color:#555; }}
</style></head><body>
<div class="sheet">
<div class="title">Turkish F keycap stickers &middot; cut along the dashed lines &middot; print at 100% (actual size)</div>
{chr(10).join(out)}
</div></body></html>'''
open(os.path.join(HERE, 'turkish-f-stickers.html'), 'w').write(doc)
print(len(out), 'keys written')
for k in ['TLDE','AE02','AD04','AC02','AB09','BKSL','LSGT']: print(k, keys.get(k))
