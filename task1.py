def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def main():
    print(is_palindrome("Madam"))   
    print(is_palindrome("hello"))  

if __name__ == "__main__":
    main()
