class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []
        for s in strs:
            parts.append(f'{len(s)}#{s}')
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        index = 0
        strs = []
        while index < len(s):
            j = index
            while s[j] != '#':
                j += 1
            length = int(s[index:j])
            start_index = j + 1
            end_index = start_index + length

            item = s[start_index:end_index]
            strs.append(item)
            index = end_index
        return strs