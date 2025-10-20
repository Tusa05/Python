from config import url_object
from config import queries
from sqlalchemy import create_engine, inspect


def test_db_connection():
    engine = create_engine(url_object)
    insp = inspect(engine)
    names = insp.get_table_names()
    assert names[0] == 'users'


def test_entity_add():
    engine = create_engine(url_object)
    new_title = "python"
    with engine.begin() as conn:
        max_id = conn.execute(queries["select max"])
        new_id = max_id.fetchall()[0][0] + 1
        conn.execute(queries["insert"], [{"id": new_id, "title": new_title}])
        result = conn.execute(queries["select by id"], [{"id": new_id}])
        assert result.fetchall()[0][1] == new_title
        conn.execute(queries["delete"], [{"id": new_id}])
    


def test_entity_mod():
    engine = create_engine(url_object)
    new_title = "python"
    mod_title = "Python with SQLAlchemy"
    with engine.begin() as conn:
        max_id = conn.execute(queries["select max"])
        new_id = max_id.fetchall()[0][0] + 1
        conn.execute(queries["insert"], [{"id": new_id, "title": new_title}])
        conn.execute(queries["update by id"],
                     [{"id": new_id, "title": mod_title}])
        result = conn.execute(queries["select by id"], [{"id": new_id}])
        assert result.fetchall()[0][1] == mod_title
        conn.execute(queries["delete"], [{"id": new_id}])
       


def test_entity_del():
    engine = create_engine(url_object)
    new_title = "sql"
    with engine.begin() as conn:
        max_id = conn.execute(queries["select max"])
        max_id_before = max_id.fetchall()[0][0]
        new_id = max_id_before + 1
        conn.execute(queries["insert"], [{"id": new_id, "title": new_title}])
        conn.execute(queries["delete"], [{"id": new_id}])
        max_id_after = conn.execute(queries["select max"])
        assert max_id_after.fetchall()[0][0] == max_id_before
