import pywordpress
import yaml

class Bot():
	def __init__(self,killfile,wp_config="wordpress.ini"):
		self.wp_config = wp_config
		self.wp = pywordpress.Wordpress.init_from_config(self.wp_config)
		self.kill = yaml.safe_load(open(killfile))

	def kill_them_all(self):
		for k in self.kill:
			self.wp.delete_page(k)

if __name__ == "__main__":
	b = Bot("kill.yaml")
	b.kill_them_all()