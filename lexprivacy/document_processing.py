import os

def load_documents(document_paths):
    documents = []
    for path in document_paths:
        with open(path, 'r') as file:
            documents.append(file.read())
    return documents

def preprocess_documents(documents):
    preprocessed_docs = []
    for doc in documents:
        preprocessed_doc = ' '.join(doc.split())  # Basic preprocessing
        preprocessed_docs.append(preprocessed_doc)
    return preprocessed_docs
