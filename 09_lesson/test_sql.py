from sqlalchemy import create_engine, text
from auth import token

db_connection_string = token
db = create_engine(db_connection_string)


def test_insert():
    connection = db.connect()
    transaction = connection.begin()

    my_id = 16

    # 1. INSERT - добавляем данные
    sql = text(
        'INSERT INTO subject(subject_id, subject_title) '
        'VALUES (:id, :title)'
    )
    connection.execute(sql, {"id": my_id, "title": "Литература"})

    # 2. SELECT - проверяем, что запись добавилась
    check_sql = text(
        'SELECT subject_id, subject_title FROM subject '
        'WHERE subject_id = :id'
    )
    result = connection.execute(check_sql, {"id": my_id})
    row = result.fetchone()

    # 3. ASSERT - проверяем успешность
    assert row is not None, "Запись не найдена в БД"
    assert row.subject_id == my_id, (
        f"ID не совпадает: {row.subject_id} != {my_id}"
    )
    assert row.subject_title == "Литература", (
        f"Title не совпадает: {row.subject_title} != Литература"
    )

    # 4. DELETE - удаляем (чистим за собой)
    delete_sql = text('DELETE FROM subject WHERE subject_id = :id')
    connection.execute(delete_sql, {"id": my_id})

    transaction.commit()
    connection.close()


def test_update():
    connection = db.connect()
    transaction = connection.begin()

    my_id = 17
    old_title = "Биология"
    new_title = "Экономику"

    # INSERT - добавляем данные
    insert_sql = text(
        'INSERT INTO subject(subject_id, subject_title) '
        'VALUES (:id, :title)'
    )
    connection.execute(insert_sql, {"id": my_id, "title": old_title})

    # UPDATE - изменяем данные
    update_sql = text(
        'UPDATE subject SET subject_title = :new_title '
        'WHERE subject_id = :id'
    )
    connection.execute(update_sql, {
        "new_title": new_title, "id": my_id
    })

    # SELECT - проверяем, что обновление прошло успешно
    check_sql = text(
        'SELECT subject_title FROM subject WHERE subject_id = :id'
    )
    actual_title = connection.execute(
        check_sql, {"id": my_id}
    ).scalar()

    # ASSERT - проверяем успешность обновления
    assert actual_title == new_title, (
        f"Ожидалось '{new_title}', получено '{actual_title}'"
    )

    # DELETE - удаляем
    delete_sql = text('DELETE FROM subject WHERE subject_id = :id')
    connection.execute(delete_sql, {"id": my_id})

    transaction.commit()
    connection.close()


def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    my_id = 18

    # INSERT
    sql = text(
        'INSERT INTO subject(subject_id, subject_title) '
        'VALUES (:id, :title)'
    )
    connection.execute(sql, {"id": my_id, "title": "Химия"})

    # DELETE
    delete_sql = text('DELETE FROM subject WHERE subject_id = :id')
    connection.execute(delete_sql, {"id": my_id})

    # SELECT - проверяем отсутствие
    check_sql = text(
        'SELECT subject_id FROM subject WHERE subject_id = :id'
    )
    result = connection.execute(check_sql, {"id": my_id})
    row = result.fetchone()

    # ASSERT - сущность должна отсутствовать
    assert row is None, f"Запись с ID {my_id} не была удалена"

    transaction.commit()
    connection.close()
