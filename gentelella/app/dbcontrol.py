from django.shortcuts import render
from django.shortcuts import redirect
from app.models import *
import datetime
import MySQLdb

def PrintAllSupplier(request):
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='db_admin',
        db='db_work',
    )
    cur = conn.cursor()
    num = cur.execute("select * from app_supplier")
    supplier_list = []
    for msg in range(num):
        list = cur.fetchone()
        tmp = {}
        tmp['id'] = list[0]
        tmp['name'] = list[1]
        tmp['address'] = list[2]
        tmp['legal_person'] = list[3]
        tmp['account'] = list[4]
        supplier_list.append(tmp)
    cur.close()
    conn.commit()
    conn.close()
    return render(request, 'app/get_supplier.html', {'supplier_list':supplier_list})

def AddSupplier(request):
    if request.method == "GET":
        return render(request, 'app/add_supplier.html')
    elif request.method == "POST":
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='db_admin',
            db='db_work',
        )
        cur = conn.cursor()
        name = request.POST.get('name')
        address = request.POST.get('address')
        legal_person = request.POST.get('legal_person')
        account = request.POST.get('account')
        cur.execute("insert into app_supplier (name, address, legal_person, account) values (\'%s\',\'%s\',\'%s\',\'%s\')"%(name,address,legal_person,account))
        cur.close()
        conn.commit()
        conn.close()
        return redirect('get_supplier.html')

def EditSupplier(request):
    if request.method == "GET":
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='db_admin',
            db='db_work',
        )
        cur = conn.cursor()
        nid = request.GET.get('nid')
        num = cur.execute("select * from app_supplier where id = %s"%(nid))
        list = cur.fetchone()
        obj = {}
        obj['id'] = list[0]
        obj['name'] = list[1]
        obj['address'] = list[2]
        obj['legal_person'] = list[3]
        obj['account'] = list[4]
        cur.close()
        conn.commit()
        conn.close()
        return render(request, 'app/edit_supplier.html', {'obj':obj})
    elif request.method == "POST":
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='db_admin',
            db='db_work',
        )
        cur = conn.cursor()
        nid = request.GET.get('nid')
        name = request.POST.get('name')
        address = request.POST.get('address')
        legal_person = request.POST.get('legal_person')
        account = request.POST.get('account')
        cur.execute("update app_supplier set name=\'%s\',address=\'%s\',legal_person=\'%s\',account=\'%s\' where id=%s"%(name,address,legal_person,account,nid))
        cur.close()
        conn.commit()
        conn.close()
        return redirect('get_supplier.html')

def DelSupplier(request):
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='db_admin',
        db='db_work',
    )
    cur = conn.cursor()
    nid = request.GET.get('nid')
    cur.execute("delete from app_supplier where id=%s"%(nid))
    cur.close()
    conn.commit()
    conn.close()
    return redirect('get_supplier.html')


def PrintAllMember(request):
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='db_admin',
        db='db_work',
    )
    cur = conn.cursor()
    num = cur.execute("select * from app_member")
    member_list = []
    for msg in range(num):
        list = cur.fetchone()
        tmp = {}
        tmp['id'] = list[0]
        tmp['name'] = list[1]
        tmp['phone'] = list[2]
        tmp['credits'] = list[3]
        member_list.append(tmp)
    cur.close()
    conn.commit()
    conn.close()
    return render(request, 'app/get_member.html', {'member_list':member_list})

def AddMember(request):
    if request.method == "GET":
        return render(request, 'app/add_member.html')
    elif request.method == "POST":
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='db_admin',
            db='db_work',
        )
        cur = conn.cursor()
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        credits = request.POST.get('credits')
        cur.execute("insert into app_member (name, phone, credits) values (\'%s\',\'%s\',%s)"%(name,phone,credits))
        cur.close()
        conn.commit()
        conn.close()
        return redirect('get_member.html')

