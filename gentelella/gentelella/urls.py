"""gentella URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from app import dbcontrol

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # app/ -> Genetelella UI and resources
    #url(r'^app/', include('app.urls')),
    url(r'^get_supplier.html', csrf_exempt(dbcontrol.PrintAllSupplier)),
    url(r'^add_supplier.html', csrf_exempt(dbcontrol.AddSupplier)),
    url(r'^edit_supplier.html', csrf_exempt(dbcontrol.EditSupplier)),
    url(r'^del_supplier.html', csrf_exempt(dbcontrol.DelSupplier)),
    url(r'^get_member.html', csrf_exempt(dbcontrol.PrintAllMember)),
    url(r'^add_member.html', csrf_exempt(dbcontrol.AddMember)),
    url(r'^edit_member.html', csrf_exempt(dbcontrol.EditMember)),
    url(r'^del_member.html', csrf_exempt(dbcontrol.DelMember)),
    url(r'^get_contract.html', csrf_exempt(dbcontrol.PrintAllContract)),
    url(r'^add_contract.html', csrf_exempt(dbcontrol.AddContract)),
    url(r'^edit_contract.html', csrf_exempt(dbcontrol.EditContract)),
    url(r'^del_contract.html', csrf_exempt(dbcontrol.DelContract)),
    url(r'^get_indent.html', csrf_exempt(dbcontrol.PrintAllIndent)),
    url(r'^add_indent.html', csrf_exempt(dbcontrol.AddIndent)),
    url(r'^edit_indent.html', csrf_exempt(dbcontrol.EditIndent)),
    url(r'^del_indent.html', csrf_exempt(dbcontrol.DelIndent)),
    url(r'^get_pricefile.html', csrf_exempt(dbcontrol.PrintAllPriceFile)),
    url(r'^add_pricefile.html', csrf_exempt(dbcontrol.AddPriceFile)),
    url(r'^edit_pricefile.html', csrf_exempt(dbcontrol.EditPriceFile)),
    url(r'^del_pricefile.html', csrf_exempt(dbcontrol.DelPriceFile)),
    url(r'^get_record.html', csrf_exempt(dbcontrol.PrintAllRecord)),
    url(r'^add_record.html', csrf_exempt(dbcontrol.AddRecord)),
    url(r'^edit_record.html', csrf_exempt(dbcontrol.EditRecord)),
    url(r'^del_record.html', csrf_exempt(dbcontrol.DelRecord)),
    url(r'^get_temprecord.html', csrf_exempt(dbcontrol.PrintAllTempRecord)),
    url(r'^add_temprecord.html', csrf_exempt(dbcontrol.AddTempRecord)),
    url(r'^edit_temprecord.html', csrf_exempt(dbcontrol.EditTempRecord)),
    url(r'^del_temprecord.html', csrf_exempt(dbcontrol.DelTempRecord)),
    url(r'^get_salesrecord.html', csrf_exempt(dbcontrol.PrintAllSalesRecord)),
    url(r'^add_salesrecord.html', csrf_exempt(dbcontrol.AddSalesRecord)),
    url(r'^edit_salesrecord.html', csrf_exempt(dbcontrol.EditSalesRecord)),
    url(r'^del_salesrecord.html', csrf_exempt(dbcontrol.DelSalesRecord)),
    url(r'^get_goodsrecord.html', csrf_exempt(dbcontrol.PrintAllGoodsRecord)),
    url(r'^add_goodsrecord.html', csrf_exempt(dbcontrol.AddGoodsRecord)),
    url(r'^edit_goodsrecord.html', csrf_exempt(dbcontrol.EditGoodsRecord)),
    url(r'^del_goodsrecord.html', csrf_exempt(dbcontrol.DelGoodsRecord)),
    url(r'^', include('app.urls')),

]
