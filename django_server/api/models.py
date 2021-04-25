from django.db import models


class User(models.Model):
    name = models.CharField(max_length=39, unique=True)
    sum_of_stars = models.IntegerField(null=True)

    def __str__(self):
        return f"user name: {self.name}, stars count: {self.sum_of_stars}"

    def set_sum_of_stars(self, count):
        self.sum_of_stars = count


class Repository(models.Model):
    name = models.CharField(max_length=100)
    star_count = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # when user is deleted, delete all his repos too

    def __str__(self):
        return f"repository name: {self.name}, stars count: {self.star_count}, user: {self.user}"

    class Meta:
        constraints = [models.UniqueConstraint(fields=["name", "user"], name="name_and_user_unique_together")]
