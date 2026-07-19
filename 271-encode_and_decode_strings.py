"""
271. Encode and Decode Strings
Solved
Medium
Topics
conpanies icon
Companies
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}
So Machine 1 does:

string encoded_string = encode(strs);
and Machine 2 does:

vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

You are not allowed to solve the problem using any serialize methods (such as eval).

 

Example 1:

Input: dummy_input = ["Hello","World"]
Output: ["Hello","World"]
Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);
Example 2:

Input: dummy_input = [""]
Output: [""]
"""

# time: O(n)
# space: O(n)

# non-ascii char

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return 'π'.join(strs)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        return s.split('π')

# time: O(n)
# space: O(n)

# escape char

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_string = ''
        for s in strs:
            encoded_string += s.replace('/','//') + '/:'
        return encoded_string
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded_string = []
        current_string = ''
        i = 0

        while i < len(s):
            if s[i:i+2] == '/:':
                decoded_string.append(current_string)
                current_string = ''
                i += 2
            elif s[i:i+2] == '//':
                current_string += '/'
                i += 2
            else:
                current_string += s[i]
                i += 1
        return decoded_string
     

# time: O(n)
# space: O(n)

# length checking

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_string = ''
        for s in strs:
            encoded_string += str(len(s)) + '/:' + s
        return encoded_string
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded_string = []
        current_string = ''
        i = 0

        while i < len(s):
            delim = s.find('/:', i)
            length = int(s[i:delim])
            str_ = s[delim+2:delim+2+length]
            decoded_string.append(str_)
            i = delim + 2 + length
        return decoded_string
     
        


