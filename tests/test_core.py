import unittest
import os
import shutil
from src.utils.crypto_seal import CryptoSeal
from src.core.bunker import Bunker

class TestKiyametCore(unittest.TestCase):
    
    def setUp(self):
        # Create a temp bunker for testing
        self.test_dir = "test_bunker_log"
        self.bunker = Bunker(location=self.test_dir)

    def tearDown(self):
        # Clean up
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_crypto_seal_integrity(self):
        """Test that seal generation and verification works."""
        data = "TEST_VECTOR_123"
        seal = CryptoSeal.generate_seal(data)
        self.assertTrue(CryptoSeal.verify_seal(data, seal))
        
    def test_crypto_seal_tamper(self):
        """Test that tampering breaks the seal."""
        data = "SECURE_DATA"
        seal = CryptoSeal.generate_seal(data)
        self.assertFalse(CryptoSeal.verify_seal("TAMPERED_DATA", seal))

    def test_bunker_storage(self):
        """Test writing to and reading from Bunker."""
        filename = "secret_plans.json"
        content = "THE EAGLE HAS LANDED"
        
        self.bunker.secure_log(filename, content)
        retrieved = self.bunker.retrieve_log(filename)
        
        self.assertIn("THE EAGLE HAS LANDED", retrieved)
        self.assertIn("[VERIFIED]", retrieved)

if __name__ == '__main__':
    unittest.main()
