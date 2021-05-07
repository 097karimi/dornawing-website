# Generated by Django 3.1.6 on 2021-02-13 13:57

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('wagtailcore', '0059_apply_collection_ordering'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitter', models.URLField(blank=True, null=True, unique=True, verbose_name='Twitter Web Page (Company)')),
                ('facebook', models.URLField(blank=True, null=True, unique=True, verbose_name='Facebook Web Page (Company)')),
                ('instagram', models.URLField(blank=True, null=True, unique=True, verbose_name='Instagram Web Page (Company)')),
                ('linkedin', models.URLField(blank=True, null=True, unique=True, verbose_name='Linedin Web Page (Company)')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('to_address', models.CharField(blank=True, help_text='Optional - form submissions will be emailed to these addresses. Separate multiple addresses by comma.', max_length=255, verbose_name='to address')),
                ('from_address', models.CharField(blank=True, max_length=255, verbose_name='from address')),
                ('subject', models.CharField(blank=True, max_length=255, verbose_name='subject')),
                ('header_title_text', models.CharField(default=' ', max_length=50, verbose_name='Header Title')),
                ('header_text', models.CharField(default=' ', max_length=100, verbose_name='Header Text')),
                ('about_title', models.CharField(default=' ', max_length=100, verbose_name='About Title')),
                ('about_left_richtext', wagtail.core.fields.RichTextField(blank=True, max_length=500, verbose_name='About Us Left Paragraph')),
                ('about_right_richtext', wagtail.core.fields.RichTextField(blank=True, max_length=500, verbose_name='About Us Right Paragraph')),
                ('location', models.CharField(default=' ', max_length=50, verbose_name='Location')),
                ('email', models.CharField(default=' ', max_length=50, verbose_name='Email')),
                ('call', models.CharField(default=' ', max_length=50, verbose_name='Call')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='updated_time')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created_time')),
                ('pub_time', models.DateTimeField(auto_now_add=True, verbose_name='pub_time')),
                ('about_us_img', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('banner_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='FormField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('clean_name', models.CharField(blank=True, default='', help_text='Safe name of the form field, the label converted to ascii_snake_case', max_length=255, verbose_name='name')),
                ('label', models.CharField(help_text='The label of the form field', max_length=255, verbose_name='label')),
                ('field_type', models.CharField(choices=[('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('email', 'Email'), ('number', 'Number'), ('url', 'URL'), ('checkbox', 'Checkbox'), ('checkboxes', 'Checkboxes'), ('dropdown', 'Drop down'), ('multiselect', 'Multiple select'), ('radio', 'Radio buttons'), ('date', 'Date'), ('datetime', 'Date/time'), ('hidden', 'Hidden field')], max_length=16, verbose_name='field type')),
                ('required', models.BooleanField(default=True, verbose_name='required')),
                ('choices', models.TextField(blank=True, help_text='Comma separated list of choices. Only applicable in checkboxes, radio and dropdown.', verbose_name='choices')),
                ('default_value', models.CharField(blank=True, help_text='Default value. Comma separated values supported for checkboxes.', max_length=255, verbose_name='default value')),
                ('help_text', models.CharField(blank=True, max_length=255, verbose_name='help text')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_fields', to='home.homepage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
