"""
Entrypoint for app.
"""

import sys

import click
import PyPDF2

@click.group()
def main():
    """
    Simple python app for managing PDF files.
    """
    return

@main.command()
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
def crop(src, dest, start, count):
    """
    Crop COUNT number of pages from pdf file at SRC into DEST, starting from page START.
    """
    with open(src, 'rb') as src_pdf:
        reader = PyPDF2.PdfFileReader(src_pdf)

        with (open(dest, 'wb+') \
                if dest is not None \
                else sys.stdout) as output_stream:
            writer = PyPDF2.PdfFileWriter()
            count = count if count > 0 else reader.numPages

            if start < 0 or (start + count) >= reader.numPages:
                raise ValueError(f"invalid start: {start}")
            i = start
            while i < (start + count):
                writer.addPage(reader.getPage(i))
                i += 1
            writer.write(output_stream)

if __name__ == '__main__':
    main()
