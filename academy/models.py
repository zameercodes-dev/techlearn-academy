from django.db import models

# Create your models here.
class course(models.Model):
    course_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    duration = models.TimeField()
    course_image = models.IntegerField
    def __str__(self):
                 return self.course_name

class trainer(models.Model):
    experties_choice = [
        ('python','python'),
        ('javascript','javascript'),
        ('node','node'),
        ('tailwind','tailwind')

    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)    
    experties = models.CharField (max_length=100,choices=experties_choice)
    trainer_photo = models.ImageField(upload_to='trainer_images',blank=True,null=True)
    def __str__(self):
           return f'{self.first_name} {self.last_name}'

class  Students(models.Model):
        first_name = models.CharField(max_length=50)
        last_name = models.CharField(max_length=50)
        email = models.EmailField(unique=True)
        is_active = models.BooleanField(default=True)
        enrolled_courses = models.ForeignKey(course,on_delete=models.CASCADE)
        trainer = models.ForeignKey(trainer,on_delete=models.CASCADE)
        def __str__(self):
               return f'{self.first_name} {self.last_name}'

        
         
