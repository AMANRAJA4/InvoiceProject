from django.shortcuts import get_object_or_404, render,redirect
from django.utils import timezone
from Model.models import Invoice,InvoiceDetail

def invoice(request):
    invoices = Invoice.objects.all()
    return render(request, 'invoice.html' , {'invoices':invoices})

def invoice_details(request,pk):
    details = InvoiceDetail.objects.get(invoice_id=pk)
    return render(request, 'invoicedetails.html', {'details':details})

def create(request):
    return render(request, 'create.html')

def save_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        des = request.POST.get('description')
        qua = request.POST.get('quantity')
        up = request.POST.get('unit_price')
        price = request.POST.get('price')

        invoice = Invoice()
        invoice.customer_name = name
        invoice.date = timezone.now().date()
        invoice.save()

        details = InvoiceDetail()
        details.invoice = invoice
        details.description = des
        details.quantity = qua
        details.unit_price = up
        details.price = price
        details.save()

    return redirect('invoice')

def invoice_update(request,pk):
    details = InvoiceDetail.objects.get(pk=pk)
    return render(request, 'detailsupdate.html', {'details':details})

def save_update(request,pk):
    details = get_object_or_404(InvoiceDetail, pk=pk)

    if request.method == 'POST':
        des = request.POST.get('description')
        qua = request.POST.get('quantity')
        up = request.POST.get('unit_price')
        price = request.POST.get('price')

        details.description = des
        details.quantity = qua
        details.unit_price = up
        details.price = price

        details.save()
    return redirect('invoice_details' ,pk)