""" Python 'utf-16-be' Codec


Written by Marc-Andre Lemburg (mal@lemburg.com).

(c) Copyright CNRI, All Rights Reserved. NO WARRANTY.

"""

import codecs

### Codec APIs

encode = codecs.utf_16_be_encode


def decode(input, errors="strict"):
    return codecs.utf_16_be_decode(input, errors, True)


class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return codecs.utf_16_be_encode(input, self.errors)[0]


class IncrementalDecoder(codecs.BufferedIncrementalDecoder):
    _buffer_decode = codecs.utf_16_be_decode


class StreamWriter(codecs.StreamWriter):
    encode = codecs.utf_16_be_encode


class StreamReader(codecs.StreamReader):
    decode = codecs.utf_16_be_decode


### encodings module API


def getregentry():
    return codecs.CodecInfo(
        name="utf-16-be",
        encode=encode,
        decode=decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
        streamreader=StreamReader,
        streamwriter=StreamWriter,
    )
