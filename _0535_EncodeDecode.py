class Codec:
    stored = dict()
    counter = 0

    def encode(self, longUrl: str) -> str:
        tiny = self.counter
        self.stored[self.counter]=longUrl
        self.counter+=1
        return "stupidURL.de/"+str(tiny)
        
    def decode(self, shortUrl: str) -> str:
        return self.stored[int(shortUrl.split('/')[1])]
    
codec = Codec()
url = "https://dawidklimont.github.io/"
short = codec.encode(url)
print(short)
print(codec.decode(short))