def EditMember(request):
    if request.method == "GET":
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='db_admin',
            db='db_work',
        )
        cur = conn.cursor()
        nid = request.GET.get('nid')
        num = cur.execute("select * from app_member where id = %s"%(nid))
        list = cur.fetchone()
        obj = {}
        obj['id'] = list[0]
        obj['name'] = list[1]
        obj['phone'] = list[2]
        obj['credits'] = list[3]
        cur.close()
        conn.commit()
        conn.close()
        return render(request, 'app/edit_member.html', {'obj':obj})
    elif request.method == "POST":
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='db_admin',
            db='db_work',
        )
        cur = conn.cursor()
        nid = request.GET.get('nid')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        credits = request.POST.get('credits')
        cur.execute("update app_member set name=\'%s\',phone=\'%s\',credits=%s where id=%s"%(name,phone,credits,nid))
        cur.close()
        conn.commit()
        conn.close()
        return redirect('get_member.html')

def DelMember(request):
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='db_admin',
        db='db_work',
    )
    cur = conn.cursor()
    nid = request.GET.get('nid')
    cur.execute("delete from app_member where id=%s"%(nid))
    cur.close()
    conn.commit()
    conn.close()
    return redirect('get_member.html')


def PrintAllContract(request):
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='db_admin',
        db='db_work',
    )
    cur = conn.cursor()
    num = cur.execute("select * from app_contract")
    contract_list = []
    for msg in range(num):
        list = cur.fetchone()
        tmp = {}
        tmp['id'] = list[0]
        tmp['supplier'] = list[1]
        tmp['name'] = list[2]
        tmp['price'] = list[3]
        tmp['cost'] = list[4]
        tmp['sales_return'] = list[5]
        tmp['complimentary'] = list[6]
        contract_list.append(tmp)
    cur.close()
    conn.commit()
    conn.close()
    return render(request, 'app/get_contract.html', {'contract_list':contract_list})

def AddContract(request):
    if request.method == "GET":
        return render(request, 'app/add_contract.html')
    elif request.method == "POST":
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='db_admin',
            db='db_work',
        )
        cur = conn.cursor()
        supplier = request.POST.get('supplier')
        name = request.POST.get('name')
        price = request.POST.get('price')
        cost = request.POST.get('cost')
        sales_return = request.POST.get('sales_return')
        complimentary = request.POST.get('complimentary')
        cur.execute("insert into app_contract (supplier, name, price, cost, sales_return, complimentary) values (%s,\'%s\',%s,%s,%s,\'%s\')"%(supplier,name,price,cost,sales_return,complimentary))
        cur.close()
        conn.commit()
        conn.close()
        return redirect('get_contract.html')

def EditContract(request):
    if request.method == "GET":
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='db_admin',
            db='db_work',
        )
        cur = conn.cursor()
        nid = request.GET.get('nid')
        num = cur.execute("select * from app_contract where id = %s"%(nid))
        list = cur.fetchone()
        obj = {}
        obj['id'] = list[0]
        obj['supplier'] = list[1]
        obj['name'] = list[2]
        obj['price'] = list[3]
        obj['cost'] = list[4]
        obj['sales_return'] = list[5]
        obj['complimentary'] = list[6]
        cur.close()
        conn.commit()
        conn.close()
        return render(request, 'app/edit_contract.html', {'obj':obj})
    elif request.method == "POST":
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='db_admin',
            db='db_work',
        )
        cur = conn.cursor()
        nid = request.GET.get('nid')
        supplier = request.POST.get('supplier')
        name = request.POST.get('name')
        price = request.POST.get('price')
        cost = request.POST.get('cost')
        sales_return = request.POST.get('sales_return')
        complimentary = request.POST.get('complimentary')
        cur.execute("update app_contract set supplier=%s,name=\'%s\',price=%s,cost=%s,sales_return=%s,complimentary=\'%s\' where id=%s"%(supplier,name,price,cost,sales_return,complimentary,nid))
        cur.close()
        conn.commit()
        conn.close()
        return redirect('get_contract.html')

