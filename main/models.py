from django.db import models
from django.core.urlresolvers import reverse_lazy as reverse
from django.core.validators import RegexValidator


class Preface(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField(blank=True, help_text="Preface project")
    image = models.ImageField(
        verbose_name=u'Preface Image', upload_to="preface_pic", blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.name


class Skill(models.Model):
    skill_name = models.CharField(max_length=255, blank=True)
    skill_percent = models.PositiveSmallIntegerField(blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.skill_name


class About(models.Model):
    name = models.CharField(max_length=80)
    preface_description = models.TextField(blank=True, help_text="Preface yourself")
    main_description = models.TextField(blank=True, help_text="About me")
    skills = models.ForeignKey(Skill)
    education = models.CharField(max_length=255, blank=True, help_text="Education name")
    education_description = models.TextField(blank=True, help_text="Describe education")
    image = models.ImageField(
        verbose_name=u'Photo', upload_to="photo", blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.name


class Goal(models.Model):
    name = models.CharField(max_length=80)
    goal_description = models.TextField(blank=True, help_text="Description")
    image = models.ImageField(
        verbose_name=u'Goal picture', upload_to="picture", blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.name


class Fee(models.Model):
    name = models.CharField(max_length=80)
    fee_description = models.TextField(blank=True, help_text="Fee Description")
    price = models.DecimalField(max_digits=15, decimal_places=2, help_text="Price")
    discount = models.DecimalField(
        max_digits=15, decimal_places=2, null=True, help_text="Discount")
    increase = models.DecimalField(
        max_digits=15, decimal_places=2, null=True, help_text="Increase")
    increase_description = models.TextField(blank=True, help_text="Increase Description")
    discount_description = models.TextField(blank=True, help_text="Discount Description")

    def __str__(self):              # __unicode__ on Python 2
        return self.name


class Benefit(models.Model):
    name = models.CharField(max_length=80)
    benefit_description = models.TextField(blank=True, help_text="Description")
    icon = models.CharField(max_length=80, blank=True, help_text="Benegit icon from fontawesome")

    def __str__(self):              # __unicode__ on Python 2
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=80)
    slug = models.SlugField(unique=True)
    avatar = models.ImageField(
        verbose_name=u'Photo', upload_to="photo_ava", blank=True)
    position = models.TextField(blank=True, help_text="Position")
    testimonial = models.TextField(blank=True, help_text="Testimonial")
    location = models.CharField(max_length=250, help_text="Location")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(max_length=15, validators=[phone_regex], blank=True) # validators should be a list
    url = models.URLField(blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

    def get_absolute_url(self):
        return reverse('testimonials_detail', kwargs={'slug': self.slug})

class Contact(models.Model):
    name = models.CharField(max_length=80)
    preface = models.TextField(blank=True, help_text="Main idea")
    definition = models.TextField(blank=True, help_text="Definition")
    fb = models.URLField(blank=True, help_text="Facebook link")
    tw = models.URLField(blank=True, help_text="Twitter link")
    gg = models.URLField(blank=True, help_text="Google plus link")
    ig = models.URLField(blank=True, help_text="Instagramm link")
    ml = models.URLField(blank=True, help_text="Email")

    def __str__(self):              # __unicode__ on Python 2
        return self.name
