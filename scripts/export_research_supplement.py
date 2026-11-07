"""Original researched supplement, questions and frameworks; no source full-text republication."""
import html,json,pathlib
from docx import Document
from docx.shared import Pt,Inches,RGBColor
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
R=pathlib.Path(__file__).resolve().parents[1]
load=lambda p:json.loads((R/'data'/p).read_text())
notes=[n for n in load('notes.json')if n['id'].startswith('E19-')];sources=load('sources.json');access=load('source-access.json');questions=load('research-practice.json')
assert len(notes)==14 and len(questions)==14
frames=(R/'volumes/Edition-19-Mains-Frameworks.md').read_text()
limit='Four AP primary-document backfills dated March–May 2026 and ten selected 1–7 November developments. Not a complete daily or monthly audit. Source bodies, proposed rules, unread instruments and reported implementation claims are explicitly distinguished. Research cut-off: 7 November 2026.'
lines=['# CIVILS ATLAS · EDITION 19','# Deep research supplement',limit,'','14 original researched notes · 14 original MCQs · 4 Mains frameworks','']
for n in notes:
 lines += ['## '+n['title'],n['id']+' · '+n['date']+' · '+n['priority']+' · '+n['subject']+' · '+n['block'],'','**Why in the news:** '+n['why'],'']
 lines += ['- '+f for f in n['facts']]
 lines += ['','**Static connection:** '+n['static_link'],'','**Original analysis:**']+['- '+a for a in n['analysis']]
 lines += ['','**Prelims caution:** '+n['trap'],'','**Mains prompt:** '+n['mains'],'','Sources: '+', '.join(n['sources']),'']
lines+=['# Original practice · attempt before reading answers','']
for q in questions:lines+=['## '+q['id']+' · '+q['question']]+[chr(65+i)+'. '+o for i,o in enumerate(q['options'])]+['']
lines+=['# Explained answer key','']
for q in questions:lines += ['**'+q['id']+'. '+chr(65+q['answer'])+'** — '+q['explanation']+' ['+q['ref']+']','']
lines+=['',frames,'','# Source register and reading limits','']
for k in sources:
 if k.startswith('E19-'):lines += ['## ['+k+'] '+sources[k][0],sources[k][1],access[k]['access'],'']
md='\n'.join(lines);base=R/'volumes/Edition-19-Research-Supplement';base.with_suffix('.md').write_text(md+'\n')
# Word uses actual semantic headings and a restrained layout.
doc=Document();sec=doc.sections[0];sec.top_margin=sec.bottom_margin=Inches(.7);sec.left_margin=sec.right_margin=Inches(.75)
for name,size in [('Normal',10),('Title',30),('Heading 1',20),('Heading 2',14)]:
 st=doc.styles[name];st.font.name='Calibri';st.font.size=Pt(size);st.font.color.rgb=RGBColor.from_string('193F37')
sec.header.paragraphs[0].text='CIVILS ATLAS / EDITION 19 / UPSC × ANDHRA PRADESH APPSC'
for line in md.splitlines():
 if not line.strip():continue
 if line.startswith('# '):doc.add_heading(line[2:],0)
 elif line.startswith('## '):doc.add_heading(line[3:],1)
 elif line.startswith('- '):doc.add_paragraph(line[2:],'List Bullet')
 else:doc.add_paragraph(line.replace('**',''))
