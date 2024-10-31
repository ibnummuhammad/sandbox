from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PDFPlumberLoader
from langchain_experimental.text_splitter import SemanticChunker


loader = PDFPlumberLoader("SSRN-id3648557.pdf")
docs = loader.load()

text_splitter = SemanticChunker(HuggingFaceEmbeddings())
print(text_splitter)
