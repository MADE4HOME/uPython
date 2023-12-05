'''

MIT License

Copyright (c) [2023] [MADE4HOME]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''

import time

class FxTimer():

    __now = 0
    __last_time = 0
    __expiration_time = 1000
    __callbackExpiration = None

    def update(self):
        self.__now = time.time()
        if (self.__now - self.__last_time) >= self.__expiration_time:
            if m_expired == False:
                m_expired = True
            if self.__callbackExpiration != None:
                self.__callbackExpiration(self.__now)

    def updateLastTime(self):
        self.__last_time = time.time()

    def clear(self):
        if m_expired == True:
            m_expired = False
	
    def setExpirationCb(self, callback):
        self.__callbackExpiration = callback

    def setExpirationTime(self, expiration_time):
        self.__expiration_time = expiration_time

    def getExpirationTime(self):
        return self.__expiration_time

    def expired(self):
        return self.__expired
