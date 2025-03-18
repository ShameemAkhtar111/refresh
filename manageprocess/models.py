from django.db import models

# Create your models here.
class PGroup(models.Model):
    group_name=models.CharField(max_length=20)

    def __str__(self):
        return self.group_name

class Process(models.Model):
    process_name = models.CharField(max_length=20)
    process_env = models.CharField(max_length=10)
    process_report = models.CharField(max_length=100)
    process_state = models.CharField(max_length=10, default="stopped")
    process_last_run = models.DateTimeField(null=True, blank=True)
    group = models.ForeignKey(PGroup, on_delete=models.CASCADE)

    def get_process_last_run(self):
        if self.process_last_run is None:
            return "Not started"
        return self.process_last_run