def DelContract(request):
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='db_admin',
        db='db_work',
    )
    cur = conn.cursor()
    nid = request.GET.get('nid')
    cur.execute("delete from app_contract where id=%s"%(nid))
    cur.close()
    conn.commit()
    conn.close()
    return redirect('get_contract.html')

def PrintAllIndent(request):
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='db_admin',
        db='db_work',
    )
    cur = conn.cursor()
    num = cur.execute("select * from app_indent")
    indent_list = []
    for msg in range(num):
        list = cur.fetchone()
        tmp = {}
        tmp['id'] = list[0]
        tmp['contract'] = list[1]
        tmp['number'] = list[2]
        tmp['date'] = list[3]
        tmp['style'] = list[4]
        indent_list.append(tmp)
    cur.close()
    conn.commit()
    conn.close()
    return render(request, 'app/get_indent.html', {'indent_list':indent_list})

def AddIndent(request):
    if request.method == "GET":
        return render(request, 'app/add_indent.html')
    elif request.method == "POST":
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='db_admin',
            db='db_work',
        )
        cur = conn.cursor()
        contract = request.POST.get('contract')
        number = request.POST.get('number')
        date = request.POST.get('date')
        style = request.POST.get('style')
        cur.execute("insert into app_contract (contract, number, date, style) values (%s,%s,\'%s\',%s)"%(contract,number,date,style))
        cur.close()
        conn.commit()
        conn.close()
        return redirect('get_indent.html')

def EditIndent(request):
    if request.method == "GET":
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='db_admin',
            db='db_work',
        )
        cur = conn.cursor()
        nid = request.GET.get('nid')
        num = cur.execute("select * from app_indent where id = %s"%(nid))
        list = cur.fetchone()
        obj = {}
        obj['id'] = list[0]
        obj['contract'] = list[1]
        obj['number'] = list[2]
        obj['date'] = list[3]
        obj['style'] = list[4]
        cur.close()
        conn.commit()
        conn.close()
        return render(request, 'app/edit_indent.html', {'obj':obj})
    elif request.method == "POST":
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='db_admin',
            db='db_work',
        )
        cur = conn.cursor()
        nid = request.GET.get('nid')
        contract = request.POST.get('contract')
        number = request.POST.get('number')
        date = request.POST.get('date')
        style = request.POST.get('style')
        cur.execute("update app_contract set contract=%s,number=%s,date=\'%s\',style=%s where id=%s"%(contract,number,date,style,nid))
        cur.close()
        conn.commit()
        conn.close()
        return redirect('get_indent.html')

def DelIndent(request):
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='db_admin',
        db='db_work',
    )
    cur = conn.cursor()
    nid = request.GET.get('nid')
    cur.execute("delete from app_indent where id=%s"%(nid))
    cur.close()
    conn.commit()
    conn.close()
    return redirect('get_indent.html')


def PrintAllPriceFile(request):
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='db_admin',
        db='db_work',
    )
    cur = conn.cursor()
    num = cur.execute("select * from app_pricefile")
    pricefile_list = []
    for msg in range(num):
        list = cur.fetchone()
        tmp = {}
        tmp['id'] = list[0]
        tmp['contract'] = list[1]
        tmp['min_price'] = list[2]
        tmp['max_price'] = list[3]
        pricefile_list.append(tmp)
    cur.close()
    conn.commit()
    conn.close()
    return render(request, 'app/get_pricefile.html', {'pricefile_list':pricefile_list})

def AddPriceFile(request):
    if request.method == "GET":
        return render(request, 'app/add_pricefile.html')
    elif request.method == "POST":
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='db_admin',
            db='db_work',
        )
        cur = conn.cursor()
        contract = request.POST.get('contract')
        min_price = request.POST.get('min_price')
        max_price = request.POST.get('max_price')
        cur.execute("insert into app_pricefile (contract, min_price, max_price) values (%s,%s,%s,%s)"%(contract,min_price,max_price))
        cur.close()
        conn.commit()
        conn.close()
        return redirect('get_pricefile.html')

