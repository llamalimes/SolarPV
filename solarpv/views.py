from django.shortcuts import render, redirect
from .models import Product, Certificate, Service, Location, Client, PerformanceData, TestSequence, TestStandard
from .forms import ProductForm, CertificateForm, ServiceForm, LocationForm, ClientForm, PerformanceDataForm, TestSequenceForm, TestStandardForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from .serializers import ProductSerializer, CertificateSerializer, ServiceSerializer, LocationSerializer, ClientSerializer, PerformanceDataSerializer, TestSequenceSerializer, TestStandardSerializer

###############################################################
# API serializers
###############################################################

class ProductAPIView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]

class CertificateAPIView(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer    
    permission_classes = [IsAdminUser]

class ServiceAPIView(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAdminUser]

class ClientAPIView(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAdminUser]

class LocationAPIView(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAdminUser]

class PerformanceDataAPIView(viewsets.ModelViewSet):
    queryset = PerformanceData.objects.all()
    serializer_class = PerformanceDataSerializer
    permission_classes = [IsAdminUser]
    
class TestSequenceAPIView(viewsets.ModelViewSet):
    queryset = TestSequence.objects.all()
    serializer_class = TestSequenceSerializer
    permission_classes = [IsAdminUser]

class TestStandardAPIView(viewsets.ModelViewSet):
    queryset = TestStandard.objects.all()
    serializer_class = TestStandardSerializer
    permission_classes = [IsAdminUser]



# basic page views

###############################################################
# Page Views
###############################################################
def home_view(request):
    return render(request, 'index.html', {})

def portal_view(request):
    return render(request, 'portal.html', {})

###############################################################
# Product Views
###############################################################
@login_required
def product_list_view(request):
    product_list = Product.objects.all()
    return render(request, 'products/product_list.html', {'product_list':product_list})

@login_required
def add_product_view(request):
    submitted = False
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_product?submitted=True')
    else:
        form = ProductForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'products/add_product.html', {'form':form, 'submitted':submitted})

@login_required
def product_detail_view(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'products/product_detail.html', {'product':product})

@login_required
def search_products_view(request):    
    return render(request, 'products/search_products.html', {})

@login_required
def product_search_results_view(request):  
    if request.method == "POST":
        searched = request.POST['searched']
        products = Product.objects.filter(product_name__contains=searched)
        return render(request, 'products/product_search_results.html', {'searched':searched, 'products':products})
    else:  
        return render(request, 'products/product_search_results.html', {})

@login_required
def update_product_view(request, product_id):    
    product = Product.objects.get(pk=product_id)
    form = ProductForm(request.POST or None, instance=product) # instance= loads information from db into form
    if form.is_valid():
        form.save()
        return redirect('list-products')
    return render(request, 'products/update_product.html', {'product':product, 'form':form})

@login_required
def delete_product_view(request, product_id):    
    product = Product.objects.get(pk=product_id)
    if request.method == "POST":
        product.delete()
        return redirect('list-products')
    return render(request, 'products/delete_product.html', {'product':product})

###############################################################
# Certificate Views
###############################################################
@login_required
def certificate_list_view(request):
    certificate_list = Certificate.objects.all()
    return render(request, 'certificates/certificate_list.html', {'certificate_list':certificate_list})

@login_required
def add_certificate_view(request):
    submitted = False
    if request.method == "POST":
        form = CertificateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_certificate?submitted=True')
    else:
        form = CertificateForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'certificates/add_certificate.html', {'form':form, 'submitted':submitted})

@login_required
def certificate_detail_view(request, certificate_id):
    certificate = Certificate.objects.get(pk=certificate_id)
    return render(request, 'certificates/certificate_detail.html', {'certificate':certificate})

@login_required
def search_certificates_view(request):    
    return render(request, 'certificates/search_certificates.html', {})

@login_required
def certificate_search_results_view(request):  
    if request.method == "POST":
        searched = request.POST['searched']
        certificates = Certificate.objects.filter(certificate_number__contains=searched)
        return render(request, 'certificates/certificate_search_results.html', {'searched':searched, 'certificates':certificates})
    else:  
        return render(request, 'certificates/certificate_search_results.html', {})

@login_required
def update_certificate_view(request, certificate_id):    
    certificate = Certificate.objects.get(pk=certificate_id)
    form = CertificateForm(request.POST or None, instance=certificate) # instance= loads information from db into form
    if form.is_valid():
        form.save()
        return redirect('list-certificates')
    return render(request, 'certificates/update_certificate.html', {'certificate':certificate, 'form':form})

@login_required
def delete_certificate_view(request, certificate_id):    
    certificate = Certificate.objects.get(pk=certificate_id)
    if request.method == "POST":
        certificate.delete()
        return redirect('list-certificates')
    return render(request, 'certificates/delete_certificate.html', {'certificate':certificate})

###############################################################
# Service Views
###############################################################
@login_required
def service_list_view(request):
    service_list = Service.objects.all()
    return render(request, 'services/service_list.html', {'service_list':service_list})

@login_required
def add_service_view(request):
    submitted = False
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_service?submitted=True')
    else:
        form = ServiceForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'services/add_service.html', {'form':form, 'submitted':submitted})

