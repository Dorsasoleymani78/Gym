from django.db import models

# Create your models here.
from apps.main.models import Major
from ckeditor.fields import RichTextField
# Create your models here.
 
    
    
class Blog(models.Model):
    category=models.ForeignKey(Major,on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=100,verbose_name='عنوان')
    content=RichTextField(verbose_name='توضیحات')
    is_active=models.BooleanField(default=False,verbose_name='فعال/غیرفعال')
    img=models.ImageField(upload_to='images/blog',verbose_name='عکس')
    create_at=models.DateField(auto_now_add=True,null=True,blank=True,verbose_name='زمان ایجاد')
    def __str__(self) -> str:
        return  self.title 
    
    class Meta:
        verbose_name='وبلاگ'
        verbose_name_plural= 'وبلاگ ها'
        db_table='T_Blog'
    
class like(models.Model):
    post=models.ForeignKey(Blog,on_delete=models.CASCADE)
    
