import mysql.connector
from mysql.connector import Error


class Database:
    def __init__(self):
        self.conn = None
        self.connect()

    def delete_data(self):
        self.mycursor.execute("DELETE FROM Text WHERE id > 0")
        self.conn.commit()

    def push_data(self, data):
        self.mycursor.execute("INSERT INTO Text(txt) VALUES(%s)", (data,))
        self.conn.commit()

    def query(self):
        txt = ''
        self.mycursor.execute("SELECT txt FROM Text")
        for i in self.mycursor:
            txt += str(i)[2:-3] + "\n"
        return txt

    def connect(self):
        """ Connect to MySQL database """
        try:
            self.conn = mysql.connector.connect(host='localhost',
                                           database='Message',
                                           user='root',
                                           password='22042004')
            self.mycursor = self.conn.cursor()
            self.mycursor.execute("CREATE TABLE IF NOT EXISTS Text(id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, txt VARCHAR(500))")
            self.conn.commit()

        except Error as e:
            print(e)


if __name__ == '__main__':
    db = Database()
    #db.delete_data()
    #db.push_data("bar")
    print(db.query())
