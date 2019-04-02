from django.db import models


class Grqx(models.Model):
    QX = models.IntegerField()

    def __str__(self):
        return str(self.QX)


class Jbxx(models.Model):
    #低级 姓名，性别，年龄，院系，专业，年级，籍贯，所在部门，所在组，
    xh = models.CharField(max_length=20, verbose_name='学号')
    name = models.CharField(max_length=20,blank=True, null=True, verbose_name='姓名')
    sex = models.CharField(max_length=20,blank=True, null=True)
    age = models.IntegerField(blank=True, null=True, verbose_name='年龄')
    yx = models.CharField(max_length=20,blank=True, null=True,verbose_name='院系')
    zy = models.CharField(max_length=20,blank=True, null=True,verbose_name='专业')
    nj = models.CharField(max_length=20,blank=True, null=True,verbose_name='年级')
    jg = models.CharField(max_length=20,blank=True, null=True,verbose_name='籍贯')
    bm = models.CharField(max_length=20,blank=True, null=True,verbose_name='部门')
    zb = models.CharField(max_length=20,blank=True, null=True,verbose_name='组')
    #中级 QQ，邮箱，课表，项目经验，特长，
    qq = models.CharField(max_length=20,blank=True, null=True)
    email = models.CharField(max_length=20,blank=True, null=True)
    # kb =
    jy = models.TextField(blank=True, null=True,verbose_name='经验')
    tc = models.TextField(blank=True, null=True,verbose_name='特长')
    #高级 联系电话，加入团队间，有无考研意向，是否是勤工，银行卡号
    tel = models.CharField(max_length=20,blank=True, null=True)
    join_time =  models.DateTimeField(verbose_name='加入时间')
    SFKY = models.CharField(max_length=20,blank=True, null=True,verbose_name='是否考研')
    SFQG = models.CharField(max_length=20,blank=True, null=True,verbose_name='是否勤工')
    YHKH = models.CharField(max_length=20,blank=True, null=True,verbose_name='银行卡号')
    #权限
    QX = models.ForeignKey(Grqx,on_delete=models.DO_NOTHING,verbose_name='权限',default=1)
    # DLMM

    def __str__(self):
        return "<member : %s>" % self.xh


class Info(models.Model):
    xh = models.IntegerField(primary_key=True)
    info = models.TextField(blank=True, null=True)


class login(models.Model):
    user = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
