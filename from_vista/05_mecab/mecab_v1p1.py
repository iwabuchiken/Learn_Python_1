#coding:utf-8

import MeCab
tagger = MeCab.Tagger("-Ochasen")
result = tagger.parse("MeCabの形態素解析機能を使ってみました。")
#print result.__class__
print result
#print result.encode('shift_jis')
