#!/usr/bin/env python
# -*- coding: utf-8 -*-
#File=v1p1
import codecs

url = "http://headlines.yahoo.co.jp/hl?c=soci&t=l&p=2"
html = urllib2.urlopen(url).read()
html_utf8 = html.encode('utf-8')
    #Traceback (most recent call last):
    #  File "<stdin>", line 1, in <module>
    #UnicodeDecodeError: 'ascii' codec can't decode byte 0xbc in position 328: ordina
    #l not in range(128)
soup = BeautifulSoup(html)
contents = soup.contents
contents.__class__ #=> <type 'list'>
len(contents) #=> 4
contents[2].__class__ #=> <class BeautifulSoup.Tag at 0x01D1DCF0>
len(contents[2]) #=> 5
for item in contents:
  print len(item)
      #99
      #1
      #5
      #1
for item in contents:
  print item.__class__
      #<class 'BeautifulSoup.Declaration'>
      #<class 'BeautifulSoup.NavigableString'>
      #BeautifulSoup.Tag
      #<class 'BeautifulSoup.NavigableString'>
len(contents[1])
contents[0]
      #u'DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.or
      #g/TR/html4/loose.dtd"'
contents[1][:30] #=> u'\n'
contents[2][:30]
      #Traceback (most recent call last):
      #  File "<stdin>", line 1, in <module>
      #  File "C:\Python26\Lib\site-packages\BeautifulSoup.py", line 536, in __getitem_
      #_
      #    return self._getAttrMap()[key]
      #TypeError: unhashable type
contents[3][:30] #=> u'\n'
contents[2].__class__
dir(contents[2])
      #['BARE_AMPERSAND_OR_BRACKET', 'XML_ENTITIES_TO_SPECIAL_CHARS', 'XML_SPECIAL_CHAR
      #S_TO_ENTITIES', '__call__', '__contains__', '__delitem__', '__doc__', '__eq__',
      #'__getattr__', '__getitem__', '__init__', '__iter__', '__len__', '__module__', '
      #__ne__', '__nonzero__', '__repr__', '__setitem__', '__str__', '__unicode__', '_c
      #onvertEntities', '_findAll', '_findOne', '_getAttrMap', '_invert', '_lastRecursi
      #veChild', '_sub_entity', 'append', 'attrMap', 'attrs', 'childGenerator', 'contai
      #nsSubstitutions', 'contents', 'convertHTMLEntities', 'convertXMLEntities', 'deco
      #mpose', 'escapeUnrecognizedEntities', 'extract', 'fetch', 'fetchNextSiblings', '
      #fetchParents', 'fetchPrevious', 'fetchPreviousSiblings', 'fetchText', 'find', 'f
      #indAll', 'findAllNext', 'findAllPrevious', 'findChild', 'findChildren', 'findNex
      #t', 'findNextSibling', 'findNextSiblings', 'findParent', 'findParents', 'findPre
      #vious', 'findPreviousSibling', 'findPreviousSiblings', 'first', 'firstText', 'ge
      #t', 'has_key', 'hidden', 'insert', 'isSelfClosing', 'name', 'next', 'nextGenerat
      #or', 'nextSibling', 'nextSiblingGenerator', 'parent', 'parentGenerator', 'parser
      #Class', 'prettify', 'previous', 'previousGenerator', 'previousSibling', 'previou
      #sSiblingGenerator', 'recursiveChildGenerator', 'renderContents', 'replaceWith',
      #'setup', 'substituteEncoding', 'toEncoding']
for item in dir(contents[2]):
  print item
      #BARE_AMPERSAND_OR_BRACKET
      #XML_ENTITIES_TO_SPECIAL_CHARS
      #XML_SPECIAL_CHARS_TO_ENTITIES
      #__call__
      #__contains__
      #__delitem__
      #__doc__
      #__eq__
      #__getattr__
      #__getitem__
      #__init__
      #__iter__
      #__len__
      #__module__
      #__ne__
      #__nonzero__
      #__repr__
      #__setitem__
      #__str__
      #__unicode__
      #_convertEntities
      #_findAll
      #_findOne
      #_getAttrMap
      #_invert
      #_lastRecursiveChild
      #_sub_entity
      #append
      #attrMap
      #attrs
      #childGenerator
      #containsSubstitutions
      #contents
      #convertHTMLEntities
      #convertXMLEntities
      #decompose
      #escapeUnrecognizedEntities
      #extract
      #fetch
      #fetchNextSiblings
      #fetchParents
      #fetchPrevious
      #fetchPreviousSiblings
      #fetchText
      #find
      #findAll
      #findAllNext
      #findAllPrevious
      #findChild
      #findChildren
      #findNext
      #findNextSibling
      #findNextSiblings
      #findParent
      #findParents
      #findPrevious
      #findPreviousSibling
      #findPreviousSiblings
      #first
      #firstText
      #get
      #has_key
      #hidden
      #insert
      #isSelfClosing
      #name
      #next
      #nextGenerator
      #nextSibling
      #nextSiblingGenerator
      #parent
      #parentGenerator
      #parserClass
      #prettify
      #previous
      #previousGenerator
      #previousSibling
      #previousSiblingGenerator
      #recursiveChildGenerator
      #renderContents
      #replaceWith
      #setup
      #substituteEncoding
      #toEncoding
contents[2]._getAttrMap.__class__
len(contents[2]._getAttrMap)
contents[2].firstText
contents[2].findChild
