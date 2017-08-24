# -*- encoding: gb2312 -*- 
import  codecs, sys
from langconv import *

 #  用codecs提供的open方法来指定打开的文件的语言编码，它会在读取的时候自动转换为内部unicode 
bfile  =  codecs.open( "ceshi.json" ,  "r" ,"utf-8" )
 # bfile = open("dddd.txt", 'r') 
 
ss  =  bfile.readline()
f=open("hello.txt","wb")


i=1
while ss:
    ss=ss.encode("utf-8")
    try:
        
        ss=Converter('zh-hans').convert(ss.decode('utf-8'))
        ss=ss.encode("utf-8")
        f.write(ss)
    except:
        print("error in line %d"% i)
    finally:
        ss = bfile.readline()
        i=i+1

    
bfile.close()





f.close()
