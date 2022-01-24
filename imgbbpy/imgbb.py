"""
The MIT License (MIT)

Copyright (c) 2021-2022 scrazzz

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from base64 import b64encode
from typing import Any, ClassVar

import requests
from yarl import URL

from .imgerrors import *
from .imggallery import *

class Client:
    """Represents a synchronous client connection that connects to the Imgbb API for uploading.

    Parameters
    ----------
    key: str
        The API Key required to make a connection with the API.

    Methods
    -------
    upload(*, url=None, file=None, name="", expiration=None)
        Uploads the image.
    """

    API_URL: ClassVar = 'https://api.imgbb.com/1/upload'

    def __init__(self, key) -> None:
        self.key: str = key
        self._session: requests.Session = requests.Session()

    def upload(
        self,
        *,
        file: str = None,
        url: str = None,
        name: str = "image",
        expiration: int = None
    ) -> Image:
        """Uploads the image.

        Note
        -----
        * Both `url` and `file` are optional, but either `url` or `file` is required for uploading the image.
        * The image to upload should not be more than 32 MB.
        * Image gets deleted automatically after 2592000 seconds (30 days) by default.

        Parameters
        ----------
        url: str, optional
            The URL of the image to upload.
        file: str, optional
            The path of the image to upload.
        name: str, optional
            The name of the file. This is automatically set if not given.
        expiration: int, optional
            Use this if you want the uploaded image to be auto deleted after certain time (in seconds 60-15552000).

        Raises
        ------
        TypeError
            Raised when `expiration` is not of type int.

        ImgbbError
            Raised when both `url` and `file` is given.
            Raised when either `url` or `file` is not given.
            Raised when an uncaught error occurs.

        MinExpirationLimit
            Raised when given `expiration` is lower than 60 seconds.

        MaxExpirationLimit
            Raised when given `expiration` is more than 15552000 seconds.

        Returns
        -------
        Image: class
            The uploaded image.
        """

        if file and url:
            raise ImgbbError('Cannot upload both URL and file.')
        if not file and not url:
            raise ImgbbError('Needs either URL or file to upload.')
        if url is not None:
            yarl_url: URL = URL(url)
            if not (yarl_url.scheme or yarl_url.host):
                raise TypeError('url paramter did not get a valid URL')

        if expiration is None:
            pass
        elif not isinstance(expiration, int):
            raise TypeError('expiration should be an int.')

        if expiration is not None:
            if expiration < 60:
                raise MinExpirationLimit('Minimum expiration limit is 60 seconds.')
            if expiration > 15552000:
                raise MaxExpirationLimit('Maximum expiration limit is 15552000 seconds.')

        params = {
            'key': self.key,
            'name': name,
            'image': b64encode(open(file, 'rb').read()) if file else url
        }

        if expiration:
           params['expiration'] = str(expiration)

        r: requests.Response = self._session.post(self.API_URL, params)
        js: Any = r.json()

        if r.status_code == 200:
            data = js['data']
            return Image(
                id = data['id'],
                filename = data['image']['filename'],
                url = data['url'],
                size = data['size'],
                expiration = data['expiration'],
                mime = data['image']['mime'],
                extension = data['image']['extension'],
                delete_url = data['delete_url']
            )
        else:
            raise ImgbbError(f"Error {js['status_code']}: {js['error']['message']}")
