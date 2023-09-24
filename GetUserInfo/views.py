from django.views.generic import TemplateView


class GetUserInfoPage(TemplateView):
    template_name = "GetUserInfo/get_user_info.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header_title'] = 'Получение информации о пользователе'

        context['all_information'] = {
            # site information
            'client_ip': self.get_client_ip(self.request),
            'previous_url': self.request.META.get('HTTP_REFERER'),
            'path': self.request.path,
            'host': self.request.get_host(),
            'user_agent': self.request.headers['User-Agent'],
            'browser': self.request.META.get('HTTP_SEC_CH_UA'),  # chrome?
            'browser_mobile': '1' == self.request.META.get('HTTP_SEC_CH_UA_MOBILE')[1],

            # computer information
            'computer_name': self.request.META.get('COMPUTERNAME'),
            'computer_username': self.request.META.get('USERNAME'),  # имя пользователя компьютера
            'processor_architecture': self.request.META.get('PROCESSOR_ARCHITECTURE'),  # amd
            'processor_level': self.request.META.get('PROCESSOR_LEVEL'),  # Номер модели процессора
            'systemdrive': self.request.META.get('SYSTEMDRIVE'),  # системный диск
            'systemroot': self.request.META.get('SYSTEMROOT'),  # расположение системы
            'system': self.request.META.get('HTTP_SEC_CH_UA_PLATFORM'),  # windows
        }
        geo_date = self.getgeo(ip=self.get_client_ip(self.request))
        if geo_date:
            context['all_information'].update({
                # geographic information
                'country': geo_date['country'],
                'subdivisions': geo_date['subdivisions'],
                'city': geo_date['city'],
                'time_zone': geo_date['time_zone'],
            })

        return context

    def get_forwarded_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def get_client_ip(self, request):
        real_ip = request.META.get('HTTP_X_REAL_IP')
        ip = real_ip if real_ip else request.META.get('REMOTE_ADDR')
        return ip

    def getgeo(self, ip):
        import maxminddb
        db_path = 'GetUserInfo/GeoLite2-City.mmdb'
        with maxminddb.open_database(db_path) as reader:
            geo_info = reader.get(ip)
            if geo_info:
                return {
                    'city': geo_info['city']['names']['ru'],
                    'subdivisions': geo_info['subdivisions'][0]['names']['ru'],
                    'country': geo_info['country']['names']['ru'],
                    'time_zone': geo_info['location']['time_zone']
                }
            return None
