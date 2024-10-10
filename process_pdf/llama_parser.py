import os
import nest_asyncio
nest_asyncio.apply()
from llama_parse import LlamaParse
from llama_index.core import VectorStoreIndex
from llama_index.core.node_parser import MarkdownElementNodeParser
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import Settings
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
tenant_id = os.getenv("tenant_id")
from llama_index.llms.openai import OpenAI
class FileParser:
    def __init__(self):
        EMBEDDING_MODEL  = "text-embedding-3-small"
        GENERATION_MODEL = "gpt-3.5-turbo-0125"
        self.llm = OpenAI(model=GENERATION_MODEL)
        embed_model = OpenAIEmbedding(model=EMBEDDING_MODEL)
        Settings.llm = self.llm
        Settings.embed_model = embed_model
    def retrieve(self,parsing_instructions:str,query:str,file,url:str):
        pdf_file_path = url+'_output_file.pdf'
        with open(pdf_file_path, 'wb') as pdf_file:
            pdf_file.write(file.getvalue())
        documents = LlamaParse(result_type="markdown", parsing_instructions=parsing_instructions).load_data([pdf_file_path])
        os.remove(pdf_file_path)
        node_parser = MarkdownElementNodeParser(llm=self.llm, num_workers=8).from_defaults()
        nodes = node_parser.get_nodes_from_documents(documents)
        base_nodes, objects = node_parser.get_nodes_and_objects(nodes)
        index = VectorStoreIndex(
        nodes= base_nodes +objects
        )
        query_index = index.as_query_engine(similarity_top_k=15)
        response = query_index.query(query)
        return str(response).strip()
    # async def retrieve(self, documents, show_progress):
    #     vector_store = PGVectorStore.from_params(
    #         database=os.getenv("name"),
    #         host=os.getenv("host"),
    #         password=os.getenv("password"),
    #         port=os.getenv("port"),
    #         user=os.getenv("user"),
    #         table_name="MguardFileEmbeddings",
    #         embed_dim=1536,  # openai embedding dimension
    #         hnsw_kwargs={
    #             "hnsw_m": 16,
    #             "hnsw_ef_construction": 64,
    #             "hnsw_ef_search": 40,
    #             "hnsw_dist_method": "vector_cosine_ops",
    #         }
    #     )
    #     storage_context = StorageContext.from_defaults(vector_store=vector_store)
    #     index = VectorStoreIndex.from_documents(
    #         documents, storage_context=storage_context, show_progress=True
    #     )
    #     return index