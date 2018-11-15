from pygments.lexer import RegexLexer, bygroups, default
from pygments.token import Text, Comment, String, Operator, Name, Keyword
from sphinx.application import Sphinx


class CfgLexer(RegexLexer):
    name = 'QCOBJ'
    aliases = ['qcobj', 'ini', 'cfg']
    filenames = ['*.ini', '*.cfg']

    tokens = {
        'root': [
                (r'\s+', Text),
                (r'#.*?$', Comment),
                (r'\[.*?\]$', Keyword),
                (r'(.*?)(\s*)(=)(\s*)(.*?)$',
                bygroups(
                Name.Attribute, Text, Operator,
                Text, String)),
                #(r'"""', String, 'triple-double-quoted-string'),
                #(r"'''", String, 'triple-single-quoted-string'),
                ],
        #'triple-double-quoted-string': [
                #(r'"""', String, 'end-of-string'),
                #(r'[^\\]+', String),
                #(r'\\', String, 'string-escape'),
                #],
        #'triple-single-quoted-string': [
                #(r"'''", String, 'end-of-string'),
                #(r'[^\\]+', String),
                #(r'\\', String, 'string-escape'),
                #],
        #'end-of-string': [
            #(r'(@)([a-z]+(:?-[a-z0-9]+)*)',
             #bygroups(Operator, Name.Function), '#pop:2'),
            #(r'\^\^', Operator, '#pop:2'),
            #default('#pop:2'),
            #],
        #'string-escape': [
            #(r'.', String, '#pop'),
            #],
    }

def setup(app):
    app.add_lexer(CfgLexer.aliases[0], CfgLexer())

