from django.db import models
from datetime import datetime
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from cloudinary_storage.storage import RawMediaCloudinaryStorage


# It is suggested to replace all spaces with underscore for best results
class Question_paper(models.Model):
    """
    Stores a Question paper, related to :model:`question_papers.Question_paper` and
    :model:`auth.User`.
    """
    provider=models.ForeignKey(User, on_delete=models.SET_DEFAULT,default=1,blank=True,help_text="The user who share the question paper")
    PAPER_CHOICES=[('board','board'),('university','university'),('competitive','competitive')]
    paper_type=models.SlugField(max_length=12,choices=PAPER_CHOICES)
    # college means your education type (Ex: SSLC, PUC or Degree, Engineering, Diploma )
    EDUCATION_CHOICES=[('sslc','sslc'),('puc','puc'),('degree','degree'),('engineering','engineering'),('diploma','diploma')]
    education_type = models.SlugField(max_length=12,choices=EDUCATION_CHOICES,null=True,blank=True)
    # university field contains diffrent board/ universities (Ex: Mangalore University, CBSE)
    governing_body=models.SlugField(max_length=800 , null=True,blank=True)
    # course - includes all courses or streams in university and for boards it's by default "board"
    course_name=models.SlugField(max_length=800,default="board")
    # year - It includes semister or years
    PERIOD_CHOICES=[
        ('first','first'),('second','second'),('third','third'),('fourth','fourth'),
        ('fifth','fifth'),('sixth','sixth'),('seventh','seventh'),('eighth','eighth'),('none','none'),
    ]
    period=models.SlugField(max_length=12,choices=PERIOD_CHOICES,null=True,blank=True)
    # subject contains name of the subject
    subject_name= models.SlugField(max_length=100,null=True,blank=True)
    # examination holds exam info like examination year
    paper_year = models.DateField()
    #examination
    paper_title=models.SlugField(max_length=100)
    paper_doc = models.FileField(upload_to='qpweb',validators=[FileExtensionValidator(allowed_extensions=['pdf'])], storage=RawMediaCloudinaryStorage())
    # complete_ref includes all the fields value used in query search
    complete_ref=models.CharField(max_length=800 , blank=True)
    created_at=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    
    def __str__(self):
        return  f"{self.paper_type}  {self.education_type}  {self.course_name} {self.period} {self.subject_name} {self.paper_year}"

    def save(self, *args, **kwargs):
        self.governing_body=slugify(self.governing_body)
        self.course_name=slugify(self.course_name)
        self.subject_name=slugify(self.subject_name)
        self.paper_title=slugify(self.paper_title)
        self.complete_ref=f"{self.governing_body}-{self.course_name}-{self.subject_name}-{self.paper_title}-{self.paper_year}-{self.education_type}"
        self.complete_ref=self.complete_ref.lower()
        super(Question_paper,self).save(*args, **kwargs)   