def EditPriceFile(request):
    if request.method == "GET":
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='db_admin',
            db='db_work',
        )
        cur = conn.cursor()
        nid = request.GET.get('nid')
        num = cur.execute("select * from app_pricefile where id = %s"%(nid))
        list = cur.fetchone()
        obj = {}
        obj['id'] = list[0]
        obj['contract'] = list[1]
        obj['min_price'] = list[2]
        obj['max_price'] = list[3]
        cur.close()
        conn.commit()
        conn.close()
        return render(request, 'app/edit_pricefile.html', {'obj':obj})
    elif request.method == "POST":
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='db_admin',
            db='db_work',
        )
        cur = conn.cursor()
        nid = request.GET.get('nid')
        name = request.POST.get('contract')
        min_price = request.POST.get('min_price')
        max_price = request.POST.get('max_price')
        cur.execute("update app_pricefile set contract=%s,min_price=%s,max_price=%s where id=%s"%(contract,min_price,max_price,nid))
        cur.close()
        conn.commit()
        conn.close()
        return redirect('get_pricefile.html')

def DelPriceFile(request):
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='db_admin',
        db='db_work',
    )
    cur = conn.cursor()
    nid = request.GET.get('nid')
    cur.execute("delete from app_pricefile where id=%s"%(nid))
    cur.close()
    conn.commit()
    conn.close()
    return redirect('get_pricefile.html')


def PrintAllRecord(request):
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='db_admin',
        db='db_work',
    )
    cur = conn.cursor()
    num = cur.execute("select * from app_record")
    record_list = []
    for msg in range(num):
        list = cur.fetchone()
        tmp = {}
        tmp['id'] = list[0]
        tmp['supplier'] = list[1]
        tmp['name'] = list[2]
        tmp['address'] = list[3]
        record_list.append(tmp)
    cur.close()
    conn.commit()
    conn.close()
    return render(request, 'app/get_record.html', {'record_list':record_list})

def AddRecord(request):
    if request.method == "GET":
        return render(request, 'app/add_record.html')
    elif request.method == "POST":
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='db_admin',
            db='db_work',
        )
        cur = conn.cursor()
        supplier = request.POST.get('supplier')
        name = request.POST.get('name')
        address = request.POST.get('address')
        cur.execute("insert into app_record (supplier, name, address) values (%s,%s,%s,%s)"%(supplier,name,address))
        cur.close()
        conn.commit()
        conn.close()
        return redirect('get_record.html')

def EditRecord(request):
    if request.method == "GET":
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='db_admin',
            db='db_work',
        )
        cur = conn.cursor()
        nid = request.GET.get('nid')
        num = cur.execute("select * from app_record where id = %s"%(nid))
        list = cur.fetchone()
        obj = {}
        obj['id'] = list[0]
        obj['supplier'] = list[1]
        obj['name'] = list[2]
        obj['address'] = list[3]
        cur.close()
        conn.commit()
        conn.close()
        return render(request, 'app/edit_record.html', {'obj':obj})

    elif request.method == "POST":
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='db_admin',
            db='db_work',
        )
        cur = conn.cursor()
        nid = request.GET.get('nid')
        supplier = request.POST.get('supplier')
        name = request.POST.get('name')
        address = request.POST.get('address')
        cur.execute("update app_record set supplier=%s,name=\'%s\',address=\'%s\' where id=%s"%(supplier,name,address,nid))
        cur.close()
        conn.commit()
        conn.close()
        return redirect('get_record.html')

def DelRecord(request):
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='db_admin',
        db='db_work',
    )
    cur = conn.cursor()
    nid = request.GET.get('nid')
    cur.execute("delete from app_record where id=%s"%(nid))
    cur.close()
    conn.commit()
    conn.close()
    return redirect('get_record.html')

