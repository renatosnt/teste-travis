import unittest
from stringListSerializer import StringListSerializer

class TestStringListSerializer(unittest.TestCase):
    def setUp(self):
        self.serializer = StringListSerializer()

    def test_encode(self):
        string_list = ["apple", "banana", "cherry"]
        encoded_string = self.serializer.encode(string_list)
        self.assertEqual(encoded_string, "5#apple6#banana6#cherry")

    def test_decode(self):
        encoded_string = "5#apple6#banana6#cherry"
        decoded_list = self.serializer.decode(encoded_string)
        self.assertEqual(decoded_list, ["apple", "banana", "cherry"])
        
if __name__ == '__main__':
    unittest.main()