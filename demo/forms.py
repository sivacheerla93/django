import django.forms as forms
import mysql.connector


class AddDeptForm(forms.Form):
    deptid = forms.IntegerField(label='Dept ID')
    deptname = forms.CharField(label='Dept Name', max_length=20)


class AddEmpForm(forms.Form):
    ename = forms.CharField(label="Full Name", max_length=20)
    salary = forms.IntegerField(label="Salary", min_value=5000)
    depts = []
    try:
        con = mysql.connector.connect(host="localhost", user="root", password="9866850403", database="python")
        cur = con.cursor()
        cur.execute("select * from dept order by id")
        depts = cur.fetchall()
    except Exception as ex:
        print("Error : ", ex)
    finally:
        cur.close()
        con.close()

    dept = forms.ChoiceField(label="Department", choices=depts)
