if __name__ == '__main__':
    s = input()
    print(any(char.isalnum()for char in s))
    print(any(char.isalpha()for char in s))