class Applicant():
    def __init__(self, raw_data):
        self.id = raw_data[0]
        self.first_name = raw_data[1]
        self.last_name = raw_data[2]
        self.phone_number = raw_data[3]
        self.email = raw_data[4]
        self.application_code = raw_data[5]

    @staticmethod
    def get_all():
        from db import Database
        return Database.get_applicants()

    # Return the full name, as a full_name property of all the applicants, whose name is Carol
    # returns: list of dictionaries
    # example: [{
    #    full_name: 'Carol James'
    # }, ...]
    @classmethod
    def _4_specific_applicant_by_first_name(cls):
        return [{'full_name': applicant.first_name + " " + applicant.last_name}
                for applicant in cls.get_all()
                if applicant.first_name == 'Carol']

    # Return the full name, as a full_name property of all the applicants, whose email ends with '@adipiscingenimmi.edu'
    # returns: list of dictionaries
    # example: [{
    #    full_name: 'Ipis Blud'
    # }, ...]
    @classmethod
    def _5_specific_applicant_by_email_domain(cls):
        return [{'full_name': applicant.first_name + ' ' + applicant.last_name}
                for applicant in cls.get_all()
                if applicant.email.endswith('@adipiscingenimmi.edu')]

    # Insert a the Applicant into Database.applicants_data,
    # and return a filtered list, where we only add the data of Markus.
    # The data of the new applicant:
    #   id: 11
    #   first_name: 'Markus'
    #   last_name: 'Schaffarzyk'
    #   phone_number: '003620/725-2666'
    #   email: 'djnovus@groovecoverage.com'
    #   application_code: 54823
    # returns: list of dictionaries (one dictionary, as the list should be filtered)
    # example return value: [{
    #    id: 500
    #    first_name: 'Bill',
    #    last_name: 'Wilkinson',
    #    phone_number: '003670/123-4567'
    #    email: 'bill@wilkins.on'
    #    application_code: 54823
    # }]
    @classmethod
    def _6_inserting_a_new_applicant(cls):
        from db import Database
        new_applicant = [11, 'Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', 54823]
        Database.applicants_data.append(new_applicant)
        return [{'id': raw_data[0],
                 'first_name': raw_data[1],
                 'last_name': raw_data[2],
                 'phone_number': raw_data[3],
                 'email': raw_data[4],
                 'application_code': raw_data[5]} for raw_data in Database.applicants_data
                if raw_data == new_applicant]

        # applicants = cls.get_all()
        # new_applicant = Applicant([11, 'Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', 54823])
        # applicants.append(new_applicant)
        # for applicant in applicants:
        #     if applicant == new_applicant:
        #         new_applicant_dict = {
        #                               'id': applicant.id,
        #                               'first_name': applicant.first_name,
        #                               'last_name': applicant.last_name,
        #                               'phone_number': applicant.phone_number,
        #                               'email': applicant.email,
        #                               'application_code': applicant.application_code
        #                               }
        #         new_applicant_list.append(new_applicant_dict)

    # Update an Applicant in the applicants_data, and returns a filtered dictionary list for checking.
    # Story: Jemima Foreman, an applicant called us, that her phone number changed to: 003670/223-7459
    # example return value: [{
    #    phone_number: '003670/223-7459'
    # }]
    @classmethod
    def _7_updating_data(cls):
        from db import Database
        updated_phone = '003670/223-7459'
        for raw_data in Database.applicants_data:
            if raw_data[1] == 'Jemima' and raw_data[2] == 'Foreman':
                raw_data[3] = updated_phone

        return [{'phone_number': raw_data[3]} for raw_data in Database.applicants_data
                if raw_data[1] == 'Jemima' and raw_data[2] == 'Foreman']

        # applicants = cls.get_all()
        # specific_applicant = []
        # for applicant in applicants:
        #     applicant_dict = {}
        #     if 'Jemima' in applicant.first_name and 'Foreman' in applicant.last_name:
        #         applicant.phone_number = '003670/223-7459'
        #         applicant_dict['phone_number'] = applicant.phone_number
        #         specific_applicant.append(applicant_dict)
        # return specific_applicant

    # Delete lines from the applicants_data, based on a filter condition
    # Story: Arsenio, an applicant called us, that he and his friend applied to Codecool.
    # They both want to cancel the process, because they got an investor for the site they run: mauriseu.net
    # Logic: remove all the applicants, who applied with emails for this domain.
    #       (e-mail address has this domain after the @ sign)
    # returns: integer (number of occurences of the @mauriseu.net e-mail domains)
    # example: 2
    @classmethod
    def _8_deleting_applicants(cls):
        from db import Database
        for raw_data in Database.applicants_data:
            if raw_data[4].endswith('@mauriseu.net'):
                Database.applicants_data.remove(raw_data)
        deleted_applicants = [raw_data for raw_data in Database.applicants_data
                              if raw_data[4].endswith('@mauriseu.net')]
        return len(deleted_applicants)

        # applicants = cls.get_all()
        # for applicant in applicants:
        #     if applicant.email.endswith('@mauriseu.net'):
        #         applicants.remove(applicant)
        # deleted_applicants = [applicant for applicant in applicants if applicant.email.endswith('@mauriseu.net')]
