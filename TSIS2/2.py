class Solution:
    def interpret(self, command: str) -> str:
        x = command.replace("()","o")
        y=x.replace("(al)","al")
        return y