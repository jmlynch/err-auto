from errbot import BotPlugin, botcmd
from subprocess import Popen, PIPE, STDOUT


class Auto(BotPlugin):
   max_err_version = '9.9.9' # Optional, but recommended

   def activate(self):
        super(Auto, self).activate()

	try:
		Popen(['/usr/bin/automater/Automater.py -b'], stdout=PIPE, stderr=STDOUT).communicate()[0]
	except Exception as e:
		self.warn_admins("This plugin uses automater and it wasn't found on your system")

   @botcmd
   def Auto(self, mess, args):
      return Popen(['/usr/bin/automater/Automater.py -b'] + args.split(), stdout=PIPE, stderr=STDOUT).communicate()[0].decode('utf-8')
	
