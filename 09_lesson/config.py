from sqlalchemy.engine import URL
from sqlalchemy import create_engine, text


url_object = URL.create(
    drivername="postgresql",
    username="postgres",
    password="admin",  
    host="localhost",
    port=5432,
    database="postgres",
)

engine = create_engine(url_object)

queries = {
    "select max": text("SELECT MAX(subject_id) FROM subject"),
    "select by id": text("SELECT * FROM subject WHERE subject_id = :id"),
    "insert": text("""INSERT INTO subject (subject_id, subject_title) VALUES
                    (:id, :title)"""),
    "update by id": text("""UPDATE subject SET subject_title = :title WHERE
                          subject_id = :id"""),
    "delete": text("DELETE FROM subject WHERE subject_id = :id")
}

