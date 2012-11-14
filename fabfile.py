import subprocess
from StringIO import StringIO
from fabric.api import *

env['target_directory'] = '/var/local/sargeapp'
env['use_ssh_config'] = True


@task
def deploy():
    tarball = subprocess.check_output(['git', 'archive', 'HEAD'])
    with cd(env['target_directory']):
        put(StringIO(tarball), '_app.tar')
        try:
            run('bin/sarge deploy _app.tar web')
        finally:
            run('rm _app.tar')
