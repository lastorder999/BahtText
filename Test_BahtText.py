import unittest
from BahtText import bahtText


class TestBahtText(unittest.TestCase):
    def testZeroDigits(self):
        self.assertEqual(bahtText(0), 'ศูนย์บาทถ้วน')
        self.assertEqual(bahtText(0.0), 'ศูนย์บาทถ้วน')
        self.assertEqual(bahtText(00.000000), 'ศูนย์บาทถ้วน')

    def testOneDigits(self):
        self.assertEqual(bahtText(1), 'หนึ่งบาทถ้วน')
        self.assertEqual(bahtText(3), 'สามบาทถ้วน')
        self.assertEqual(bahtText(6), 'หกบาทถ้วน')
        self.assertEqual(bahtText(9), 'เก้าบาทถ้วน')

    def testTenDigits(self):
        self.assertEqual(bahtText(37), 'สามสิบเจ็ดบาทถ้วน')
        self.assertEqual(bahtText(48), 'สี่สิบแปดบาทถ้วน')
        self.assertEqual(bahtText(50), 'ห้าสิบบาทถ้วน') 

    def testHundredDigits(self):
        self.assertEqual(bahtText(100), 'หนึ่งร้อยบาทถ้วน')
        self.assertEqual(bahtText(232), 'สองร้อยสามสิบสองบาทถ้วน')
        self.assertEqual(bahtText(317), 'สามร้อยสิบเจ็ดบาทถ้วน')
        self.assertEqual(bahtText(474), 'สี่ร้อยเจ็ดสิบสี่บาทถ้วน')

    def testThousandDigits(self):
        self.assertEqual(bahtText(3333), 'สามพันสามร้อยสามสิบสามบาทถ้วน')  
        self.assertEqual(bahtText(5789), 'ห้าพันเจ็ดร้อยแปดสิบเก้าบาทถ้วน')
        self.assertEqual(bahtText(50947), 'ห้าหมื่นเก้าร้อยสี่สิบเจ็ดบาทถ้วน')
        self.assertEqual(bahtText(63147), 'หกหมื่นสามพันหนึ่งร้อยสี่สิบเจ็ดบาทถ้วน')
        self.assertEqual(bahtText(474289), 'สี่แสนเจ็ดหมื่นสี่พันสองร้อยแปดสิบเก้าบาทถ้วน')

    def testMillionAndBillion(self):
        self.assertEqual(bahtText(9872346), 'เก้าล้านแปดแสนเจ็ดหมื่นสองพันสามร้อยสี่สิบหกบาทถ้วน')
        self.assertEqual(bahtText(12000000), 'สิบสองล้านบาทถ้วน')
        self.assertEqual(bahtText(21000000), 'ยี่สิบเอ็ดล้านบาทถ้วน')
        self.assertEqual(bahtText(501100098), 'ห้าร้อยหนึ่งล้านหนึ่งแสนเก้าสิบแปดบาทถ้วน')
        self.assertEqual(bahtText(1018763451), 'หนึ่งพันสิบแปดล้านเจ็ดแสนหกหมื่นสามพันสี่ร้อยห้าสิบเอ็ดบาทถ้วน')
        self.assertEqual(bahtText(98365419364), 'เก้าหมื่นแปดพันสามร้อยหกสิบห้าล้านสี่แสนหนึ่งหมื่นเก้าพันสามร้อยหกสิบสี่บาทถ้วน')
        self.assertEqual(
            bahtText(51000000000000.51), 'ห้าสิบเอ็ดล้านล้านบาทห้าสิบเอ็ดสตางค์')
        self.assertEqual(
            bahtText(10000000680000.51), 'สิบล้านล้านหกแสนแปดหมื่นบาทห้าสิบเอ็ดสตางค์')
        self.assertEqual(bahtText(1234567890123450), 'หนึ่งพันสองร้อยสามสิบสี่ล้านห้าแสนหกหมื่นเจ็ดพันแปดร้อยเก้าสิบล้านหนึ่งแสนสองหมื่นสามพันสี่ร้อยห้าสิบบาทถ้วน')
        

    def testDigitEndWithOne(self):
        self.assertEqual(bahtText(11), 'สิบเอ็ดบาทถ้วน')
        self.assertEqual(bahtText(101), 'หนึ่งร้อยเอ็ดบาทถ้วน')
        self.assertEqual(bahtText(201), 'สองร้อยเอ็ดบาทถ้วน')
        self.assertEqual(bahtText(1001), 'หนึ่งพันเอ็ดบาทถ้วน')
        self.assertEqual(bahtText(5011), 'ห้าพันสิบเอ็ดบาทถ้วน')
        self.assertEqual(bahtText(3061.21), 'สามพันหกสิบเอ็ดบาทยี่สิบเอ็ดสตางค์')

    def testDigitEndWithTwenty(self):
        self.assertEqual(bahtText(20), 'ยี่สิบบาทถ้วน')
        self.assertEqual(bahtText(2024), 'สองพันยี่สิบสี่บาทถ้วน')
        self.assertEqual(bahtText(87621), 'แปดหมื่นเจ็ดพันหกร้อยยี่สิบเอ็ดบาทถ้วน')
        self.assertEqual(bahtText(57.23), 'ห้าสิบเจ็ดบาทยี่สิบสามสตางค์')
        self.assertEqual(bahtText(422.26),'สี่ร้อยยี่สิบสองบาทยี่สิบหกสตางค์')

    def testGeneralDigits(self):
        self.assertEqual(bahtText(1.02), 'หนึ่งบาทสองสตางค์')
        self.assertEqual(bahtText(32.23), 'สามสิบสองบาทยี่สิบสามสตางค์')
        self.assertEqual(bahtText(474.45), 'สี่ร้อยเจ็ดสิบสี่บาทสี่สิบห้าสตางค์')
        self.assertEqual(bahtText(63147.89), 'หกหมื่นสามพันหนึ่งร้อยสี่สิบเจ็ดบาทแปดสิบเก้าสตางค์')

    def testMoreThan2Decimal(self):
        self.assertEqual(bahtText(0.87623), 'แปดสิบแปดสตางค์')
        self.assertEqual(bahtText(21.12978), 'ยี่สิบเอ็ดบาทสิบสามสตางค์')
        self.assertEqual(bahtText(7509.02734), 'เจ็ดพันห้าร้อยเก้าบาทสามสตางค์')
        self.assertEqual(bahtText(23.9874), 'ยี่สิบสามบาทเก้าสิบเก้าสตางค์')
        
    def testLessThanOne(self):
        self.assertEqual(bahtText(0.21), 'ยี่สิบเอ็ดสตางค์')
        self.assertEqual(bahtText(0.5), 'ห้าสิบสตางค์')
        self.assertEqual(bahtText(0.18),'สิบแปดสตางค์')
        self.assertEqual(bahtText(0.69), 'หกสิบเก้าสตางค์')

    def testNagativeDigits(self):
        self.assertEqual(bahtText(-1.10), 'ลบหนึ่งบาทสิบสตางค์')
        self.assertEqual(bahtText(-0.69), 'ลบหกสิบเก้าสตางค์')
        self.assertEqual(bahtText(-1000.0), 'ลบหนึ่งพันบาทถ้วน')
        self.assertEqual(
            bahtText(-258065.81), 'ลบสองแสนห้าหมื่นแปดพันหกสิบห้าบาทแปดสิบเอ็ดสตางค์')

if __name__ == "__main__":
    unittest.main()