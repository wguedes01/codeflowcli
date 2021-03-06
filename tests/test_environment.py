import pytest
from util import get_linux_32
from codeflow.errors import AppAlreadyInstalledError
from codeflow.application import Application

class TestEnvironment(object):

	def test_install_app_already_installed(self):
		with pytest.raises(AppAlreadyInstalledError):
			app = Application('my_app', {'Linux': ['32bit', '64bit']})
			get_linux_32(pre_installed=['my_app']).install_app(app)

	def test_install_app(self):
		app = Application('my_app', {'Linux': ['32bit', '64bit']})
		assert True == get_linux_32(pre_installed=[]).install_app(app)

	def test_install_app_not_supported_os(self):
		with pytest.raises(ValueError):
			app = Application('my_app', {'Linux': ['64bit']})
			get_linux_32().install_app(app)

			app = Application('my_app', {'Windows': ['64bit', '32bit']})
			get_linux_32().install_app(app)