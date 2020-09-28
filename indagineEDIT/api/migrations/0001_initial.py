# Generated by Django 3.0.5 on 2020-09-28 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_EDIT', models.CharField(blank=True, max_length=300, null=True)),
                ('ANNO', models.IntegerField(blank=True, null=True)),
                ('PESO', models.CharField(blank=True, max_length=300, null=True)),
                ('GENERE', models.CharField(blank=True, max_length=300, null=True)),
                ('ETA', models.IntegerField(blank=True, null=True)),
                ('PROVINCIA_RESIDENZA', models.CharField(blank=True, max_length=300, null=True)),
                ('COMUNE_RESIDENZA', models.CharField(blank=True, max_length=300, null=True)),
                ('GIOCO', models.CharField(blank=True, max_length=300, null=True)),
                ('NASCONDI_ENTITA_DENARO', models.CharField(blank=True, max_length=300, null=True)),
                ('IMPULSO_A_SPENDERE_DI_PIU', models.CharField(blank=True, max_length=300, null=True)),
                ('PROVATO_FUMARE', models.CharField(blank=True, max_length=300, null=True)),
                ('ATTUALMENTE_FUMI', models.CharField(blank=True, max_length=300, null=True)),
                ('NUMERO_SIGARETTE', models.CharField(blank=True, max_length=300, null=True)),
                ('ANNI_FUMO', models.CharField(blank=True, max_length=300, null=True)),
                ('BEVUTO_VITA', models.CharField(blank=True, max_length=300, null=True)),
                ('UBRIACO_ANNO', models.CharField(blank=True, max_length=300, null=True)),
                ('FREQUENZA_UBRIACATO_ANNO', models.CharField(blank=True, max_length=300, null=True)),
                ('BINGE_MESE', models.CharField(blank=True, max_length=300, null=True)),
                ('FREQ_BINGE_MESE', models.CharField(blank=True, max_length=300, null=True)),
                ('PRIMA_SOSTANZA', models.CharField(blank=True, max_length=300, null=True)),
                ('ETA_PRIMO_USO_SOSTANZA', models.CharField(blank=True, max_length=300, null=True)),
                ('FREQUENZA_GUIDA', models.CharField(blank=True, max_length=300, null=True)),
                ('GUIDA_TIPO_MEZZO', models.CharField(blank=True, max_length=300, null=True)),
                ('ALMENO_1_INCIDENTE', models.CharField(blank=True, max_length=300, null=True)),
                ('NUM_INCIDENTI', models.CharField(blank=True, max_length=300, null=True)),
                ('GUIDA_CELL', models.CharField(blank=True, max_length=300, null=True)),
                ('GUIDA_SIGARETTA', models.CharField(blank=True, max_length=300, null=True)),
                ('GUIDA_UBRIACO', models.CharField(blank=True, max_length=300, null=True)),
                ('GUIDA_UBRIACO_VOLTE', models.CharField(blank=True, max_length=300, null=True)),
                ('GUIDA_DOPO_DROGA', models.CharField(blank=True, max_length=300, null=True)),
                ('VOLTE_GUIDA_DOPO_DROGA', models.CharField(blank=True, max_length=300, null=True)),
                ('SU_MEZZO_CON_UBRIACO', models.CharField(blank=True, max_length=300, null=True)),
                ('VOLTE_CON_UBRIACO_GUIDA', models.CharField(blank=True, max_length=300, null=True)),
                ('SU_MEZZO_CON_DROGATO', models.CharField(blank=True, max_length=300, null=True)),
                ('VOLTE_SU_MEZZO_CON_DROGATO', models.CharField(blank=True, max_length=300, null=True)),
                ('SUBITO_PREPOTENZE', models.CharField(blank=True, max_length=300, null=True)),
                ('ATTIVITA_FISICA', models.CharField(blank=True, max_length=300, null=True)),
                ('ATTIVITA_SPORTIVA', models.CharField(blank=True, max_length=300, null=True)),
                ('TIPO_SPORT', models.CharField(blank=True, max_length=300, null=True)),
                ('FREQ_SPORT', models.CharField(blank=True, max_length=300, null=True)),
                ('RAPPORTO_SESSUALE', models.CharField(blank=True, max_length=300, null=True)),
                ('ANNI_PRIMO_RAPPORTO', models.CharField(blank=True, max_length=300, null=True)),
                ('NUMERO_PARTNER', models.CharField(blank=True, max_length=300, null=True)),
                ('USO_ALCOL_DROGA_PRIMA_SESSO', models.CharField(blank=True, max_length=300, null=True)),
                ('USO_PRESERVATIVO', models.CharField(blank=True, max_length=300, null=True)),
                ('BMI', models.CharField(blank=True, max_length=300, null=True)),
                ('BMI_4CLASSI', models.CharField(blank=True, max_length=300, null=True)),
                ('BMI_6CLASSI', models.CharField(blank=True, max_length=300, null=True)),
                ('PESO_CORPOREO', models.CharField(blank=True, max_length=300, null=True)),
                ('ALTEZZA', models.CharField(blank=True, max_length=300, null=True)),
                ('CONSUMO_VERDURA', models.CharField(blank=True, max_length=300, null=True)),
                ('CONSUMO_FRUTTA', models.CharField(blank=True, max_length=300, null=True)),
                ('PORZ_FRUTTA_E_VERDURA', models.CharField(blank=True, max_length=300, null=True)),
                ('SOSTANZE_VITA', models.CharField(blank=True, max_length=300, null=True)),
                ('GHB_1_VOLTA', models.CharField(blank=True, max_length=300, null=True)),
                ('CANNA_1_VOLTA', models.CharField(blank=True, max_length=300, null=True)),
                ('ECSTASY_1_VOLTA', models.CharField(blank=True, max_length=300, null=True)),
                ('AMFETAMINE_1_VOLTA', models.CharField(blank=True, max_length=300, null=True)),
                ('LSD_1_VOLTA', models.CharField(blank=True, max_length=300, null=True)),
                ('COCA_1_VOLTA', models.CharField(blank=True, max_length=300, null=True)),
                ('FUNGHI_1_VOLTA', models.CharField(blank=True, max_length=300, null=True)),
                ('POPPER_1_VOLTA', models.CharField(blank=True, max_length=300, null=True)),
                ('EROINA_1_VOLTA', models.CharField(blank=True, max_length=300, null=True)),
                ('KETAMINA_1_VOLTA', models.CharField(blank=True, max_length=300, null=True)),
                ('CRACK_1_VOLTA', models.CharField(blank=True, max_length=300, null=True)),
                ('ANABOL_1_VOLTA', models.CharField(blank=True, max_length=300, null=True)),
                ('PILLOLE_1_VOLTA', models.CharField(blank=True, max_length=300, null=True)),
                ('SMART_1_VOLTA', models.CharField(blank=True, max_length=300, null=True)),
                ('ALTRE_SOST_1_VOLTA', models.CharField(blank=True, max_length=300, null=True)),
                ('ECST_GHB_1_VOLTA', models.CharField(blank=True, max_length=300, null=True)),
                ('ANAB_ENERGY_1_VOLTA', models.CharField(blank=True, max_length=300, null=True)),
                ('CANNAB_SINT_1_VOLTA', models.CharField(blank=True, max_length=300, null=True)),
                ('USO_SOST_NEI_30_GG', models.CharField(blank=True, max_length=300, null=True)),
                ('GHB_30_GG', models.CharField(blank=True, max_length=300, null=True)),
                ('CANNA_30_GG', models.CharField(blank=True, max_length=300, null=True)),
                ('ECSTASY_30_GG', models.CharField(blank=True, max_length=300, null=True)),
                ('AMFETAMINE_30_GG', models.CharField(blank=True, max_length=300, null=True)),
                ('LSD_30_GG', models.CharField(blank=True, max_length=300, null=True)),
                ('COCA_30_GG', models.CharField(blank=True, max_length=300, null=True)),
                ('FUNGHI_30_GG', models.CharField(blank=True, max_length=300, null=True)),
                ('POPPER_30_GG', models.CharField(blank=True, max_length=300, null=True)),
                ('EROINA_30_GG', models.CharField(blank=True, max_length=300, null=True)),
                ('KETAMINA_30_GG', models.CharField(blank=True, max_length=300, null=True)),
                ('CRACK_30_GG', models.CharField(blank=True, max_length=300, null=True)),
                ('ANABOLIZZ_30_GG', models.CharField(blank=True, max_length=300, null=True)),
                ('PILLOLE_30_GG', models.CharField(blank=True, max_length=300, null=True)),
                ('SMART_30_GG', models.CharField(blank=True, max_length=300, null=True)),
                ('ALTRO_30_GG', models.CharField(blank=True, max_length=300, null=True)),
                ('ECSTASY_GHB_30_GG', models.CharField(blank=True, max_length=300, null=True)),
                ('ANABOL_ENERGY_30_GG', models.CharField(blank=True, max_length=300, null=True)),
                ('CANNAB_SINT_30_GG', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
    ]