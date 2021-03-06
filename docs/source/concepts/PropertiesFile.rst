.. _Properties File:

Properties File
===============

The ``*.properties`` Files
--------------------------

The Mantid framework is configured using up to three simple text ``*.properties`` files that are read an interpreted every time the framework is started. These properties are not the same as the properties of algorithms. All three have the same format. The three files are read from first to last, with the values in subsequent ``*.properties`` overriding those in previous ones.

1. Install directory ``Mantid.properties`` defines the default configuration that the development team suggest as sensible defaults. This file should not be altered by users as it will be replaced with every new install or upgrade of Mantid.
2. ``/etc/mantid.local.properties`` is an optional, linux only file that sets shared defaults on a shared system. This is commonly used for setting the ``default.facility``, ``default.instrument``, and ``datasearch.searcharchive`` properties.
3. Home directory ``Mantid.user.properties`` is where users may override any property setting in Mantid. Any Property setting in this file will override anything set in the ``Mantid.properties`` file. Simply either enter the property you wish to override in this file together with it's new value. The change will take effect the next time Mantid is started. Subsequent installs or upgrades of Mantid will never alter this file.

The Properties
--------------

.. note:: Use forward slash (``/``) or double up on the number of backslash (``\``) characters for all paths


General properties
******************

+----------------------------------+--------------------------------------------------+-------------------+
|Property                          |Description                                       | Example value     |
+==================================+==================================================+===================+
| ``algorithms.retained``          | The Number of algorithms properties to retain in | ``50``            |
|                                  | memory for refence in scripts.                   |                   |
+----------------------------------+--------------------------------------------------+-------------------+
| ``algorithms.categories.hidden`` | A comma separated list of any categories of      | ``Muons,Testing`` |
|                                  | algorithms that should be hidden in Mantid.      |                   |
+----------------------------------+--------------------------------------------------+-------------------+
| ``MultiThreaded.MaxCores``       | Sets the maximum number of cores available to be | ``0``             |
|                                  | used for threads for                             |                   |
|                                  | `OpenMP <http://www.openmp.org/>`_. If zero it   |                   |
|                                  | will use one thread per logical core available.  |                   |
+----------------------------------+--------------------------------------------------+-------------------+

Facility and instrument properties
**********************************

+------------------------------+----------------------------------------------------+---------------------+
|Property                      |Description                                         |Example value        |
+==============================+====================================================+=====================+
| ``default.facility``         | The name of the default facility. The facility     | ``ISIS``            |
|                              | must be defined within the facilites.xml file to   |                     |
|                              | be considered valid. The file is described         |                     |
|                              | :ref:`here <Facilities file>`.                     |                     |
+------------------------------+----------------------------------------------------+---------------------+
| ``default.instrument``       | The name of the default instrument. The instrument | ``WISH``            |
|                              | must be defined within the facilities.xml file to  |                     |
|                              | be valid. The file is described                    |                     |
|                              | :ref:`here <Facilities file>`.                     |                     |
+------------------------------+----------------------------------------------------+---------------------+
| ``Q.convention``             | The convention for converting to Q. For            | ``Crystallography`` |
|                              | ``Inelastic`` the convention is ki-kf.  For        | or ``Inelastic``    |
|                              | ``Crystallography`` the convention is kf-ki.       |                     |
+------------------------------+----------------------------------------------------+---------------------+

Directory Properties
********************

