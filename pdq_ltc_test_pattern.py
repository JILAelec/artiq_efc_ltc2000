from artiq.experiment import *
from artiq.coredevice.spi2 import SPI_END
from artiq.language.units import ms

class DAC_Init(EnvExperiment):
    MHz = 1e6

    def build(self):
        self.setattr_device("core")
        self.setattr_device("ttl0")
        self.setattr_device("spi_ltc")
        self.spi_config = SPI_END

    @kernel
    def run(self):
        self.core.reset()
        self.ttl0.output()
        delay(20*ms)
        print("Performing software reset...")
        self.spi_write(0x01, 0x01)  # Write 1 to the reset bit
        delay(10*ms)  # Wait for reset to complete
        self.spi_write(0x01, 0x00)  # Clear the reset bit
        delay(20*ms)
        # Simply adding one sample here to get f/64 blips out of the LTC2000
        self.spi_write(0x1F, 0x55)  # Pattern generator data
        self.spi_write(0x1F, 0x55)  # Pattern generator data
        delay(10*ms)
        self.spi_write(0x1E, 0x1)  # Pattern generator enable
        delay(10*ms)
        self.spi_write(0x04, 0x8)  # Data input controls

    @kernel
    def spi_write(self, addr, data):
        self.spi_ltc.set_config_mu(self.spi_config, 32, 256, 0b0001)
        delay(20*us)
        self.spi_ltc.write((addr << 24) | (data << 16))
        delay(2*us)
        self.spi_ltc.set_config_mu(self.spi_config, 32, 256, 0b0000)
        delay(20000*us)
        # print("SPI Write - Addr:", addr, "Data:", data)