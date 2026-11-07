"""Build offline study app and consistent Markdown, DOCX and PDF volumes."""
import json,pathlib,collections,html,re
from docx import Document
from docx.shared import Inches,Pt,RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
R=pathlib.Path(__file__).resolve().parents[1]
def load(name,default):
 p=R/'data'/name;return json.loads(p.read_text()) if p.exists() else default
notes=load('notes.json',[]);sources=load('sources.json',{});inbox=load('inbox.json',[]);logs=load('update-log.json',[]);quiz=load('january-mcqs.json',[]);access=load('source-access.json',{})
import datetime
QS={}
for f in sorted((R/'data').glob('*-mcqs.json')):
 stem=f.stem.replace('-mcqs','')
 if re.fullmatch(r'\d{4}-\d{2}',stem):
  datetime.datetime.strptime(stem,'%Y-%m');month_key=stem
 else:
  try: m=datetime.datetime.strptime(stem,'%B').month
  except ValueError: continue
  month_key=f'2025-{m:02}'
 assert month_key not in QS,('Duplicate monthly practice',month_key)
 QS[month_key]=json.loads(f.read_text())
expanded=sorted(QS)
AUTO=load('automation-status.json',{})
AUTO_TEXT=('A scheduled discovery run has been observed; inspect current source health.' if AUTO.get('scheduler_active') else ('Hosted '+str(AUTO.get('last_event'))+' run observed; first scheduled execution remains unverified.' if AUTO.get('last_run_environment')=='github-actions' else 'Local build: inspect hosted deployment and first scheduled execution separately.'))+' Automation collects unreviewed source links, not researched study notes.'
D=dict(notes=notes,sources=sources,inbox=inbox,logs=logs,quiz=[dict(q,month=m) for m,qs in QS.items() for q in qs],source_access=access,expanded=expanded,linkages=load('linkages.json',[]),automation=AUTO,registry=load('source-registry.json',[]),source_coverage=load('source-coverage.json',{}),research_updates=load('research-updates.json',[]),research_practice=load('research-practice.json',[]),document_intake=load('document-intake.json',{}))
MONTH='January 2025'
(R/'index.html').write_text((R/'template.html').read_text().replace('__DATA__',json.dumps(D,ensure_ascii=False).replace('</','<\\/')))
ORDER=['Polity & Governance','Economy','Agriculture','Society & Welfare','Environment','Science & Technology','Security','International Relations','Andhra Pradesh','Culture & History','Awards & Sports']
def key(n):return (ORDER.index(n['subject']) if n['subject'] in ORDER else 99,n['block'],n['date'],n['priority'])
def date_label(n):
 if n.get('magazine_edition'):return 'Magazine coverage: '+n['magazine_edition']+' · web posted: '+n['magazine_posted']+' · event date varies'
 return n['date'][:7]+' (month-level index)' if n.get('date_precision')=='month' else n['date']+(' (reporting date)' if n.get('date_precision')=='reporting-day' else '')
