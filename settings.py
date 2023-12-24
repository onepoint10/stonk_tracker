class AppSettings(object):
    def __init__(self, api_key, api_url_pref, server_mail, server_mail_passw, client_mail, sendmail):
        self.api_key = api_key
        self.api_url_pref = api_url_pref
        self.server_mail = server_mail
        self.server_mail_passw = server_mail_passw
        self.client_mail = client_mail
        self.sendmail = sendmail


def as_AppSettings(dct):
    return AppSettings(dct['api_key'], dct['api_url_pref'], dct['server_mail'], dct['server_mail_passw'],
                       dct['client_mail'], dct['sendmail'])
