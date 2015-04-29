import sublime_info
import subprocess

class SublimePluginManager():

	def __init__(self):
		pass

	def install(self, sublime_text_plugin):

		has_subl, subl_version, package_dir = self.__has_sublime()
		if not has_subl:
			print('Sublime not installed.')
			return False

		print('Sublime Version: %s' % subl_version)
		print('Sublime Package Dir: %s' % package_dir)
		print('Installing sublime plugin from: %s' % sublime_text_plugin.get_repo())

		subprocess.call(['git', 'clone', sublime_text_plugin.get_repo(), ('%s/%s' % (package_dir, sublime_text_plugin.get_name()))])

	def __has_sublime(self):
		try:
			subl_version = sublime_info.get_sublime_version()
			package_dir = sublime_info.get_package_directory()
			return True, subl_version, package_dir
		except sublime_info.errors.STNotFoundError as e:
			return False, None, None