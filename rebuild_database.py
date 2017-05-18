import os
import sys
import getopt
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wwinkel.settings")
django.setup()
from django.core.management import call_command
from django.utils import timezone
from custom_users.models import User
from subprocess import call
from glob import glob
from cms.api import create_page
from time import sleep


def main(argv):
    solr_install_path = None
    try:
        opts, args = getopt.getopt(argv, "", ["solr_install_path="])
    except getopt.GetoptError:
        print('usage: rebuild_database [--solr_install_path <solr installation directory>]')
        sys.exit(2)
    for opt, arg in opts:
        if opt == "--solr_install_path":
            solr_install_path = arg
    # """
    if True:
        print('deleting old db...')
        try:
            os.remove('db.sqlite3')
        except FileNotFoundError:
            print('no db.sqlite3 found')
        print('  done')

        print('deleting old migrations...')
        migration_files = (
            glob('./custom_users/migrations/*_auto_*.py') +
            glob('./dbwwinkel/migrations/0001_initial.py') +
            glob('./dbwwinkel/migrations/*_auto_*.py')
        )
        [os.remove(file) for file in migration_files]
        print('  done')

        print('generating new migrations...')
        call_command('makemigrations', 'custom_users')
        call_command('makemigrations')
        print('  done')

        print('executing migrations...')
        call_command('migrate')
        print('  done')

    if True:
        print('importing data from csv...')
        csv_files = [
            'Province',
            'JuridicalEntity',
            'organisationtyes',
            'knowfrom',
            'organiation_details',
            'questiontypes',
            'institution',
            'faculty',
            'education',
            'question',
            'keywords',
            'organisation_has_keyword',
            'promotor',
            'organisationusers',
        ]
        call(['python', '-W ignore', 'script.py'] + ['./CSV/'+file+'.csv' for file in csv_files])
        print('  done')

        print('creating permission groups...')
        call(['python', 'add_perm_group_script.py'])
        print('  done')

    if True:
        print('creating home page...')
        create_page(
            title='Home', slug='home', template='INHERIT', language='nl', publication_date=timezone.now(), published=True
        )
        print('  done')

    if True:
        print('creating superuser (user:admin@admin.be, pw:admin)...')
        call_command('createsuperuser', '--email', 'admin@admin.be')
        admin = User.objects.get(email='admin@admin.be')
        admin.set_password('admin')
        admin.save()
        print('  done')
    # """
    # print('creating manager user (user:central@manager.be, pw:admin)...')


    # print('creating regional user (user:regional@manager.be, pw:admin, region:antwerp)...')

    if solr_install_path:
        os.chdir(solr_install_path)
        temp_command = '.\\bin\\solr' if os.name == 'nt' else './bin/solr'
        print('stopping solr if it is running...')
        call([temp_command, 'stop', '-all'], shell=True)
        sleep(5)
        print('  done')

        print('generating haystack schema.xml...')
        with open('example\solr\collection1\conf\schema.xml', mode='w') as f:
            call_command('build_solr_schema', stdout=f)
        print('  done')

        print('start solr...')
        call([temp_command, 'start'], shell=True)
        sleep(5)
        print('  done')

        print('rebuilding index...')
        call_command('rebuild_index', '--noinput')
        print('  done')


if __name__ == '__main__':
    main(sys.argv[1:])
