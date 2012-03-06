#!/usr/bin/env python
# -*- coding: utf-8 -*-
#File=v1p2
import codecs, urllib2
import BeautifulSoup

url = "http://headlines.yahoo.co.jp/hl?c=soci&t=l&p=2"
req = urllib2.urlopen(url)
req.headers #=> <httplib.HTTPMessage instance at 0x022ED238>
dir(req.headers)
      #['__contains__', '__delitem__', '__doc__', '__getitem__', '__init__', '__iter__'
      #, '__len__', '__module__', '__setitem__', '__str__', 'addcontinue', 'addheader',
      # 'dict', 'encodingheader', 'fp', 'get', 'getaddr', 'getaddrlist', 'getallmatchin
      #gheaders', 'getdate', 'getdate_tz', 'getencoding', 'getfirstmatchingheader', 'ge
      #theader', 'getheaders', 'getmaintype', 'getparam', 'getparamnames', 'getplist',
      #'getrawheader', 'getsubtype', 'gettype', 'has_key', 'headers', 'iscomment', 'ish
      #eader', 'islast', 'items', 'keys', 'maintype', 'parseplist', 'parsetype', 'plist
      #', 'plisttext', 'readheaders', 'rewindbody', 'seekable', 'setdefault', 'startofb
      #ody', 'startofheaders', 'status', 'subtype', 'type', 'typeheader', 'unixfrom', '
      #values']
req.headers.__class__ #=> <class httplib.HTTPMessage at 0x01C40C60>
req.headers.keys()
      #['transfer-encoding', 'vary', 'connection', 'pragma', 'cache-control', 'date', '
      #p3p', 'content-type']
req.headers['content-type'] #=> 'text/html; charset=euc-jp'
req.headers['content-type'].__class__ #=> <type 'str'>
for item in req.headers.keys():
  print "%s=%s" % (item, req.headers[item])
      #transfer-encoding=chunked
      #vary=Accept-Encoding
      #connection=close
      #pragma=no-cache
      #cache-control=no-cache, must-revalidate, private
      #date=Sun, 17 Apr 2011 05:04:12 GMT
      #p3p=policyref="http://privacy.yahoo.co.jp/w3c/p3p.xml", CP="CAO DSP COR CUR ADM
      #DEV TAI PSA PSD IVAi IVDi CONi TELo OTPi OUR DELi SAMi OTRi UNRi PUBi IND PHY ON
      #L UNI PUR FIN COM NAV INT DEM CNT STA POL HEA PRE GOV"
      #content-type=text/html; charset=euc-jp
