from django.conf import settings

from datetime import datetime


class Limit():
    """
    It controls users requests using session according to their ip address 
    """
    def __init__(self, request):        
        self.session = request.session
        
        
        self.ip = self.get_client_ip(request)  # getting ip adress        
        ip_adress = self.session.get(self.ip)  # adding ip adress to session
        if not ip_adress:
            ip_adress = self.session[self.ip] = {"time_list" : [],}
        self.ip_adress = ip_adress
        
        self.add_time()  # adding time as seconds into time_list in the session


    
    def get_client_ip(self, request):
        """
        Return ip address of a user
        """
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    

    def add_time(self):
        """
        Insert request time as second to the beginning of the time list
        """
        self.ip_adress["time_list"].insert(0, (datetime.now() - datetime(2020, 1, 1)).total_seconds())
        self.save()
    

    def save(self):
        """
        Record request time to the session
        """
        self.session[self.ip] = self.ip_adress


    def check(self):
        """
        If if a user makes more than 10 requests in 10 seconds, it returns 
        True otherwise False.
        """
        time_list = self.ip_adress["time_list"]
        if len(time_list) >= settings.OVERFLOW_REQUEST_NUMBER and \
            time_list[0] - time_list[settings.OVERFLOW_REQUEST_NUMBER - 1] < settings.OVERFLOW_REQUEST_TIME:
            return True
        else:
            del self.ip_adress["time_list"][10:]
            self.save()
            return False



