# -*- encoding: gb2312 -*- 
import  codecs, sys
from langconv import *

 #  ��codecs�ṩ��open������ָ���򿪵��ļ������Ա��룬�����ڶ�ȡ��ʱ���Զ�ת��Ϊ�ڲ�unicode 
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
