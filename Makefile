export
PLATFORM := $(shell uname)
ARCH := $(shell uname -m)
TOPDIR := $(shell pwd)

# Allow custom libc++ hack for Ubuntu
ifeq ("$(wildcard /etc/centos-release)", "")
  LIBSTDCPP_HACK ?= 1
endif

ifeq ($(ARCH),x86_64)
  ARCH := x64
else
  $(error Not prepared to compile on $(ARCH))
endif
