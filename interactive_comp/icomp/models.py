from django.db import models

# Create your models here.
class SamInput(models.Model):
	sequence_string = models.CharField(max_length=256)
	sequence_count = models.IntegerField(default=0)
	sam_flag = models.IntegerField(default=0)
	gene = models.CharField(max_length=128)

	def __str__(self):
		return self.gene

class SamOutput(models.Model):
	sequence_count_out = models.IntegerField(default=0)
	gene_out = models.CharField(max_length=128)
	noMatch1_counts = models.IntegerField(default=0)
	noMatch2_counts = models.IntegerField(default=0)
	match_count = models.IntegerField(default=0)

	def __str__(self):
		return self.gene_out