@login_required
def service_detail_view(request, service_id):
    service = Service.objects.get(pk=service_id)
    return render(request, 'services/service_detail.html', {'service':service})

@login_required
def search_services_view(request):    
    return render(request, 'services/search_services.html', {})

@login_required
def service_search_results_view(request):  
    if request.method == "POST":
        searched = request.POST['searched']
        services = service.objects.filter(service_name__contains=searched)
        return render(request, 'services/service_search_results.html', {'searched':searched, 'services':services})
    else:  
        return render(request, 'services/service_search_results.html', {})

@login_required
def update_service_view(request, service_id):    
    service = Service.objects.get(pk=service_id)
    form = ServiceForm(request.POST or None, instance=service) # instance= loads information from db into form
    if form.is_valid():
        form.save()
        return redirect('list-services')
    return render(request, 'services/update_service.html', {'service':service, 'form':form})

@login_required
def delete_service_view(request, service_id):    
    service = Service.objects.get(pk=service_id)
    if request.method == "POST":
        service.delete()
        return redirect('list-services')
    return render(request, 'services/delete_service.html', {'service':service})

###############################################################
# Location Views
###############################################################
@login_required
def location_list_view(request):
    location_list = Location.objects.all()
    return render(request, 'locations/location_list.html', {'location_list':location_list})

@login_required
def add_location_view(request):
    submitted = False
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_location?submitted=True')
    else:
        form = LocationForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'locations/add_location.html', {'form':form, 'submitted':submitted})

@login_required
def location_detail_view(request, location_id):
    location = Location.objects.get(pk=location_id)
    return render(request, 'locations/location_detail.html', {'location':location})

@login_required
def search_locations_view(request):    
    return render(request, 'locations/search_locations.html', {})

@login_required
def location_search_results_view(request):  
    if request.method == "POST":
        searched = request.POST['searched']
        locations = Location.objects.filter(address1__contains=searched)
        return render(request, 'locations/location_search_results.html', {'searched':searched, 'locations':locations})
    else:  
        return render(request, 'locations/location_search_results.html', {})

@login_required
def update_location_view(request, location_id):    
    location = Location.objects.get(pk=location_id)
    form = LocationForm(request.POST or None, instance=location) # instance= loads information from db into form
    if form.is_valid():
        form.save()
        return redirect('list-locations')
    return render(request, 'locations/update_location.html', {'location':location, 'form':form})

@login_required
def delete_location_view(request, location_id):    
    location = Location.objects.get(pk=location_id)
    if request.method == "POST":
        location.delete()
        return redirect('list-locations')
    return render(request, 'locations/delete_location.html', {'location':location})

###############################################################
# Client Views
###############################################################
@login_required
def client_list_view(request):
    client_list = Client.objects.all()
    return render(request, 'clients/client_list.html', {'client_list':client_list})

@login_required
def add_client_view(request):
    submitted = False
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_client?submitted=True')
    else:
        form = ClientForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'clients/add_client.html', {'form':form, 'submitted':submitted})

@login_required
def client_detail_view(request, client_id):
    client = Client.objects.get(pk=client_id)
    return render(request, 'clients/client_detail.html', {'client':client})

@login_required
def search_clients_view(request):    
    return render(request, 'clients/search_clients.html', {})

@login_required
def client_search_results_view(request):  
    if request.method == "POST":
        searched = request.POST['searched']
        clients = Client.objects.filter(client_name__contains=searched)
        return render(request, 'clients/client_search_results.html', {'searched':searched, 'clients':clients})
    else:  
        return render(request, 'clients/client_search_results.html', {})

@login_required
def update_client_view(request, client_id):    
    client = Client.objects.get(pk=client_id)
    form = ClientForm(request.POST or None, instance=client) # instance= loads information from db into form
    if form.is_valid():
        form.save()
        return redirect('list-clients')
    return render(request, 'clients/update_client.html', {'client':client, 'form':form})

@login_required
def delete_client_view(request, client_id):    
    client = Client.objects.get(pk=client_id)
    if request.method == "POST":
        client.delete()
        return redirect('list-clients')
    return render(request, 'clients/delete_client.html', {'client':client})

###############################################################
# Performance Data Views
###############################################################
@login_required
def performance_data_list_view(request):
    performance_data_list = PerformanceData.objects.all()
    return render(request, 'performance_datas/performance_data_list.html', {'performance_data_list':performance_data_list})

@login_required
def add_performance_data_view(request):
    submitted = False
    if request.method == "POST":
        form = PerformanceDataForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_performance_data?submitted=True')
    else:
        form = PerformanceDataForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'performance_datas/add_performance_data.html', {'form':form, 'submitted':submitted})

@login_required
def performance_data_detail_view(request, performance_data_id):
    performance_data = PerformanceData.objects.get(pk=performance_data_id)
    return render(request, 'performance_datas/performance_data_detail.html', {'performance_data':performance_data})

@login_required
def search_performance_datas_view(request):    
    return render(request, 'performance_datas/search_performance_datas.html', {})

