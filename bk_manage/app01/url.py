from django.urls import path
from . import views

urlpatterns = [
    path('userinfo/',views.get_user_info.as_view(),name='userinfo'),
    path('cron/', views.cron.as_view(),name='cron'),                      # 获取或创建 提交定时任务到数据库/获取数据库的定时任务
    path('crondetail/<int:id>/',views.crondetail.as_view(),name='crondetail'),  # get、post、put、update、单个备份任务
    path('bkip/',views.Bkip.as_view(),name='bkip'),
    path('bkipdetail/<int:id>/',views.BkipDetail.as_view(),name='bkip'), # 备份服务器ip
    path('croncreate/<int:id>/',views.croncreate.as_view(),name='croncreate'),       # 创建定时任务
    path('cronshow/<int:id>/',views.cronshow.as_view(),name='cronshow'),           # 展示定时任务
    path('logshow/<int:id>/',views.logshow.as_view(),name='logshow')               # 展示日志
]

