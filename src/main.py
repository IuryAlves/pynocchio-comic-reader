# coding=UTF-8
#
# Copyright (C) 2015  Michell Stuttgart

# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.

# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.
#
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QLocale, QTranslator
from main_window import MainWindow


def main():
    import sys

    app = QApplication(sys.argv)
    app.setApplicationName('Pynocchio Comic Reader')

    qm = QLocale().name()

    if qm != 'en_US':
        translator = QTranslator()
        translator.load("../i18n/qt_%s.qm" % qm)
        app.installTranslator(translator)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()