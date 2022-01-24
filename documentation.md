# imgbbpy
An Asynchronous and Synchronous API Wrapper for the Imgbb API.

# Table of Contents
- API Reference
  
  - [Client](https://github.com/scrazzz/imgbbpy/blob/master/documentation.md#client)
    - [Async Client](https://github.com/scrazzz/imgbbpy/blob/master/documentation.md#async-client)
    - [Sync Client](https://github.com/scrazzz/imgbbpy/blob/master/documentation.md#sync-client)
  
  - [Models](https://github.com/scrazzz/imgbbpy/blob/master/documentation.md#models)
    - [Image](https://github.com/scrazzz/imgbbpy/blob/master/documentation.md#image)

  - [Exceptions](https://github.com/scrazzz/imgbbpy/blob/master/documentation.md#exceptions)
    - [ImgbbError](https://github.com/scrazzz/imgbbpy/blob/master/documentation.md#imgbbimgbberrors-imgbberror)
    - [MinExpirationLimit](https://github.com/scrazzz/imgbbpy/blob/master/documentation.md#imgbbimgbberrors-minexpirationlimit)
    - [MaxExpirationLimit](https://github.com/scrazzz/imgbbpy/blob/master/documentation.md#imgbbimgbberrors-maxexpirationlimit)

## API Reference

### Client
#### Async Client
*`class imgbbpy.aio.Client(key)`*  
Represents an asynchronous client connection that connects to the Imgbb API for uploading.

Parameters:
  * __key__ (str) - The API Key required to make a connection with the API.

` ` `await upload(*, url, file, name, expiration)`  
Parameters:
  * __url__ (Optional[str]) - The URL of the image to upload. The image to upload should not be more than 32 MB.
  * __file__ (Optional[str]) - The path of the image to upload. The image to upload should not be more than 32 MB.
  * __name__ (Optional[str]) - The name of the image to set when uploading.
  * __expiration__ (Optional[int]) - The expiration to set when you want the image to be auto deleted after certain time (in seconds 60 - 15552000). The uploaded image gets deleted automatically after 2592000 seconds (30 days) by default.

__Note__:  
* Both `url` and `file` are optional, but either `url` or `file` is needed to upload the image.

Returns:
  * [__Image__](https://github.com/scrazzz/imgbbpy/blob/master/documentation.md#image) - The uploaded image.

Raises:
* __TypeError__ - Raised when `expiration` is not of type int.
* [__ImgbbError__](https://github.com/scrazzz/imgbbpy/blob/master/documentation.md#imgbbimgbberrors-imgbberror) - Raised when:  
Both `url` and `file` is given.  
Either `url` or `file` is not given.  
An uncaught error occurs.  
* [__MinExpirationLimit__](https://github.com/scrazzz/imgbbpy/blob/master/documentation.md#imgbbimgbberrors-minexpirationlimit) - Raised when given `expiration` is lower than 60 seconds.
* [__MaxExpirationLimit__](https://github.com/scrazzz/imgbbpy/blob/master/documentation.md#imgbbimgbberrors-maxexpirationlimit) - Raised when given `expiration` is more than 15552000 seconds.

#### Sync Client
*`class imgbbpy.imgbb.Client(key)`*  
Represents a synchronous client connection that connects to the Imgbb API for uploading.
Parameters:
  * __key__ (str) - The API Key required to make a connection with the API.

` ` `upload(*, url, file, name, expiration)`  
Parameters:
  * __url__ (Optional[str]) - The URL of the image to upload. The image to upload should not be more than 32 MB.
  * __file__ (Optional[str]) - The path of the image to upload. The image to upload should not be more than 32 MB.
  * __name__ (Optional[str]) - The name of the image to set when uploading.
  * __expiration__ (Optional[int]) - The expiration to set when you want the image to be auto deleted after certain time (in seconds 60 - 15552000). The uploaded image gets deleted automatically after 2592000 seconds (30 days) by default.

__Note__:  
* Both `url` and `file` are optional, but either `url` or `file` is needed to upload the image.

Returns:
  * [__Image__](https://github.com/scrazzz/imgbbpy/blob/master/documentation.md#image) - The uploaded image.

Raises:
* __TypeError__ - Raised when `expiration` is not of type int.
* [__ImgbbError__](https://github.com/scrazzz/imgbbpy/blob/master/documentation.md#imgbbimgbberrors-imgbberror) - Raised when:  
Both `url` and `file` is given.  
Either `url` or `file` is not given.  
An uncaught error occurs.  
* [__MinExpirationLimit__](https://github.com/scrazzz/imgbbpy/blob/master/documentation.md#imgbbimgbberrors-minexpirationlimit) - Raised when given `expiration` is lower than 60 seconds.
* [__MaxExpirationLimit__](https://github.com/scrazzz/imgbbpy/blob/master/documentation.md#imgbbimgbberrors-maxexpirationlimit) - Raised when given `expiration` is more than 15552000 seconds.

### Models
#### Image
*`class imgbbpy.imgbbgallery.Image`*  
Represents the uploaded image.  
This is returned from `Client.upload`.

* __id__ (str) - The ID of the image.
* __filename__ - (str) - The filename of the image.
* __url__ (str) - The URL of the image.
* __size__ (int) - The size of the image in bytes.
* __expiration__ (int) - The time left (in seconds) for the image to expire.
* __mime__ (str) - The mime type of the image.
* __extension__ (str) - The extension of the image.
* __delete_url__ (str) - The delete URL to delete the image.

### Exceptions

#### *`class imgbb.imgbberrors.ImgbbError`*

Base class for all Imgbb exceptions.

#### *`class imgbb.imgbberrors.MinExpirationLimit`*

Exeption raised when the expiration given is less than 60 seconds.

#### *`class imgbb.imgbberrors.MaxExpirationLimit`*

Exeption raised when the expiration given is more than 15552000 seconds.
