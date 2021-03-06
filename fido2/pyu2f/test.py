from . import base
import socket

class HidOverUDP(base.HidDevice):

  @staticmethod
  def Enumerate():
    a = [
            {
                'vendor_id':0x1234,
                'product_id':0x5678,
                'product_string': 'software test interface',
                'usage': 0x01,
                'usage_page': 0xf1d0,
                'path': 'localhost:8111'
            },]
    return a

  def __init__(self, path):
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self.sock.bind(('127.0.0.1',7112))
    addr,port = path.split(':')
    port = int(port)
    self.token = (addr,port)
    self.sock.settimeout(1.0)

  def GetInReportDataLength(self):
    return 64

  def GetOutReportDataLength(self):
    return 64

  def Write(self, packet):
    self.sock.sendto(bytearray(packet), self.token)

  def Read(self):
    msg = [0]*64
    pkt, _ = self.sock.recvfrom(64)
    for i,v in enumerate(pkt):
        msg[i] = ord(v)
    return msg



