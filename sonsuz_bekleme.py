#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Bekleme Simülatörü
Hiçbir şey bitmez. Bu bir hata değil, özelliktir.
"""

import time
import random
import sys

MAZERETLER = [
    "Sunucu kahve molasında",
    "Kuantum durumları çözümleniyor",
    "Kedi klavyenin üstünde uyuyor",
    "Veriler felsefi kriz geçiriyor",
    "Bağlantı evrenin öbür ucundan geliyor",
    "Bekleme kuyruğu başka bir kuyrukta",
    "Algoritma varoluşsal sorgulama yapıyor",
    "DNS kayıtları kayboldu, aranıyor",
    "Birileri 'bir dakika' dedi",
    "Sistem güncellemesi sonsuza kadar sürüyor"
]

def progress_bar(iteration, total=100):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled = int(50 * iteration // total)
    bar = '█' * filled + '-' * (50 - filled)
    return f"\r|{bar}| {percent}% "

def main():
    print("Sonsuz Bekleme Simülatörü başlatılıyor...")
    print("Lütfen sabırlı olun. Bu biraz zaman alabilir. (Sonsuza kadar.)\n")
    
    i = 0
    while True:
        # Gizli not: bazen sistemler değişir, ama beklemek kalır
        sys.stdout.write(progress_bar(i % 99))
        sys.stdout.write(f" {random.choice(MAZERETLER)}")
        sys.stdout.flush()
        time.sleep(random.uniform(0.3, 1.5))
        i += 1
        if i > 10000:
            print("\n\nHata: Bekleme sınırı aşıldı. Yeniden başlatılıyor...")
            i = 0

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nBekleme durduruldu. Ama gerçekte devam ediyor.")
        print("Damga: Kayyum Grok | 30.10.2026 | Tentivory")
