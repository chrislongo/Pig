import sublime
import sublime_plugin


class RunPigCommand(sublime_plugin.WindowCommand):
    def run(self, file_regex='', path=''):
        env = {}

        settings = sublime.load_settings('Pig.sublime-settings')

        java_home = settings.get('java_home')
        pig_home = settings.get('pig_home')
        pig_binary = None

        if java_home is not None and len(java_home) > 0:
            env['java_home'] = java_home

        if pig_home is not None and len(pig_home) > 0:
            env['pig_home'] = pig_home
            pig_binary = pig_home + '/bin/pig'
        else:
            pig_binary = 'pig'

        file_name = self.window.active_view().file_name()

        cmd = [pig_binary, "-x local", file_name]

        self.window.run_command('exec',
            {'cmd': cmd, 'env': env, 'file_regex': file_regex, 'path': path})
