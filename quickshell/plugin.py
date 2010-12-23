import imp, os, sys
from easycast_utils.patterns import DictList

def get_commands():
    commands = DictList()

    from plugins import __all__
    for cls in __all__:
        print 'Importing system-wide plugin %s' %cls
        system_plugin = __import__("plugins.%s" %cls, fromlist=__all__, globals=globals(), locals=locals())
        cmd_list = getattr(system_plugin, 'commands')
        commands.extend(cmd_list)

    path = os.path.join(os.environ['HOME'], '.quickshell')
    if not os.path.isdir(path):
        print 'User has no .quickshell directory, skipping user plugins loading'
    else:
        plugins_paths = scan_user_directory_for_plugins(path)
        for plugin_path in plugins_paths:
            plugin_commands = get_commands_from_plugin(plugin_path)
            if plugin_commands:
                commands.extend(plugin_commands)

    quit = ({'title': 'Quit', 'cb': sys.exit, 'category': True, 'key': 'q'},)
    commands.extend(quit)
    return commands

def scan_user_directory_for_plugins(path):
    filenames = []
    print 'Scanning folder %s for plugins' %path
    for filename in os.listdir(path):
        if filename.endswith('.py'):
            abs_filename = os.path.join(path, filename)
            print 'Found plugin', abs_filename
            filenames.append(abs_filename)
    return filenames

def get_commands_from_plugin(plugin_abspath):
    try:
        plugin = imp.load_source('plugin', plugin_abspath)
        if hasattr(plugin, 'commands'):
            commands = plugin.commands
    except Exception, e:
        print 'Error while importing plugin %s, %s, %s' %(plugin_abspath, e, plugin_abspath)
        commands = None
    return commands

# Code from gst-qa-system
def scan_directory_for_plugins(directory):

    source_ext = [t[0] for t in imp.get_suffixes() if t[2] == imp.PY_SOURCE]
    import_names = []

    for dirpath, dirnames, filenames in os.walk(directory):

        for filename in filenames:
            basename, ext = os.path.splitext(filename)
            if ext in source_ext and basename != "__init__":
                import_names.append(basename)

        for dirname in dirnames:
            for ext in source_ext:
                if os.path.exists(os.path.join(dirpath, dirname, "__init__%s" % (ext,))):
                    import_names.append(dirname)

        # Don't descent to subdirectories:
        break

    return import_names
