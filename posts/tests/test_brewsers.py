from rest_framework import status
from rest_framework.test import APITestCase

from posts.models import Brewser

class BrewserTests(APITestCase):
    def setUp(self):
        Brewser.objects.create(
            username='Digijan',
            email='digijan@test.net',
            picture='http://cdn.forum280.org/logos/forum280_logo_no_tagline.png',
            password='janpass2018'
        )
        
    # C 
    def test_post_brewser(self):
        """
        POST to /users/ creates a new Brewser.
        """
        url = '/users/'
        data = {
            'username': 'Anajan',
            'email': 'anajan@test.net',
            'picture': 'http://cdn.forum280.org/logos/forum280_logo_no_tagline.png',
            'password': 'janpass2018'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {
            'id': 2,
            'username': 'Anajan',
            'email': 'anajan@test.net',
            'picture': 'http://cdn.forum280.org/logos/forum280_logo_no_tagline.png',
            'posts': [],
            'channels': []
        })
    
    # R
    def test_get_brewser(self):
        """
        GET to /users/:id retrieves Brewser matching :id
        """ 
        url = '/users/1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'id': 1,
            'username': 'Digijan',
            'email': 'digijan@test.net',
            'picture': 'http://cdn.forum280.org/logos/forum280_logo_no_tagline.png',
            'posts': [],
            'channels': []
        })
    
    def test_get_brewsers(self):
        """
        GET to /users/ retrieves all Brewsers
        """ 
        url = '/users/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [{
            'id': 1,
            'username': 'Digijan',
            'email': 'digijan@test.net',
            'picture': 'http://cdn.forum280.org/logos/forum280_logo_no_tagline.png',
            'posts': [],
            'channels': []
        }])
        
    # D
    def test_delete_own_brewser(self):
        """
        DELETE to /users/:id with authenticated Brewser matching :id deletes Brewser matching :id
        """ 
        #Bypass JWT process
        self.client.force_authenticate(user=Brewser.objects.get(username='Digijan'))

        url = '/users/1'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data, None)
        self.assertEqual(Brewser.objects.count(), 0)
    
    # D
    def test_delete_other_brewser(self):
        """
        DELETE to /users/:id with authenticated Brewser not matching :id does not delete Brewser
        """ 
    
        user = Brewser.objects.create(
            username='NotDigijan',
            email='notdigijan@test.net',
            picture='http://cdn.forum280.org/logos/forum280_logo_no_tagline.png',
            password='janpass2018'
        )
        
        #Bypass JWT process
        self.client.force_authenticate(user=user)

        url = '/users/1'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Brewser.objects.count(), 2)

    # U
    def test_patch_own_brewser(self):
        """
        PATCH to /users/:id with authenticated Brewser matching :id updates Brewser matching :id
        """ 
        #Bypass JWT process
        self.client.force_authenticate(user=Brewser.objects.get(username='Digijan'))

        url = '/users/1'
        response = self.client.patch(url, {'channels': [{'tag': 'testCase'}]})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'id': 1,
            'username': 'Digijan',
            'email': 'digijan@test.net',
            'picture': 'http://cdn.forum280.org/logos/forum280_logo_no_tagline.png',
            'posts': [],
            'channels': [{'tag': 'testCase', 'posts': []}]
        })
    # U        
    def test_patch_other_brewser(self):
        """
        PATCH to /users/:id with authenticated Brewser not matching :id does not update Brewser matching :id
        """
        user = Brewser.objects.create(
            username='NotDigijan',
            email='notdigijan@test.net',
            picture='http://cdn.forum280.org/logos/forum280_logo_no_tagline.png',
            password='janpass2018'
        )
         
        #Bypass JWT process
        self.client.force_authenticate(user=user)

        url = '/users/1'
        response = self.client.patch(url, {'email': 'digijan@test.com'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Brewser.objects.get(id=1).email, 'digijan@test.net')