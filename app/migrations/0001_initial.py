# Generated by Django 4.2.4 on 2023-09-04 14:40

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gling')),
                ('Service_Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='projectimg')),
                ('Project_name', models.CharField(max_length=100)),
                ('Project_content', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ServicePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Service_Title', models.CharField(max_length=50)),
                ('First_Service_Image', models.ImageField(upload_to='servimg')),
                ('First_Service_Content', models.TextField(max_length=2000)),
                ('Service_Subtitle', models.CharField(max_length=200)),
                ('Service_Image_Second', models.ImageField(upload_to='servimg')),
                ('Service_Image_Third', models.ImageField(upload_to='servimg')),
                ('Second_Service_Content', models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Testomonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='testmoimg')),
                ('clint_coments', models.TextField(max_length=1000)),
                ('name', models.CharField(max_length=100)),
                ('city', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('video', embed_video.fields.EmbedVideoField()),
            ],
            options={
                'ordering': ['-added'],
            },
        ),
    ]