"""
pdfs library module.
"""

import PyPDF2

def crop(count: int, src: str, start: int, skip_set, output_stream):
    """
    Crop ``count`` number of pages from pdf file at
    ``src`` into ``output_stream``, starting from page ``start``.

    :param count: number of pages to crop.
    :param src: source PDF file.
    :param start: starting page in ``src`` to crop.
    :param output_stream: where the cropped output will be written to.
    """
    with open(src, 'rb') as src_pdf:
        reader = PyPDF2.PdfFileReader(src_pdf)
        writer = PyPDF2.PdfFileWriter()
        count = count if count > 0 else reader.numPages

        if start < 0 or (start + count) >= reader.numPages:
            raise ValueError(f"invalid start: {start}")
        i = start
        while i < (start + count):
            if skip_set is None or i not in skip_set:
                writer.addPage(reader.getPage(i))

            i += 1
        writer.write(output_stream)
