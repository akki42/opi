import opi
from opi.plugins import BasePlugin

class PackmanCodecsPlugin(BasePlugin):
	main_query = "codecs"
	description = "Media Codecs from Packman and official repo"
	queries = ('packman', 'codecs')

	@classmethod
	def run(cls, query):
		# Install Packman Codecs
		if not opi.ask_yes_or_no("Do you want to install codecs from Packman repository?", 'y'):
			return

		opi.add_packman_repo(dup=True)
		opi.install_packman_packages([
			'ffmpeg',
			'libavcodec-full',
			'vlc-codecs',
			'pipewire-aptx',
			'gstreamer-plugins-bad-codecs',
			'gstreamer-plugins-ugly-codecs',
			'gstreamer-plugins-libav',
		])

		opi.install_packages([
			'gstreamer-plugins-good',
			'gstreamer-plugins-good-extra',
			'gstreamer-plugins-bad',
			'gstreamer-plugins-ugly',
		])
