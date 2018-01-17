import usbtmc

class Bkp8600(object):
    Instrument = None

    # Init. if resource (i.e. "USB::65535::34816::602197010707610021::INSTR" is not set auto detect is tried)
    def __init__(self, resource=None):
        if resource is not None:
            self.Instrument = usbtmc.Instrument(resource)
        else:
            for r in usbtmc.list_resources():
                tmpIntrument = usbtmc.Instrument(str(r))
                if tmpIntrument.ask("*IDN?").startswith("B&K Precision, 8600"):
                    self.Instrument = tmpIntrument
                    break

    def getDescription(self):
        return self.Instrument.ask("*IDN?")

    def getCurrent(self):
        return self.Instrument.ask("current?")

    def getVoltage(self):
        return self.Instrument.ask("voltage?")

    def measureCurrent(self):
        return self.Instrument.ask(":MEASure:current?")

    def measureVoltage(self):
        return self.Instrument.ask(":MEASure:VOLTage?")

    def initialize(self):
        self.Instrument.write("SYSTem:REMote")
        self.Instrument.write("INPut OFF")
        self.Instrument.write("*RST")
        self.Instrument.write("*CLS")
        self.Instrument.write("*SRE 0")
        self.Instrument.write("*ESE 0")

    def setCurrent(self, current):
        print "current "+str(current)
        self.Instrument.write("INPut ON")
        self.Instrument.write("CURRent "+str(current))

    def getError(self):
        self.Instrument.ask("SYSTem:ERRor?")

    def getFunction(self):
        return self.Instrument.write("SYSTem:REMote")

    def resetDeviceToManual(self):
        self.Instrument.write("INPut OFF")
        self.Instrument.write("SYSTem:LOCal")

if __name__ == '__main__':
    #last = Bkp8600(resource="USB::65535::34816::602197010707610021::INSTR")
    last = Bkp8600()
    #print last.getDescription()
    #print last.getCurrent()
    #print last.getVoltage()
    #print last.measureVoltage()
    #print last.measureCurrent()
    #
    last.initialize()
    #last.setCurrent(1)
    #print last.getError()
    #print last.getFunction()
    #last.setCurrent(1)
    #print last.getError()
    #print last.getCurrent()
