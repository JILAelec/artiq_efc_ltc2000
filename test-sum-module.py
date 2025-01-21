from migen import *
from migen.fhdl import verilog

class SumAndScale(Module):
    def __init__(self):
        self.inputs = [Signal((16, True)) for _ in range(4)]
        self.amplitudes = [Signal((16, False)) for _ in range(4)]  # Unsigned
        self.output = Signal((16, True))
        
        ###
        products = [Signal((16, True)) for _ in range(4)]
        for i in range(4):
            mult = Signal((32, True))
            self.sync += [
                mult.eq(self.inputs[i] * self.amplitudes[i]),
                products[i].eq(mult >> 16)
            ]
        
        sum_all = Signal((18, True))
        self.comb += sum_all.eq(products[0] + products[1] + products[2] + products[3])
        
        self.sync += [
            If(sum_all > 32767,
                self.output.eq(32767)
            ).Elif(sum_all < -32768,
                self.output.eq(-32768)
            ).Else(
                self.output.eq(sum_all)
            )
        ]

def test_bench():
    dut = SumAndScale()
    
    sample_data = [
        0x0000, 0x2120, 0x3fff, 0x5a81, 0x6ed9, 0x7ba2, 0x7fff, 0x7ba2, 0x6ed9, 0x5a81,
        0x3fff, 0x2120, 0x0000, 0xdee0, 0xc001, 0xa57f, 0x9127, 0x845e, 0x8001, 0x845e,
        0x9127, 0xa57f, 0xc001, 0xdee0
    ]

    def tb_generator():
        test_amplitudes = [0x4000, 0x8000]  # Test with 0.5 and 1.0 gain
        
        for amp in test_amplitudes:
            print(f"\nTesting with amplitude {amp:04x}")
            for i in range(4):
                yield dut.amplitudes[i].eq(amp)
            
            # Initialize pipeline
            for i in range(4):
                yield dut.inputs[i].eq(0)
            yield
            yield
            
            # Process all samples and collect outputs
            outputs = []
            for i in range(len(sample_data)):
                # Set current inputs
                for j in range(4):
                    yield dut.inputs[j].eq(sample_data[i])
                yield
                outputs.append((yield dut.output))
            
            # Get final outputs
            yield
            outputs.append((yield dut.output))
            yield
            outputs.append((yield dut.output))
            
            # Display with outputs shifted up to align with their inputs
            print("     Inputs                          Output")
            print("----------------------------------------")
            for i in range(len(sample_data)):
                if i < len(sample_data)-3:  # Regular output
                    print(f"{sample_data[i]:4x} {sample_data[i]:4x} {sample_data[i]:4x} {sample_data[i]:4x} {outputs[i+3]:4x}")
                else:  # Last three samples don't have corresponding outputs yet
                    print(f"{sample_data[i]:4x} {sample_data[i]:4x} {sample_data[i]:4x} {sample_data[i]:4x}    -")
    
    from migen.sim import run_simulation
    run_simulation(dut, tb_generator(), vcd_name="sum_and_scale.vcd")

if __name__ == "__main__":
    print("Converting to Verilog...")
    dut = SumAndScale()
    print(verilog.convert(dut, ios={*dut.inputs, *dut.amplitudes, dut.output}))
    print("\nRunning testbench...")
    test_bench()
