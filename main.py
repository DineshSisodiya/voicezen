#author : Dinesh Kumar Sisoidya
import random
import time

# constants
CHARS_TO_BE_READ = 3000
ONE_GB_IN_BYTES = 4000#pow(10,9)

def write_file():
    # t0=time.time() 
    file = open("random_text.txt", "a+")
    if file:
        characters = 'abcdefghijklmnopqrstuvwxyz'
        single_write_size = ONE_GB_IN_BYTES #1gb
        write_size = 3 * ONE_GB_IN_BYTES #3gb
        random_str = ''
        for i in range(1, write_size+1):
            index = random.randint(0,25)
            random_str += characters[index]
            if i % single_write_size == 0:
                file.write(random_str)
                random_str = ''
        # d=time.time()-t0
        # print("duration: %.2f s." % d)
        return True
    else:
        return False

def read_char(n):
    str = ""
    file = open("random_text.txt", "r")
    if n >= 0 and file is not None:
        str = file.read(n)
    return str

# score calculation formula 
formula = lambda length, freq: length * length * pow(freq - 1, 0.33)

class TrieNode:
    def __init__(self, value): 
        self.value = value
        self.freq = 1
        self.next = {}
        self.parent = None

    def insert(self, str):
        cur = self
        for char in str:
            if char in cur.next:
                cur = cur.next[char]
                cur.freq += 1
            else:
                cur.next[char] = TrieNode(char)
                cur.next[char].parent = cur
                cur = cur.next[char]

def dfs(node):
    #store node with depth
    stack = [[node, 0]]
    #answer value and answer node
    ans = {
        "score": 0,
        "node": node,
    }

    while len(stack):
        [currentNode, depth] = stack.pop()
        score = formula(depth, currentNode.freq)
        if (score > ans["score"]):
            ans["score"] = score
            ans["node"] = currentNode
        for nextNode in currentNode.next.values():
            stack.append([nextNode, depth + 1])

    return ans

def find_highest_scored_string():
    print("--calculating highest scroed string--")
    # intialize root node for trie
    root = TrieNode("$")

    # read first N chars
    str = read_char(CHARS_TO_BE_READ)
    
    # insert substrings into trie
    for i in range(len(str)) :
        sub_str = str[i:]
        root.insert(sub_str)

    # traverse trie to find that string
    result = dfs(root)
    resultString = "";
    
    # reconstruct string
    node = result["node"]
    while (node.value != "$"):
        resultString += node.value
        node = node.parent

    resultString = resultString[::-1]
    return {"string": resultString, "score": result["score"]}


def main():
    # print instructions
    print("Enter number from given choices:")
    print("  1 : Write 3gb Random text File")
    print("  2 : Find Substring with Highest Score")
    print("  0 : Exit")
    
    while True:
        choice = int(input("\nYour choice : "))
        if choice == 0:
            print("finished.")
            exit()
        elif choice == 1:
            print("...writing data to file... please wait.")
            written = write_file()
            if written:
                print('file written successfully.')
            else:
                print("failed to open file for writing.")
        elif choice == 2:
            result = find_highest_scored_string()
            print("Substring with highest score %d is :: %s" %(result['score'], result['string']))
        else:
            print("Invalid choice. please select from given choices")

# start execution
main()