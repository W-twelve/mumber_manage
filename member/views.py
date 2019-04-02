from django.shortcuts import render,render_to_response,get_object_or_404
from .models import Grqx,Jbxx,Info
# from django.apps import apps
# import member

# Create your views here.
def home(request):
    context={}
    return render_to_response('home.html',context)

def member_list(request):
    context = {}
    context['members'] = Jbxx.objects.all()
    return render_to_response('member/member_list.html',context)

def member_detail(request,member_id):
    context = {}
    # modelobj = apps.get_model(member,Jbxx)
    # for field in modelobj._meta.fields:
    #     context[field.name] = field.verbose_name

    context['member'] = get_object_or_404(Jbxx,id=member_id)
    return render_to_response('member/member_detail.html',context)

# def member_add_xx(request):
#     if request.method == 'GET':
#         return render(request, 'addstu.html')
#
#     if request.method == 'POST':
#         stu_name = request.POST.get('name')
#         stu_num = request.POST.get('num')
#
#     context = {}
#     return render_to_response('member/member_add.html',context)

def member_add_xx(request):
    if request.method == 'GET':
        return render(request, 'member/member_add.html')

    if request.method == 'POST':
        xh = request.POST.get('xh')
        name = request.POST.get('name')
        sex = request.POST.get('sex')
        age = request.POST.get('age')
        yx = request.POST.get('yx')
        zy = request.POST.get('zy')
        nj = request.POST.get('nj')
        jg = request.POST.get('jg')
        bm = request.POST.get('bm')
        zb = request.POST.get('zb')
        qq = request.POST.get('qq')
        email = request.POST.get('email')
        jy = request.POST.get('jy')
        tc = request.POST.get('tc')
        tel = request.POST.get('tel')
        join_time = request.POST.get('join_time')
        SFKY = request.POST.get('SFKY')
        SFQG = request.POST.get('SFQG,')
        YHKH = request.POST.get('YHKH,')
        QX = request.POST.get('QX')

        if not Jbxx.objects.filter(xh=xh).exists():
            # jbxx = Jbxx()
            Jbxx.objects.create(
                xh=xh,
                name=name,
                sex =sex,
                age = age,
                yx = yx,
                zy = zy,
                nj = nj,
                jg = jg,
                bm = bm,
                zb = zb,
                qq = qq,
                email = email,
                jy = jy,
                tc = tc,
                tel = tel,
                join_time = join_time,
                SFKY = SFKY,
                SFQG = SFQG,
                YHKH = YHKH,
                QX = get_object_or_404(Grqx,QX=QX)
            ).save()
            return render(request, 'member/member_add.html',{'message': '提交成功'})
        else:
            return render(request, 'member/member_add.html', {'message': '该学号已经存在！'})

def member_delet(request,id):
    pass
    Jbxx.objects.get(id=id).delete()
    return HttpResponseRedirect('/stu/allstu')

def login():
    pass

def judge_qx():
    qx = Grqx.objects.filter()