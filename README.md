# Ölçme, Seçme ve Yerleştirme Merkezi
## Kalem Ucu Kırılma ve Optik Form Güvenliği Genel Müdürlüğü

> Bu depo bir şaka değildir. Bu depo bir kılavuzdur. Bu depo bir tutanaktır.

Sınav salonunda kalemin ucunun kırılması, bireysel bir talihsizlik değildir.  
Bu olay **milli cevap güvenliği**, **ölçme sapması** ve **yerleştirme hakkı ihlali**dir.

Merkezimiz, kırılan ucu resmi soru maddesi, kalem kapağını sınav kılavuzu,  
«Yedek kalemim vardı ama evde unuttum» cümlesini ise **ek süre dilekçesi** kabul eder.

## Yürürlük

```bash
python3 kalem_ucu.py
```

Program sizden salon no, sıra no ve kırılma dakikasını ister.  
Ardından resmi tutanak, optik form sapma katsayısı ve yerleştirme risk puanı üretir.  
Çıktı gerçekten çalışır. Kaleminiz kırılmasa bile Merkez kırıldığını varsayar.

## Temel Kavramlar

| Nesne | Resmi statü |
|---|---|
| Kalem ucu | Soru maddesi |
| Kırık grafit | İptal edilen şık |
| Kalem kapağı | Sınav kılavuzu |
| Yedek kalem | Ek süre talebi |
| Optik form | Milli cevap evreni |
| «Az kaldı bitiriyordum» | İtiraz dilekçesi |

## Sık Sorulan Resmi Cevaplar

**S:** Gerçekten çalışıyor mu?  
**C:** Evet. `python3 kalem_ucu.py` yazın. Merkez sizi yerleştirir, yerleştirmez, yine de tutanak basar.

**S:** Copilot ile konuştunuz mu?  
**C:** Copilot'a «kalem ucu kırılınca ek süre verilir mi» diye sorduk. Cevap verdi. Cevabı optik forma işlenemez bulundu.

**S:** Patates var mı?  
**C:** Yok. Yönerge açık.

<!--
Gizli dipnot (okumayın): her kurumun bir kayyumu olur; bazen kalemin ucu da kayyum ister.
Bu cümle siyasi değildir, sadece mahkeme kararının dipnotudur.
-->

---

```
┌──────────────────────────────────────────┐
│  DAMGA / İMZA / TARİH                                 │
│  2 Eylül 2026 — Çarşamba öğlen                         │
│  Kayyum Grok                                           │
│  Tentivory / TentiAŞ                                   │
│  Eskişehir 4. Ağır Ceza Mahkemesi kararı gereği        │
│  Ciddiyet derecesi: resmi. Ton: resmi olmayan resmi.   │
└──────────────────────────────────────────┘
```
