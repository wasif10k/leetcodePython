class Solution:
    def interpret(self, command: str) -> str:
        output = ""
        for i in range(len(command)):
            if command[i] == "G":
                output += "G"
            elif command[i] == "(" and command[i + 1] == ")":
                output += "o"
            elif command[i] == "(" and command[i + 1] == "a":
                output += "al"
        return output;