def PrintAllTempRecord(request):
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='db_admin',
        db='db_work',
    )
    cur = conn.cursor()
    num = cur.execute("select * from app_temprecord")
    temprecord_list = []
    for msg in range(num):
        list = cur.fetchone()
        tmp = {}
        tmp['id'] = list[0]
        tmp['contract'] = list[1]
        tmp['name'] = list[2]
        tmp['address'] = list[3]
        temprecord_list.append(tmp)
    cur.close()
    conn.commit()
    conn.close()
    return render(request, 'app/get_temprecord.html', {'temprecord_list':temprecord_list})

def AddTempRecord(request):
    if request.method == "GET":
        return render(request, 'app/add_temprecord.html')
    elif request.method == "POST":
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='db_admin',
            db='db_work',
        )
        cur = conn.cursor()
        contract = request.POST.get('contract')
        name = request.POST.get('name')
        address = request.POST.get('address')
        cur.execute("insert into app_temprecord (contract, name, address) values (%s,%s,%s,%s)"%(contract,name,address))
        cur.close()
        conn.commit()
        conn.close()
        return redirect('get_temprecord.html')

def EditTempRecord(request):
    if request.method == "GET":
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='db_admin',
            db='db_work',
        )
        cur = conn.cursor()
        nid = request.GET.get('nid')
        num = cur.execute("select * from app_temprecord where id = %s"%(nid))
        list = cur.fetchone()
        obj = {}
        obj['id'] = list[0]
        obj['contract'] = list[1]
        obj['name'] = list[2]
        obj['address'] = list[3]
        cur.close()
        conn.commit()
        conn.close()
        return render(request, 'app/edit_temprecord.html', {'obj':obj})

    elif request.method == "POST":
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='db_admin',
            db='db_work',
        )
        cur = conn.cursor()
        nid = request.GET.get('nid')
        contract = request.POST.get('contract')
        name = request.POST.get('name')
        address = request.POST.get('address')
        cur.execute("update app_temprecord set contract=%s,name=\'%s\',address=\'%s\' where id=%s"%(contract,name,address,nid))
        cur.close()
        conn.commit()
        conn.close()
        return redirect('get_temprecord.html')

def DelTempRecord(request):
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='db_admin',
        db='db_work',
    )
    cur = conn.cursor()
    nid = request.GET.get('nid')
    cur.execute("delete from app_temprecord where id=%s"%(nid))
    cur.close()
    conn.commit()
    conn.close()
    return redirect('get_temprecord.html')

def PrintAllSalesRecord(request):
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='db_admin',
        db='db_work',
    )
    cur = conn.cursor()
    num = cur.execute("select * from app_salesrecord")
    salesrecord_list = []
    for msg in range(num):
        list = cur.fetchone()
        tmp = {}
        tmp['id'] = list[0]
        tmp['supplier'] = list[1]
        tmp['member'] = list[2]
        tmp['pricefile'] = list[3]
        tmp['supplier_discount'] = list[4]
        tmp['company_discount'] = list[5]
        tmp['address'] = list[6]
        salesrecord_list.append(tmp)
    cur.close()
    conn.commit()
    conn.close()
    return render(request, 'app/get_salesrecord.html', {'salesrecord_list':salesrecord_list})

def AddSalesRecord(request):
    if request.method == "GET":
        return render(request, 'app/add_salesrecord.html')
    elif request.method == "POST":
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='db_admin',
            db='db_work',
        )
        cur = conn.cursor()
        supplier = request.POST.get('supplier')
        member = request.POST.get('member')
        pricefile = request.POST.get('pricefile')
        supplier_discount = request.POST.get('supplier_discount')
        company_discount = request.POST.get('company_discount')
        address = request.POST.get('address')
        cur.execute("insert into app_salesrecord (supplier, nember, pricefile, supplier_discount, company_discount, address) values (%s,%s,%s,%s,%s,\'%s\')"%(supplier,member,pricefile,supplier_discount,company_discont,address))
        cur.close()
        conn.commit()
        conn.close()
        return redirect('get_salesrecord.html')

