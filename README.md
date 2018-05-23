BENDEN KAÇAMAZSIN!


Proje Sahipleri:
Emine Meltem HAMZAOĞLU 170215002
Tugay Kaan ARSLAN 171214003

Raspberry Pi kullanarak Parmak İzi Sensörü İle İşçilerin Bilgilerinin Alınması ve Renk Sensörü İle İş Önlüklerinin tespit edilmesi


MALZEMELER
1 adet Raspberry Pi 3 B+ (Raspbian Jessie Os kurulu)
1 adet TCS3200 Renk Sensörü
1 adet ZFM60 Parmak İzi Okuyucu Sensör 
1 adet Breadboard
Jumper Kablolar


YAZILIMLAR
Raspbian Jessie OS
Python 3.6

Malzemelerin alındığı yerler
1-	ZFM60 Parmak İzi Okuyucu Sensör https://www.direnc.net/parmak-izi-okuyucu
2-	TCS3200 Renk Sensörü https://www.robotistan.com/tcs3200-renk-sensoru-karti



Sırasıyla Terminale yazacağımız kodlar:

Paketleri Yüklemek için:
sudo apt-get install git devscripts

Bu konuda daha önce çalışmış birinin kütüphanesini kopyalıyoruz.
git clone https://github.com/bastianraschke/pyfingerprint.git

Kurmaya başlıyoruz
cd ./pyfingerprint/src/

Yapılandırıyoruz
dpkg-buildpackage -uc -us

Python 3 için:
sudo dpkg -i ../python3-fingerprint*.deb

Bağımlı eksiklikleri yüklüyoruz
sudo apt-get -f install

sudo usermod -a -G dialout pi

yeniden başlatıyoruz.
sudo reboot

DENEMEYE BAŞLIYORUZ.

Yeni bir parmak eklemek için 
python /usr/share/doc/python-fingerprint/examples/example_enroll.py

Eklenen parmağı bulmak için
python /usr/share/doc/python-fingerprint/examples/example_search.py

Ekli parmağı silmek için
python /usr/share/doc/python-fingerprint/examples/example_delete.py

Taranan parmağın resmini indirmek için
python /usr/share/doc/python-fingerprint/examples/example_downloadimage.py


Daha sonra Terminalden çıkarak verdiğimiz BENDENKACAMAZSIN.py adlı kodumuzu çalıştırıyoruz.
