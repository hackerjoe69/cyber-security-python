import phonenumbers

def main():
    number_input = input("Enter a phone number with country code : ").strip()
    
    try:
        number = phonenumbers.parse(number_input, None)
        is_valid = phonenumbers.is_valid_number(number)
        print(f"✅ Valid Number: {is_valid}")
    except phonenumbers.NumberParseException as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
