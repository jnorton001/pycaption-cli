import optparse
import codecs

import pycaption

if __name__ == "__main__":
    parser = optparse.OptionParser("usage: %prog [options]")
    parser.add_option("--sami",
            action='store_true',
            dest='sami',
            default=False,)
    parser.add_option("--dfxp",
            action='store_true',
            dest='dfxp',
            default=False,)
    parser.add_option("--srt",
            action='store_true',
            dest='srt',
            default=False,)
    parser.add_option("--transcript",
            action='store_true',
            dest='transcript',
            default=False,)
    (options, args) = parser.parse_args()

    try:
        filename = args[0]
    except:
        raise Exception(
        ('Expected usage: python caption_converter.py <path to caption file> ',
        '[--sami --dfxp --srt --transcript]'))

    try:
        captions = codecs.open(filename, encoding='utf-8', mode='r').read()
    except:
        captions = open(filename, 'r').read()
        captions = unicode(captions, errors='replace')

    scc = pycaption.SCCReader()
    srt = pycaption.SRTReader()
    sami = pycaption.SAMIReader()
    dfxp = pycaption.DFXPReader()
    
    if scc.detect(captions):
        cont = scc.read(captions)
    elif srt.detect(captions):
        cont = srt.read(captions)
    elif sami.detect(captions):
        cont = sami.read(captions)
    elif dfxp.detect(captions):
        cont = dfxp.read(captions)
    else:
        raise Exception('No caption format detected :(')

    if options.sami:
        print pycaption.SAMIWriter().write(cont)
    if options.dfxp:
        print pycaption.DFXPWriter().write(cont)
    if options.srt:
        print pycaption.SRTWriter().write(cont)
    if options.transcript:
        print pycaption.TranscriptWriter().write(cont)
