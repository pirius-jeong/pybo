from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=20)
    grade = models.CharField(max_length=2)
    create_date = models.DateTimeField()


class Account(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    substudent = models.ManyToManyField(Student, null=True, blank=True, related_name='student_brother')
    payer = models.CharField(max_length=40)  # 계좌이체 보낸사람
    pay_type = models.CharField(max_length=1)  # p1:김포페이, p2:계좌이체
    brother_dc_yn = models.CharField(max_length=1, null=True, blank=True)
    recommend_dc_start = models.CharField(max_length=8, null=True, blank=True)
    recommend_dc_end = models.CharField(max_length=8, null=True, blank=True)
    create_date = models.DateTimeField()


class PricePlan(models.Model):
    grade = models.CharField(max_length=2)  # a6:6세, a7:7세, b1~b6:1학년~6학년
    sugang_type = models.CharField(max_length=2)  # d4 : 주 4일, d3 : 주 3일
    price = models.IntegerField()  # 월수강료
    refund = models.IntegerField()  # 환불시 1일 기준금액
    start_dt = models.CharField(max_length=8)
    end_dt = models.CharField(max_length=8)


class Sugang(models.Model):
    class_id = models.CharField(max_length=1)  # a:심미경반, b:심애경반
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    day = models.IntegerField()  # 0:mon, tue, wed, thu 4:fri
    time = models.IntegerField()  # 1시~5시
    start_dt = models.CharField(max_length=8)
    end_dt = models.CharField(max_length=8)
