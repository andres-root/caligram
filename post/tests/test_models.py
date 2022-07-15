from django.test import TestCase
from model_mommy import mommy

from authentication.models import User
from post.models import Comment, Media, Post, Reaction


class PostTest(TestCase):
    """
    Post model test
    """

    def setUp(self):
        self.post = mommy.make(Post)

    def test_post(self):
        self.assertTrue(isinstance(self.post, Post))
        self.assertTrue(isinstance(self.post.media, Media))
        self.assertTrue(isinstance(self.post.user, User))


class MediaTest(TestCase):
    """
    Media model test
    """

    def setUp(self):
        self.media = mommy.make(Media)

    def test_media(self):
        self.assertTrue(isinstance(self.media, Media))


class CommentTest(TestCase):
    """
    Comment model test
    """

    def setUp(self):
        self.comment = mommy.make(Comment)
        self.reply = mommy.make(Comment)
        self.comment_with_reply = mommy.make(
            Comment,
            reply=self.reply,
        )

    def test_comment(self):
        self.assertTrue(isinstance(self.comment, Comment))
        self.assertTrue(isinstance(self.comment.post, Post))
        self.assertEqual(self.comment.reply, None)

    def test_comment_with_reply(self):
        self.assertTrue(isinstance(self.comment_with_reply, Comment))
        self.assertTrue(isinstance(self.comment_with_reply.reply, Comment))


class ReactionTest(TestCase):
    """
    Reaction model test
    """

    def setUp(self):
        self.reaction = mommy.make(Reaction)

    def test_reaction(self):
        self.assertTrue(isinstance(self.reaction, Reaction))
        self.assertTrue(isinstance(self.reaction.user, User))
        self.assertTrue(isinstance(self.reaction.post, Post))