+--------------------------------------+---------------------------------------------------+-------------------------------------+
|Property                              |Description                                        |Example value                        |
+======================================+===================================================+=====================================+
| ``datasearch.directories``           | A semi-colon(``;``) separated list of directories | ``../data;\\\\isis\\isis$\\ndxgem`` |
|                                      | to use to search for data.                        |                                     |
+--------------------------------------+---------------------------------------------------+-------------------------------------+
| ``datasearch.searcharchive``         | ``on`` (only the default facility), ``off``       | ``on`` or ``hfir,sns``              |
|                                      | (none), ``all`` (all archives), or a list of      |                                     |
|                                      | individual facilities to search for files in the  |                                     |
|                                      | data archive                                      |                                     |
+--------------------------------------+---------------------------------------------------+-------------------------------------+
| ``defaultsave.directory``            | A default directory to use for saving files.      | ``../data``                         |
|                                      | the data archive                                  |                                     |
+--------------------------------------+---------------------------------------------------+-------------------------------------+
| ``instrumentDefinition.directory``   | Where to load instrument definition files from    | ``../Test/Instrument``              |
+--------------------------------------+---------------------------------------------------+-------------------------------------+
| ``parameterDefinition.directory``    | Where to load parameter definition files from     | ``../Test/Instrument``              |
+--------------------------------------+---------------------------------------------------+-------------------------------------+
| ``pythonscripts.directories``        | Python will also search the listed directories    | ``../scripts`` or ``C:/MyScripts``  |
|                                      | when importing modules.                           |                                     |
+--------------------------------------+---------------------------------------------------+-------------------------------------+
| ``pythonscripts.directory``          | **DEPRECATED:** Use ``pythonscripts.directories`` | N/A                                 |
|                                      | instead                                           |                                     |
+--------------------------------------+---------------------------------------------------+-------------------------------------+
| ``requiredpythonscript.directories`` | A list of directories containing Python scripts   | N/A                                 |
|                                      | that Mantid requires to function correctly.       |                                     |
|                                      | **WARNING:** Do not alter the default value.      |                                     |
+--------------------------------------+---------------------------------------------------+-------------------------------------+
| ``framework.plugins.directory``      | The path to the directory that contains the       | ``../plugins``                      |
|                                      | Mantid plugin libraries                           |                                     |
+--------------------------------------+---------------------------------------------------+-------------------------------------+
| ``framework.plugins.exclude``        | A list of substrings to allow libraries to be     | ``Qt4;Qt5``                         |
|                                      | skipped                                           |                                     |
+--------------------------------------+---------------------------------------------------+-------------------------------------+
| ``mantidqt.plugins.directory``       | The path to the directory containing the          | ``../plugins/qtX``                  |
|                                      | Mantid Qt-based plugin libraries                  |                                     |
+--------------------------------------+---------------------------------------------------+-------------------------------------+
| ``requiredpythonscript.directories`` | A list of directories containing Python scripts   | N/A                                 |
|                                      | that Mantid requires to function correctly.       |                                     |
|                                      | **WARNING:** Do not alter the default value.      |                                     |
+--------------------------------------+---------------------------------------------------+-------------------------------------+



Logging Properties
******************

The details of configuring the logging functionality within Mantid will not be explained here. For those who want more
details look into the `POCO logging classes <https://pocoproject.org/docs/package-Foundation.Logging.html>`_ and the
`Log4J logging module <https://logging.apache.org/log4j/>`_ that it closely emulates. There are several comments in the
properties file itself that explain the configuration we provide by default.  However there are some obvious areas that
you may want to alter and those properties are detailed below.

+-------------------------------------------------+---------------------------------------------------+-----------------------------+
|Property                                         |Description                                        |Example value                |
+=================================================+===================================================+=============================+
| ``logging.loggers.root.level``                  |Defines the lowest level of messages to be output  | ``debug``, ``information``, |
|                                                 |by the system, and will override lower settings in | ``notice``, ``warning``,    |
|                                                 |filterChannels. The default is information, but    | ``error``, ``critical``     |
|                                                 |this can be lowered to debug for more detailed     | or ``fatal``                |
|                                                 |feedback.                                          |                             |
|                                                 |                                                   |                             |
+-------------------------------------------------+---------------------------------------------------+-----------------------------+
| ``logging.channels.fileFilterChannel.level``    | The lowest level messages to output to the log    | ``debug``, ``information``, |
|                                                 | file. The default is warning, but this can be     | ``notice``, ``warning``,    |
|                                                 | lowered to debug for more detailed feedback. The  | ``error``, ``critical``     |
|                                                 | higher level of this and                          | or ``fatal``                |
|                                                 | ``logging.loggers.root.level`` will apply.        |                             |
+-------------------------------------------------+---------------------------------------------------+-----------------------------+
| ``logging.channels.consoleFilterChannel.level`` | The lowest level messages to output to the        | ``debug``, ``information``, |
|                                                 | console. The default is warning, but this can be  | ``notice``, ``warning``,    |
|                                                 | lowered to debug for more detailed feedback. The  | ``error``, ``critical``     |
|                                                 | higher level of this and                          | or ``fatal``                |
|                                                 | ``logging.loggers.root.level`` will apply.        |                             |
+-------------------------------------------------+---------------------------------------------------+-----------------------------+
| ``logging.channels.fileChannel.path``           | The Path to the log file.                         | ``../logs/mantid.log``      |
+-------------------------------------------------+---------------------------------------------------+-----------------------------+

The logging priority levels for the file logging and console logging can also be adjusted in python using the commands:

