from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.


class Student(AbstractBaseUser):
    name = models.CharField(max_length=100)
    student_id = models.IntegerField()

    city = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    level = models.ForeignKey(
        "SchoolLevel", on_delete=models.CASCADE, verbose_name=("level")
    )

    region = models.ForeignKey(
        "Region", on_delete=models.CASCADE, verbose_name=("region")
    )
    school = models.ManyToManyField("School", verbose_name=("school"))
    enrolled_courses = models.ManyToManyField(
        "Course", verbose_name=("enrolled courses")
    )
    assignments_student = models.ManyToManyField(
        "Assignment", verbose_name=("assignments_student")
    )

    def __str__(self):
        return self.name


class Teacher(AbstractBaseUser):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    level = models.ManyToManyField("TeacherLevel", verbose_name=("level"))

    region = models.ForeignKey(
        "Region", on_delete=models.CASCADE, verbose_name=("region")
    )
    school = models.ManyToManyField("School")
    courses_teaching = models.ManyToManyField("Course")

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)

    tags = models.ManyToManyField("Tag", verbose_name=("tags"))

    students_enrolled = models.ManyToManyField(
        "Student", verbose_name=("students enrolled")
    )
    teachers = models.ManyToManyField("Teacher", verbose_name=("teachers"))
    views_number = models.IntegerField(default=0)


class Assignment(models.Model):
    name = models.CharField(max_length=100)

    tags = models.ManyToManyField("Tag", verbose_name=("tags"))

    date_submitted = models.DateField()
    date_due = models.DateField()

    students_enrolled = models.ManyToManyField(
        "Student", verbose_name=("students enrolled"), related_name="students_enrolled"
    )
    teachers = models.ManyToManyField("Teacher", verbose_name=("teachers"))

    course = models.ForeignKey(
        "Course", on_delete=models.CASCADE, verbose_name=("course")
    )
    student_enrolled_assignment = models.ForeignKey(
        "Student",
        on_delete=models.CASCADE,
        verbose_name=("student_enrolled_assignment"),
    )


class School(models.Model):
    region = models.ForeignKey(
        "Region", on_delete=models.CASCADE, verbose_name=("region")
    )
    name = models.CharField(max_length=100)


class StudyField(models.Model):
    name = models.CharField(max_length=100)
    school = models.ForeignKey(
        "School", on_delete=models.CASCADE, verbose_name=("school")
    )


class Subject(models.Model):
    name = models.CharField(max_length=100)
    study_fileds = models.ManyToManyField("StudyField", verbose_name=("study fields"))


class SchoolLevel(models.Model):
    name = models.CharField(max_length=100)
    power = models.IntegerField()


class TeacherLevel(models.Model):
    name = models.CharField(max_length=100)
    power = models.IntegerField()


class Region(models.Model):
    name = models.CharField(max_length=100)


class Tag(models.Model):
    name = models.CharField(max_length=100)
