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
    parser.add_option("--scc",
            action='store_true',
            dest='dfxp',
            help="write captions in SCC format",
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
    parser.add_option("--scc_lang",
            dest='lang',
            help="choose override language for input",
            default='',)
    parser.add_option("--scc_offset",
            dest='offset',
            help="choose offset for SCC file; measured in seconds",
            default=0)
    (options, args) = parser.parse_args()

    try:
        filename = args[0]
    except:
        raise Exception(
        ('Expected usage: python caption_converter.py <path to caption file> ',
        '[--sami --dfxp --srt --transcript --scc]'))

    try:
        captions = codecs.open(filename, encoding='utf-8', mode='r').read()
    except:
        captions = open(filename, 'r').read()
        captions = unicode(captions, errors='replace')

    content = read_captions(captions, options)
    write_captions(content, options)


def read_captions(captions, options):
    scc_reader = pycaption.SCCReader()
    srt_reader = pycaption.SRTReader()
    sami_reader = pycaption.SAMIReader()
    dfxp_reader = pycaption.DFXPReader()

    if scc_reader.detect(captions):
        if options.lang:
            return scc_reader.read(captions, lang=options.lang,
                                   offset=int(options.offset))
        else:
            return scc_reader.read(captions, offset=int(options.offset))
    elif srt_reader.detect(captions):
        return srt_reader.read(captions)
    elif sami_reader.detect(captions):
        return sami_reader.read(captions)
    elif dfxp_reader.detect(captions):
        return dfxp_reader.read(captions)
    else:
        raise Exception('No caption format detected :(')


def write_captions(content, options):
    if options.scc:
        print pycaption.SCCWriter().write(content).encode("utf-8")
    if options.sami:
        print pycaption.SAMIWriter().write(content).encode("utf-8")
    if options.dfxp:
        print pycaption.DFXPWriter().write(content).encode("utf-8")
    if options.srt:
        print pycaption.SRTWriter().write(content).encode("utf-8")
    if options.transcript:
        print pycaption.TranscriptWriter().write(content).encode("utf-8")


if __name__ == '__main__':
    main()