LIMIT='Not exhaustive. Expanded monthly volumes are selected research batches; the rest of the requested archive remains incomplete. No month has passed a complete daily source audit. Full-text and source-extract evidence are distinguished. Historical notes do not certify current law, implementation or latest statistics.'
METHOD='New notes separate reported facts from original static connections, analysis, cautions and Mains prompts. P1 = core; P2 = consolidation; P3 = selective factual recall. Broad AP relevance is not exact APPSC paper mapping. Read the research audit for omissions and unresolved claims.'
FRAME=''
def md_text(ns,jan):
 lines=['# CIVILS ATLAS', '## '+(MONTH+' · Expanded research volume' if jan else 'Full working archive · Incomplete'),'',f'UPSC × Andhra Pradesh APPSC · English · Research cut-off: 7 November 2026 · {len(ns)} notes','', '**Coverage warning:** '+LIMIT,'',METHOD,'',AUTO_TEXT,'', '## Subject guide','']
 for s in ORDER:
  c=sum(n['subject']==s for n in ns)
  if c:lines.append(f'- {s}: {c} notes')
 lastsubject=lastblock=None
 for n in sorted(ns,key=key):
  if n['subject']!=lastsubject:lines+=['','## '+n['subject']];lastsubject=n['subject'];lastblock=None
  if n['block']!=lastblock:lines+=['','### '+n['block']];lastblock=n['block']
  lines+=['','#### '+n['title'],f"{n['id']} · {n['priority']} · {date_label(n)} · {'AP-linked' if n['ap'] else 'National / other'}",'']
  if n.get('why'):lines+=['**Why in the news:** '+n['why'],'']
  lines+=['**Source-backed essentials**']+['- '+f for f in n['facts']]+['']
  if n.get('static_link'):lines+=['**Static connection · original guidance:** '+n['static_link'],'']
  if n.get('analysis'):lines+=['**Analysis · original guidance**']+['- '+a for a in n['analysis']]+['']
  if n.get('related_notes'):lines+=['**Read across months · note IDs:** '+', '.join(n['related_notes'][:8])+(' · Full sequences: Cross-Month Reading Journeys.' if len(n['related_notes'])>8 else ''),'']
  lines+=['**Prelims caution:** '+n['trap'],'','**Mains prompt:** '+n['mains'],'','**Evidence access:** '+n.get('evidence_access','Not recorded'),'','**Sources:** '+', '.join('['+k+']' for k in n['sources']), '**Status:** '+n['status']+' · researched '+n['checked']]
 if jan:
  lines+=['','## Original practice · '+str(len(quiz))+' MCQs','Attempt first; the answer key follows all questions. These are not previous-year questions.','']
  for q in quiz:lines+=['### '+str(q['id'])+'. '+q['question']]+[f'{chr(65+i)}. {o}' for i,o in enumerate(q['options'])]+['']
  lines+=['## Answer key and explanations','']
  for q in quiz:lines+=[f"**{q['id']}. {chr(65+q['answer'])}** — {q['explanation']} Study reference: {q['ref']}.",'']
  lines+=['',FRAME]
 lines+=['','## Source register and access provenance','Source references are not a count of fully read documents. Some legal/primary references were located via PRS; many others were inspected as search-result extracts.','']
 used=set(k for n in ns for k in n['sources'])
 for k in sources:
  if k in used:lines += [f"### [{k}] {sources[k][0]}",sources[k][1],access.get(k,{}).get('access','Access provenance not recorded'),'']
 lines+=['## Research close-out','See research/Research-Status.md, research/remaining-period-inventory.csv and the day/month coverage ledgers. Neither counts nor queued links prove completeness.']
 return '\n'.join(lines)+'\n'
