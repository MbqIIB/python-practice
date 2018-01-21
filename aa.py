import random
def demo_string():
    stra = 'hello world'
    print stra.capitalize()
    print stra.replace('world','nowcoder')
    strb = '   \n\r hello nowcoder \r\n'
    print 11,strb.lstrip()
    print 2,strb.rstrip()
    strc = 'hello w'
    print 3,strc.startswith('hel')
    print 4,strc.endswith('x')

    print 5, stra + strb + strc
    print 6, len(stra)
    print 7, '_'.join(['a','b','c'])
    print 8, strc.split(' ')


def demo_operation():
    print 1,2+3,2*3,2/3
    print 2, True, not True
    print 2 << 2,2>>4

def demo_controlflow():
    for i in range(1,10,2):
        if i < 5:
            continue
            print i

def demo_dict():
    dicta = {4:16,1:1,2:4,3:9}
    print 1, dicta
    print 2, dicta.keys(), dicta.values()
    print 3, dicta.has_key(1),dicta.has_key(2)
    for key,values in dicta.items():
        print "key--values:",key,values
    def add(a,b):
        return a + b
    def sub(a,b):
        return a - b
    dictb = {'+':add,'-':sub}
    print dictb.get('-')(10,2)
    print dictb['+'](1,2)

    def mul(a,b):
        return a * b
    dictb['*'] = mul
    dictb.pop('*')
    del dictb['+']

    for key,values in dictb.items():
        print key,values
    print dictb

def demo_set():
    seta = (1,2,3)
    print 1,seta


class User:
    type = 'USER'
    def __init__(self,name,uid):
        self.name = name
        self.uid = uid
    def __repr__(self):
        return 'im ' + self.name + ' ' + str(self.uid)

class Admin(User):
    type = 'ADMIN'
    def __init__(self,name,uid,group):
        User.__init__(self,name,uid)
        self.group = group
    def __repr__(self):
        return 'im ' + self.name + ' ' + str(self.uid) + ' ' + self.group

def demo_random():
    print int(random.random() * 100)
    print random.randint(1,200)

if __name__ == '__main__':
    '''
    user1 = User('u1',1)
    print user1
    admin1 = Admin('a1',101,'g1')
    print admin1
    '''
    #demo_string()
    #demo_operation()
    #demo_controlflow()
    #demo_dict()
    #demo_set()
    demo_random()