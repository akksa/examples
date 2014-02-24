import re
import cgi
import traceback

def stripHtml(text):
    re_null_unicode_chr = re.compile(u'\u0000',re.UNICODE)
    """Strip the given text off all HTML tags

    >>> strip_html("<p>This is a test<br/> of strip</p>")
    This is a test\n of strip
    """
    #text = re.sub(r'<br(\s)*?(\/)?>', '\n', text)
    text = re_null_unicode_chr.sub('',text)
    text = re.sub(r'</?(p|br)\s?/?>', r'\n', text)
    text = re.sub(r'<[^<>]+>', ' ', text)
    text = re.sub(r'^(\s)+', '', text)
    re1 = re.compile(r'^(\s*\n)+',re.M)
    text = re1.sub(r'\n',text)
    #re2 = re.compile(r'\n(\S)',re.M)
    #text = re2.sub(r' \1', text)
    #text = re.sub(r'\s+', ' ', text)

    
    text=text.replace('\');" onMouseOut="setTimeout(\'hideLayer()\',500);" class=hotlink2>','')
    text=text.replace('Click for the lowest price on dmnobieblank','')
    
    
    text = text.replace('&nbsp;',' ')
    text = text.replace('&raquo;','')
    try:
        if not isinstance(text, unicode):
            text = text.decode('utf-8','ignore')
        else:
            text = text.encode('utf-8','ignore').decode('utf-8','ignore')
#         if not isinstance(text,unicode):
#             text = cgi.unescape(unicode(text,'utf-8'))
#         else:
        text = cgi.unescape(text)
    except:
        print traceback.format_exc()
#        print text
        
    return text.strip()

