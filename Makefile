# Configuration
REMOTE_HOST ?= artiq
REMOTE_PATH ?= /home/artiq/artiq/artiq/gateware/targets/artiq_efc
VARIANT ?= ltc
LOCAL_DIR ?= build_$(VARIANT)

# Directory structure
DIRS = $(LOCAL_DIR)/gateware \
       $(LOCAL_DIR)/software/bootloader \
       $(LOCAL_DIR)/software/satman

.PHONY: all clean dirs fetch

all: dirs fetch

dirs:
	mkdir -p $(DIRS)

fetch: dirs
	scp $(REMOTE_HOST):$(REMOTE_PATH)/$(VARIANT)/gateware/top.bit $(LOCAL_DIR)/gateware/top.bit
	scp $(REMOTE_HOST):$(REMOTE_PATH)/$(VARIANT)/software/bootloader/bootloader.bin $(LOCAL_DIR)/software/bootloader/
	scp $(REMOTE_HOST):$(REMOTE_PATH)/$(VARIANT)/software/satman/satman.fbi $(LOCAL_DIR)/software/satman/

clean:
	rm -rf $(LOCAL_DIR)

# Usage examples:
# make REMOTE_HOST=user@artiqhost VARIANT=nist_qc2
# make clean
