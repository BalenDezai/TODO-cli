from todocli.todo.config import lang_list, Lang
import re

class TestConfig(object):
    def test_Lang(self):

        lang = Lang('.py', [r"#\s*(TODO.*)"])
        compiled_regex = lang.get_compiled_regexes()

        assert isinstance(lang, Lang)

        assert isinstance(compiled_regex, list)

        assert compiled_regex[0] == re.compile(r'#\s*(TODO.*)')

    def test_LangList(self):
        lang_regex_to_get = '.py'
        lang = lang_list[lang_regex_to_get]
        lang_regex = lang.get_compiled_regexes()

        assert isinstance(lang, Lang)
        assert lang_regex[0] == re.compile(r'#\s*(TODO.*)')