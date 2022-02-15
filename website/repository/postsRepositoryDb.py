from ..models.previewPost import PreviewPost
import psycopg2 as driver

class PostsRepositoryDb:
    def __init__(self):
        self.repo = driver.connect("dbname=blogapp user=postgres password=admin")

    def verifica(self):
        conn = None
        try:
            print('PostgreSQL database version:')
            cursor = self.repo.cursor()
            cursor.execute('SELECT version()')
            db = cursor.fetchone()
            print(db)
            self.repo.cursor().close()
        except (Exception, driver.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                print('Database connection closed.')