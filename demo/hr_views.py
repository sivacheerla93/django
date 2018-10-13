from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import AddDeptForm, AddEmpForm
from django.http import JsonResponse
import mysql.connector


def add_dept(request):
    if request.method == "POST":
        form = AddDeptForm(request.POST)
        message = ""
        if form.is_valid():
            id = form.cleaned_data["deptid"]
            name = form.cleaned_data["deptname"]
            print(id, name)
            # insert row into DEPT table
            try:
                con = mysql.connector.connect(host="localhost", user="root", password="9866850403", database="python")
                cur = con.cursor()
                # take input from user
                cur.execute("insert into dept values({},'{}')".format(id, name))
                con.commit()
                return HttpResponseRedirect('/demo/list_dept/')
            except Exception as ex:
                print("Error : ", ex)
                message = "Error : " + str(ex)
            finally:
                cur.close()
                con.close()

        return render(request, 'demo/hr/add_dept.html', {'form': form, 'message': message})
    else:  # GET
        form = AddDeptForm()  # empty form
        return render(request, 'demo/hr/add_dept.html', {'form': form})


def list_dept(request):
    depts = []
    try:
        con = mysql.connector.connect(host="localhost", user="root", password="9866850403", database="python")
        cur = con.cursor()
        # take input from user
        cur.execute("select * from dept")
        depts = cur.fetchall()
        print(depts)
    except Exception as ex:
        print("Error : ", ex)
    finally:
        cur.close()
        con.close()

    return render(request, 'demo/hr/list_dept.html', {"depts": depts})


def list_emp(request, id):
    employees = []
    try:
        con = mysql.connector.connect(host="localhost", user="root", password="9866850403", database="python")
        cur = con.cursor()
        # take input from user
        cur.execute("select * from emp where deptid = {}".format(id))
        employees = cur.fetchall()
    except Exception as ex:
        print("Error : ", ex)
    finally:
        cur.close()
        con.close()

    return render(request, 'demo/hr/list_emp.html',
                  {"employees": employees, 'deptid': id})


def add_emp(request):
    if request.method == "POST":
        form = AddEmpForm(request.POST)
        message = ""
        if form.is_valid():
            ename = form.cleaned_data["ename"]
            salary = form.cleaned_data["salary"]
            dept = form.cleaned_data["dept"]

            # insert row into EMP table
            try:
                con = mysql.connector.connect(host="localhost", user="root", password="9866850403", database="python")
                cur = con.cursor()
                # Find out next empid
                cur.execute("select max(id) + 1 from emp")
                empid = cur.fetchone()[0]
                cur.execute("insert into emp values({},'{}',{},{})".format(empid, ename, salary, dept))
                con.commit()
                message = "Employee [%d] has been inserted!" % (empid)
            except Exception as ex:
                print("Error : ", ex)
                message = "Error : " + str(ex)
            finally:
                cur.close()
                con.close()
        else:
            print(form.errors)

        return render(request, 'demo/hr/add_emp.html',
                      {'form': form, 'message': message})
    else:
        form = AddEmpForm()  # empty form
        return render(request, 'demo/hr/add_emp.html', {'form': form})


def list_all_emp(request):
    employees = []
    try:
        con = mysql.connector.connect(host="localhost", user="root", password="9866850403", database="python")
        cur = con.cursor()
        # take input from user
        cur.execute("select * from emp")
        employees = cur.fetchall()
    except Exception as ex:
        print("Error : ", ex)
    finally:
        cur.close()
        con.close()

    return render(request, 'demo/hr/list_all_emp.html',
                  {"employees": employees})


# For Ajax
def search(request):
    return render(request, 'demo/hr/search_emp.html')


def get_employees(request):
    name = request.GET.get('name', None)
    name = name + "%"
    print(name)
    employees = []

    try:
        con = mysql.connector.connect(host="localhost", user="root", password="9866850403", database="python")
        cur = con.cursor()
        # take input from user
        cur.execute("select * from emp where name like '{}'".format(name))
        for row in cur.fetchall():
            emp = {"id": row[0], "name": row[1], "salary": row[2], "deptid": row[3]}
            employees.append(emp)
    except Exception as ex:
        print("Error : ", ex)
    finally:
        cur.close()
        con.close()

    return JsonResponse(employees, safe=False)
