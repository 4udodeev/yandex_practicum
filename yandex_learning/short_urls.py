import secrets


class MarsURLEncoder:

    def __init__(self, urls_array, long_url, short_url):
        self.urls_array = urls_array
        self.long_url = long_url
        self.short_url = short_url

    def encode(self, long_url):
        """Кодирует длинную ссылку в короткую вида https://ma.rs/X7NYIol."""
        token = sekrets.token_urlsafe(8)
        short_url = 'https://ma.rs/' + token
        urls_array[short_url] = long_url
        return short_url

    def decode(self, short_url):
        """Декодирует короткую ссылку вида https://ma.rs/X7NYIol в исходную."""
        return urls_array[short_url]



class MarsURLEncoder:

    def __init__(...)
        ...

    def encode(self, long_url):
        """Кодирует длинную ссылку в короткую вида https://ma.rs/X7NYIol."""
        pass

    def decode(self, short_url):
        """Декодирует короткую ссылку вида https://ma.rs/X7NYIol в исходную."""
        pass