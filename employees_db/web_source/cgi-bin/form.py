#!/usr/bin/python
# -*- coding: utf-8 -*-
import cgi
form = cgi.FieldStorage()

print('Content-type: text/html')
html = """
    <!DOCTYPE html>
        <html lang='en'>
        <head>
            <meta charset="UTF-8">
            <title>Employees</title>
        </head>
        <body>
            <form method=POST, action="cgi-bin/employees.py">
                <table>
                    <tr><th>pk</th><td><input type=text name=pk></td></tr>
                    <tr><th>Name</th><td><input type=text name=Name></td></tr>
                    <tr><th>Age</th><td><input type=text name=Age></td></tr>
                    <tr><th>Job</th><td><input type=text name=Job></td>
                    <tr><th>Pay</th><td><input type=text name=Pay></td></tr>
                </table>
                <br>
                <input type=submit value="Fetch" name=action>
                <input type=submit value="Update" name=action>
            </form>
        </body>
        </html>
    """

print(html)