@login_required
def performance_data_search_results_view(request):  
    if request.method == "POST":
        searched = request.POST['searched']
        performance_datas = PerformanceData.objects.filter(model_number__contains=searched)
        return render(request, 'performance_datas/performance_data_search_results.html', {'searched':searched, 'performance_datas':performance_datas})
    else:  
        return render(request, 'performance_datas/performance_data_search_results.html', {})

@login_required
def update_performance_data_view(request, performance_data_id):    
    performance_data = PerformanceData.objects.get(pk=performance_data_id)
    form = PerformanceDataForm(request.POST or None, instance=performance_data) # instance= loads information from db into form
    if form.is_valid():
        form.save()
        return redirect('list-performance-datas')
    return render(request, 'performance_datas/update_performance_data.html', {'performance_data':performance_data, 'form':form})

@login_required
def delete_performance_data_view(request, performance_data_id):    
    performance_data = PerformanceData.objects.get(pk=performance_data_id)
    if request.method == "POST":
        performance_data.delete()
        return redirect('list-performance-datas')
    return render(request, 'performance_datas/delete_performance_data.html', {'performance_data':performance_data})

###############################################################
# Test Sequence Views
###############################################################
@login_required
def test_sequence_list_view(request):
    test_sequence_list = TestSequence.objects.all()
    return render(request, 'test_sequences/test_sequence_list.html', {'test_sequence_list':test_sequence_list})

@login_required
def add_test_sequence_view(request):
    submitted = False
    if request.method == "POST":
        form = TestSequenceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_test_sequence?submitted=True')
    else:
        form = TestSequenceForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'test_sequences/add_test_sequence.html', {'form':form, 'submitted':submitted})

@login_required
def test_sequence_detail_view(request, test_sequence_id):
    test_sequence = TestSequence.objects.get(pk=test_sequence_id)
    return render(request, 'test_sequences/test_sequence_detail.html', {'test_sequence':test_sequence})

@login_required
def search_test_sequences_view(request):    
    return render(request, 'test_sequences/search_test_sequences.html', {})

@login_required
def test_sequence_search_results_view(request):  
    if request.method == "POST":
        searched = request.POST['searched']
        test_sequences = TestSequence.objects.filter(sequence_name__contains=searched)
        return render(request, 'test_sequences/test_sequence_search_results.html', {'searched':searched, 'test_sequences':test_sequences})
    else:  
        return render(request, 'test_sequences/test_sequence_search_results.html', {})

@login_required
def update_test_sequence_view(request, test_sequence_id):    
    test_sequence = TestSequence.objects.get(pk=test_sequence_id)
    form = TestSequenceForm(request.POST or None, instance=test_sequence) # instance= loads information from db into form
    if form.is_valid():
        form.save()
        return redirect('list-test-sequences')
    return render(request, 'test_sequences/update_test_sequence.html', {'test_sequence':test_sequence, 'form':form})

@login_required
def delete_test_sequence_view(request, test_sequence_id):    
    test_sequence = TestSequence.objects.get(pk=test_sequence_id)
    if request.method == "POST":
        test_sequence.delete()
        return redirect('list-test-sequences')
    return render(request, 'test_sequences/delete_test_sequence.html', {'test_sequence':test_sequence})

###############################################################
# Test Standard Views
###############################################################
@login_required
def test_standard_list_view(request):
    test_standard_list = TestStandard.objects.all()
    return render(request, 'test_standards/test_standard_list.html', {'test_standard_list':test_standard_list})

@login_required
def add_test_standard_view(request):
    submitted = False
    if request.method == "POST":
        form = TestStandardForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_test_standard?submitted=True')
    else:
        form = TestStandardForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'test_standards/add_test_standard.html', {'form':form, 'submitted':submitted})

@login_required
def test_standard_detail_view(request, test_standard_id):
    test_standard = TestStandard.objects.get(pk=test_standard_id)
    return render(request, 'test_standards/test_standard_detail.html', {'test_standard':test_standard})

@login_required
def search_test_standards_view(request):    
    return render(request, 'test_standards/search_test_standards.html', {})

@login_required
def test_standard_search_results_view(request):  
    if request.method == "POST":
        searched = request.POST['searched']
        test_standards = TestStandard.objects.filter(standard_name__contains=searched)
        return render(request, 'test_standards/test_standard_search_results.html', {'searched':searched, 'test_standards':test_standards})
    else:  
        return render(request, 'test_standards/test_standard_search_results.html', {})

@login_required
def update_test_standard_view(request, test_standard_id):    
    test_standard = TestStandard.objects.get(pk=test_standard_id)
    form = TestStandardForm(request.POST or None, instance=test_standard) # instance= loads information from db into form
    if form.is_valid():
        form.save()
        return redirect('list-test-standards')
    return render(request, 'test_standards/update_test_standard.html', {'test_standard':test_standard, 'form':form})

@login_required
def delete_test_standard_view(request, test_standard_id):    
    test_standard = TestStandard.objects.get(pk=test_standard_id)
    if request.method == "POST":
        test_standard.delete()
        return redirect('list-test-standards')
    return render(request, 'test_standards/delete_test_standard.html', {'test_standard':test_standard})

