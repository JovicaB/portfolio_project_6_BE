from datetime import datetime, timedelta
import random
import string

from data.database import DatabaseManager


class URLManager:
    """
    A class for managing URL operations for psychological instruments in Project 3.
    """
    def __init__(self) -> None:
        self.database = DatabaseManager('mysql')

    def read_duration_settings(self, user_identifier:str):
        """
        Read test duration from user settings.
        """
        query = "SELECT test_duration FROM login WHERE user_mail = %s"
        parameter = (user_identifier, )
        return self.database.read_data(query, parameter)[0][0]
        
    def _generate_url(self):
        """
        Generates random URL
        """
        random_str = ''.join(random.choices(
            string.ascii_lowercase + string.digits, k=8))
        result = "upitnik_" + random_str
        return result

    def save_url(self, pi_code:str, user_identifier:str):
        """
        Save URL and add x hours to URL duration
        """
        random_url = self._generate_url()
        duration = self.read_duration_settings(user_identifier)
        url_duration = datetime.now() + timedelta(hours=duration)

        sql_query = "INSERT INTO p6_random_url (random_url, url_expiration, user_identifier, pi_code) " \
                    "VALUES (%s, %s, %s, %s)"
        data = (random_url, url_duration, user_identifier, pi_code)
        self.database.execute_query(sql_query, data)
        return random_url

    def read_url_info(self, url:str):
        """
        reads record from random url
        """
        query = "SELECT * FROM p6_random_url WHERE random_url = %s"
        random_url_data = self.database.read_data(query, (url,))
        return random_url_data

    def delete_url(self, url: str):
        """
        deletes the generated URL after the examinee's assessment is finished
        """
        sql_query = "DELETE FROM p6_random_url WHERE random_url = %s"
        data = (url,)
        self.database.execute_query(sql_query, data)
        return f"url is deleted from database"


class ClientSettings:
    """
    A class for managing user settings in Project 3
    """
    def __init__(self, user_identifier: str) -> None:
        self.database = DatabaseManager('mysql')
        self.user_identifier = user_identifier

    def save_duration_settings(self, duration: int):
        """
        sets user duration setting for new generated instrument url
        """
        sql_query = "UPDATE login SET test_duration = %s WHERE user_mail = %s"
        data = (duration, self.user_identifier)
        self.database.execute_query(sql_query, data)
        return f"url duration is set for {duration} hours"

    def reset_results(self, pi_code: str):
        """
        resets assesment results for selected instrument (pi_code)
        """
        sql_query = "DELETE FROM p6_results WHERE user_identifier = %s AND pi_code = %s"
        data = (self.user_identifier, pi_code)
        self.database.execute_query(sql_query, data)
        return f"data for {pi_code} test is deleted"
    

class ResultsManager:
    """
    A class for saving assesment data to database
    """
    def __init__(self, user_identifier: str, pi_code: str) -> None:
        self.database = DatabaseManager('mysql')
        self.user_identifier = user_identifier
        self.pi_code = pi_code

    def get_results(self):
        query = 'SELECT results, examinee_name FROM p6_results WHERE user_identifier = %s AND pi_code = %s'
        sql_args = (self.user_identifier, self.pi_code)

        return self.database.read_data(query, sql_args)

    def save_results(self, examinee_name: str, results: list):
        """
        saves assesment results
        """
        sql_query = "INSERT INTO p6_results (user_identifier, pi_code, examinee_name, results) " \
                    "VALUES (%s, %s, %s, %s)"
        if examinee_name is None:
            examinee_name = ""
        data = (self.user_identifier, self.pi_code, examinee_name, results)
        self.database.execute_query(sql_query, data)
        return f"data for test {self.pi_code}, for user {self.user_identifier} has been saved"
    
