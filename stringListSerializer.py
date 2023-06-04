class StringListSerializer:
    """
    The StringListSerializer class provides methods to encode and decode a list of strings into a string representation.
    """
    def encode(self, stringList):
        """
        Encodes a list of strings into a string representation.
        
        Args:
            stringList (list): The list of strings to be encoded.
        
        Returns:
            str: The encoded string representation of the input list of strings.
        """
        encodedString = ""
        for s in stringList:
            encodedString += str(len(s)) + "#" + s
        return encodedString
    

    def decode(self, encodedString):
        """
        Decodes a string representation into a list of strings.
        
        Args:
            encodedString (str): The string to be decoded.
        
        Returns:
            list: The decoded list of strings.
        """
        i = 0
        ret = []

        while (i < len(encodedString)):
            j = i
            while (encodedString[j] != '#'):
                j += 1
            
            size = int(encodedString[i : j])
            ret.append(encodedString[j + 1 : j + 1 + size])
            i = j + 1 + size
        return ret