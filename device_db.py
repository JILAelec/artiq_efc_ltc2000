
# Autogenerated for the shuttlerdemo variant
core_addr = "192.168.7.75"

device_db = {
    "core": {
        "type": "local",
        "module": "artiq.coredevice.core",
        "class": "Core",
        "arguments": {
            "host": core_addr,
            "ref_period": 1.25e-09,
            "analyzer_proxy": "core_analyzer",
            "target": "rv32g",
            "satellite_cpu_targets": {}
        },
    },
    "core_log": {
        "type": "controller",
        "host": "::1",
        "port": 1068,
        "command": "aqctl_corelog -p {port} --bind {bind} " + core_addr
    },
    "core_moninj": {
        "type": "controller",
        "host": "::1",
        "port_proxy": 1383,
        "port": 1384,
        "command": "aqctl_moninj_proxy --port-proxy {port_proxy} --port-control {port} --bind {bind} " + core_addr
    },
    "core_analyzer": {
        "type": "controller",
        "host": "::1",
        "port_proxy": 1385,
        "port": 1386,
        "command": "aqctl_coreanalyzer_proxy --port-proxy {port_proxy} --port-control {port} --bind {bind} " + core_addr
    },
    "core_cache": {
        "type": "local",
        "module": "artiq.coredevice.cache",
        "class": "CoreCache"
    },
    "core_dma": {
        "type": "local",
        "module": "artiq.coredevice.dma",
        "class": "CoreDMA"
    },

    "i2c_switch0": {
        "type": "local",
        "module": "artiq.coredevice.i2c",
        "class": "I2CSwitch",
        "arguments": {"address": 0xe0}
    },
    "i2c_switch1": {
        "type": "local",
        "module": "artiq.coredevice.i2c",
        "class": "I2CSwitch",
        "arguments": {"address": 0xe2}
    },
}

# master peripherals

device_db["ttl0"] = {
    "type": "local",
    "module": "artiq.coredevice.ttl",
    "class": "TTLInOut",
    "arguments": {"channel": 0x000000},
}

device_db["ttl1"] = {
    "type": "local",
    "module": "artiq.coredevice.ttl",
    "class": "TTLInOut",
    "arguments": {"channel": 0x000001},
}

device_db["ttl2"] = {
    "type": "local",
    "module": "artiq.coredevice.ttl",
    "class": "TTLInOut",
    "arguments": {"channel": 0x000002},
}

device_db["ttl3"] = {
    "type": "local",
    "module": "artiq.coredevice.ttl",
    "class": "TTLInOut",
    "arguments": {"channel": 0x000003},
}

device_db["ttl4"] = {
    "type": "local",
    "module": "artiq.coredevice.ttl",
    "class": "TTLOut",
    "arguments": {"channel": 0x000004},
}

device_db["ttl5"] = {
    "type": "local",
    "module": "artiq.coredevice.ttl",
    "class": "TTLOut",
    "arguments": {"channel": 0x000005},
}

device_db["ttl6"] = {
    "type": "local",
    "module": "artiq.coredevice.ttl",
    "class": "TTLOut",
    "arguments": {"channel": 0x000006},
}

device_db["ttl7"] = {
    "type": "local",
    "module": "artiq.coredevice.ttl",
    "class": "TTLOut",
    "arguments": {"channel": 0x000007},
}

device_db["led0"] = {
    "type": "local",
    "module": "artiq.coredevice.ttl",
    "class": "TTLOut",
    "arguments": {"channel": 0x000008}
}

device_db["led1"] = {
    "type": "local",
    "module": "artiq.coredevice.ttl",
    "class": "TTLOut",
    "arguments": {"channel": 0x000009}
}

device_db["led2"] = {
    "type": "local",
    "module": "artiq.coredevice.ttl",
    "class": "TTLOut",
    "arguments": {"channel": 0x00000a}
}

# DEST#4 peripherals

device_db["core"]["arguments"]["satellite_cpu_targets"][4] = "rv32g"

device_db["shuttler0_led0"] = {
    "type": "local",
    "module": "artiq.coredevice.ttl",
    "class": "TTLOut",
    "arguments": {"channel": 0x040000}
}

device_db["shuttler0_led1"] = {
    "type": "local",
    "module": "artiq.coredevice.ttl",
    "class": "TTLOut",
    "arguments": {"channel": 0x040001}
}

# SPI master for LTC2000
device_db["spi_ltc"] = {
    "type": "local",
    "module": "artiq.coredevice.spi2",
    "class": "SPIMaster",
    "arguments": {"channel": 0x040002}
}

device_db["ltc_dds0"] = {
    "type": "local",
    "module": "artiq.coredevice.ltc2000",
    "class": "DDS",
    "arguments": {"channel": 0x040003},
}

device_db["ltc_dds1"] = {
    "type": "local",
    "module": "artiq.coredevice.ltc2000",
    "class": "DDS",
    "arguments": {"channel": 0x040004},
}

device_db["ltc_dds2"] = {
    "type": "local",
    "module": "artiq.coredevice.ltc2000",
    "class": "DDS",
    "arguments": {"channel": 0x040005},
}

device_db["ltc_dds3"] = {
    "type": "local",
    "module": "artiq.coredevice.ltc2000",
    "class": "DDS",
    "arguments": {"channel": 0x040006},
}

device_db["ltc_trigger"] = {
    "type": "local",
    "module": "artiq.coredevice.ltc2000",
    "class": "Trigger",
    "arguments": {"channel": 0x040007},
}

device_db["ltc_clear"] = {
    "type": "local",
    "module": "artiq.coredevice.ltc2000",
    "class": "Clear",
    "arguments": {"channel": 0x040008},
}

device_db["ltc_reset"] = {
    "type": "local",
    "module": "artiq.coredevice.ltc2000",
    "class": "Reset",
    "arguments": {"channel": 0x040009},
}

device_db["ltc_gain"] = {
    "type": "local",
    "module": "artiq.coredevice.ltc2000",
    "class": "Gain",
    "arguments": {"channel": 0x040008},
}

