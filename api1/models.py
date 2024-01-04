from django.db import models

# Create your models here.

# create a movie model

class Movie(models.Model):
    movie_id =models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)  # the maximum length
    # of characters allowed for the title field
    release_date = models.DateField() 
    # stores date in 'YYYY-MM
    Description = models.TextField()
    Certifications =models.CharField(max_length=100,choices=
                                     (("adult","A+"),
                                      ("under supervision","UA"),
                                      ("Universal","U")))
    def __str__(self):
        return(self.title)
     

class collections(models.Model):
    #user_id = models.ForeignKey('auth.User', on_delete=models.
    #                           CASCADE)   # link to User model
    name= models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.IntegerField(),
    address=models.CharField(max_length=300),
    position=models.CharField(max_length=200,choices=
                              (("manager","manager"),
                               ("sda","sda"),
                               ("tester","tester"))),
    movie =models.ForeignKey(Movie,on_delete=models.CASCADE)