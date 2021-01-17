from django.test import TestCase

# Create your tests here.

class TestImage(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username = "username", email = "e@e.com", password = "password")
        self.profile= Profile(user = self.user)
        self.img =  Image(name ="test", caption = "haha", likes = 0, profile = self.profile)

       
    def test_instance(self):
        self.user.save()
        self.profile.save()
        self.assertTrue(isinstance(self.img, Image))

    def test_save_image(self):
        self.user.save()
        self.profile.save()
        self.img.save_image()
        imgs = Image.objects.all()
        self.assertTrue(len(imgs) > 0)

    def test_delete_image(self):
        self.user.save()
        self.profile.save()
        self.img.save_image()
        self.img.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    def test_update_image(self):
        cwd = os.getcwd()
        self.user.save()
        self.profile.save()
        self.img.save_image()
        self.assertTrue(self.img.image == None)
        self.img = self.img.update_image("HI", f'{cwd}/media/home.png')
        self.img.save_image()
        img =Image.objects.filter(caption='HI')
        self.assertTrue(len(img)>0)
    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
        Image.objects.all().delete()