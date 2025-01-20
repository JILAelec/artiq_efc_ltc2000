from artiq.experiment import *
from artiq.language.units import us, ms

class DAC_Init(EnvExperiment):
    MHz = 1e6

    def build(self):
        self.setattr_device("core")
        self.setattr_device("ttl0")
        self.setattr_device("ltc_trigger")
        self.setattr_device("ltc_dds0")
        self.setattr_device("ltc_clear")

    @kernel
    def run(self):
        self.core.reset()
        self.ttl0.output()
        delay(20000*us)
        self.ltc_clear.clear(1)
        # self.ltc_dds0.set_waveform(0, 0, 0, 0, 0, 286331153, 0) #0x11111111
        self.ltc_dds0.set_waveform(0, 0, 0, 0, 0, 0x01000000, 0)
        # self.ltc_dds0.set_waveform(0, 0, 0, 0, 0, 0x0000FFFF, 0)
        #self.ltc_dds0.set_waveform(0, 0, 0, 0, 0, 0, 0)
        # self.ltc_dds0.set_waveform(0, 0, 0, 0, 0, 0x0000FFFF, 0x1)
        self.ltc_trigger.trigger(1)
        delay(1000*us)
        self.ltc_clear.clear(0)