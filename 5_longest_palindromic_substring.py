import unittest

def is_palindrome(s: str) -> bool:
    length = len(s)

    if length == 0:
        return False
    if length == 1:
        return True

    if length % 2 == 0:
        return s[:length // 2] == s[length//2::][::-1]
    else:
        return s[:(length//2)] == s[(length//2)+1:][::-1]


def longest_palindromic_substring(s):
    if len(s) == 1:
        return s
    if len(s) == 2:
        return s if is_palindrome(s) else s[0]
    if is_palindrome(s):
        return s

    result = ""

    for i in range(len(s)):
        for j in range(len(s)):
            if is_palindrome(s[i:j+1]):
                if len(s[i:j+1]) > len(result):
                    result = s[i:j+1]

    return result
#
# print(longest_palindromic_substring("babad"))
# print(longest_palindromic_substring("cbbd"))
# print(longest_palindromic_substring("s"))
# print(longest_palindromic_substring("ac"))
# print(longest_palindromic_substring("bb"))
# print(longest_palindromic_substring("abb"))
# print(longest_palindromic_substring("cstgvkbrxacmpxdxxktktvpdzcuxmnhvuxdgsmskgeeawzeikhtmhdvnccbrgifpzmiuytfmeyfoxsntrdtxeuxcqsndexbgfxnthqwveujqzemloooyddparbjcuiwpopjwvvmwblsamkhjhlnoxinkpsempexmipifsfwzxbetgvfnkngzxcpizwctpdlpngjpyovmjllxfiwktghkxvyelwjwdztujmunijfsfdvmhgqhlpouewgyznphlmccjmqaqncwbeqheohibafqfunfywmrvqvjygjwqoclijwkcfiuaiymeagdbwyejnvtosxylptbtyoahfzfmwzrkhzdamknleroffmsqcaryibamgdpcumlhrblypddzhaxfeztokgogzgvpfvlmetiwsamhdidmvxavleryfyakendwrbslcavlqkerrnvpuzhdgwzuyorxzbkzhxhpbvkflgxouvaavxrdzsjlgrmogzvlhhdidldsxqhrqlryaanffhxnutcycnczuedtrwcnfiqrtoafvdfnfhxhyjivzalozrbrajboecfyalisxxanduzraqdrbzsbkobaieqpzcawrunxucypqyjnmrlrlivrrwwhdpekeelsphhunzbhkkejvqfopjsuholutgmtnleqdrntbqgrobnuhqpdkbjtikijkdiwqvnxgajaaqgswrdamzv"
# ))


class Tests(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertEqual(is_palindrome(""), False)
        self.assertEqual(is_palindrome("bb"), True)
        self.assertEqual(is_palindrome("abcd"), False)
        self.assertEqual(is_palindrome("abba"), True)
        self.assertEqual(is_palindrome("abcba"), True)

    def test_longest_palindromic_substring(self):
        self.assertEqual(longest_palindromic_substring("babad"), "bab")
        self.assertEqual(longest_palindromic_substring("abcd"), "a")
        self.assertEqual(longest_palindromic_substring("s"), "s")
        self.assertEqual(longest_palindromic_substring("ac"), "a")
