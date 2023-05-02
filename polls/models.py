from django.db import models

class Schedule(models.Model):
    description = models.CharField('hollidaydescription', max_length=200)
    date = models.DateTimeField(verbose_name='Sheduled At')
    updated_at = models.DateTimeField(
        verbose_name='Updated At',
        auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Schedule'
        verbose_name_plural = 'Schedules'
