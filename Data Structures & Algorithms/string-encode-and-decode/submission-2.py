class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []
        for s in strs:
            parts.append(f'{len(s)}#{s}')
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        index = 0
        result = []
        while index < len(s):
            j = index
            while s[j] != '#':
                j += 1
            start_index = j + 1
            length = int(s[index:j])
            end_index = start_index + length
            result.append(s[start_index:end_index])
            index = end_index
        return result
