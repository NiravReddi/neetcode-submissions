class Solution:

    def encode(self, strs: List[str]) -> str:
        r=""
        for i in strs:
            r+=" # "+i
        return r

    def decode(self, s: str) -> List[str]:
        l=list(s.split(" # "))
        l.pop(0)
        return l
