from fpdf import FPDF
import os

try:
    os.remove("html-page.pdf")
finally:
    pass

pdf = FPDF()

# First page:
pdf.add_page()
pdf.set_font("helvetica", size=20)
pdf.write(5, "To find out what's new in self tutorial, click ")
pdf.set_font(style="U")
link = pdf.add_link(page=2)
pdf.write(5, "here", link)
pdf.set_font()

# Second page:
pdf.add_page()
pdf.image(
    "download.jpg", 10, 10, 50, 0, "", "<https://pyfpdf.github.io/fpdf2/>"
)
pdf.set_left_margin(60)
pdf.set_font_size(18)
# """ triple quotes to write html normal
pdf.write_html(
    """You can print text mixing different styles using HTML tags: <b>bold</b>, <i>italic</i>,
<u>underlined</u>, or <b><i><u>all at once</u></i></b>!
<br><br>You can also insert links on text, such as <a href="<https://www.google.com>">link: https://www.google.com</a>,
or on an image: the logo is clickable!"""
)
pdf.output("html-page.pdf")
