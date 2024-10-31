from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PDFPlumberLoader
from langchain_experimental.text_splitter import SemanticChunker


loader = PDFPlumberLoader("SSRN-id3648557.pdf")
docs = loader.load()

text_splitter = SemanticChunker(HuggingFaceEmbeddings())
documents = text_splitter.split_documents(docs)

# print("Number of chunks created: ", len(documents))

# for i in range(3):
#     print()
#     print(f"CHUNK: {i+1}")
#     print(documents[i].page_content)
