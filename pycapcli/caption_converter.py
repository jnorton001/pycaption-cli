import optparse
import codecs

import pycaption


def main():
    parser = optparse.OptionParser("usage: %prog [options]")
    parser.add_option("--sami",
            action='store_true',
            dest='sami',
            help="write captions in SAMI format",
            default=False,)
    parser.add_option("--dfxp",
            action='store_true',
            dest='dfxp',
            help="write captions in DFXP format",
            default=False,)
    parser.add_option("--srt",
            action='store_true',
            dest='srt',
            help="write captions in SRT format",
            default=False,)
    parser.add_option("--transcript",
            action='store_true',
            dest='transcript',
            help="write transcript for captions",
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

    content = read_captions(captions)
    print write_captions(content, options)


def read_captions(captions):
    scc_reader = pycaption.SCCReader()
    srt_reader = pycaption.SRTReader()
    sami_reader = pycaption.SAMIReader()
    dfxp_reader = pycaption.DFXPReader()

    if scc_reader.detect(captions):
        return scc_reader.read(captions)
    elif srt_reader.detect(captions):
        return srt_reader.read(captions)
    elif sami_reader.detect(captions):
        return sami_reader.read(captions)
    elif dfxp_reader.detect(captions):
        return dfxp_reader.read(captions)
    else:
        raise Exception('No caption format detected :(')


def write_captions(content, options):
    if options.sami:
        return pycaption.SAMIWriter().write(content)
    elif options.dfxp:
        return pycaption.DFXPWriter().write(content)
    elif options.srt:
        return pycaption.SRTWriter().write(content)
    elif options.transcript:
        return pycaption.TranscriptWriter().write(content)
    else:
        raise Exception(('No output specified! Use one or more of these:\n',
                         '[--sami --dfxp --srt --transcript]'))


if __name__ == '__main__':
    main()
