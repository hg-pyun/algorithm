# https://algospot.com/judge/problem/read/HELLOWORLD
limit = int(input())
words = []

for i in range(0, limit):
    words.append(input())

def get_hello(word):
    return "Hello, " + word + "!"

hello_worlds = map(get_hello, words)

for word in hello_worlds:
    print(word)