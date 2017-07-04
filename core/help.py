#!/usr/bin/env python
# -*- coding: utf-8 -*-
# WebSploit FrameWork Help Module
# Created By 0x0ptim0us (Fardin Allahverdinazhand)
# Email : 0x0ptim0us@Gmail.Com

from core import wcolors
from time import sleep
def help():
    print "\n"
    print (wcolors.color.BLUE + "Commands\t\tDescription" + wcolors.color.ENDC)
    print (wcolors.color.GREEN + "---------------\t\t----------------" + wcolors.color.ENDC)
    print "set \t\t\tSeçeneklerin Değeri Modüllere Ayarla"
    print "scan\t\t\tWifi Tarama (Kablosuz Modüller)"
    print "stop\t\t\tSaldırı ve Taramayı Durdur (Kablosuz Modüller)"
    print "run \t\t\tModül Yürüt"
    print "use \t\t\tKullanım Modülünü Seçin"
    print "os \t\t\tLinux Komutlarını çalıştırın (örneğin: ifsconfig)"
    print "back\t\t\tModülden Çık"
    print "show modules\t\tMevcut Veritabanının Modüllerini Göster"
    print "show options\t\tSeçili Modülün Mevcut Seçeneklerini Göster"
    print "upgrade\t\t\tYeni Sürüm Edin"
    print "update\t\t\tWebSploit Çerçevesini Güncelle "
    print "about\t\t\tHakkımızda"
    print ""
