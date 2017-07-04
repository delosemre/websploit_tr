#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Websploit FrameWork Database Module
# Created By 0x0ptim0us (Fardin Allahverdinazhand)
# Email : 0x0ptim0us@Gmail.Com

from core import wcolors
from time import sleep
def modules_database():
    print ""
    print (wcolors.color.BLUE + "Web Modülleri\t\t\tAçıklama" + wcolors.color.ENDC)
    print (wcolors.color.GREEN + "-------------------\t\t---------------------" + wcolors.color.ENDC)
    print "web/apache_users\t\tApache Kullanıcılarının Tarama Dizini"
    print "web/dir_scanner\t\t\tDizin Tarayıcı"
    print "web/wmap\t\t\tMağdur İnternet'ten Bilgi Toplama (Metasploit Wmap)"
    print "web/pma\t\t\t\tPHPMyAdmin Giriş Sayfası Tarayıcısı"
    print "web/cloudflare_resolver\t\tCloudFlare Çözümleyici"
    print "\n"
    print (wcolors.color.BLUE + "Ağ Modülleri\t\t\tAçıklama" + wcolors.color.ENDC)
    print (wcolors.color.GREEN + "-------------------\t\t---------------------" + wcolors.color.ENDC)
    print "network/arp_dos\t\t\tARP Önbellek Hizmet Reddini Saldırısı"
    print "network/mfod\t\t\tDoom Atak Orta Parmak"
    print "network/mitm\t\t\tOrta Saldırıda Adam"
    print "network/mlitm\t\t\tOrta Saldırıda Adam Oturdu"
    print "network/webkiller\t\tTCP öldürme saldırısı"
    print "network/fakeupdate\t\tDNS Spoof'u Kullanarak Sahte Güncelleme Saldırısı"
    print "network/arp_poisoner\t\tArp Zehirlenmesi"
    print "\n"
    print (wcolors.color.BLUE + "Exploit Modülleri\t\t\tAçıklama" + wcolors.color.ENDC)
    print (wcolors.color.GREEN + "-------------------\t\t---------------------" + wcolors.color.ENDC)
    print "exploit/autopwn\t\t\tMetasploit Otoport Hizmeti"
    print "exploit/browser_autopwn\t\tMetasploit Tarayıcı Otomatik Çizme Hizmeti"
    print "exploit/java_applet\t\tJava Applet Saldırısı (Using HTML)"
    print "\n"
    print (wcolors.color.BLUE + "Kablosuz / Bluetooth Modülleri\tAçıklama" + wcolors.color.ENDC)
    print (wcolors.color.GREEN + "-------------------\t\t---------------------" + wcolors.color.ENDC)
    print "wifi/wifi_jammer\t\tWifi kilitleyici"
    print "wifi/wifi_dos\t\t\tWifi Dos Saldırısı"
    print "wifi/wifi_honeypot\t\tKablosuz balina(Fake AP)"
    print "wifi/mass_deauth\t\tKitlesel Deauthentication Saldırısı"
    print "bluetooth/bluetooth_pod\t\tBluetooth Ping Ve Ölüm Saldırısı"
    print "\n"
