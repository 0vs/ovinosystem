# Generated by Django 3.1.1 on 2021-02-26 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5)),
                ('nome', models.CharField(max_length=30)),
                ('raca', models.CharField(max_length=30)),
                ('especie', models.CharField(choices=[('C', 'Caprino'), ('O', 'Ovino')], max_length=10)),
                ('sexo', models.CharField(choices=[('F', 'Fêmea'), ('M', 'Macho')], max_length=10)),
                ('data_nascimento', models.DateField()),
                ('pelagem', models.CharField(max_length=50)),
                ('registro', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Doenca',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('descricao', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('tipo', models.CharField(choices=[('med', 'Medicamento'), ('equip', 'Equipamento Veterinário'), ('limp', 'Material de Limpeza')], max_length=30)),
                ('nome', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('quantidade', models.IntegerField()),
                ('validade', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=20)),
                ('senha', models.CharField(max_length=50)),
                ('nome', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='VincularDoenca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teste.animal')),
                ('doenca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teste.doenca')),
                ('dataregistro', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Gravidez',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio', models.DateField(blank=True, null=True)),
                ('fim', models.DateField(blank=True, null=True)),
                ('inicio2', models.DateField(blank=True, null=True)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teste.animal')),
            ],
        ),
        migrations.CreateModel(
            name='Cobertura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio', models.DateField(blank=True, null=True)),
                ('inicio2', models.DateField(blank=True, null=True)),
                ('femea', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='femea', to='teste.animal')),
                ('macho', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='macho', to='teste.animal')),
            ],
        ),
        migrations.CreateModel(
            name='Acessa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permissao', models.CharField(choices=[('adm', 'Administrador'), ('cord', 'Cordenador'), ('bols', 'Bolsista'), ('vist', 'Visitante')], max_length=15)),
                ('setor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teste.setor')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teste.usuario')),
            ],
        ),
    ]
