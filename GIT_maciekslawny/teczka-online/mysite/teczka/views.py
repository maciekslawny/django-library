from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from .models import Profile, Teczka, Document
import datetime
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from .forms import DocumentForm
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from django.core.paginator import Paginator
from django.shortcuts import render
from .tasks import celery_function

# Create your views here.




def cases_list(request):

    username = request.user
    
    try:
        cases = get_list_or_404(Teczka, owner=username, case_status = 'active')
    except:
        cases = []
    paginator = Paginator(cases, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'cases_list.html', {'cases': cases, 'page_obj': page_obj})


def cases_list_ended(request):

    username = request.user
    try:
        cases = get_list_or_404(Teczka, owner=username, case_status = 'ended')
    except:
        cases = []
    paginator = Paginator(cases, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'cases_list.html', {'cases': cases, 'page_obj': page_obj})


def cases_list_loading_date(request):
    date_today = datetime.datetime.today().strftime('%Y-%m-%d')
    print(date_today)
    username = request.user
    try:
        cases = get_list_or_404(Teczka, owner=username)
    except:
        cases = []
    cases_list = []
    if cases:
        for case in cases:
            print(case.loading_data)
            try:
                if case.loading_data.strftime('%Y-%m-%d') >= date_today:
                    cases_list.append(case)
            except:
                pass
    return render(request, 'cases_list_loading_date.html', {'cases': cases_list})


def case_detail(request, case_id):
    try:
        case = get_object_or_404(Teczka, id=case_id)
    except:
        case = 0

    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        name_file = request.FILES['document'].name
        title = request.POST.get('title')
        document = Document.objects.create(case_number=Teczka.objects.get(id=case_id), title=title, file=uploaded_file, name_file=name_file)
        document.save()
        '''
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        '''
    
    try:
        documents = get_list_or_404(Document, case_number=case_id)
    except:
        documents = []

    return render(request, 'case_detail.html', {'case': case, 'documents':documents})

def delete_document(request, case_id, document_id):
    if request.method == 'POST':
        try:
            document = Document.objects.get(id=document_id)
            document.delete()
        except:
            document = 0
    return redirect(f'/teczka/case-detail/{case_id}')
    


def add_case(request):
    if request.method == 'POST':
        company = request.POST.get('company')
        shipowner = request.POST.get('shipowner')
        booking = request.POST.get('booking')
        case_number = request.POST.get('case_number')
        year = request.POST.get('year')
        amount = request.POST.get('amount')
        container_type = request.POST.get('container_type')
        load_place = request.POST.get('load_place')
        destination = request.POST.get('destination')
        loading_data = request.POST.get('loading_data')
        cut_off = request.POST.get('cut_off')  
        etd = request.POST.get('etd')  
        eta = request.POST.get('eta')
        si = request.POST.get('si')
        coo = request.POST.get('coo')
        insurance = request.POST.get('insurance')
        import_export = request.POST.get('import_export_add')
        print(import_export)
        if etd == '':
            etd = None
        if cut_off == '':
            cut_off = None
        if eta == '':
            eta = None
        if loading_data == '':
            loading_data = None
        if amount == '':
            amount = 0
        
        if si == 'on':
            si = 'waiting'
        else:
            si = ''
        if coo == 'on':
            coo = 'waiting'
        else:
            coo = ''
        if insurance == 'on':
            insurance = 'waiting'
        else:
            insurance = ''
        username = request.user
        try:
            case = Teczka.objects.create(company=company, owner=username, booking=booking, case_number=case_number, shipowner=shipowner, year=year, amount=amount, container_type=container_type, loading_data=loading_data, load_place=load_place, destination=destination, cut_off=cut_off, etd=etd, eta=eta, si=si, coo=coo, insurance=insurance, import_export=import_export)
            case.save()
        except:
            pass
    return redirect('/teczka')
    #cases = get_list_or_404(Teczka, owner=username)
    #return render(request, 'cases_list.html', {'cases': cases})


def edit_case(request, case_id):
    if request.method == 'POST':
        company = request.POST.get('company')
        shipowner = request.POST.get('shipowner')
        booking = request.POST.get('booking')
        case_number = request.POST.get('case_number')
        offer_number = request.POST.get('offer_number')
        year = request.POST.get('year')
        amount = request.POST.get('amount')
        container_type = request.POST.get('container_type')
        container_numbers = request.POST.get('container_numbers')
        loading_data = request.POST.get('loading_data')
        loading_port = request.POST.get('loading_port')
        load_place = request.POST.get('load_place')
        destination = request.POST.get('destination')
        cut_off = request.POST.get('cut_off')  
        etd = request.POST.get('etd') 
        eta = request.POST.get('eta')  
        si = request.POST.get('si')
        coo = request.POST.get('coo')
        invoice = request.POST.get('invoice')
        customs = request.POST.get('customs')
        vgm = request.POST.get('vgm')
        insurance = request.POST.get('insurance')
        case_status = request.POST.get('case_status')
        description = request.POST.get('description') 
        import_export = request.POST.get('import-export-edit')
        username = request.user
        print(import_export)
        
        if etd == '':
            etd = None
        if cut_off == '':
            cut_off = None
        if eta == '':
            eta = None
        if loading_data == '':
            loading_data = None
        if amount == '':
            amount = 0

        if invoice == 'on':
            invoice = True
        else:
            invoice = False

        if customs == 'on':
            customs = True
        else:
            customs = False
    
        if vgm == 'on':
            vgm = True
        else:
            vgm = False
        
        
        case = Teczka.objects.get(id = case_id) 
        case.company = company
        case.shipowner = shipowner
        case.booking = booking
        case.case_number = case_number
        case.offer_number = offer_number
        case.year = year
        case.amount = amount
        case.container_type = container_type
        case.load_place = load_place
        case.destination = destination
        case.import_export = import_export
        
        case.loading_data = loading_data
        case.cut_off = cut_off
        case.etd = etd
        case.eta = eta
        case.si = si
        case.coo = coo
        case.invoice = invoice
        case.customs = customs
        case.vgm = vgm
        case.container_numbers = container_numbers
        case.loading_port = loading_port
        case.insurance = insurance
        case.case_status = case_status
        case.description = description
        case.save()
    

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def delete_case(request, case_id):
    try:
        documents = get_list_or_404(Document, case_number=case_id)
    except:
        documents = []
    for document in documents:
        document.delete()
    case = Teczka.objects.get(id = case_id)
    case.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'upload.html')

def generate_pdf(request, case_id):
    print('generate PDF', case_id)
    case = Teczka.objects.get(id = case_id)
    
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4, bottomup=0)
    c.setFontSize(22)
    
    c.drawString(50, 30, f'{case.company}        {case.case_number}/{case.year}')
    c.showPage()
    c.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=f'sped-{case.case_number}.pdf')
    
    #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def test_page(request):
    now = datetime.datetime.today().replace(tzinfo=datetime.timezone.utc)
    celery_function.delay()
    case = get_object_or_404(Teczka, id='74').cut_off

    
    minutes = int((case - now).total_seconds()/60)%60
    hours = int((case - now).total_seconds()/3600)%24
    days = int((case - now).total_seconds()/86400)
    print(now, case, 'PRZYKŁAD:', days, hours, minutes)
    return render(request, 'test_page.html')



def settings(request):
    now = datetime.datetime.today().replace(tzinfo=datetime.timezone.utc)
    profile = get_object_or_404(Profile, user=request.user)


    return render(request, 'settings.html', {'profile': profile})