def docx_make(ns,path,jan):
 doc=Document();sec=doc.sections[0];sec.page_width=Inches(8.27);sec.page_height=Inches(11.69);sec.top_margin=Inches(.72);sec.bottom_margin=Inches(.7);sec.left_margin=Inches(.78);sec.right_margin=Inches(.78)
 normal=doc.styles['Normal'];normal.font.name='Calibri';normal.font.size=Pt(10.5);normal.paragraph_format.space_after=Pt(6);normal.paragraph_format.line_spacing=1.12
 for hn,size in [('Title',35),('Heading 1',24),('Heading 2',16),('Heading 3',13)]:
  st=doc.styles[hn];st.font.name='Georgia';st.font.size=Pt(size);st.font.color.rgb=RGBColor.from_string('193F37')
 doc.styles['Caption'].font.size=Pt(8);doc.styles['Caption'].font.color.rgb=RGBColor.from_string('53685D')
 sec.header.paragraphs[0].text='CIVILS ATLAS  /  UPSC × ANDHRA PRADESH APPSC'
 sec.header.paragraphs[0].style=doc.styles['Caption']
 foot=sec.footer.paragraphs[0];foot.style=doc.styles['Caption'];foot.add_run('RESEARCH EDITION 19 · 7 NOV 2026 · Incomplete archive    /    ')
 field=OxmlElement('w:fldSimple');field.set(qn('w:instr'),'PAGE');foot._p.append(field)
 doc.add_paragraph('EVIDENCE-LED CURRENT AFFAIRS / EDITION 19','Subtitle');doc.add_heading(MONTH if jan else 'The working archive',0)
 doc.add_paragraph('Understand the news.\nRetain what matters.','Subtitle')
 doc.add_paragraph(f'{len(ns)} study notes · English · UPSC + Andhra Pradesh APPSC')
 doc.add_paragraph('Requested period: 1 January 2025–7 November 2026\n'+('This volume: '+MONTH+', with explicitly labelled later corroboration.' if jan else 'This volume: selected notes across the requested period; monthly selections and daily-source audits remain incomplete.'))
 doc.add_heading('Coverage and evidence contract',1);doc.add_paragraph(LIMIT);doc.add_paragraph(METHOD)
 doc.add_paragraph(AUTO_TEXT+' The inbox has '+str(len(inbox))+' unreviewed links; those are not additional study notes.')
 doc.add_heading('Study routine',2)
 for x in ['Read P1 first; use P2 for consolidation and P3 for factual recall.','Recall after 1, 7 and 30 days. Explain the caution without looking.','Write a 150-word answer with a dated fact, a mechanism, a limitation and a balanced conclusion.','Read source access caveats. Re-check current law, court orders, mission status and volatile statistics before the exam.']:doc.add_paragraph(x,'List Bullet')
 doc.add_heading('Contents · subject guide',1)
 for s in ORDER:
  c=sum(n['subject']==s for n in ns)
  if c:doc.add_paragraph(f'{s} — {c} notes')
 if jan:doc.add_paragraph(f'After notes: {len(quiz)} original MCQs · explained answer key · Mains frameworks · source register')
 lastsubject=lastblock=None
 for n in sorted(ns,key=key):
  if n['subject']!=lastsubject:doc.add_page_break();doc.add_heading(n['subject'],1);lastsubject=n['subject'];lastblock=None
  if n['block']!=lastblock:doc.add_heading(n['block'],2);lastblock=n['block']
  doc.add_heading(n['title'],3);doc.add_paragraph(f"{n['id']} | {n['priority']} | {date_label(n)} | {'AP-linked' if n['ap'] else 'National / other'}",'Caption')
  def labelled(label,text):
   p=doc.add_paragraph();p.add_run(label+' ').bold=True;p.add_run(text)
  if n.get('why'):labelled('WHY IN THE NEWS',n['why'])
  for f in n['facts']:doc.add_paragraph(f,'List Bullet')
  if n.get('static_link'):labelled('STATIC CONNECTION · ORIGINAL GUIDANCE',n['static_link'])
  if n.get('analysis'):
   doc.add_paragraph('ANALYSIS · ORIGINAL STUDY GUIDANCE','Caption')
   for a in n['analysis']:doc.add_paragraph(a,'List Bullet')
  if n.get('related_notes'):labelled('READ ACROSS MONTHS · NOTE IDS',', '.join(n['related_notes'][:8])+(' · Full sequences: Cross-Month Reading Journeys.' if len(n['related_notes'])>8 else ''))
  labelled('PRELIMS / CAUTION',n['trap']);labelled('MAINS PROMPT',n['mains'])
  doc.add_paragraph('Sources: '+', '.join('['+k+']' for k in n['sources'])+' · See source register for URLs.','Caption')
  doc.add_paragraph('Evidence access: '+n.get('evidence_access','Not recorded')+'\n'+n['status']+' · researched '+n['checked'],'Caption')
 if jan:
  doc.add_page_break();doc.add_heading(MONTH+' recall laboratory',1);doc.add_paragraph(f'{len(quiz)} original questions. Not previous-year UPSC/APPSC questions. Historical monthly snapshot only. Answers follow the complete question set.')
  for q in quiz:
   doc.add_heading(str(q['id'])+'. '+q['question'],3)
   for i,o in enumerate(q['options']):
    option=doc.add_paragraph(chr(65+i)+'. '+o)
    option.paragraph_format.keep_together=True
    option.paragraph_format.keep_with_next=(i<len(q['options'])-1)
  doc.add_page_break();doc.add_heading('Explained answer key',1)
  for q in quiz:doc.add_paragraph(f"{q['id']}. {chr(65+q['answer'])} — {q['explanation']} [{q['ref']}]")
  doc.add_page_break();doc.add_heading('Mains answer laboratory',1)
  for line in FRAME.splitlines():
   if line.startswith('## '):doc.add_heading(line[3:],2)
   elif line.startswith('# '):continue
   elif line.strip():doc.add_paragraph(line.replace('**',''))
 doc.add_page_break();doc.add_heading('Source register · access provenance',1);doc.add_paragraph('Source counts are not counts of fully read original documents. Full-text PRS synthesis does not imply independent full-text review of every primary reference.')
 used=set(k for n in ns for k in n['sources'])
 for k in sources:
  if k in used:
   doc.add_heading('['+k+'] '+sources[k][0],3);doc.add_paragraph(sources[k][1],'Caption');doc.add_paragraph(access.get(k,{}).get('access','Access provenance not retained'),'Caption')
 doc.add_heading('Unfinished research',1);doc.add_paragraph('Daily-source reconciliation is still open for every month. The remainder of the archive is unfinished. Read research/Research-Status.md and the accompanying CSV ledgers. No automatic background researcher will complete them after this edition.')
 doc.save(path)
