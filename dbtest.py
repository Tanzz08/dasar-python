import unittest

def koneksi_ke_db():
    print("[terhubung ke db]")

def putus_koneksi_db(db):
    print("[tidak terhubung ke db {}]".format(db))

class User: 
    username = ""
    aktif = False

    def __init__(self, db, username):
        self.username = username

    def set_altif(self):
        self.aktif = True

class TestUser(unittest.TestCase):

    # test fixture
    def setUp(self):
        self.db = koneksi_ke_db()
        self.dicoding = User(self.db, "dicoding")

    def tearDown(self):
        putus_koneksi_db(self.db)

    # test case 1
    def test_user_default_not_active(self):
        db = koneksi_ke_db()
        dicoding = User(db, "dicoding")
        self.assertFalse(dicoding.aktif)
        putus_koneksi_db(db)

    # test case 2
    def test_user_is_active(self):
        db = koneksi_ke_db()
        dicoding = User(db, "dicdong")
        dicoding.set_altif()
        self.assertTrue(dicoding.aktif)
        putus_koneksi_db(db)

if __name__ == "__main__":
    # test runner
    unittest.main()