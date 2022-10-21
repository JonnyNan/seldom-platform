# Generated by Django 4.0.6 on 2022-10-22 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestCaseTemp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(default='', max_length=500, verbose_name='文件名')),
                ('class_name', models.CharField(default='', max_length=200, verbose_name='类名')),
                ('class_doc', models.TextField(blank=True, default='', null=True, verbose_name='类描述')),
                ('case_name', models.CharField(default='', max_length=200, verbose_name='方法名')),
                ('case_doc', models.TextField(blank=True, default='', null=True, verbose_name='方法描述')),
                ('case_hash', models.CharField(default='', max_length=200, verbose_name='用例hash')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_project.project')),
            ],
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(default='', max_length=500, verbose_name='文件名')),
                ('class_name', models.CharField(default='', max_length=200, verbose_name='类名')),
                ('class_doc', models.TextField(blank=True, default='', null=True, verbose_name='类描述')),
                ('case_name', models.CharField(default='', max_length=200, verbose_name='方法名')),
                ('case_doc', models.TextField(blank=True, default='', null=True, verbose_name='方法描述')),
                ('status', models.IntegerField(default=0, verbose_name='状态')),
                ('case_hash', models.CharField(default='', max_length=200, verbose_name='用例hash')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_project.project')),
            ],
        ),
        migrations.CreateModel(
            name='CaseResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='名称')),
                ('report', models.TextField(default='', null=True, verbose_name='报告内容')),
                ('passed', models.IntegerField(default=0, verbose_name='通过用例')),
                ('error', models.IntegerField(default=0, verbose_name='错误用例')),
                ('failure', models.IntegerField(default=0, verbose_name='失败用例')),
                ('skipped', models.IntegerField(default=0, verbose_name='跳过用例')),
                ('tests', models.IntegerField(default=0, verbose_name='总用例数')),
                ('system_out', models.TextField(default='', null=True, verbose_name='日志')),
                ('run_time', models.FloatField(default=0, verbose_name='运行时长')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_case.testcase')),
            ],
        ),
    ]
