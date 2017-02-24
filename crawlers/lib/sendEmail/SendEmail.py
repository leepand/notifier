#
# Autogenerated by Thrift Compiler (0.10.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
import sys
import logging
from .ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport


class Iface(object):
    def send(self, toAddrs, subject, body):
        """
        Parameters:
         - toAddrs
         - subject
         - body
        """
        pass


class Client(Iface):
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot
        self._seqid = 0

    def send(self, toAddrs, subject, body):
        """
        Parameters:
         - toAddrs
         - subject
         - body
        """
        self.send_send(toAddrs, subject, body)
        return self.recv_send()

    def send_send(self, toAddrs, subject, body):
        self._oprot.writeMessageBegin('send', TMessageType.CALL, self._seqid)
        args = send_args()
        args.toAddrs = toAddrs
        args.subject = subject
        args.body = body
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_send(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = send_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        raise TApplicationException(TApplicationException.MISSING_RESULT, "send failed: unknown result")


class Processor(Iface, TProcessor):
    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap["send"] = Processor.process_send

    def process(self, iprot, oprot):
        (name, type, seqid) = iprot.readMessageBegin()
        if name not in self._processMap:
            iprot.skip(TType.STRUCT)
            iprot.readMessageEnd()
            x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
            oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
            x.write(oprot)
            oprot.writeMessageEnd()
            oprot.trans.flush()
            return
        else:
            self._processMap[name](self, seqid, iprot, oprot)
        return True

    def process_send(self, seqid, iprot, oprot):
        args = send_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = send_result()
        try:
            result.success = self._handler.send(args.toAddrs, args.subject, args.body)
            msg_type = TMessageType.REPLY
        except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
            raise
        except Exception as ex:
            msg_type = TMessageType.EXCEPTION
            logging.exception(ex)
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("send", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

# HELPER FUNCTIONS AND STRUCTURES


class send_args(object):
    """
    Attributes:
     - toAddrs
     - subject
     - body
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'toAddrs', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'subject', 'UTF8', None, ),  # 2
        (3, TType.STRING, 'body', 'UTF8', None, ),  # 3
    )

    def __init__(self, toAddrs=None, subject=None, body=None,):
        self.toAddrs = toAddrs
        self.subject = subject
        self.body = body

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.toAddrs = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.subject = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.body = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('send_args')
        if self.toAddrs is not None:
            oprot.writeFieldBegin('toAddrs', TType.STRING, 1)
            oprot.writeString(self.toAddrs.encode('utf-8') if sys.version_info[0] == 2 else self.toAddrs)
            oprot.writeFieldEnd()
        if self.subject is not None:
            oprot.writeFieldBegin('subject', TType.STRING, 2)
            oprot.writeString(self.subject.encode('utf-8') if sys.version_info[0] == 2 else self.subject)
            oprot.writeFieldEnd()
        if self.body is not None:
            oprot.writeFieldBegin('body', TType.STRING, 3)
            oprot.writeString(self.body.encode('utf-8') if sys.version_info[0] == 2 else self.body)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class send_result(object):
    """
    Attributes:
     - success
    """

    thrift_spec = (
        (0, TType.BOOL, 'success', None, None, ),  # 0
    )

    def __init__(self, success=None,):
        self.success = success

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.BOOL:
                    self.success = iprot.readBool()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('send_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.BOOL, 0)
            oprot.writeBool(self.success)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
