# Türkçe F Klavye Etiketleri

Q düzenli klavyenizi **Türkçe F** düzenine dönüştürmek için kendiniz yazdırıp yapıştırabileceğiniz tuş kapağı etiketleri.

Etiketlerde her tuş için dört karakter yer alır:

- **Sol üst:** Shift ile
- **Orta alt:** tuşun normal karakteri
- **Sağ alt:** AltGr ile
- **Sağ üst:** AltGr + Shift ile

## İçerik

| Dosya | Açıklama |
|---|---|
| `configurator.html` | Etiket düzenleyici. Tarayıcıda açın, ayarları yapın ve yazdırın |
| `generate_configurator.py` | `configurator.html` dosyasını üreten betik |
| `generate_sheet.py` | Tuş düzenini X11 klavye tanımından okuyan betik |

## Kullanım

1. `configurator.html` dosyasını tarayıcıda açın.
2. Etiket boyutunu kontrol edin. Varsayılan 10 mm kare etiketler, dizüstü klavye tuşlarının düz üst yüzeyine (yaklaşık 1 cm × 1 cm) uyacak şekilde ayarlanmıştır. Masaüstü klavye için de bu boyut uygundur.
3. İsterseniz yazı boyutunu, rengini veya kesim çizgisini değiştirin. Tek tek tuşlara tıklayarak yalnızca o tuşun renklerini de değiştirebilirsiniz.
4. **Print / Save as PDF** düğmesine basın. Yazdırma ayarlarında **gerçek boyut / %100** seçin, ölçekleme ve kenar boşluğu kapalı olsun.
5. Etiketleri yapışkan etiket kağıdına (beyaz veya şeffaf) yazdırın ve dikkatlice kesin. Kesim çizgileri kesikli çizgilerle gösterilir.
6. Etiketleri tuş kapaklarının düz üst yüzeyine yapıştırın.

Ayarlarınız tarayıcıda otomatik olarak saklanır.

## Önemli notlar

- Tuş düzeni Linux X11 klavye tanımındaki `tr(f)` varyantından alınmıştır. Windows'taki Türkçe F düzeni ile küçük farklar olabilir. Özellikle AltGr karakterlerini kullanmadan önce kendi sisteminizle karşılaştırın.
- **Shift + AltGr + X** tuşu bir ölü tuştur (`` ` `` aksan). Bu tuşa basıp ardından bir harfe basarsanız harf aksanlı görünür. Ölü tuşa basıp boşluk benzeri bir tuşa basarsanız aksan tek başına yazılır.
- **Shift + AltGr + B** tuşu boşluğa benzeyen **kesmez boşluk** (NBSP) karakterini yazar. Etiketinde `⍽` işareti bulunur. Bu boşluk, iki kelimenin satır sonunda ayrılmasını engeller.

## Yeniden üretme

Gereksinimler: Python 3.

```sh
python3 generate_configurator.py   # configurator.html dosyasını üretir
```

Klavye tanımı farklı bir yerdeyse `XKB_TR` ortam değişkeniyle yolunu belirtebilirsiniz.
