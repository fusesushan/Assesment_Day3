from abc import ABC, abstractmethod

# Product: Document
class Document:
    def __init__(self):
        self.content = ""

    def add_content(self, content):
        self.content += content

    def display(self):
        pass

# Abstract Builder
class DocumentBuilder(ABC):
    @abstractmethod
    def add_title(self, title):
        pass

    @abstractmethod
    def add_heading(self, heading):
        pass

    @abstractmethod
    def add_paragraph(self, paragraph):
        pass

    @abstractmethod
    def get_document(self):
        pass

class PDFDocumentBuilder(DocumentBuilder):
    def __init__(self):
        self.document = Document()

    def add_title(self, title):
        self.document.add_content(f"PDF Title: {title}\n")

    def add_heading(self, heading):
        self.document.add_content(f"PDF Heading: {heading}\n")

    def add_paragraph(self, paragraph):
        self.document.add_content(f"PDF Paragraph: {paragraph}\n")

    def get_document(self):
        return self.document


class HTMLDocumentBuilder(DocumentBuilder):
    def __init__(self):
        self.document = Document()

    def add_title(self, title):
        self.document.add_content(f"<h1>{title}</h1>\n")

    def add_heading(self, heading):
        self.document.add_content(f"<h2>{heading}</h2>\n")

    def add_paragraph(self, paragraph):
        self.document.add_content(f"<p>{paragraph}</p>\n")

    def get_document(self):
        return self.document


class DocumentCreator:
    def create_document(self, builder):
        builder.add_title("Builder Design Pattern Example")
        builder.add_heading("Introduction")
        builder.add_paragraph(
            "The Builder pattern separates the construction...")
        return builder.get_document()


pdf_builder = PDFDocumentBuilder()
html_builder = HTMLDocumentBuilder()

document_creator = DocumentCreator()

pdf_document = document_creator.create_document(pdf_builder)
pdf_document.display()

html_document = document_creator.create_document(html_builder)
html_document.display()
