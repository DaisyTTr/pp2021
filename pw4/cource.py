class Cource:
    def __init__(self, ci, cn):
        self.cname = cn
        self.cid = ci

    def get_cn(self):
        return self.cname

    def get_ci(self):
        return self.cid

    def cource_des(self):
        print("Cource Name",self.cname)
        print("Cource Id: ",self.cid)
    
    def __str__(self):
        return f"Cource name is:{self.cname}, Cource Id is: {self.cid} ."

