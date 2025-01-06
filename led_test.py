from artiq.experiment import *
from artiq.language.units import us, ms

class DAC_Init(EnvExperiment):

    def build(self):
        self.setattr_device("core")
        self.setattr_device("ttl0")
        self.setattr_device("ttl1")
        self.setattr_device("led1")
        self.setattr_device("led2")
        self.setattr_device("led3")

    @kernel
    def run(self):
        self.core.reset()
        while True:
            self.led1.pulse(100*ms)
            self.led2.pulse(100*ms)
            self.led3.pulse(100*ms)
            self.ttl0.pulse(100*ms)
            self.ttl1.pulse(100*ms)
            delay(100*ms)