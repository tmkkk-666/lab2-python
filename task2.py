def filter_strings(filter_func, string_array):
    if filter_func is None:
        # Exclude strings with spaces
        filtered = list(filter(lambda s: " " not in s, string_array))
        
        # Exclude strings starting with 'a'
        filtered = list(filter(lambda s: not s.lower().startswith('a'), filtered))
        
        # Exclude strings with length less than 5: lambda s: len(s) >= 5
        result = list(filter(lambda s: len(s) >= 5, filtered))
        
        return result
    else:
        return list(filter(filter_func, string_array))

def main():
    """Main function for testing and output"""
    test_strings = [
        "python",           # normal string
        "Hello World",      # contains space
        "animal",           # starts with 'a'
        "flag",             # length < 5
        "beautiful day",    # contains space and length >= 5
        "ant",              # starts with 'a' and length < 5
        "a pig"             # starts with 'a' and contains space
    ]
    
    result = filter_strings(None, test_strings)
    print(result)

if __name__ == "__main__":
    main()

