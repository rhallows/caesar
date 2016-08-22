#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from caesar import encrypt


form =
"""
<html>
  <head>
    <title>Caeaser Cypher</title>
  </head>

  <body>
    <h2>Enter some text to ROT13:</h2>
    <form method="post">
      <textarea name="text"style="height: 100px; width: 400px;">
      {text}
      </textarea>
      <br>
      <input type="submit">
    </form>
  </body>
</html>
"""


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(form)
    def post(self):
       rot13 = ''
       text = self.request.get('text')
       rot13 = encrypt(text, 13)
       self.response.write(form.replace('{text}', rot13))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
