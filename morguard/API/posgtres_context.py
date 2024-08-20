from llama_index.legacy import StorageContext
import psycopg2

class PostgresStorageContext(StorageContext):
    def __init__(self, db_url):
        self.conn = psycopg2.connect(db_url)
        self.cur = self.conn.cursor()

    def add(self, document):
        self.cur.execute("INSERT INTO documents (text, metadata) VALUES (%s, %s)", (document.text, document.metadata))
        self.conn.commit()
        return document.id

    def get(self, id):
        self.cur.execute("SELECT text, metadata FROM documents WHERE id = %s", (id,))
        result = self.cur.fetchone()
        if result:
            return {"text": result[0], "metadata": result[1]}
        else:
            return None

    def delete(self, id):
        self.cur.execute("DELETE FROM documents WHERE id = %s", (id,))
        self.conn.commit()

    def list(self):
        self.cur.execute("SELECT id, text, metadata FROM documents")
        return [{"id": row[0], "text": row[1], "metadata": row[2]} for row in self.cur.fetchall()]

    def close(self):
        self.cur.close()
        self.conn.close()
