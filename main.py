from stringListSerializer import StringListSerializer

def main():
    serializer = StringListSerializer()

    # Example usage
    string_list = ["apple", "banana", "cherry"]
    encoded_string = serializer.encode(string_list)
    print("Encoded string:", encoded_string)

    decoded_list = serializer.decode(encoded_string)
    print("Decoded list:", decoded_list)

if __name__ == "__main__":
    main()