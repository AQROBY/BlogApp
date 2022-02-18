import psycopg2 as db
import datetime

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
            self.__connect()
            self.__checkTableCreation()

    def __checkTableCreation(self):
        try:
            self.repo.cursor().execute("CREATE TABLE posts \
                (id smallserial, \
                title character varying(255) NOT NULL,\
                content text NOT NULL, owner character varying(255) NOT NULL, \
                created_at timestamp without time zone NOT NULL DEFAULT CURRENT_DATE, \
                modified_at timestamp without time zone NOT NULL DEFAULT CURRENT_DATE, \
                PRIMARY KEY (id))")
            self.repo.commit()
        except (Exception, db.DatabaseError) as error:
            print(error)

    def __connect(self):
        try:
            self.repo = db.connect("dbname=blogapp user=postgres password=admin")
        except (Exception, db.DatabaseError) as error:
            print(error)

    def __assignOwner(self):
        cursor = self.repo.cursor()
        cursor.execute('SELECT max(id) FROM posts')
        query = cursor.fetchone()
        
        return "Owner " + str(query[0])

    def findById(self, id):
        try:
            self.__connect()
            cursor = self.repo.cursor()
            cursor.execute('SELECT * FROM posts WHERE id = %s', [id])
            return cursor.fetchone()
        except(Exception, db.DatabaseError) as error:
            print(error)
            return None

    def getAll(self):
        try:
            self.__connect()
            cursor = self.repo.cursor()
            cursor.execute('SELECT * FROM posts')
            return cursor.fetchall()
        except:
            return None

    def create(self, item):
        try:
            self.__connect()
            query = self.repo.cursor().execute('INSERT INTO posts VALUES(DEFAULT, %s, %s, %s, %s, %s)', (item.title, item.content,
                                               self.__assignOwner(), item.created_at, item.modified_at))
            self.repo.commit()
            return True
        except (Exception, db.DatabaseError) as error:
            print(error)
            return False

    def update(self, item):
        try:
            self.__connect()
            query = self.repo.cursor().execute('UPDATE posts SET title = %s, content = %s, modified_at = %s WHERE id = %s',
                                               (item.title, item.content, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                                item.id))
            self.repo.commit()
            return True
        except (Exception, db.DatabaseError) as error:
            print(error)
            return False

    def delete(self, post):
        try:
            self.__connect()
            self.repo.cursor().execute('DELETE FROM posts WHERE id = %s', [post.id])
            self.repo.commit()
            return True
        except (Exception, db.DatabaseError) as error:
            print(error)
            return False