def pdf_make(ns,path):
 from reportlab.pdfgen import canvas
 from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,ListFlowable,ListItem,KeepTogether
 from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
 from reportlab.lib import colors
 from reportlab.pdfbase import pdfmetrics
 from reportlab.pdfbase.ttfonts import TTFont
 from reportlab.lib.enums import TA_LEFT
 fonts=pathlib.Path('/usr/share/fonts/truetype/dejavu')
 for name,file in [('Atlas','DejaVuSans.ttf'),('AtlasBold','DejaVuSans-Bold.ttf'),('AtlasSerif','DejaVuSerif.ttf')]:pdfmetrics.registerFont(TTFont(name,str(fonts/file)))
 pdfmetrics.registerFontFamily('Atlas',normal='Atlas',bold='AtlasBold',italic='Atlas',boldItalic='AtlasBold')
 st={};ink=colors.HexColor('#193F37');muted=colors.HexColor('#53685D')
 for name,font,size,leading in [('cover','AtlasSerif',37,44),('h1','AtlasSerif',23,29),('h2','AtlasSerif',15,20),('h3','AtlasBold',11,15),('body','Atlas',9,13.3),('small','Atlas',7,10)]:
  st[name]=ParagraphStyle(name,fontName=font,fontSize=size,leading=leading,textColor=ink if name!='small' else muted,spaceAfter=7,keepWithNext=name in ('h1','h2','h3'))
 story=[]
 def p(text,style='body'):
  story.append(Paragraph(html.escape(text).replace('\n','<br/>'),st[style]))
 def bullet(text):p('•  '+text)
 def label(label,text):story.append(Paragraph('<b>'+html.escape(label)+'</b> '+html.escape(text),st['body']))
 p('CIVILS ATLAS / RESEARCH EDITION 19','small');story.append(Spacer(1,50));p(MONTH,'cover');p('Understand the news.\nRetain what matters.','h2');p(f'{len(ns)} study notes · {len(quiz)} MCQs · Mains frameworks');p('UPSC × Andhra Pradesh APPSC · English\nResearch cut-off: 7 November 2026');story.append(Spacer(1,25));p('Read the coverage contract','h2');p(LIMIT);p(METHOD);p(AUTO_TEXT);p('Source extracts are not whole-document reviews. November covers only 1–7 November. Review research/Research-Status.md before treating any month as complete.');story.append(PageBreak())
 p('Subject guide','h1')
 for s in ORDER:
  c=sum(n['subject']==s for n in ns)
  if c:p(s+' — '+str(c)+' notes')
 p('How to study','h2');p('Read P1 → consolidate P2 → recall P3. Review after 1, 7 and 30 days. Explain each caution unaided. Build answers with a dated fact, mechanism, limitation and conclusion.');p('Sources and access provenance appear in the appendix. Original analysis is not a sourced prediction of exam questions.')
 lastsubject=lastblock=None
 for n in sorted(ns,key=key):
  if n['subject']!=lastsubject:story.append(PageBreak());p(n['subject'],'h1');lastsubject=n['subject'];lastblock=None
  note_start=len(story)
  if n['block']!=lastblock:p(n['block'],'h2');lastblock=n['block']
  p(n['title'],'h3');p(f"{n['id']} · {n['priority']} · {date_label(n)} · {'AP-linked' if n['ap'] else 'National / other'}",'small')
  if n.get('why'):label('WHY IN THE NEWS',n['why'])
  for f in n['facts']:bullet(f)
  if n.get('static_link'):label('STATIC CONNECTION · ORIGINAL',n['static_link'])
  if n.get('analysis'):
   p('ANALYSIS · ORIGINAL GUIDANCE','small')
   for a in n['analysis']:bullet(a)
  if n.get('related_notes'):label('READ ACROSS MONTHS · NOTE IDS',', '.join(n['related_notes'][:8])+(' · Full sequences: Cross-Month Reading Journeys.' if len(n['related_notes'])>8 else ''))
  label('PRELIMS CAUTION',n['trap']);label('MAINS PROMPT',n['mains']);p('Sources: '+', '.join('['+k+']' for k in n['sources']),'small');p('Evidence access: '+n.get('evidence_access','Not recorded'),'small');story.append(Spacer(1,10))
  note_flow=story[note_start:];del story[note_start:];story.append(KeepTogether(note_flow))
 story.append(PageBreak());p(MONTH+' recall laboratory','h1');p(f'{len(quiz)} original questions, not previous-year questions. Answers follow all questions. Historical monthly snapshot only.')
 for q in quiz:
  question_start=len(story)
  p(str(q['id'])+'. '+q['question'],'h3')
  for i,o in enumerate(q['options']):p(chr(65+i)+'. '+o)
  question_flow=story[question_start:];del story[question_start:]
  story.append(KeepTogether(question_flow))
 story.append(PageBreak());p('Explained answer key','h1')
 for q in quiz:label(f"{q['id']}. {chr(65+q['answer'])}",q['explanation']+' ['+q['ref']+']')
 story.append(PageBreak());p('Mains answer laboratory','h1')
 for line in FRAME.splitlines():
  if line.startswith('## '):p(line[3:],'h2')
  elif line.startswith('# '):continue
  elif line.strip():p(line.replace('**',''))
 story.append(PageBreak());p('Source register','h1');p('Evidence access is recorded explicitly. Most non-PRS references were inspected as source extracts; primary full-text review remains open for them.')
 used=set(k for n in ns for k in n['sources'])
 for k in sources:
  if k in used:
   p('['+k+'] '+sources[k][0],'h3');u=sources[k][1];story.append(Paragraph('<link href="'+html.escape(u,quote=True)+'" color="#21645c">'+html.escape(u)+'</link>',st['small']));p(access.get(k,{}).get('access','Not recorded'),'small')
 story.append(PageBreak());p('Unfinished research','h1');p(LIMIT);p('Daily-source reconciliation remains open for every month. Further periods remain unfinished. The monthly inventory and daily/monthly ledgers record work required, not additional completed coverage.');p('The automation files collect links only after deployment and enabling. No hidden researcher will fill the remaining months after this response.');p('Read research/Research-Status.md for corrections, exclusions, evidence caveats and close-out tasks.')
 def furniture(c,d):
  w,h=d.pagesize;c.setStrokeColor(colors.HexColor('#D9DFD6'));c.line(44,h-34,w-44,h-34);c.setFont('Atlas',7);c.setFillColor(muted);c.drawString(44,h-26,'CIVILS ATLAS  /  '+MONTH.upper()+'  /  UPSC × APPSC');c.drawString(44,25,'RESEARCH EDITION 19 · INCOMPLETE MONTHLY/DAY-BY-DAY AUDIT');c.drawRightString(w-44,25,str(d.page))
 doc=SimpleDocTemplate(str(path),pagesize=(595.28,841.89),rightMargin=46,leftMargin=46,topMargin=49,bottomMargin=45,title='Civils Atlas · '+MONTH,author='Civils Atlas research edition')
 doc.build(story,onFirstPage=furniture,onLaterPages=furniture)
