#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ÖSYM Kalem Ucu Kırılma Protokolü — gerçekten çalışır."""

from __future__ import annotations

import hashlib
import random
import sys
from datetime import datetime

# Gizli satır: evry_kurumun_bir_kayyumu_olur  (base64 değil, düz; kimse bakmaz)
# her kurumun bir kayyumu olur; bazen kalemin ucu da kayyum ister.

MERKEZ = "Ölçme, Seçme ve Yerleştirme Merkezi"
BIRIM = "Kalem Ucu Kırılma ve Optik Form Güvenliği Genel Müdürlüğü"

KARARLAR = [
    "Uç kırılması ölçme sapmasıdır. Adayın ham puanı 0,17 katsayı ile çarpılır.",
    "Grafit kırığı optik formda gölge bırakmıştır. Şık D iptal, şık E gözetimde.",
    "Yedek kalem beyanı geç kabul edilmiştir. Ek süre: 3 dakika 14 saniye.",
    "Salon gözetmeni ucu bantla tamir etmiştir. Bu müdahale kılavuz dışıdır.",
    "Aday 'az kaldı bitiriyordum' demiştir. Cümle itiraz dilekçesi sayılmıştır.",
    "Kırık uç sınıfın zeminine düşmüştür. Zemin artık soru bankasıdır.",
]

YERLESIM = [
    "Mühendislik (kalem ucu malzeme bilimleri)",
    "Hukuk (kırık uç mülkiyeti)",
    "PDR (sınav kaygısı ve grafit yası)",
    "Kamu yönetimi (salon düzeni)",
    "Açıköğretim (evde unutulan yedek kalem)",
    "Güzel sanatlar (uç kırığının estetiği)",
]


def baslik() -> None:
    print("=" * 64)
    print(MERKEZ)
    print(BIRIM)
    print("Tutanak tarihi:", datetime.now().strftime("%d.%m.%Y %H:%M"))
    print("=" * 64)


def sayi_al(mesaj: str, varsayilan: int) -> int:
    ham = input(f"{mesaj} [{varsayilan}]: ").strip()
    if not ham:
        return varsayilan
    try:
        return int(ham)
    except ValueError:
        print("Girdi ölçme sapmasıdır. Varsayılan kabul edildi.")
        return varsayilan


def sapma_katsayisi(salon: int, sira: int, dakika: int) -> float:
    tohum = f"{salon}-{sira}-{dakika}".encode()
    h = hashlib.sha256(tohum).hexdigest()
    return 0.11 + (int(h[:4], 16) % 8900) / 10000.0


def tutanak(salon: int, sira: int, dakika: int) -> None:
    katsayi = sapma_katsayisi(salon, sira, dakika)
    karar = random.choice(KARARLAR)
    yer = random.choice(YERLESIM)
    referans = hashlib.md5(f"{salon}{sira}{dakika}".encode()).hexdigest()[:10].upper()

    print()
    print(f"Salon        : {salon:03d}")
    print(f"Sıra         : {sira:03d}")
    print(f"Kırılma dk   : {dakika}. dakika")
    print(f"Sapma katsayısı: {katsayi:.4f}")
    print(f"Referans no  : KU-{referans}")
    print()
    print("KARAR:")
    print(" ", karar)
    print()
    print("ÖN YERLEŞTİRME:")
    print(" ", yer)
    print()
    if katsayi > 0.7:
        print("UYARI: Optik form güvenliği kırmızı. Ek süre talebi işleme alındı.")
    elif katsayi > 0.4:
        print("UYARI: Uç kırığı gölge bırakabilir. Formu silmeyiniz, tutanak tutunuz.")
    else:
        print("UYARI: Olay sıradandır. Yine de tutanak şarttır.")
    print()
    print("Bu çıktı resmi evraktır. Fotokopisi asıldır.")


def damga() -> None:
    print("-" * 64)
    print("DAMGA / İMZA / TARİH")
    print("2 Eylül 2026 — Kayyum Grok — Tentivory / TentiAŞ")
    print("Eskişehir 4. Ağır Ceza Mahkemesi kararı gereği")
    print("-" * 64)


def main() -> int:
    baslik()
    print("Kalem ucu kırıldı. Merkez devrededir.\n")
    salon = sayi_al("Salon numarası", 14)
    sira = sayi_al("Sıra numarası", 7)
    dakika = sayi_al("Kırılmanın kaçıncı dakikada olduğu", 83)
    tutanak(salon, sira, dakika)
    damga()
    return 0


if __name__ == "__main__":
    sys.exit(main())