encoding=req.headers['content-type'].split('charset=')[-1]
content = req.read()
ucontent = unicode(content, encoding)
ucontent[:10].encode('utf-8')
ucontent.encode('euc-jp')
#html = req.read()
soup = BeautifulSoup(ucontent)
contents = soup.contents
dir(soup)
      #['ALL_ENTITIES', 'BARE_AMPERSAND_OR_BRACKET', 'CHARSET_RE', 'HTML_ENTITIES', 'MA
      #RKUP_MASSAGE', 'NESTABLE_BLOCK_TAGS', 'NESTABLE_INLINE_TAGS', 'NESTABLE_LIST_TAG
      #S', 'NESTABLE_TABLE_TAGS', 'NESTABLE_TAGS', 'NON_NESTABLE_BLOCK_TAGS', 'PRESERVE
      #_WHITESPACE_TAGS', 'QUOTE_TAGS', 'RESET_NESTING_TAGS', 'ROOT_TAG_NAME', 'SELF_CL
      #OSING_TAGS', 'STRIP_ASCII_SPACES', 'XHTML_ENTITIES', 'XML_ENTITIES', 'XML_ENTITI
      #ES_TO_SPECIAL_CHARS', 'XML_SPECIAL_CHARS_TO_ENTITIES', '_SGMLParser__starttag_te
      #xt', '__call__', '__contains__', '__delitem__', '__doc__', '__eq__', '__getattr_
      #_', '__getitem__', '__init__', '__iter__', '__len__', '__module__', '__ne__', '_
      #_nonzero__', '__repr__', '__setitem__', '__str__', '__unicode__', '_convertEntit
      #ies', '_convert_ref', '_decl_otherchars', '_feed', '_findAll', '_findOne', '_get
      #AttrMap', '_invert', '_lastRecursiveChild', '_parse_doctype_attlist', '_parse_do
      #ctype_element', '_parse_doctype_entity', '_parse_doctype_notation', '_parse_doct
      #ype_subset', '_popToTag', '_scan_name', '_smartPop', '_sub_entity', '_toStringSu
      #bclass', 'append', 'attrs', 'childGenerator', 'close', 'containsSubstitutions',
      #'contents', 'convertEntities', 'convertHTMLEntities', 'convertXMLEntities', 'con
      #vert_charref', 'convert_codepoint', 'convert_entityref', 'currentData', 'current
      #Tag', 'decompose', 'endData', 'entity_or_charref', 'entitydefs', 'error', 'escap
      #eUnrecognizedEntities', 'extract', 'feed', 'fetch', 'fetchNextSiblings', 'fetchP
      #arents', 'fetchPrevious', 'fetchPreviousSiblings', 'fetchText', 'find', 'findAll
      #', 'findAllNext', 'findAllPrevious', 'findChild', 'findChildren', 'findNext', 'f
      #indNextSibling', 'findNextSiblings', 'findParent', 'findParents', 'findPrevious'
      #, 'findPreviousSibling', 'findPreviousSiblings', 'finish_endtag', 'finish_shortt
      #ag', 'finish_starttag', 'first', 'firstText', 'fromEncoding', 'get', 'get_startt
      #ag_text', 'getpos', 'goahead', 'handle_charref', 'handle_comment', 'handle_data'
      #, 'handle_decl', 'handle_endtag', 'handle_entityref', 'handle_pi', 'handle_start
      #tag', 'has_key', 'hidden', 'insert', 'instanceSelfClosingTags', 'isSelfClosing',
      # 'isSelfClosingTag', 'lasttag', 'lineno', 'literal', 'markup', 'name', 'next', '
      #nextGenerator', 'nextSibling', 'nextSiblingGenerator', 'nomoretags', 'offset', '
      #parent', 'parentGenerator', 'parseOnlyThese', 'parse_comment', 'parse_declaratio
      #n', 'parse_endtag', 'parse_marked_section', 'parse_pi', 'parse_starttag', 'parse
      #rClass', 'popTag', 'prettify', 'previous', 'previousGenerator', 'previousSibling
      #', 'previousSiblingGenerator', 'pushTag', 'quoteStack', 'rawdata', 'recursiveChi
      #ldGenerator', 'renderContents', 'replaceWith', 'report_unbalanced', 'reset', 'se
      #tliteral', 'setnomoretags', 'setup', 'smartQuotesTo', 'stack', 'start_meta', 'su
      #bstituteEncoding', 'tagStack', 'toEncoding', 'unknown_charref', 'unknown_decl',
      #'unknown_endtag', 'unknown_entityref', 'unknown_starttag', 'updatepos', 'verbose
      #']
len(dir(soup)) #=> 175
soup.ALL_ENTITIES #=> 'xhtml'
soup.lasttag #=> u'script'
soup.popTag

#02
req = urllib2.urlopen('http://lenta.ru')
content = req.read()
encoding=req.headers['content-type'].split('charset=')[-1]
ucontent = unicode(content, encoding)
print ucontent[76:110].encode('utf-8') #=> <title>Lenta.ru: ﾐ寅ｻﾐｰﾐｲﾐｽﾐｾﾐｵ: </title>
req.headers['content-type'] #=> 'text/html; charset=windows-1251'