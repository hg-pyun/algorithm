# https://algospot.com/judge/problem/read/HELLOWORLD
limit = int(input())
words = []

for i in range(limit):
    words.append(input())

def get_hello(word):
    print("Hello, " + word + "!")

list(map(get_hello, words))