.. testcode:: LoggingConfigExample

  #Set the console to log at debug level on above (7=debug)
  ConfigService.setConsoleLogLevel(7)
  #Set the file to only log at critical level (2=critical)
  ConfigService.setConsoleLogLevel(2)



MantidPlot Properties
*********************

+--------------------------------------------+---------------------------------------------------+-----------------+
|Property                                    |Description                                        |Example value    |
+============================================+===================================================+=================+
| ``MantidOptions.InvisibleWorkspaces``      |Do not show 'invisible' workspaces                 | ``0``, ``1``    |
+--------------------------------------------+---------------------------------------------------+-----------------+
| ``MantidOptions.InstrumentView.UseOpenGL`` |Controls the use of OpenGL in rendering the        | ``On``, ``Off`` |
|                                            |"unwrapped" (flat) instrument views.               |                 |
+--------------------------------------------+---------------------------------------------------+-----------------+

Network Properties
******************

+-------------------------------------------+---------------------------------------------------+---------------------------------+
|Property                                   |Description                                        |Example value                    |
+===========================================+===================================================+=================================+
| ``CheckMantidVersion.OnStartup``          | Check if there is a newer version available and   |                                 |
|                                           | logs a message at ``information`` level           | ``1``                           |
+-------------------------------------------+---------------------------------------------------+---------------------------------+
| ``network.default.timeout``               |Defines the default timeout for all network        | ``30``                          |
|                                           |operations (in seconds).                           |                                 |
+-------------------------------------------+---------------------------------------------------+---------------------------------+
| ``network.scriptrepo.timeout``            |The timeout for network operations in the script   | ``5``                           |
|                                           |repository, this overrides the deafault timeout.   |                                 |
+-------------------------------------------+---------------------------------------------------+---------------------------------+
| ``proxy.host``                            | Allows the system proxy to be overridden, if not  | ``http://www.proxy.org``        |
|                                           | set mantid will use the system proxy              |                                 |
+-------------------------------------------+---------------------------------------------------+---------------------------------+
| ``proxy.port``                            | Must be set if proxy.host is set                  | ``8080``                        |
+-------------------------------------------+---------------------------------------------------+---------------------------------+
| ``proxy.httpsTargetUrl``                  | A sample url used to determine the system proxy to| ``http://www.google.com``       |
|                                           | use on windows.                                   |                                 |
+-------------------------------------------+---------------------------------------------------+---------------------------------+
| ``UpdateInstrumentDefinitions.OnStartup`` | Download new instrument definition files and      |                                 |
|                                           | ``Facilities.xml`` to ``~/.mantid/instruments``   |                                 |
|                                           | on linux or ``APPDATA`` directory on windows. If  |                                 |
|                                           | this is disabled, previously downloaded           |                                 |
|                                           | instruments are ignored and only those in the     |                                 |
|                                           | installation are used.                            | ``1``                           |
+-------------------------------------------+---------------------------------------------------+---------------------------------+
| ``usagereports.enabled``                  | Enable usage reporting                            | ``1``                           |
+-------------------------------------------+---------------------------------------------------+---------------------------------+




ScriptRepository Properties
***************************

+----------------------------+-----------------------------------------------+----------------------------------------------------------------------+
|Property                    |Description                                    |Example value                                                         |
+============================+===============================================+======================================================================+
| ``ScriptLocalRepository``  |Directory where ScriptRepository is Installed. | ``C:\\MantidInstall\\MyScriptRepository``                            |
+----------------------------+-----------------------------------------------+----------------------------------------------------------------------+
| ``ScriptRepository``       |Base URL for the remote script repository.     | ``http://download.mantidproject.org/scriptrepository/``              |
+----------------------------+-----------------------------------------------+----------------------------------------------------------------------+
| ``UploaderWebServer``      |URL for uploading scripts.                     | ``http://upload.mantidproject.org/scriptrepository/payload/publish`` |
+----------------------------+-----------------------------------------------+----------------------------------------------------------------------+
| ``ScriptRepositoryIgnore`` |CSV patterns for paths that should not be      | ``*pyc;``                                                            |
|                            |listed at ScriptRepository.                    |                                                                      |
+----------------------------+-----------------------------------------------+----------------------------------------------------------------------+


Getting access to Mantid properties
***********************************

To get access to, e.g. data saving path property from a C++ program one has to issue the following command:


.. testcode:: properties

  path = ConfigService.getString("defaultsave.directory")

.. categories:: Concepts
