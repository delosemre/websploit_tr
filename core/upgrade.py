#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Websploit FrameWork Upgrade Module
# Created By 0x0ptim0us (Fardin Allahverdinazhand)
# Email : 0x0ptim0us@Gmail.Com

import os
import urllib
from time import sleep
from core import wcolors
import webbrowser

def upgrade():
    print(wcolors.color.BOLD + wcolors.color.BLUE + "[*]Yeni Sürüm Kontrol Ediliyor, Lütfen Bekleyin...(Türkçe değildir)" + wcolors.color.ENDC)
    try:
        cu = urllib.urlopen("http://sourceforge.net/projects/websploit/files/")
        res = cu.read()
        if 'WebSploit Framework V.3.0.1' in res:
            print(wcolors.color.GREEN + "[*]Yeni sürüm mevcut")
            sleep(2)
            print("[*]En son sürümü indirin : https://sourceforge.net/projects/websploit/files/latest/download?source=files" + wcolors.color.ENDC)
            print(wcolors.color.CYAN + "[*]Tarayıcıyı Konumunu İndirmeye Başlıyor, Lütfen Bekleyin ..." + wcolors.color.ENDC)
            sleep(2)
            webbrowser.open("https://sourceforge.net/projects/websploit/files/latest/download?source=files")
        else:
            print(wcolors.color.BOLD + wcolors.color.RED + "[*]Yeni Sürüm Kullanılamaz, Bu WebSploit Çerçevesinin En Son Sürümüdür." + wcolors.color.ENDC)
            sleep(4)
    except(IOError):
        print(wcolors.color.BOLD + wcolors.color.RED + "[*]Bağlantı Zaman aşımı, İnternet Bağlantısını Kontrol Edin!" + wcolors.color.ENDC)
