
from secrets import choice
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.utils.text import slugify

# Create your models here.


    


class Profile(models.Model):
    
    DOCTOR_IN = {
        ("جلدية","جلدية"),
        ("أسنان","أسنان"),
        ("نفسي","نفسي"),
        ("أطفال حديثي الولادة","أطفال حديثي الولادة"),
        ("مخ و أعصاب","مخ و أعصاب"),
        ("عظام","عظام"),
        ("نساء و توليد","نساء و توليد"),
        ("أنف و أذن و حنجرة","أنف و أذن و حنجرة"),
        ("قلب و أوعية دموية","قلب و أوعية دموية"),
        ("أمراض دم","أمراض دم"),
        ("أورام","أورام"),
        ("باطنة","باطنة"),
        ("التجميل","التجميل"),





    }

    user = models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE)
    name = models.CharField(_("الإسم :"),max_length=150)
    who_i = models.TextField(_("من أنا :"),max_length=150)
    price = models.IntegerField(_("سعر الكشف :"),null=True,blank=True)
    image = models.ImageField(_("الصورة الشخصية :"), upload_to='profile',null=True,blank=True)
    slug = models.SlugField(_("slug"),null=True,blank=True)
    subtitle = models.CharField(_("نبذة عنك : "),max_length=50)
    address = models.CharField(_("الولاية : "),max_length=50,default="باتنة") 
    address_detail = models.CharField(_("العنوان بالتفصيل : "),max_length=50,default="سريانة")
    phone_number = models.CharField(_("رقم الهاتف"),max_length=10,default="0000000000")
    working_hours = models.CharField(_("ساعات العمل : "),max_length=50)
    wating_time = models.IntegerField(_("مدة الإنتضار : "),null=True,blank=True)
    doctor =  models.CharField(_("دكتور ؟"),choices=DOCTOR_IN ,max_length=50 ,null=True,blank=True)
    facebook = models.CharField(max_length=50 ,null=True,blank=True)
    twitter = models.CharField(max_length=50 ,null=True,blank=True)
    instagram = models.CharField(max_length=50 ,null=True,blank=True)
    specialist_doctor = models.CharField(_("متخصص في : "), max_length=50 ,null=True,blank=True)
    #type_person = models.CharField(_("النوع : "), max_length=50,choices=TYPE_OF_PERSON,null=True,blank=True)     

    def save (self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify (self.user.username)
        super(Profile,self).save(*args, **kwargs)


    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return '%s' %(self.user.username)


def create_profile (sender , **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])
        
post_save.connect(create_profile,sender=User)


