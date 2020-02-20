
class SignalSlot(object):

    def __init__(self):
        self._SSPool = {};

    def connect(self, signal, slot):
        if(signal not in self._SSPool):
            self._SSPool[signal] = [];
        if(slot not in self._SSPool[signal]):
            self._SSPool[signal] += [slot];

    def emit(self, signal, args):
        if(signal in self._SSPool):
            slots = self._SSPool[signal];
            for i in range(len(slots)):
                slots[i](*args);

class Interface(SignalSlot):

    #signals
    def ValueChanged(self):
        self.emit("ValueChanged", ());
    def InputDone(self, text):
        self.emit("InputDone", (text,));
    def Scroll(self, x, y):
        self.emit("Scroll", (x, y));

class User(object):

    #slots
    def ValueChanged(self):
        # print(self);
        print("ValueChanged-User");
    def InputDone(self, text):
        # print(self);
        print("InputDone-User the text is:", text);
    def Scroll(self, x, y):
        # print(self);
        print("Scroll-User go to (%d:%d)" % (x, y));



inf = Interface();
user1 = User();
user2 = User();

inf.connect("ValueChanged", user1.ValueChanged);
inf.connect("ValueChanged", user1.ValueChanged);
inf.connect("ValueChanged", user2.ValueChanged);
inf.connect("InputDone", user1.InputDone);
inf.connect("Scroll", user2.Scroll);

inf.ValueChanged();
inf.InputDone("my name is Tim");
inf.Scroll(100, 200);

