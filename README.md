# ARTIQ Development

To develop ARTIQ, navigate to the ARTIQ folder and run the following command:

    nix develop

Next, use the local copy of MiSoC, Migen and Artiq by exporting the `PYTHONPATH`:

    export PYTHONPATH="/home/artiq/artiq_and_co/migen:$PYTHONPATH"
    export PYTHONPATH="/home/artiq/artiq_and_co/misoc:$PYTHONPATH"
    export PYTHONPATH="/home/artiq/artiq_and_co/artiq:$PYTHONPATH"

Check out the modified activate script in this repository to see how to add
local folders to be loaded with the venv automatically.

## Building a 100 MHz Kasli/EFC pair for LTC project

    python kasli.py kasli_shuttler_100MHz.json
    python efc.py --drtio100mhz --variant blank

### Then make flash storage images

    artiq_mkfs flash_storage_blank.img
    artiq_mkfs flash_storage_int_125.img -s rtio_clock int_125
    artiq_mkfs flash_storage_ext0_synth0_10to100.img -s rtio_clock ext0_synth0_10to100

### Flashing the boards, making sure flash image does not contain any old settings for DRTIO

    artiq_flash --srcbuild -d artiq_kasli_100MHz/shuttlerdemo/
    artiq_flash -f flash_storage_ext0_synth0_10to100.img storage start
    artiq_flash -t efc1v1 --srcbuild -d artiq_efc_100MHz/blank/
    artiq_flash -t efc1v1 -f flash_storage_blank.img storage start