def EditSalesRecord(request):
    if request.method == "GET":
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='db_admin',
            db='db_work',
        )
        cur = conn.cursor()
        nid = request.GET.get('nid')
        num = cur.execute("select * from app_salesrecord where id = %s"%(nid))
        list = cur.fetchone()
        obj = {}
        obj['id'] = list[0]
        obj['supplier'] = list[1]
        obj['member'] = list[2]
        obj['pricefile'] = list[3]
        obj['supplier_discount'] = list[4]
        obj['company_discount'] = list[5]
        obj['address'] = list[6]
        cur.close()
        conn.commit()
        conn.close()
        return render(request, 'app/edit_salesrecord.html', {'obj':obj})
    elif request.method == "POST":
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='db_admin',
            db='db_work',
        )
        cur = conn.cursor()
        nid = request.GET.get('nid')
        supplier = request.POST.get('supplier')
        member = request.POST.get('member')
        pricefile = request.POST.get('pricefile')
        supplier_discount = request.POST.get('supplier_discount')
        company_discount = request.POST.get('company_discount')
        address = request.POST.get('address')
        cur.execute("update app_salesrecord set supplier=%s,member=%s,price=%s,supplier_discount=%s,company_discount=%s,address=\'%s\' where id=%s"%(supplier,member,pricefile,supplier_discount,company_discount,address,nid))
        cur.close()
        conn.commit()
        conn.close()
        return redirect('get_salesrecord.html')

def DelSalesRecord(request):
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='db_admin',
        db='db_work',
    )
    cur = conn.cursor()
    nid = request.GET.get('nid')
    cur.execute("delete from app_salesrecord where id=%s"%(nid))
    cur.close()
    conn.commit()
    conn.close()
    return redirect('get_salesrecord.html')

def PrintAllGoodsRecord(request):
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='db_admin',
        db='db_work',
    )
    cur = conn.cursor()
    num = cur.execute("select * from app_goodsrecord")
    goodsrecord_list = []
    for msg in range(num):
        list = cur.fetchone()
        tmp = {}
        tmp['id'] = list[0]
        tmp['record'] = list[1]
        tmp['temprecord'] = list[2]
        goodsrecord_list.append(tmp)
    cur.close()
    conn.commit()
    conn.close()
    return render(request, 'app/get_goodsrecord.html', {'goodsrecord_list':goodsrecord_list})

def AddGoodsRecord(request):
    if request.method == "GET":
        return render(request, 'app/add_goodsrecord.html')
    elif request.method == "POST":
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='db_admin',
            db='db_work',
        )
        cur = conn.cursor()
        record = request.POST.get('record')
        temprecord = request.POST.get('temprecord')
        cur.execute("insert into app_goodsrecord (record, temprecord) values (%s,%s)"%(record,temprecord))
        cur.close()
        conn.commit()
        conn.close()
        return redirect('get_goodsrecord.html')

def EditGoodsRecord(request):
    if request.method == "GET":
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='db_admin',
            db='db_work',
        )
        cur = conn.cursor()
        nid = request.GET.get('nid')
        num = cur.execute("select * from app_goodsrecord where id = %s"%(nid))
        list = cur.fetchone()
        obj = {}
        obj['id'] = list[0]
        obj['record'] = list[1]
        obj['temprecord'] = list[2]
        cur.close()
        conn.commit()
        conn.close()
        return render(request, 'app/edit_goodsrecord.html', {'obj':obj})
    elif request.method == "POST":
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='db_admin',
            db='db_work',
        )
        cur = conn.cursor()
        nid = request.GET.get('nid')
        record = request.POST.get('record')
        temprecord = request.POST.get('temprecord')
        cur.execute("update app_goodsrecord set record=%s,record=%s where id=%s"%(record,temprecord,nid))
        cur.close()
        conn.commit()
        conn.close()
        return redirect('get_goodsrecord.html')

def DelGoodsRecord(request):
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='db_admin',
        db='db_work',
    )
    cur = conn.cursor()
    nid = request.GET.get('nid')
    cur.execute("delete from app_goodsrecord where id=%s"%(nid))
    cur.close()
    conn.commit()
    conn.close()
    return redirect('get_goodsrecord.html')