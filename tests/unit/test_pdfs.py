import io
from pdf_cli.pdfs import pdfs


def test_crop_crops_src_pdf(mocker):
    pdf_reader = mocker.Mock()
    pdf_writer = mocker.Mock()
    output_stream = io.StringIO("")

    src_pages = [
        "first",
        "second",
        "third",
    ]

    def _get_page(page_number):
        return src_pages[page_number]

    pdf_reader.numPages = len(src_pages)
    pdf_reader.getPage.side_effect = _get_page

    dest_pages = []

    def _add_page(page):
        dest_pages.append(page)

    def _write(output_stream):
        for page in dest_pages:
            output_stream.write(page)

    pdf_writer.addPage.side_effect = _add_page
    pdf_writer.write.side_effect = _write

    pdfs.crop(pdf_reader, pdf_writer, output_stream)

    output_stream.seek(0)
    assert "firstsecondthird" == output_stream.read()
