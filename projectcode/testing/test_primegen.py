"""
This file has unit tests for prime_gen.py.
"""

import sys
import unittest
from unittest.mock import patch
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from projectcode.rsa.primegen import eratosieve, millerrabin, dobigprime

class TestPrimeGen(unittest.TestCase):
    """
    This class tests the prime number generation functions.
    """
    def test_eratosieve(self):
        """
        The method tests the sieve of eratosthenes function by calling the argument 30.
        """
        primes = eratosieve(30)
        self.assertEqual(primes, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

    def test_millerrabin(self):
        """
        We check the Miller Rabin Primality Test.
        """
        self.assertTrue(millerrabin(13))
        self.assertFalse(millerrabin(15))
        self.assertFalse(millerrabin(0))
        self.assertFalse(millerrabin(1))
        self.assertFalse(millerrabin(-5))

    @patch('projectcode.rsa.primegen.millerrabin')
    def test_dobigprime(self, mock_millerrabin):
        """
        Test if dobigprime generates a 1024-bit prime correctly.
        """
        primeknow = 501441072220541957049234065828634418715981667500176406110008358357312818303975503592374124439003466489623421219965617047865238357436470449985678224929607813401792599257942957628500427479741651492120812990181456350169359902364222796426403283814639365444660390268191198983085522679346586630169353736067
        mock_millerrabin.return_value = True
        
        bits = 1024
        bitraw = primeknow & ((1 << (bits - 1)) - 1) & ~1
        expected = bitraw | (1 << (bits - 1)) | 1
        
        with patch('random.getrandbits', return_value=bitraw):
            prime = dobigprime(bits)
            self.assertEqual(prime, expected)
            self.assertTrue(prime % 2 != 0)

    def test_bigcomposite(self):
        """
        We test Miller-Rabin with a composite number that is a product of two large primes.
        """
        p = 707234082546876263128579065501331592098806161112982685308310097787681520455067224070898546691593867560419709010543007505152058910816300669572279385643416241847844185767781527209446208882599738220041792778562498519019530480722015452327827901108898485274495562948946845501232650993290661736738666181311
        q = 707938787841940790461120032886364170736757918738998575941762378581533655433516521411840463755227319404102086601471570684513207209461339477674129166709421226635853743516567137976488523252817449039044104853949982505598304002372710740183429003987294114746624809489487812019212257928933473816911461526643
        composite = p * q

        self.assertFalse(millerrabin(composite))
        self.assertTrue(millerrabin(p))
        self.assertTrue(millerrabin(q))

    def test_bigprime(self):
        """
        This test is similar to the one above, it tests Miller-Rabin with a known large prime.
        """
        primeknow = 960505218615459804690730722853916775440121191289245066334043444092712905050020275817680435184842306740775571463004468604223141771760561199421665788623013108859118193815442888280382318937243437395715842395252529080349278950143089388715556815861099370378385769364565347226800227635779070720790830312693
        self.assertTrue(millerrabin(primeknow))
        self.assertFalse(millerrabin(primeknow + 2))

# pragma: no cover
if __name__ == "__main__":
    unittest.main()
