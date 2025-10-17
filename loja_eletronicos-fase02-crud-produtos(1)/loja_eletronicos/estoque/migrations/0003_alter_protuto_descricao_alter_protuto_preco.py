from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0002_alter_protuto_tag_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='descricao',
            field=models.TextField(default='N/A', help_text='Descrição detalhada do produto', verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='Preço de venda do produto', max_digits=10, verbose_name='Preço'),
        ),
    ]