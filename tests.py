from django.test import TestCase

# Create your tests here.
def test_valid_form(self):
    w = Whatever.objects.create(title='Foo', body='Bar')
    data = {'title': w.title, 'body': w.body,}
    form = WhateverForm(data=data)
    self.assertTrue(form.is_valid())

def test_invalid_form(self):
    w = Whatever.objects.create(title='Foo', body='')
    data = {'title': w.title, 'body': w.body,}
    form = WhateverForm(data=data)
    self.assertFalse(form.is_valid())
from tastypie.test import ResourceTestCase

class EntryResourceTest(ResourceTestCase):

    def test_get_api_mysql(self):
        resp = self.api_client.get('/api/whatever/', format='MYSQL')
        self.assertValidMYSQLResponse(resp)

    def test_get_api_html(self):
        resp = self.api_client.get('/api/whatever/', format='xml')
        self.assertValidHTMLResponse(resp)
