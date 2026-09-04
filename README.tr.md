# AI Ajanı Yetki Fişi

Bir AI ajanına araç veya hesap erişimi vermeden önce altı kutu dolduruyorum:

`goal | may_read | may_write | ask_before | stop_if | show_me`

Fiş bu kadar. Model seçmez, ajan çalıştırmaz. Anahtarları vermeden önce hangi kapıları açtığını yazılı hâle getirir.

Önce [Markdown şablonunu](templates/permission-card.md) kopyalayabilirsin. Yapılandırılmış veriyle çalışan bir akış için [JSON](templates/permission-card.json) ve [YAML](templates/permission-card.yaml) sürümleri de var.

## Altı kutu ne işe yarıyor?

### `goal`

Kontrol edebileceğin tek bir sonuç yaz. "Rakipleri izle" bulanık kalır. "Verdiğim üç sayfadaki bugünkü fiyatları dünkü dosyayla karşılaştır" dediğinde işin kenarları belli olur.

### `may_read`

Ajanın okuyabileceği her URL'yi, dosyayı, hesabı veya veri kaynağını tek tek yaz. İş üç açık ürün sayfasıyla bitiyorsa bütün Drive hesabını açmanın anlamı yok.

### `may_write`

Değiştirebileceği yerleri listele. Fiyatı okumak başka iş, canlı fiyatı değiştirmek başka. İlk koşum yalnız yerel bir rapora yazabilir.

### `ask_before`

Fiili açık yaz. Göndermeden, yayınlamadan, ödeme veya iade yapmadan, silmeden ve dosyanın üstüne yazmadan önce sorsun. Onay, araç çalıştıktan sonra verilen açıklama değildir.

### `stop_if`

İşler yamulduğunda nerede duracağını baştan belirle. Giriş ekranı, belirsiz eşleşme, eksik veri veya deneme sınırı koşumu durdurabilir. Ajan kapsamı kendi kendine genişletmesin; takıldığı yeri göstersin.

### `show_me`

İşin makbuzunu belirle. Baktığı URL, yazdığı dosya, kayıt kimliği, test, saat veya log neyse fişe koy. Kuru bir "tamamlandı" kanıt sayılmaz.

## Temsili fiyat kontrolünü dene

[Fiyat kontrolü örneği](examples/price-check.md), `example.com` üzerindeki üç ürün sayfasını ve bir yerel dosyayı okur. Yalnız bir Markdown raporuna yazabilir. Giriş yapamaz, mağazayı değiştiremez, mesaj gönderemez ve sonsuza kadar tekrar deneyemez.

Aynı fişin [doğrulanmış JSON sürümü](examples/price-check.json) de var. Örnekteki bütün alan adları ve fiyatlar temsilidir.

## Fişi doğrula

Sabitlenmiş iki geliştirme bağımlılığını kurup kontrolleri çalıştır:

```bash
python3 -m pip install -r requirements-dev.txt
python3 -m unittest discover -s tests -v
python3 scripts/validate_examples.py
```

[JSON Schema](schema/permission-card.schema.json), altı zorunlu kutudan biri eksikse veya tanımsız bir üst alan eklenmişse fişi reddeder. Bu kontrol bozuk belgeyi yakalar. Tarayıcıda, API'de, işletim sisteminde veya ajanın çalışma zamanında teknik yetki uygulamaz.

## Güvenlik sınırı

Public repoya koyacağın fişe gerçek parola, token, müşteri kaydı, özel URL veya gizli olay ayrıntısı yazma. Örnek eklemeden önce [SECURITY.md](SECURITY.md) dosyasını oku.

Bu repoda ajan, telemetri, uzaktan çağrı, hesap entegrasyonu veya barındırılan form yok. Elindeki şey koşumdan önce okuyacağın bir belge. Kullandığın araçların ve sistemlerin kendi erişim kontrolleri yine gerekli.

## Kaynak

Bu fişi ilk kez bir e-ticaret otomasyonunu sıkıcı ve salt okunur bir pilota indirirken kullandım. Daha uzun anlatımı kendi sitemdeki [AI ajanı rehberinde](https://www.mehmetkocabas.com/blog/ai-ajan-nedir-chatbot-farki) bulabilirsin. Bu repo, o altı kutuyu kopyalanabilir ve doğrulanabilir dosyalara çeviriyor.

Proje [MIT Lisansı](LICENSE) ile yayımlanır. Katkılarda temsili veya karartılmış örnek kullan; ayrıntılar [CONTRIBUTING.md](CONTRIBUTING.md) dosyasında.
