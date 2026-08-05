from django.test import override_settings, TestCase

from kobo.apps.openrosa.apps.main.context_processors import site_name


class CustomContextProcessorsTest(TestCase):
    @override_settings(KOBOCAT_PUBLIC_HOSTNAME='kc.data.movin.com.ar')
    def test_site_name(self):
        context = site_name(None)
        self.assertEqual(context, {'SITE_NAME': 'kc.data.movin.com.ar'})
