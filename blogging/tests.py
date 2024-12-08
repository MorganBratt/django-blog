from django.test import TestCase
from django.contrib.auth.models import User
import datetime
import subprocess
from django.utils import timezone
from blogging.models import Post, Category

# Create your tests here.
# from blogging.models import Post, Category

# need to come to 1:30 ish in the lecture
# need to come to 1:21:50 in the lecture


class PostTestCase(TestCase):
    fixtures = [
        "blogging_test_fixture.json",
    ]  # need to find ths file

    def setUp(self):
        self.user = User.objects.get(pk=1)

    def test_string_representation(self):
        expected = "This is a blog title"
        p1 = Post(title=expected)
        actual = str(p1)
        self.assertEqual(expected, actual)


class CategoryTestCase(TestCase):
    def test_string_representation(self):
        expected = "A Category"
        category1 = Category(name=expected)
        actual = str(category1)
        self.assertEqual(expected, actual)


class FrontEndTestCase(TestCase):
    fixtures = [
        "blogging_test_fixture.json",
    ]  # need to find ths file

    def setUp(self):
        self.now = timezone.now()
        self.timedelta = datetime.timedelta(seconds=15)
        author = User.objects.get(pk=1)
        for count in range(1, 11):
            post = Post(title=f"Post {count} Title", text="foo", author=author)
            if count < 6:
                pubdate = self.now - self.timedelta * count
                post.published_date = pubdate
            post.save()

    def test_list_only_published(self):
        resp = self.client.get("/blogging/")
        resp_text = resp.content.decode(resp.charset)
        self.assertTrue("Recent Posts" in resp_text)
        for count in range(1, 11):
            title = f"Post {count} Title"
            if count < 6:
                self.assertContains(resp, title, count=1)
            else:
                self.assertNotContains(resp, title)

    def test_details_only_published(self):

        for count in range(1, 11):
            title = f"Post {count} Title"
            post = Post.objects.get(title=title)
            resp = self.client.get("/posts/%d/" % post.pk)
            if count < 6:
                self.assertEqual(resp.status_code, 200)
                # self.assertContains(resp, title)
            else:
                self.assertEqual(resp.status_code, 404)


class CodeStyleTest(TestCase):
    def test_black_formatting(self):
        """Test that code complies with Black formatting."""
        try:
            # Run Black in --check mode
            result = subprocess.run(
                ["black", "--check", "blogging", "django_blog", "polling"],
                capture_output=True,
                text=True,
                encoding="utf-8",  # Ensure UTF-8 encoding
            )
            # Combine stdout and stderr safely
            output = (result.stdout or "") + (result.stderr or "")
            # Assert that Black returns a success code
            self.assertEqual(result.returncode, 0, msg=output)
        except FileNotFoundError:
            self.fail("Black is not installed. Please install it to run this test.")
