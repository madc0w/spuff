#!/usr/bin/python
import cgi

form = cgi.FieldStorage()
print "Content-type:text/html\n"
print '<html>'
print '<head>'
print '<title>'
print form.getvalue('t')
print '</title>'
print ' <script>'
print '         const args = location.href.substring(location.href.indexOf("?") + 1).split("&");'
print 'console.log(args)'
print '         let url, protocol = "https";'
print '         for (const arg of args) {'
print '                 if (arg.startsWith("t=")) {'
print '                         document.title = arg.substring("t=".length);'
print '                 } else if (arg.startsWith("u=")) {'
print '                         url = arg.substring("u=".length).replaceAll("%2F", "/");'
print '                 } else if (arg.startsWith("p=")) {'
print '                         protocol = arg.substring("p=".length);'
print '                 }'
print '         }'
print '         location = `${protocol}://${url}`;'
print ' </script>'
print '</head>'
print '<body>'
print '</body>'
print '</html>'
