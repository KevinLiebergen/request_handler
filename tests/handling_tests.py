import unittest
from request_handler import RequestHandler


class HandlerTestCase(unittest.TestCase):

    def test_good_response(self):
        """ 200 status code """
        handler = RequestHandler('https://catfact.ninja/fact')
        response = handler.is_good_response()
        self.assertEqual(response, True)

    def test_not_found(self):
        """ 404 status code """
        handler = RequestHandler('https://catfact.ninja/factsss')
        response = handler.is_good_response()
        self.assertEqual(response, False)


if __name__ == '__main__':
    unittest.main()
