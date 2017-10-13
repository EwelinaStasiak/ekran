import machine
import time

DIN = machine.Pin(12, machine.Pin.OUT)
CS = machine.Pin(13, machine.Pin.OUT)
CLK = machine.Pin(14, machine.Pin.OUT)

DIN.value(0)
CS.value(1)
DIN.value(0)

def bits(value):
  return [value >> i & 1 for i in range(7,-1,-1)]

def shift(val):
  for b in bits(val):
    CLK.value(0)
    DIN.value(b)
    time.sleep_us(25)
    CLK.value(1)

def write(addr, value):
  assert isinstance(addr, int), "addres nie jest intem"
  assert isinstance(value, int), "wartosc nie jest intem"
  CS.value(0)
  shift(addr)
  shift(value)
  CS.value(1)

