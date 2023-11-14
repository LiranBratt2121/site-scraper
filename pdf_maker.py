import aspose.pdf as ap

document = ap.Document()

page = document.pages.add()

text_fragment = ap.text.TextFragment("Hello,world!")

page.paragraphs.add(text_fragment)

document.save("output.pdf")