import sublime
import sublime_plugin


class RunPigCommand(sublime_plugin.WindowCommand):
    settings = None

    def get_setting(self, name):
        setting = self.settings.get(name)

        if setting is not None and len(setting) == 0:
            setting = None

        return setting

    def run(self, file_regex='', path=''):
        env = {}

        self.settings = sublime.load_settings('Pig.sublime-settings')

        java_home = self.get_setting('java_home')
        pig_home = self.get_setting('pig_home')
        execution_mode = self.get_setting('execution_mode')
        pig_classpath = self.get_setting('pig_classpath')
        log4j_properties = self.get_setting('log4j_properties')

        print java_home

        pig_binary = None

        if java_home is not None:
            env['JAVA_HOME'] = java_home

        if pig_home is not None:
            env['PIG_HOME'] = pig_home
            pig_binary = pig_home + '/bin/pig'
        else:
            pig_binary = 'pig'

        if execution_mode is not None:
            execution_mode = '-x ' + execution_mode

        if pig_classpath is not None:
            env['PIG_CLASSPATH'] = pig_classpath

        if log4j_properties is not None:
            log4j_properties = '-4 ' + log4j_properties
        else:
            log4j_properties = ''

        file_name = self.window.active_view().file_name()

        cmd = [pig_binary, execution_mode, log4j_properties, file_name]

        self.window.run_command('exec',
            {'cmd': cmd, 'env': env, 'file_regex': file_regex, 'path': path})
