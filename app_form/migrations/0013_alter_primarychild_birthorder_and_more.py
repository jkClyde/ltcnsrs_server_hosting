# Generated by Django 4.2.6 on 2024-01-28 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_form', '0012_alter_primarychild_fathercontact_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primarychild',
            name='birthOrder',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='primarychild',
            name='fatherEthnicity',
            field=models.CharField(blank=True, choices=[('OTHERS', 'Others'), ('AGGAY', 'AGGAY'), ('AKEANON/AKLANON', 'Akeanon/Aklanon'), ('APAYAO/YAPAYAO', 'Apayao/Yapayao'), ('AYANGAN', 'Ayangan'), ('BALANGAO/BALIWON', 'Balangao/Baliwon'), ('BIKOL/BICOL', 'Bikol/Bicol'), ('BISAYA/BINISAYA', 'Bisaya/Binisaya'), ('BONTOK/BINONTOK', 'Bontok/Binontok'), ('CEBUANO', 'Cebuano'), ('HAMTIKANON', 'Hamtikanon'), ('HILIGAYNON,ILONGGO', 'Hiligaynon,Ilonggo'), ('IBALOI/INIBALOI', 'Ibaloi/Inibaloi'), ('IBANAG', 'Ibanag'), ('IBONTOC', 'Ibontoc'), ('IFUGAO', 'Ifugao'), ('KALANGUYA/IKALAHAN', 'Kalanguya/Ikalahan'), ('ILOCANO', 'Ilocano'), ('IRANON', 'Iranon'), ('ITNEG', 'Itneg'), ('KALINGA', 'Kalinga'), ('KANKANAI/KANKANAEY', 'Kankanai/Kankanaey'), ('KAPAMPANGAN', 'Kapampangan'), ('KARAO', 'Karao'), ('KINALINGA', 'Kinalinga'), ('KINIRAY-A', 'Kiniray-a'), ('MARANAO', 'Maranao'), ('MASBATENO/MASBATEAN', 'Masbateno/Masbatean'), ('PANGASINAN/PANGGALATO', 'Pangasinan/Panggalato'), ('SURIGAONON', 'Surigaonon'), ('TAGALOG', 'Tagalog'), ('TAUSUG', 'Tausug'), ('WARAY', 'Waray')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='primarychild',
            name='motherEthnicity',
            field=models.CharField(blank=True, choices=[('OTHERS', 'Others'), ('AGGAY', 'AGGAY'), ('AKEANON/AKLANON', 'Akeanon/Aklanon'), ('APAYAO/YAPAYAO', 'Apayao/Yapayao'), ('AYANGAN', 'Ayangan'), ('BALANGAO/BALIWON', 'Balangao/Baliwon'), ('BIKOL/BICOL', 'Bikol/Bicol'), ('BISAYA/BINISAYA', 'Bisaya/Binisaya'), ('BONTOK/BINONTOK', 'Bontok/Binontok'), ('CEBUANO', 'Cebuano'), ('HAMTIKANON', 'Hamtikanon'), ('HILIGAYNON,ILONGGO', 'Hiligaynon,Ilonggo'), ('IBALOI/INIBALOI', 'Ibaloi/Inibaloi'), ('IBANAG', 'Ibanag'), ('IBONTOC', 'Ibontoc'), ('IFUGAO', 'Ifugao'), ('KALANGUYA/IKALAHAN', 'Kalanguya/Ikalahan'), ('ILOCANO', 'Ilocano'), ('IRANON', 'Iranon'), ('ITNEG', 'Itneg'), ('KALINGA', 'Kalinga'), ('KANKANAI/KANKANAEY', 'Kankanai/Kankanaey'), ('KAPAMPANGAN', 'Kapampangan'), ('KARAO', 'Karao'), ('KINALINGA', 'Kinalinga'), ('KINIRAY-A', 'Kiniray-a'), ('MARANAO', 'Maranao'), ('MASBATENO/MASBATEAN', 'Masbateno/Masbatean'), ('PANGASINAN/PANGGALATO', 'Pangasinan/Panggalato'), ('SURIGAONON', 'Surigaonon'), ('TAGALOG', 'Tagalog'), ('TAUSUG', 'Tausug'), ('WARAY', 'Waray')], max_length=100, null=True),
        ),
    ]
