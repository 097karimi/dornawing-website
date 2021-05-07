# Generated by Django 3.1.6 on 2021-03-26 15:46

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('about', '0002_auto_20210326_1443'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutpage',
            old_name='our_story_img',
            new_name='about_us_img',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='our_story_richtext',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='our_story_title',
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='about_left_richtext',
            field=wagtail.core.fields.RichTextField(blank=True, max_length=500, verbose_name='About Us Left Paragraph'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='about_right_richtext',
            field=wagtail.core.fields.RichTextField(blank=True, max_length=500, verbose_name='About Us Right Paragraph'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='about_title',
            field=models.CharField(default=' ', max_length=100, verbose_name='About Title'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='fourth_member_of_team_description',
            field=models.CharField(default=' ', max_length=100, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='fourth_member_of_team_facebook',
            field=models.URLField(blank=True, null=True, unique=True, verbose_name='Facebook web page'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='fourth_member_of_team_img',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='fourth_member_of_team_instagram',
            field=models.URLField(blank=True, null=True, unique=True, verbose_name='Email Address'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='fourth_member_of_team_linkedin',
            field=models.URLField(blank=True, null=True, unique=True, verbose_name='Linedin web page'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='fourth_member_of_team_name',
            field=models.CharField(default=' ', max_length=30, verbose_name='Full Name'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='fourth_member_of_team_position',
            field=models.CharField(default=' ', max_length=30, verbose_name='Organizational Position'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='fourth_member_of_team_twitter',
            field=models.URLField(blank=True, null=True, unique=True, verbose_name='Twitter web page'),
        ),
    ]
