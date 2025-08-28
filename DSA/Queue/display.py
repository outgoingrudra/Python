class Queue:
    def __init__(self):
        self.q=[]
    def disp(self):
        print(" -> ".join(map(str,self.q)))

qq=Queue()
qq.q=[9,8,7]
qq.disp()
