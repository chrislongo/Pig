import sublime
import sublime_plugin
import os


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

        pig_binary = None

        if java_home is not None:
            env['JAVA_HOME'] = java_home

        if pig_home is not None:
            env['PIG_HOME'] = pig_home
            pig_binary = os.path.join(pig_home, 'bin', 'pig')
        else:
            pig_binary = 'pig'

        cmd = [pig_binary]

        if pig_classpath is not None:
            env['PIG_CLASSPATH'] = pig_classpath

        if log4j_properties is not None:
            cmd.extend(['-4 ', log4j_properties])

        if execution_mode is not None:
            cmd.extend(['-x', execution_mode])

        cmd.append(self.window.active_view().file_name())

        self.window.run_command('exec',
            {'cmd': cmd, 'env': env, 'file_regex': file_regex, 'path': path})
