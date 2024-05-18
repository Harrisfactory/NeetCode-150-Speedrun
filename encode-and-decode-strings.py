class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoder = '--msg-->'
        encoded_msg = ''
        for i in range(len(strs)-1):
            encoded_msg += strs[i] + encoder
        encoded_msg += strs[-1]
        return encoded_msg

        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        s = s.split('--msg-->')
        return s