#PARMAKİZİİÇİN

from pyfingerprint.pyfingerprint import PyFingerprint
# Set fingerprint sensor to ttyUSB0 with buadrate 57600
fingerprintSensor = PyFingerprint(
    '/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
# Flag for checking sensor available
fingerprintSensorStateFlag = False

i=0

while True:
    
    def verify():
        # Verify fingerprintsensor
        global fingerprintSensorStateFlag
        try:
            if(fingerprintSensor.verifyPassword() is False):
                print('Parmak izi okuyucu hatası!')

            fingerprintSensorStateFlag = True
            print('Parmakizi okuyucu kullanılabilir!')
        except Exception as e:
            print('Birşeyler Ters Gitti 1: ' + str(e))


    def scan():
        if(fingerprintSensorStateFlag):
            try:
                print('Parmak bekleniyor...')
                # wait for finger
                while(fingerprintSensor.readImage() is False):
                    pass

                # save fingerprint image
                print('Parmakizi kaydediliyor...')
                fingerprintSensor.downloadImage(
                '/home/pi/Documents/parmakiziokuma/parmakizi{}_img.bmp'.format(i))
                print('Parmakizi kaydedildi!')
                
                
            except Exception as e:
                print('Birşeyler ters gitti : ' + str(e))

    i+=1
    def main():
        verify()
        scan()

    if __name__ == '__main__':
        main()

#RENK SENSÖRÜ İÇİN
import RPi.GPIO as GPIO
import time

