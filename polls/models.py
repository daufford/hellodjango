from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
class Question(models.Model):
  #list model attributes below, as subclasses of with models.<type>
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')

  #default string description of the model object
  def __str__(self):
    return self.question_text
  #create a custom attribute that returns a calculation
  def was_published_recently(self):
    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
  #some customizations to how the field is displayed in admin.  See Django list display
  was_published_recently.admin_order_field = 'pub_date'
  was_published_recently.boolean = True
  was_published_recently.short_description='Published Recently?'


class Choice(models.Model):
  question = models.ForeignKey(Question)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)

  def __str__(self):
    return "%s (%d votes)" % (self.choice_text, self.votes)
