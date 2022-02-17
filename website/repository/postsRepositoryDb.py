import psycopg2 as db

class PostsRepositoryDb:
    def __init__(self):
        try:
            self.repo = db.connect("dbname=blogapp user=postgres password=admin")
        except(Exception, db.DatabaseError) as error:
            if(error):
                connection = db.connect("dbname=postgres user=postgres password=admin")
                connection.set_session(autocommit=True)
                connection.cursor().execute("CREATE database blogapp")
                connection.commit()
                connection.close()
        finally:
            self.repo = db.connect("dbname=blogapp user=postgres password=admin")

    def verifica(self):
        try:
            print('PostgreSQL database version:')
            cursor = self.repo.cursor()
            cursor.execute('SELECT version()')
            db = cursor.fetchone()
            print(db)
            self.repo.cursor().close()
        except (Exception, db.DatabaseError) as error:
            print(error)