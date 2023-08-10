from django.test import TestCase
from .models import Article, Category


# Create your tests here.
class SimpleTest(TestCase):
    def test_home_page_status(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)


class ArticleTest(TestCase):
    def setUp(self):
        Article.objects.create(
            title="test",
            slug="test",
            status="P",
            ordering=1,
            special=False,
            publish_date="2019-01-01 00:00:00",
            content="test",
            image="test",
            category=Category.objects.create(
                title="test",
                slug="test",
                is_homepage=False,
                layout="L",
                status="P",
                ordering=1
            )
        )

    def test_string_representation(self):
        article = Article(title="test")
        self.assertEqual(str(article), article.title)

    def test_article_content(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, 'test')
        self.assertTemplateUsed(res, 'news/index.html')

    def test_article_detail_view(self):
        res = self.client.get('/1/')
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, 'test')
        self.assertTemplateUsed(res, 'news/detail.html')
