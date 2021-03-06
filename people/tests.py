from django.test import TestCase

# Create your tests here.

class TestImage(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username = "username", email = "", password = "password")
        self.profile= Profile(user = self.user)
        self.img =  Image(name ="test", caption = "", likes = 0, profile = self.profile)

       
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


class TestProfile(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username = "username", email = "", password = "password")
        self.profile= Profile(bio = "new me", user = self.user)
        # self.img =  Image(name ="test", caption = "haha", likes = 0, profile = self.profile)
       
    def test_instance(self):
        self.user.save()
        self.profile.save()
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_profile(self):
        self.user.save()
        self.profile.save()
        profs = Profile.objects.all()
        self.assertTrue(len(profs) > 0)

    def test_search_users(self):
        self.user.save()
        self.profile.save()
        user = Profile.search_users("username")
        self.assertTrue(len(user) > 0)

    def test_delete_profile(self):
        self.user.save()
        self.profile.save()
        self.profile.delete_profile()
        profs = Profile.objects.all()
        self.assertTrue(len(profs) == 0)

    def test_update_profile(self):
        cwd = os.getcwd()
        self.user.save()
        self.profile.save()
        self.assertTrue(self.profile.dp == None)
        self.profile.update_profile(f'{cwd}/media/home.png',"changed")
        profs = Profile.objects.filter(bio = "changed")
        self.assertTrue(len(profs) > 0)

    def tearDown(self):
        User.objects.all().delete()
        self.assertTrue(len(User.objects.all()) == 0)
        Profile.objects.all().delete()
        self.assertTrue(len(Profile.objects.all()) == 0)
