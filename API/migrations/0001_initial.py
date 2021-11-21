# Generated by Django 3.2.9 on 2021-11-21 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataPacket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.FloatField()),
                ('vboost_1', models.FloatField()),
                ('vboost_2', models.FloatField()),
                ('vboost_3', models.FloatField()),
                ('vbatt', models.FloatField()),
                ('curin_1', models.FloatField()),
                ('curin_2', models.FloatField()),
                ('curin_3', models.FloatField()),
                ('sun_current', models.FloatField()),
                ('cursys', models.FloatField()),
                ('curout1', models.FloatField()),
                ('curout2', models.FloatField()),
                ('curout3', models.FloatField()),
                ('curout4', models.FloatField()),
                ('curout5', models.FloatField()),
                ('curout6', models.FloatField()),
                ('outputs', models.FloatField()),
                ('latchup1', models.FloatField()),
                ('latchup2', models.FloatField()),
                ('latchup3', models.FloatField()),
                ('latchup4', models.FloatField()),
                ('latchup5', models.FloatField()),
                ('latchup6', models.FloatField()),
                ('wdt_time_i2c', models.FloatField()),
                ('wdt_time_and', models.FloatField()),
                ('wdt_counts_i2c', models.FloatField()),
                ('wdt_counts_gnd', models.FloatField()),
                ('gom_boots', models.FloatField()),
                ('boot_cause', models.FloatField()),
                ('battmode', models.FloatField()),
                ('hk_temp_1', models.FloatField()),
                ('hk_temp_2', models.FloatField()),
                ('hk_temp_3', models.FloatField()),
                ('hk_temp_4', models.FloatField()),
                ('ppt_mode', models.FloatField()),
                ('reserved2', models.FloatField()),
                ('rtc_time', models.FloatField()),
                ('rpi_cpu', models.FloatField()),
                ('rpi_ram', models.FloatField()),
                ('rpi_disk', models.FloatField()),
                ('rpi_temp', models.FloatField()),
                ('rpi_boot', models.FloatField()),
                ('rpi_uptime', models.FloatField()),
                ('gyro_x', models.FloatField()),
                ('gyro_y', models.FloatField()),
                ('gyro_z', models.FloatField()),
                ('acc_x', models.FloatField()),
                ('acc_y', models.FloatField()),
                ('acc_z', models.FloatField()),
                ('mag_x', models.FloatField()),
                ('mag_y', models.FloatField()),
                ('mag_z', models.FloatField()),
                ('gyro_temp', models.FloatField()),
                ('thermo_temp', models.FloatField()),
                ('prs_pressure', models.FloatField()),
                ('position_x', models.FloatField()),
                ('position_y', models.FloatField()),
                ('position_z', models.FloatField()),
                ('attitude_1', models.FloatField()),
                ('attitutde_2', models.FloatField()),
                ('attitude_3', models.FloatField()),
                ('attitude_4', models.FloatField()),
            ],
        ),
    ]