doc.save(base.with_suffix('.docx'))
fonts=pathlib.Path('/usr/share/fonts/truetype/dejavu')
for name,file in [('Atlas','DejaVuSans.ttf'),('AtlasBold','DejaVuSans-Bold.ttf'),('AtlasSerif','DejaVuSerif.ttf')]:pdfmetrics.registerFont(TTFont(name,str(fonts/file)))
pdfmetrics.registerFontFamily('Atlas',normal='Atlas',bold='AtlasBold',italic='Atlas',boldItalic='AtlasBold')
styles={name:ParagraphStyle(name,fontName=font,fontSize=size,leading=leading,textColor=colors.HexColor('#193F37'),spaceAfter=7,keepWithNext=name in ('h1','h2'),splitLongWords=True)for name,font,size,leading in [('cover','AtlasSerif',34,41),('h1','AtlasSerif',22,28),('h2','AtlasBold',12,17),('body','Atlas',9.3,14),('small','Atlas',7.3,10.5)]}
styles['body'].spaceAfter=5
story=[]
def p(s,style='body'):story.append(Paragraph(html.escape(s).replace('\n','<br/>'),styles[style]))
def label(k,s):story.append(Paragraph('<b>'+html.escape(k)+'</b> '+html.escape(s),styles['body']))
p('CIVILS ATLAS / RESEARCH EDITION 19','small');story.append(Spacer(1,45));p('Deep research.\nClear distinctions.','cover');p('UPSC × Andhra Pradesh APPSC','h1');p('14 researched notes · 14 original MCQs · 4 Mains frameworks');p(limit);p('Source-backed facts → static connections → original analysis → exam caution → Mains application.');p('Daily website: automatic discovery and permitted primary-document extraction are distinct from this in-session editorial research. No unseen researcher continues after the response.','small');story.append(PageBreak())
p('Study route','h1')
for n in notes:p(n['id']+' · '+n['date']+' · '+n['title'],'small')
p('Read P1 first. Preserve legal and implementation stages. Attempt the original questions before the explained key. Sources and reading limits follow the frameworks.')
for n in notes:
 story.append(PageBreak());p(n['subject']+' / '+n['block'],'small');p(n['title'],'h1');p(n['id']+' · '+n['date']+' · '+n['priority']+(' · AP-linked'if n['ap']else' · National / other'),'small');label('WHY IN THE NEWS',n['why'])
 for f in n['facts']:p('• '+f)
 label('STATIC CONNECTION',n['static_link']);p('ORIGINAL ANALYSIS','small')
 for a in n['analysis']:p('• '+a)
 label('PRELIMS CAUTION',n['trap']);label('MAINS PROMPT',n['mains']);p('Sources: '+', '.join(n['sources'])+' · See reading limits in source register.','small')
story.append(PageBreak());p('Original practice','h1');p('Attempt first; explained answers follow. These are not previous-year questions.')
for q in questions:
 block=[Paragraph(html.escape(q['id']+'. '+q['question']),styles['h2'])]+[Paragraph(html.escape(chr(65+i)+'. '+o),styles['body'])for i,o in enumerate(q['options'])]+[Spacer(1,8)]
 story.append(KeepTogether(block))
story.append(PageBreak());p('Explained answer key','h1')
for q in questions:label(q['id']+'. '+chr(65+q['answer']),q['explanation']+' ['+q['ref']+']')
story.append(PageBreak());p('Mains frameworks','h1')
for line in frames.splitlines():
 if line.startswith('# '):continue
 if line.startswith('## '):p(line[3:],'h2')
 elif line.strip():p(line.replace('**',''))
story.append(PageBreak());p('Sources & actual reading depth','h1')
for k in sources:
 if k.startswith('E19-'):
  p('['+k+'] '+sources[k][0],'h2');u=sources[k][1];story.append(Paragraph('<link href="'+html.escape(u,quote=True)+'" color="#21645c">'+html.escape(u)+'</link>',styles['small']));p(access[k]['access'],'small')
def furniture(c,d):
 c.setFillColor(colors.HexColor('#53685D'));c.setFont('Atlas',7);c.drawString(44,816,'CIVILS ATLAS / EDITION 19 / SELECTED RESEARCH THROUGH 7 NOVEMBER 2026');c.drawString(44,25,'SOURCE ACCESS ≠ COMPLETE COVERAGE · ORIGINAL ANALYSIS LABELLED');c.drawRightString(551,25,str(d.page))
SimpleDocTemplate(str(base.with_suffix('.pdf')),pagesize=(595.28,841.89),topMargin=46,bottomMargin=43,leftMargin=44,rightMargin=44,title='Civils Atlas · Edition 19 research supplement',author='Civils Atlas').build(story,onFirstPage=furniture,onLaterPages=furniture)
print('Built supplement PDF, Word and Markdown:',len(notes),'notes;',len(questions),'questions; 4 frameworks')
