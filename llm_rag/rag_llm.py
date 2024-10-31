from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PDFPlumberLoader
# from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_experimental.text_splitter import SemanticChunker


loader = PDFPlumberLoader("monster.pdf")
docs = loader.load()

text_splitter = SemanticChunker(HuggingFaceEmbeddings())
documents = text_splitter.split_documents(docs)

# print("Number of chunks created: ", len(documents))

# for i in range(3):
#     print()
#     print(f"CHUNK: {i+1}")
#     print(documents[i].page_content)

embedder = HuggingFaceEmbeddings()
vector = FAISS.from_documents(documents, embedder)

retriever = vector.as_retriever(search_type="similarity", search_kwargs={"k": 3})
retrieved_docs = retriever.invoke("Who is naoki urasawa?")
print(retrieved_docs)
