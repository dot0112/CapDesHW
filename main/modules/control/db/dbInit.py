createTableQuery = [
    "CREATE TABLE LIGHT (MONTH INT, AM_SHADING INT, PM_SHADING INT);",
    "CREATE TABLE WATERING (MONTH INT, ISDAY INT, INTERVAL INT);",
    "CREATE TABLE HUMIDIFICATION (MONTH INT, MIN_HUMI INT, MAX_HUMI INT);",
]


def dbInit(conn):
    cursor = conn.cursor()
    for query in createTableQuery:
        cursor.execute(query)
