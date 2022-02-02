# check if a given number is a palindrome (number is the same read from left or right)

def palindrome(x):
    print(str(x) == str(x)[::-1])
    return str(x) == str(x)[::-1]

if __name__ == "__main__":
    x = 129
    palindrome(x)
