class Mentor():
    def __init__(self, raw_data):
        self.id = raw_data[0]
        self.first_name = raw_data[1]
        self.last_name = raw_data[2]
        self.nick_name = raw_data[3]
        self.phone_number = raw_data[4]
        self.email = raw_data[5]
        self.city = raw_data[6]
        self.favourite_number = raw_data[7]

    @staticmethod
    def get_all():
        from db import Database
        return Database.get_mentors()

    # Return the 2 name property of all the mentors
    # returns: list of dictionaries
    # example: [{
    #    first_name: 'Bill',
    #    last_name: 'Wilkinson'
    # }, ...]
    @classmethod
    def _1_list_mentors(cls):
        return [{'first_name': mentor.first_name, 'last_name': mentor.last_name} for mentor in cls.get_all()]

    # Return the nick_name property of all the mentors located in Miskolc
    # returns: list of dictionaries
    # example: [{
    #    nick_name: 'Billy'
    # }, ...]
    @classmethod
    def _2_list_mentors_from_miskolc(cls):
        return [{'nick_name': mentor.nick_name} for mentor in cls.get_all() if mentor.city == 'Miskolc']

    # Return the highest favourite number of all mentors
    # returns: integer
    # example: 927
    @classmethod
    def _3_greatest_favourite_number(cls):
        return max(mentor.favourite_number for mentor in cls.get_all() if mentor.favourite_number is not None)
