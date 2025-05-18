from dotenv import load_dotenv
load_dotenv()

from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
from langchain_community.llms import HuggingFacePipeline


embedder = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2")
db = FAISS.load_local("faiss_index", embedder, allow_dangerous_deserialization=True)

tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")
hf_pipeline = pipeline(
    "text2text-generation",
    model=model,
    tokenizer=tokenizer,
    truncation=True,
    max_length=256
)
llm = HuggingFacePipeline(pipeline=hf_pipeline)

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

conv_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=db.as_retriever(k=3),
    memory=memory,
    return_source_documents=False,
)