import sys

import click
import PyPDF2

@click.command()
@click.option(
    '-s',
    '--src',
    required=True,
    type=str,
)
@click.option(
    '-d',
    '--dest',
    default=None,
    type=str,
)
@click.option(
    '-p',
    '--start',
    default=0,
    type=int,
)
@click.option(
    '-c',
    '--count',
    default=-1,
    type=int,
)
def main(src, dest, start, count):
    with open(src, 'rb') as src_pdf:
        reader = PyPDF2.PdfFileReader(src_pdf)

        output_stream = sys.stdout
        try:
            if dest is not None:
                output_stream = open(dest, 'wb+')
            writer = PyPDF2.PdfFileWriter()
            count = count if count > 0 else reader.numPages
            i = 0
            while i < count:
                writer.addPage(reader.getPage(i))
                i += 1
            writer.write(output_stream)
        finally:
            output_stream.close()

if __name__ == '__main__':
    main()
