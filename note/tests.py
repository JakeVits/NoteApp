from django.test import TestCase
from django.shortcuts import reverse
from .models import Note


class Test_NoteCreation(TestCase):

    """ test if note title can be emptied """
    def test_empty_note_title(self):
        response = self.client.post(reverse('create'), {'title': '', 'context': 'body'}, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'Note is Successfully Created!')

    """ test if note body can be emptied """
    def test_empty_note_body(self):
        response = self.client.post(reverse('create'), {'title': 'Java', 'context': ''}, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'Note is Successfully Created!')

    """ test if note title can be duplicated """
    def test_duplicate_title(self):
        response1 = self.client.post(reverse('create'), {'title': 'Java', 'context': 'wonderland'}, follow=True)
        response2 = self.client.post(reverse('create'), {'title': 'Java', 'context': 'android'}, follow=True)
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 200)
        self.assertContains(response2, 'Note is Successfully Created!')

    """ test if note title can have spaces in note-creation """
    def test_spaced_title(self):
        response = self.client.post(reverse('create'), {'title': 'Java Programming', 'context': 'body'}, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'Note is Successfully Created!')


class Test_NoteView(TestCase):

    """ test if any message is there when no note is created """
    def test_unavailable_note(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'No Note is Available in the Moment!')

    """ test if particular note's information can be viewed without passing any pk or in the url """
    def test_blank_pk_view(self):
        Note.objects.create(title='Java')
        response = self.client.get(reverse('view', args=['']), follow=True)
        self.assertEquals(response.status_code, 200)

    """ test if particular note's information can be viewed by passing non-existing pk in the url """
    def test_non_existing_pk_view(self):
        Note.objects.create(title='Java')
        response = self.client.get(reverse('view', args=['Python']), follow=True)
        self.assertEquals(response.status_code, 200)


class Test_NoteUpdate(TestCase):

    """ test if note title can be updated emptily """
    def test_empty_note_title(self):
        Note.objects.create(title='Java')
        response = self.client.post(reverse('update', args=['Java']), {"title": '', "context": 'Javas'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Note is Successfully Updated!')

    """ test if note body can be updated emptily """
    def test_empty_note_body(self):
        Note.objects.create(title='Python')
        response = self.client.post(reverse('update', args=['Python']), {'title': 'Python', 'context': ''}, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'Note is Successfully Updated!')

    """ test if duplicated note titles are allowed in note-update """
    def test_duplicate_title(self):
        Note.objects.create(title='Python')
        Note.objects.create(title='Java')
        response = self.client.post(reverse('update', args=['Java']), {'title': 'Python', 'context': 'AI'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Note is Successfully Updated!')

    """ test if note title can have spaces in note-update """
    def test_spaced_title(self):
        response = self.client.post(reverse('create'), {'title': 'Python AI', 'context': 'body'}, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'Note is Successfully Created!')


class Test_NoteDelete(TestCase):

    """ test if emptied note title can be deleted """
    def test_empty_note_title(self):
        Note.objects.create(title='Java')
        response = self.client.get('/delete/{}'.format(''))
        self.assertEquals(response.status_code, 200)

    """ test if in-existent note title can be deleted """
    def test_absent_title(self):
        Note.objects.create(title='Java')
        response = self.client.get('/delete/{}'.format('Python'))
        self.assertEquals(response.status_code, 200)