(R/'volumes').mkdir(exist_ok=True)
for m in expanded:
 MONTH=datetime.datetime.strptime(m,'%Y-%m').strftime('%B %Y')
 slug=MONTH.replace(' ','-')
 if m=='2026-11':MONTH='1–7 November 2026'
 ns=[n for n in notes if n['date'].startswith(m)];quiz=QS[m]
 fp=R/'volumes'/f'{slug}-Mains-Frameworks.md';FRAME=fp.read_text() if fp.exists() else ''
 (R/'volumes'/f'{slug}-Study-Volume.md').write_text(md_text(ns,True))
 docx_make(ns,R/'volumes'/f'{slug}-Study-Volume.docx',True)
 pdf_make(ns,R/'volumes'/f'{slug}-Study-Volume.pdf')
 print('Built',MONTH,len(ns),'notes',len(quiz),'MCQs')
docx_make(notes,R/'Study-Notes.docx',False)
print('Built archive',len(notes),'notes;',len(sources),'source references; offline HTML')
# A separate, compact reading atlas accompanies—not replaces—the monthly volumes.
def reading_atlas():
 from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer
 from reportlab.lib.styles import ParagraphStyle
 from reportlab.lib import colors
 md=(R/'volumes/Cross-Month-Reading-Journeys.md').read_text();doc=Document();normal=doc.styles['Normal'];normal.font.name='Calibri';normal.font.size=Pt(10.5)
 doc.sections[0].header.paragraphs[0].text='CIVILS ATLAS / EDITION 19 / UPSC × APPSC'
 doc.add_paragraph('7 November 2026 · Original reading guidance · Historical snapshots require current checks')
 story=[]
 styles={k:ParagraphStyle(k,fontName='AtlasSerif' if k!='body' else 'Atlas',fontSize=z,leading=z*1.4,spaceAfter=8,keepWithNext=k!='body',textColor=colors.HexColor('#193F37')) for k,z in [('cover',26),('head',15),('body',9)]}
 for line in md.splitlines():
  if not line.strip():continue
  style='cover' if line.startswith('# ') else 'head' if line.startswith('## ') else 'body';text=re.sub(r'^#{1,2} ','',line).replace('**','')
  if style=='cover':doc.add_heading(text,0)
  elif style=='head':doc.add_heading(text,1)
  else:doc.add_paragraph(text)
  story.append(Paragraph(html.escape(text),styles[style]))
 doc.save(R/'volumes/Cross-Month-Reading-Journeys.docx')
 def foot(c,d):c.setFont('Atlas',7);c.drawString(46,25,'CIVILS ATLAS / CROSS-MONTH READING JOURNEYS / HISTORICAL GUIDANCE');c.drawRightString(550,25,str(d.page))
 SimpleDocTemplate(str(R/'volumes/Cross-Month-Reading-Journeys.pdf'),pagesize=(595.28,841.89),leftMargin=46,rightMargin=46,topMargin=46,bottomMargin=45).build(story,onFirstPage=foot,onLaterPages=foot)
 print('Built cross-month reading atlas',18,'paths')
reading_atlas()
