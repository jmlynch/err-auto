from errbot import BotPlugin, botcmd
from subprocess import Popen, PIPE, STDOUT


class Whois(BotPlugin):
   max_err_version = '3.2.2' # Optional, but recommended

   def activate(self):
        super(Whois, self).activate()

	try:
		Popen(['whois'], stdout=PIPE, stderr=STDOUT).communicate()[0]
	except Exception as e:
		self.warn_admins("This plugin uses whois and it wasn't found on your system")

   @botcmd
   def whois(self, mess, args):
      return Popen(['whois'] + args.split(), stdout=PIPE, stderr=STDOUT).communicate()[0].decode('utf-8')
	
