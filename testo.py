from mimetypes import init



class bot:
    demo=50


    def inc(self):
        self.demo=100

class testo(bot):
    
    def inc(self):
        self.i=2
        return super().inc()
    

 

    def test(self):
        print(self.i)

d=testo()
d.inc()
print(d.i)